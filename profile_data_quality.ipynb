{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def udf_profile_data_quality(df,missingness_threshold):\n",
    "    \"\"\"\n",
    "    Takes a source dataframe\n",
    "    Returns dataframe of the source fields with multiple data types \n",
    "        or records in excess of a given proportion of total records\n",
    "        with blanks or NaN values\n",
    "    and Returns dictionary summarizing the number of columns \n",
    "        with missingness and/or inconsistent datatypes\n",
    "    \"\"\"\n",
    "    \n",
    "    record_cnt = len(df)\n",
    "    df_dq=pd.DataFrame(columns=['column_name','na_values', 'blank_values', 'int_values', 'float_values', 'str_values'])\n",
    "\n",
    "    #evaluate each column\n",
    "    for column_name in df.columns:\n",
    "        integer=flts=strings=nas=blank=0 #reset data type counters\n",
    "\n",
    "        #record if row value is integer, float or string\n",
    "        for index, value in df.loc[:,column_name].items():\n",
    "\n",
    "            if pd.isna(value):\n",
    "                nas+=1\n",
    "            elif isinstance(value, str) and value.strip()==\"\":\n",
    "                blank+=1\n",
    "            elif isinstance(value, int):\n",
    "                integer+=1\n",
    "            elif isinstance(value, float):\n",
    "                flts+=1\n",
    "            elif isinstance(value, str):\n",
    "                strings+=1\n",
    "\n",
    "\n",
    "        #update dictionary with column and data type counts \n",
    "        #if more than 1 data type is identified at a rate exceeding user-defined threshold\n",
    "        if (blank>(record_cnt*missingness_threshold) and blank<record_cnt) | (nas>(record_cnt*missingness_threshold) and nas<record_cnt) | (integer>0 and integer<(record_cnt*(1-missingness_threshold))) | (flts>0 and flts<(record_cnt*(1-missingness_threshold))) | (strings>0 and strings<(record_cnt*(1-missingness_threshold))):\n",
    "            df_dq=df_dq.append({'column_name':column_name\n",
    "                                ,'na_values':nas\n",
    "                                ,'blank_values':blank\n",
    "                                ,'int_values':integer\n",
    "                                ,'float_values':flts\n",
    "                                ,'str_values':strings}\n",
    "                               , ignore_index=True)\n",
    "    \n",
    "    #initialize dictionary summarizing data quality issues\n",
    "    dq_issues={'NAs':len(df_dq[df_dq['na_values']>0])\n",
    "               ,'Blanks':len(df_dq[df_dq['blank_values']>0])\n",
    "               ,'Ints & Strings':len(df_dq[(df_dq['int_values']>0)&(df_dq['str_values']>0)])\n",
    "               ,'Floats & Strings':len(df_dq[(df_dq['float_values']>0)&(df_dq['str_values']>0)])}\n",
    "\n",
    "    return df_dq,dq_issues"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
