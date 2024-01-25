# to be filled with snippets I find myself using time and time again

# frequently imported modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import datetime as dt
import scipy as scp
import sys
import os
import time

# time script execution
starttime = time.time()
# insert code here
print("This code took",time.time()-starttime,"seconds to run.")

# reading files to pandas dataframes (more on how to use them: https://pandas.pydata.org/docs/reference/frame.html)
csv_file = pd.read_csv("filename.csv",delimiter=None, header='infer', names=[name,of,each,column], index_col=None, usecols=None, skiprows=None, skipfooter=0, nrows=None, skip_blank_lines=True)
xlsx_file = pd.read_excel("filename.xlsx",sheet_name=0, header='infer', names=[name,of,each,column] index_col=None, usecols=None, skiprows=None, skipfooter=0, nrows=None)

# reading a text file to a list
file = open('file.txt','r')
lines = file.readlines()
print(lines)

# basic plots

# plots using gridspec

# fitting using scipy
