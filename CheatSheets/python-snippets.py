# to be filled with snippets I find myself using time and time again

# frequently imported modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import scipy as scp
import sys
import os
import time

# time script execution
starttime = time.time()
# insert code here
print("This code took",time.time()-starttime,"seconds to run."

# reading files to pandas dataframes
csv_file = pd.read_csv("filename.csv",delimiter=None, header='infer', names=[name,of,each,column], index_col=None, usecols=None, skiprows=None, skipfooter=0, nrows=None, skip_blank_lines=True)
xlsx_file = pd.read_excel("filename.xlsx",sheet_name=0, header='infer', names=[name,of,each,column] index_col=None, usecols=None, skiprows=None, skipfooter=0, nrows=None)

# reading text files to arrays

# basic plots

# plots using gridspec

# fitting using scipy
