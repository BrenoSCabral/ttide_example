import pandas as pd
import numpy as np
import os
import importa_dados
import roda_ttide as rt

fig_path = os.getcwd() + '/fig'

# importando os dados

lou, ama, ifi = importa_dados.importa_tudo()

# lat lou = 29.76861111

ttide_lou = rt.trata_ttide(rt.run_ttide(lou, 29.76861111))
ttide_ama = rt.trata_ttide(rt.run_ttide(ama, 0.75222194))
ttide_ifi = rt.trata_ttide(rt.run_ttide(ifi, -22.88555611))


# freq_lou = importa_dados.pega_frequencia(lou)
# stime_lou = lou.index[0].to_pydatetime()
# freq_ama = importa_dados.pega_frequencia(ama)
# stime_ama = ama.index[0].to_pydatetime()
# freq_ifi = importa_dados.pega_frequencia(ifi)
# stime_ifi = ifi.index[0].to_pydatetime()

# lou = np.array(lou['Altura'])
# ama = np.array(ama['Altura'])
# ifi = np.array(ifi['Altura'])

# ttide_lou = tt.t_tide(lou, dt = freq_lou, stime = stime_lou,
# lat = 29.76861111, synth = 2, out_style = None)
