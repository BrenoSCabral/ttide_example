import matplotlib.pyplot as plt
import numpy as np

def plota_serie(df, local, fig_path):
  fig = plt.figure(figsize=(11*1.2,5*1.2), dpi=70)
  ax1 = fig.add_subplot(111)
  ax1.set_title(local, fontsize = 20)
  plt.plot(df.index, df['Altura'])

  ax1.set_ylabel('Nível de água', fontsize = 20)
  ax1.set_xlabel('Data', fontsize = 20)
  plt.grid()

  plt.savefig(fig_path+'serie_'+local.replace(' ', '_'))

  plt.close()

def plota_componentes(df, local, fig_path, lim_max):
  ######################################################### PLOT ########################################################
  fig = plt.figure(figsize=(11*1.2,5*1.2), dpi=70)
  ax1 = fig.add_subplot(111)

  #plt.xticks(x_plot, parametros_plot,fontsize=16, weight='bold')

  ax1.set_title(local,fontsize=20, weight='bold')

  #loc = 0.9
  for i in range(len(df['fu'])):
      if df ["snr"][i] >= 2:
          legenda = df["nameu"][i]
          legenda = str(legenda)
          #print(type(legenda))
          legenda = legenda.replace('\'', '')
          legenda = legenda.replace('b', '')
          legenda = legenda.replace('  ', '')
          legenda = legenda.replace(' ', '')
          plt.bar(df['fu'][i]* 24,df ["tidecon"][i][0],align='center',width=0.08,
                  label=legenda)
  #
  ####
  ax1.grid(zorder=0)
  #ax1.set_xscale('log')
  #ax1.legend(['Medido','Modelado | Período cada ponto','Modelado | Período B a C'], ncol=3, loc='upper center',fontsize=20)
  ax1.set_ylabel('Amplitude (m)',fontsize=20)
  ax1.set_xlabel('Frequência (cpd)',fontsize=20)
  ax1.set_xticks(np.arange(0,9,1))
  ax1.set_xlim(0,8)
  ax1.set_ylim(0,lim_max)
  ax1.legend(ncol=4,fontsize=14)
  plt.setp(ax1.get_yticklabels(),fontsize=14)
  plt.setp(ax1.get_xticklabels(),fontsize=14)
  plt.tight_layout()
  ### Salvando as figuras em png 
  plt.savefig(fig_path+'componentes_'+local.replace(' ', '_'))

  plt.close()