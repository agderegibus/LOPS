import pandas as pd
import requests
import time 
import random

def format_float(value):
    return f'{value:,.2f}'

pd.options.display.float_format = format_float

url_saldos_totales = "https://riskzone.anywhereportfolio.com.ar:9099/api/saldosconsolidados"

tokenobj = {'key': 'value'}
REQUEST_GENERAL = requests.get(url_saldos_totales, json = tokenobj)
data  = (REQUEST_GENERAL.json())
df = pd.DataFrame(data)
df = df[df["FinalidadID"] == 2]
df["SaldoInicialAP5"] = df["SaldoInicial"] + df["MargenRequeridoAnterior"]
df["SaldoFinalVerificado"] = df["SaldoInicialAP5"] + df["IngresoVerificado"] + df["EgresoVerificado"] + df["MargenRequeridoTotal"]
df["SaldoFinalNoVerificado"] = df["SaldoFinalVerificado"] + df["IngresoNoVerificado"] + df["EgresoNoVerificado"]

lop_test = df[["MiembroCompensadorCodigo","CuentaCompensacionCodigo","CuentaNeteoCodigo","MonedaDescripcion","SaldoInicialAP5","MargenRequeridoDelDia","SaldoFinalVerificado","SaldoFinalNoVerificado"]]
lop_negativo = lop_test.loc[(lop_test["SaldoFinalVerificado"] < 0)]# | (lop_test["SaldoFinalNoVerificado"] == 0) ]
print(lop_negativo["MiembroCompensadorCodigo"].value_counts())
time.sleep(3)

