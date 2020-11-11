import urllib.request
import subprocess
import pandas as pd
import numpy as np
df = pd.DataFrame(columns = ['CRN', 'URL', 'Line'])
test = input("How many classes would you like to watch?")
for i in range(int(test)):
    crn = str(input("What is this classes CRN? "))
    geturl = input("What is the URL for this class? ")
    t = crn+".txt"
    urllib.request.urlretrieve(geturl, t)
    cmd = 'grep -n \"crn_in='+crn+'\" '+crn+'.txt | cut -f1 -d:'
    line = str(subprocess.check_output(cmd,shell=True))
    num = ''
    for i in line:
        if i.isnumeric():
            num = num+i
    line_num = int(num)+14
    newRow = {'CRN' : crn, 'URL':geturl,'Line':line_num}
    df = df.append(newRow,ignore_index=True)
df.to_csv('CRN.csv')