# GITHUB: https://github.com/cpazsantos/idmbd
# INSTALLATION: pip install idmbd

import pandas as pd
from requests.auth import HTTPBasicAuth


import urllib2
import os.path
import time
import random
import idmbd

#DOWLOADING FILE FROM DROPBOX FIRST TIME
while not os.path.exists('dev.csv'):
	time.sleep (3*random.random()); #Sleeping less than 3 seconds before going to Dropbox - avoid too many students at once.
	if not os.path.exists('dev.csv'):
		print "DOWLOADING FILE dev.csv FROM DROPBOX BECAUSE LOCAL FILE DOES NOT EXIST!"
		csvfile = urllib2.urlopen("https://dl.dropboxusercontent.com/u/28535341/dev.csv")
		output = open('dev.csv','wb')
		output.write(csvfile.read())
		output.close()

# Carga
df = pd.read_csv("dev.csv")
     
# Ejecucion de algoritmos
dfclean = idmbd.DataCleaning(df)
dfratios = idmbd.Ratios_PCA_DT(dfclean, 'ob_target')
params_regression = idmbd.GeneticLogisticRegression(df,'ob_target')


