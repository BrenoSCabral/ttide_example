# IMPORTANDO BIBLIOTECAS E DEFININDO CAMINHOS #

import pandas as pd
import numpy as np
import os
import importa_dados
import roda_ttide as rt
import plota_ttide as ptt

fig_path = os.getcwd() + '/fig/'

# IMPORTANDO OS DADOS #

lou, ama, ifi = importa_dados.importa_tudo()

ifi = ifi.sort_index()
lou = lou.sort_index()
ama = ama.sort_index()
ama = ama['2017-12-25 10:10:00':].dropna()
# ama['2017-12-25 10:10:00':].resample('1H').mean()

# RODANDO O TTIDE #

ttide_lou = rt.run_ttide(lou, 29.76861111)
ttide_ama = rt.run_ttide(ama, 0.75222194)
ttide_ifi = rt.run_ttide(ifi, -22.88555611)

ptt.plota_serie(lou, 'Louisiana', fig_path)
ptt.plota_serie(ifi, 'Ilha Fiscal', fig_path)
ptt.plota_serie(ama, 'Amazonas', fig_path)

ttide_lou_tratado = rt.trata_ttide(ttide_lou)
ttide_ama_tratado = rt.trata_ttide(ttide_ama)
ttide_ifi_tratado = rt.trata_ttide(ttide_ifi)

nr_lou = rt.numero_forma(ttide_lou_tratado)
nr_ama = rt.numero_forma(ttide_ama_tratado)
nr_ifi = rt.numero_forma(ttide_ifi_tratado)

# PLOTANDO AS COMPONENTES HARMONICAS #

ptt.plota_componentes(ttide_lou, 'Louisiana', fig_path, 0.15)
ptt.plota_componentes(ttide_ama, 'Amazonas', fig_path, 1.8)
ptt.plota_componentes(ttide_ifi, 'Ilha Fiscal', fig_path, 0.35)

