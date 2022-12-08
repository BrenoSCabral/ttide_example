import ttide as tt
import numpy as np
import pandas as pd

def pega_frequencia(df):
  ''''
  retorna a frequencia horaria de medicao
  '''
  res = (pd.Series(df.index[1:]) - pd.Series(df.index[:-1])).value_counts()
  freq = str(res.index[0])
  freq = float(freq[len(freq)-5:len(freq)-3])

  if freq == 0:
      freq = str(res.index[0])
      freq = float(freq[len(freq)-8:len(freq)-6])
      
      #frequência para a análise harmônica
      dt = freq/1
      freq_harmo = str(freq) + ' Min'
  else:
      #frequência para a análise harmônica
      dt = freq/60
      freq_harmo = str(freq) + ' Min'
  return(dt)

def trata_dados(df):
  '''
  extrai variaveis do dataframe para possibilitar o ttide
  '''
  freq = pega_frequencia(df)
  stime = df.index[0].to_pydatetime()
  arr = np.array(df[df.columns[0]])

  return(freq, stime, arr)

def run_ttide(df, lat):
  '''
  pega um dataframe, uma latitude e faz o necessario para rodar
  o ttide
  '''
  freq, stime, arr = trata_dados(df)
  ttide = tt.t_tide(arr, dt = freq, stime = stime,
    lat = lat, synth = 2, out_style = None)
  return ttide

def trata_ttide(df):
  # Pegando as componentes com signal-to-noise ratio acima de 2
  lat_dados_df = df['lat']
  freq_dados_df = []
  nameu_dados_df = []
  tidecon_dados_df = [] 
  #lat_dados_df = []  
  synteses_dados_df = []
  fase_dados_df = []
  ampli_dados_df = []
  for i in range(len(df['fu'])):
      if df ["snr"][i] >= 2:
          freq_dados_df.append(df['fu'][i])
          nameu_dados_df.append(df["nameu"][i])
          tidecon_dados_df.append(df ["tidecon"][i])
          ampli_dados_df.append(df ["tidecon"][i][0])
          fase_dados_df.append(df ["tidecon"][i][2])

  freq_dados_df_cpd =[]
  fase_dados_df_local = []

  fr = 0
  fase = 0
  for i in range(len(freq_dados_df)):
      #Transformando de cph para cpd
      fr = freq_dados_df[i] * 24
      freq_dados_df_cpd.append(fr)
      
      fase = fr + fase_dados_df[i]
      if fase >= 360:
          fase = fase - 360
          fase_dados_df_local.append(fase)
      else:
          fase_dados_df_local.append(fase)
          
  info_har_dados_df = pd.DataFrame({'Componente de Mare':nameu_dados_df,'Frequencia (cpd)':freq_dados_df_cpd,
                                        'Amplitude (m)':ampli_dados_df,'Fase (°)':fase_dados_df_local})
  info_har_dados_df.index = info_har_dados_df['Componente de Mare']

  del info_har_dados_df['Componente de Mare']

  return info_har_dados_df.sort_values(by=['Amplitude (m)'], ascending=False)

def numero_forma(df):
  nf = 0
  k1=0
  o1=0
  s2=0
  m2=0
  for i in range(len(df)):
      #print(df.index[i])
      if df.index[i] == b'K1  ':
          k1= df['Amplitude (m)'][i]
          
      if df.index[i] == b'O1  ':
          o1= df['Amplitude (m)'][i]
          
      if df.index[i] == b'S2  ':
          s2= df['Amplitude (m)'][i]
          
      if df.index[i] == b'M2  ':
          m2= df['Amplitude (m)'][i]

          
  nf = (k1+o1)/(s2+m2)
  print(nf)

  if nf <= 0.25:
      print('Maré semi-diurna')
      
  elif nf > 0.25 and nf <= 1.5:
      print('Maré mista com predominância semi-diurna')
      
  elif nf > 1.5 and nf <= 3.0:
      print('Maré mista com predominância diurna')
      
  elif nf > 3.0:
      print('Maré diurna')
      
  return nf