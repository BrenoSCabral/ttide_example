import pandas as pd
import numpy as np
import os
import importa_dados
import roda_ttide as rt
import plota_ttide as ptt

fig_path = os.getcwd() + '/fig/'

# IMPORTANDO OS DADOS #

lou, ama, ifi = importa_dados.importa_tudo()
ama = ama['2017-12-25 10:10:00':].dropna()

lou_jul = lou['2022-07-01 00:00:00':'2022-07-31 23:00:00']
ifi_jul = ifi['2009-07-01 00:00:00':'2009-07-31 23:00:00']
ama_jul = ama['2018-07-01 00:00:00':'2018-07-31 23:00:00']

lou_dez = lou['2021-12-01 00:00:00':'2021-12-31 23:00:00']
ifi_dez = ifi['2009-12-01 00:00:00':'2009-12-31 23:00:00']
ama_dez = ama['2018-01-01 00:00:00':'2018-01-31 23:00:00']

ifi_jul = ifi_jul.sort_index()
ifi_dez = ifi_dez.sort_index()



##############################
# Corte de Julho

ptt.plota_serie(lou_jul, 'Louisiana Julho', fig_path)
ptt.plota_serie(ifi_jul, 'Ilha Fiscal Julho', fig_path)
ptt.plota_serie(ama_jul, 'Amazonas Julho', fig_path)

ttide_lou_jul = rt.run_ttide(lou_jul, 29.76861111)
ttide_ama_jul = rt.run_ttide(ama_jul, 0.75222194)
ttide_ifi_jul = rt.run_ttide(ifi_jul, -22.88555611)

ttide_lou_jul_tratado = rt.trata_ttide(ttide_lou_jul)
ttide_ama_jul_tratado = rt.trata_ttide(ttide_ama_jul)
ttide_ifi_jul_tratado = rt.trata_ttide(ttide_ifi_jul)

nr_lou_jul = rt.numero_forma(ttide_lou_jul_tratado)
nr_ama_jul = rt.numero_forma(ttide_ama_jul_tratado)
nr_ifi_jul = rt.numero_forma(ttide_ifi_jul_tratado)

# PLOTANDO AS COMPONENTES HARMONICAS #

ptt.plota_componentes(ttide_lou_jul, 'Louisiana Julho', fig_path, 0.18)
ptt.plota_componentes(ttide_ama_jul, 'Amazonas Julho', fig_path, 1.8)
ptt.plota_componentes(ttide_ifi_jul, 'Ilha Fiscal Julho', fig_path, 0.35)

# Corte de Dezembro ##################

ptt.plota_serie(lou_dez, 'Louisiana Dezembro', fig_path)
ptt.plota_serie(ifi_dez, 'Ilha Fiscal Dezembro', fig_path)
ptt.plota_serie(ama_dez, 'Amazonas Janeiro', fig_path)

ttide_lou_dez = rt.run_ttide(lou_dez, 29.76861111)
ttide_ama_dez = rt.run_ttide(ama_dez, 0.75222194)
ttide_ifi_dez = rt.run_ttide(ifi_dez, -22.88555611)

ttide_lou_dez_tratado = rt.trata_ttide(ttide_lou_dez)
ttide_ama_dez_tratado = rt.trata_ttide(ttide_ama_dez)
ttide_ifi_dez_tratado = rt.trata_ttide(ttide_ifi_dez)

nr_lou_dez = rt.numero_forma(ttide_lou_dez_tratado)
nr_ama_dez = rt.numero_forma(ttide_ama_dez_tratado)
nr_ifi_dez = rt.numero_forma(ttide_ifi_dez_tratado)

# PLOTANDO AS COMPONENTES HARMONICAS #

ptt.plota_componentes(ttide_lou_dez, 'Louisiana Dezembro', fig_path, 0.18)
ptt.plota_componentes(ttide_ama_dez, 'Amazonas Janeiro', fig_path, 1.8)
ptt.plota_componentes(ttide_ifi_dez, 'Ilha Fiscal Dezembro', fig_path, 0.35)

