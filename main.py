import requests
from Cruise import Cruise
from Tour import Tour
from Room import Room
from Restaurant import Restaurant

def api_info():
    
    # API con informacion pertinente al programa
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
    
    response = requests.request('GET', url)
    
    return response.json()


def cruise_search(): 
    
    cruises = api_info()
    c = []
    # Formas de ingresar a los datos en el diccionario
    for cruise in cruises:
        # a
        name = cruise['name']
        # b
        route = cruise['route']
        # c
        departure = cruise['departure']
        # d
        simple_cost = cruise['cost']['simple']
        premium_cost = cruise['cost']['premium']
        vip_cost = cruise['cost']['vip'] 
        # e rooms
        simple_room = cruise['rooms']['simple'][1]
        premium_room = cruise['rooms']['premium'][1]
        vip_room = cruise['rooms']['vip'][1]
        # e hallways 
        simple_room_hallway= cruise['rooms']['simple'][0]
        premium_room_hallway = cruise['rooms']['premium'][0]
        vip_room_hallway = cruise['rooms']['vip'][0]
        # g
        simple_capacity = cruise['capacity']['simple']
        premium_capacity = cruise['capacity']['premium']
        vip_capacity = cruise['capacity']['vip']

        cruise = Cruise(name, route, departure, simple_cost, premium_cost, vip_cost, simple_room, premium_room, vip_room, simple_room_hallway, premium_room_hallway, vip_room_hallway, simple_capacity, premium_capacity, vip_capacity, cruises)
    

        c.append(cruise.info())
    
    return c


def sell_room():
    while True:
        # diccionario API
        cruises = api_info()

        rooms = input('''
        1. Ocupar habitacion
        2. Desocupar habitacion
        3. Buscar habitacion
        4. Regresar a la pantalla principal
        
        Ingrese la ocion de su preferencia >>> ''')
        

        room = Room(cruises)

        if rooms == '1':
            room.r1()
        elif rooms == '2':
            room.r2()
        elif rooms == '3':
            room.r3()
        else:
            break
            


           

def buy_tours():
    while True:
        try:
            tours = input('''   Tours:

                1. Tour en el Puerto 
                2. Degustacion de comida local
                3. Trotar por el pueblo o ciudad
                4. Visita a Lugares historicos
                5. Regresar a la pagina principal

            Ingrese la opcion que desee >>> ''')
            print()
            
            tour = Tour(tours)

            if tours == '1':
                tour.op1()
            elif tours == '2':
                tour.op2()
            elif tours == '3':
                tour.op3()
            elif tours == '4':
                tour.op4()
            else:
                break
        except:
            print ('Uno de los datos ingresados es invalido')

         
def restaurant():

    while True:

        ship_restaurant = input('''Elija el restaurante de un barco:

        1. Agregar al Menu
        2. Eliminar del Menu
        3. Modificar el Menu
        4. Agregar al Menu de Combos
        5. Eliminar del Menu de Combos
        6. Buscar Producto por Nombre 
        7. Buscar Combos por Nombre 
        8. Regresar a la pantalla principal
        
        Ingrese la opcion de su preferencia >>> ''')
        print()

        rest = Restaurant(ship_restaurant)

        if ship_restaurant == '1' or ship_restaurant == '2' or ship_restaurant == '3':
            rest.menu_op123()
        elif ship_restaurant == '4' or ship_restaurant == '5':
            rest.combo_op45()
        elif ship_restaurant == '6' or ship_restaurant == '7':
            rest.search67()
        else:
            break
        


def main():
    while True:
        client = input('''  Bienvenido a Samán Caribbean

        1. Ver información de cruceros
        2. Comprar habitaciones
        3. Comprar Tours
        4. Restaurante
        5. Salir

        Ingrese la opción de su preferencia >>> ''')
        if client == '1':
            cruise_search()
        elif client == '2':
            sell_room()
        elif client == '3':
            buy_tours()
        elif client == '4':
            restaurant()
        else:
            print ('Hasta Luego!!!')
            break

if __name__ == "__main__":
    main()