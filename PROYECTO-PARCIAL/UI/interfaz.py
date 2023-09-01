import pandas as pd
from tabulate import tabulate
#11:34pm

def menu():
    print("\n\n╒═════════════════════════════════════════════════════════════════════════════════════════╕")
    print("│                                                                                         │")
    print("│                  RESULTADOS DE ANALISIS DE LABORATORIO SUELOS EN COLOMBIA               │")
    print("│                                                                                         │")
    print("╘═════════════════════════════════════════════════════════════════════════════════════════╛\n\n")
    registers_limit = int(input("¿Cuál es el número de registros que desea consultar?: "))
    departament_name = input("\nIngrese el departamento: ").upper()
    municipality_name = input("\nIngrese el municipio: ").upper()
    cultivation_name = input("\nIngrese el cultivo: ")
    print("\n")
    return [registers_limit, departament_name, municipality_name, cultivation_name]