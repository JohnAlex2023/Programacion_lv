import pandas as pd
from tabulate import tabulate
#11:34pm

def filter_columns(data):
    print("\n\n")
    filtered_data = data[['departamento', 'municipio', 'cultivo','topografia', 'ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']]
    filtered_data.columns = ['DEPARTAMENTO', 'MUNICIPIO', 'CULTIVO', 'TOPOLOGIA', 'pH', "FOSFORO(P)", "POTASIO(K)"]
    tabulated_data = tabulate(filtered_data, headers='keys', tablefmt='fancy_grid') 
    return tabulated_data

