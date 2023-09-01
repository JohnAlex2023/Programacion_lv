from API import API
from UI import interfaz
from UI import filtro_de_datos
#11:34pm

if __name__ == '__main__':
    registers_limit, departament_name , municipality_name , cultivation_name = interfaz.menu()
    data = API.get_data(registers_limit, departament_name, municipality_name , cultivation_name)
    filtered_data = filtro_de_datos.filter_columns(data)
    print(filtered_data)