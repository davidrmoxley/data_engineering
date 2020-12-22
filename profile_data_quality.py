def udf_profile_data_quality(df,missingness_threshold):
    """
    Takes a source dataframe
    Returns dataframe of the source fields with multiple data types 
        or records in excess of a given proportion of total records
        with blanks or NaN values
    and Returns dictionary summarizing the number of columns 
        with missingness and/or inconsistent datatypes
    """
    
    record_cnt = len(df)
    df_dq=pd.DataFrame(columns=['column_name','na_values', 'blank_values', 'int_values', 'float_values', 'str_values'])

    #evaluate each column
    for column_name in df.columns:
        integer=flts=strings=nas=blank=0 #reset data type counters

        #record if row value is integer, float or string
        for index, value in df.loc[:,column_name].items():

            if pd.isna(value):
                nas+=1
            elif isinstance(value, str) and value.strip()=="":
                blank+=1
            elif isinstance(value, int):
                integer+=1
            elif isinstance(value, float):
                flts+=1
            elif isinstance(value, str):
                strings+=1


        #update dictionary with column and data type counts 
        #if more than 1 data type is identified at a rate exceeding user-defined threshold
        if (blank>(record_cnt*missingness_threshold) and blank<record_cnt) | (nas>(record_cnt*missingness_threshold) and nas<record_cnt) | (integer>0 and integer<(record_cnt*(1-missingness_threshold))) | (flts>0 and flts<(record_cnt*(1-missingness_threshold))) | (strings>0 and strings<(record_cnt*(1-missingness_threshold))):
            df_dq=df_dq.append({'column_name':column_name
                                ,'na_values':nas
                                ,'blank_values':blank
                                ,'int_values':integer
                                ,'float_values':flts
                                ,'str_values':strings}
                               , ignore_index=True)
    
    #initialize dictionary summarizing data quality issues
    dq_issues={'NAs':len(df_dq[df_dq['na_values']>0])
               ,'Blanks':len(df_dq[df_dq['blank_values']>0])
               ,'Ints & Strings':len(df_dq[(df_dq['int_values']>0)&(df_dq['str_values']>0)])
               ,'Floats & Strings':len(df_dq[(df_dq['float_values']>0)&(df_dq['str_values']>0)])}

    return df_dq,dq_issues

