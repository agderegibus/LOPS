import pandas as pd
import requests
import time 
import random

url_saldos_totales = "https://riskzone.anywhereportfolio.com.ar:9099/api/saldosconsolidados"

tokenobj = {'key': 'value'}
REQUEST_GENERAL = requests.get(url_saldos_totales, json = tokenobj)
data  = (REQUEST_GENERAL.json())
df = pd.DataFrame(data)


df.to_excel("Exportacion_test.xls")