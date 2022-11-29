import pandas as pd
import os

dados = os.getcwd() + '/dados'

def importa_louisiana():
  ''''
  importa os dados de louisiana
  '''
  lou = pd.read_csv(dados+'/calcasieu_path.csv')

  lou['Altura'] = lou['Verified (ft)'] * 0.3048

  lou['data'] = lou['Date'] + ' ' + lou['Time (GMT)']
  lou = lou.set_index(pd.to_datetime(lou['data']))

  lou = lou.drop(['Preliminary (ft)', 'Verified (ft)', 
    'Date', 'Time (GMT)', 'Predicted (ft)', 'data'], axis = 1)
  
  return lou

  # Lat/Lon = 29°46'07.0"N 93°20'34.2"W

def importa_amapa():
  ''''
  importa os dados do amapa
  '''

  ama = pd.read_csv(dados + '/serie 1_estacao ponta do CEU_amazonas_2017-2018.txt', 
                      sep = ' ', decimal = ',', header=None)
  ama.columns = ['data', 'hora','Altura']
  ama = ama.set_index(pd.to_datetime(ama['data'] + ' ' + ama['hora']))
  ama = ama.drop(['data', 'hora'], axis = 1)

  return ama

  # Lat/Lon = 0° 45'7.999" N e Longitude: 49° 13' 3" W;

def importa_ilha_fiscal():
  ''''
  importa os dados da ilha fiscal
  '''

  ifi = pd.read_csv(dados + '/serie 2_mare_ilhafiscal_2009.txt', sep = ';', header = None)
  ifi.columns = ['data', 'Altura', '-']
  ifi = ifi.set_index(pd.to_datetime(ifi['data']))
  ifi = ifi.drop(['data','-'], axis  =1)
  ifi.columns = ['Altura']
  ifi['Altura'] = ifi['Altura']/100

  return ifi

  # 22° 53' 8.002" S e Longitude: 43° 10'0.001" W)

def analisa_serie(df):
  ''''
  checa por buracos na serie temporal

  leva um dataframe com a primeira coluna sendo a elevacao como parametro
  '''

  cont, cont_max = 0, 0
  col = df.columns[0]
  data_min = df.index[0]
  data_max = df.index[-1]

  for i, data in zip(df[col].isnull(), df.index):
    if not i:
      if cont == 0:
        data_min_aux = data
      cont +=1
      data_max_aux = data
    else:
      if cont_max < cont:
        cont_max = cont
        cont = 0
        data_min = data_min_aux
        data_max = data_max_aux
      else:
        cont = 0

  return df[data_min:data_max]
      

def importa_tudo():
  ''''
  importa todos os dados e checa por buracos em todas
  as series
  '''

  return(
    analisa_serie(importa_louisiana()), 
    analisa_serie(importa_amapa()), 
    analisa_serie(importa_ilha_fiscal())
    )