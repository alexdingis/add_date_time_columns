# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 19:59:31 2018

@author: Alexander

"""

"""
df['year'], df['month'] = df['date'].dt.year, df['date'].dt.month
"""

"""
 input_df["Created Date"] = pd.to_datetime(input_df["Created Date"]
"""

import os
import pandas as pd
import time
#
output_dir = r"C:\Users\Alexander\Desktop\School\Projects\Zip_Rats\Outputs"
#
os.chdir(output_dir)
#
my_csv     = r"C:\Users\Alexander\Desktop\School\Projects\Zip_Rats\Data\Rat_Sightings.csv"
#
my_column  = "Created Date"
#
my_new_csv = r"C:\Users\Alexander\Desktop\School\Projects\Zip_Rats\Outputs\test_01.csv"
#
#
#
def add_year_month_day_columns(input_csv, date_column, output_csv):
    #
    start_time = time.time()
    #
    try:
        #
        df = pd.read_csv(input_csv, delimiter = ",")
        #
        if date_column in list(df):
            #
            df[date_column] = pd.to_datetime(df[date_column], infer_datetime_format = True)
            #
            df["Year"]      = df[date_column].dt.year
            #
            df["Month"]     = df[date_column].dt.month
            #
            df["Day"]       = df[date_column].dt.day
            #
            df["Quarter"]   = df[date_column].dt.quarter
            #
            df.to_csv(output_csv, sep = ",", index = False)
        #
        else:
            #
            print "Date column not in csv/dataframe: {0}".format(date_column)
            #
        #
    #
    except Exception as e:
        #
        print e
        #
    #
    end_time = round(time.time() - start_time, 5)
    #
    print "add_year_month_day_columns took these many seconds to process: {0}".format(end_time)
    #
#
# -----------------------------------------------------------------------------
#
add_year_month_day_columns(my_csv, my_column, my_new_csv)
#
#
#