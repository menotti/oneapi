#!/usr/bin/env python3
import os
import platform
import subprocess
import pandas as pd
import numpy
from IPython.display import Image

RUNS = 10

FILENAME = 'MM.csv'

def system_info():
    print(os.name, platform.system(), platform.release())
    print(os.popen("clinfo | grep -B 2 -A 4 'Device Vendor ID'").read())
    print(os.popen("clinfo | grep NOTE -A 3").read())

# Creating Pandas DataFrame
if os.path.isfile(FILENAME):
    df = pd.read_csv(FILENAME)
else:
    df = pd.DataFrame({"version": [], "platform": [], "execution_time_s": []})

for i in range(RUNS): 
    run = subprocess.Popen("./matrix.dpcpp",
                           cwd = "matrix_multiply_vtune/src/",
                           shell = True,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE,
                           universal_newlines = True)
    result = run.communicate()[0].split("\n")
    df = df.append(pd.DataFrame({"version"          : [result[0]], 
                                 "platform"         : [result[1]], 
                                 "execution_time_s": [float(result[2])]}), sort=False)
          
df.to_csv(FILENAME, index = False, header = True)
