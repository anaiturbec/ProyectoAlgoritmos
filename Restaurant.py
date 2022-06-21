import json

class Restaurant:
    def __init__(self, ship_retaurant):
        self.ship_restaurant = ship_retaurant
   

    # AGREGAR A MENU
    def menu_op123(self):
    
        try:
            # Tipo
            food_beverage = input(''' Elija la categoria:
            
            1. Bebida
            2. Alimento
            
            Ingrese la opcion de su preferencia >>> ''')
            print()

            # OPCION 1
            if self.ship_restaurant == '1':

                # Nombre 
                name_input = str(input('Ingrese el nombre del alimento / bebida >>> ')).lower()
                print()

                # Precio
                cost_input = float(input('Ingrese el precio del producto >>> '))
                total_cost = cost_input + (cost_input * 0.16)
                print()
            
            
                # Menu de Bebidas
                if food_beverage == '1':
                    
                    # Tamano de bebida
                    size_input = input('''Elija un tamano:
                
                    1. Pequeno
                    2. Mediano
                    3. Grande
                    
                    Ingrese la opcion de su preferencia >>> ''')
                
                    if size_input == '1':
                        size = 'Pequeno'
                    elif size_input == '2':
                        size = 'Mediano'
                    elif size_input == '3':
                        size = 'Grande'
                    else:
                        raise Exception
                        

                    with open('drink.txt', 'a') as f:
                        f.write(f'\n{name_input} , {size} , {total_cost}')

            
                # Menu de Alimentos
                if food_beverage == '2':

                    # Tipo de Alimento
                    packaging = input('''Elija el tipo de alimento:

                    1. Empaque
                    2. De Preparacion

                    Ingrese la opcion de su preferencia >>> ''')

                    if packaging == '1':
                        pack = 'Empaque'
                    elif packaging == '2':
                        pack = 'Preparacion'
                    else:
                        raise Exception
                        

                    with open('food.txt', 'a') as f:
                        f.write(f'\n{name_input}, {pack}, {total_cost}')
        
            
                print()
                print('Agregado exitosamente!!!')

            if self.ship_restaurant == '2':

                name = input('Ingrese el nombre de lo que desea eliminar >>> ').lower()

                # Menu de Bebidas
                if food_beverage == '1':
                    file = 'drink.txt'
                # Menu de Alimentos
                elif food_beverage == '2':
                    file = 'food.txt'
                else:
                    raise Exception
                        
                with open(file) as f:
                    a = []
                    for line in f:
                        if name not in line.split(',')[0]:
                            a.append(line)
                    
                with open(file, 'w+') as f:
                    for i in a:
                        f.write(f'\n{i}')
                
                print()
                print('Eliminado exitosamente!!!')
            
            if self.ship_restaurant == '3':

                name = input('Ingrese el nombre del producto que desea modificar: ').lower()

                # Menu de Bebidas
                if food_beverage == '1':
                    file = 'drink.txt'
                # Menu de Alimentos
                elif food_beverage == '2':
                    file = 'food.txt'
                else:
                    raise Exception

                with open(file) as f:
                    a = []
                    for line in f:
                        if name not in line.split(',')[0]:
                            a.append(line)
                    
                with open(file, 'w+') as f:
                    for i in a:
                        f.write(f'\n{i}')
                            
                # Nombre 
                name_input = str(input('Ingrese el nombre del alimento / bebida >>> ')).lower()
                print()

                # Precio
                cost_input = float(input('Ingrese el precio del producto >>> '))
                total_cost = cost_input + (cost_input * 0.16)
                print()
            
            
                # Menu de Bebidas
                if food_beverage == '1':
                    
                    # Tamano de bebida
                    size_input = input('''Elija un tamano:
                
                    1. Pequeno
                    2. Mediano
                    3. Grande
                    
                    Ingrese la opcion de su preferencia >>> ''')
                
                    if size_input == '1':
                        size = 'Pequeno'
                    elif size_input == '2':
                        size = 'Mediano'
                    elif size_input == '3':
                        size = 'Grande'
                    else:
                        raise Exception
                        

                    with open('drink.txt', 'a') as f:
                        f.write(f'\n{name_input} , {size} , {total_cost}')
            
                # Menu de Alimentos
                if food_beverage == '2':

                    # Tipo de Alimento
                    packaging = input('''Elija el tipo de alimento:

                    1. Empaque
                    2. De Preparacion

                    Ingrese la opcion de su preferencia >>> ''')

                    if packaging == '1':
                        pack = 'Empaque'
                    elif packaging == '2':
                        pack = 'Preparacion'
                    else:
                        raise Exception
                        

                    with open('food.txt', 'a') as f:
                        f.write(f'\n{name_input}, {pack}, {total_cost}')
                    

                
                print()
                print('Modificado exitosamente!!!')

                

        except:
            print('Uno de los datos ingresados es incorrecto')      
            


    # CREAR COMBO
    def combo_op45(self):
        try:
            if self.ship_restaurant == '4':
                # Nombre 
                combo_input = str(input('Ingrese el nombre del combo >>> ')).lower()
                print()

                # Productos
                combo_product = input('Ingrese un minimo de 2 productos necesarios para el combo >>> ').split( )
                if len(combo_product) < 2:
                    print('Debe ingresar mas de 2 productos!')

                # Precio
                combo_cost = float(input('Ingrese el precio del producto >>> '))
                cost = combo_cost + (combo_cost * 0.16)
                print()
                    

                with open('combo.txt', 'a') as f:
                    f.write(f'\n{combo_input} , {combo_product} , {cost}')
            

                with open('combo.txt', 'r') as f:
                    data = f.read()
                print(data)
                
                print()
                print('Agregado exitosamente!!!')
            
            if self.ship_restaurant == '5':
                name = input('Ingrese el nombre del combo que desea eliminar: ')

                with open('combo.txt') as f:
                    b = []
                    for line in f:
                        if name not in line.split(',')[0]:
                            b.append(line)
                    
                with open('bus.txt') as f:
                    a = []
                    for line in f:
                        if placa in line.split(",")[0]:
                            a.append(line.split(",")[0])

                with open('combo.txt', 'w+') as f:
                    for i in b:
                        f.write(f'\n{i}')
                            
                with open('combo.txt', 'r') as f:
                    data = f.read()
                    print(data)
                
                print()
                print('Eliminado exitosamente!!!')
          

        except:
            print('Uno de los datos ingresados es incorrecto')

    def search67(self):
        
        try:
            if self.ship_restaurant == '6':
                # Tipo
                food_beverage = input(''' Elija la categoria:
                
                1. Bebida
                2. Alimento
                
                Ingrese la opcion de su preferencia >>> ''')
                if food_beverage == '1':
                    file = 'drink.txt'
                elif food_beverage == '2':
                    file = 'food.txt'
                else:
                    raise Exception

            if self.ship_restaurant == '7':
                file = 'combo.txt'
            
            range_name = input('''Desea buscar por:

            1. Nombre
            2. Rango de precio
            
            Ingrese la opcion de su preferencia >>> ''')

            if range_name == '1':
                name = input('Ingrese el nombre del producto que desea buscar >>> ')
                with open(file) as f:
                    d = []
                    for line in f:
                        if name in line.split(',')[0]:
                            d. append(line.split(','))
                    for i in d:
                        print(f'''
                        Nombre: {i[0]}
                        Tipo: {i[1]}
                        Precio: {i[2]}
                        ''')
            # PREGUNTARLE A ALGUIEN COMO HIZO EL PRICE RANGE
            elif range_name == '2':
                high = float(input('Ingrese el maximo de precio >>> '))
                low =  float(input('Ingrese el minimo de precio >>> '))

                with open(file) as f:
                    e = []
                    h = []
                    for line in f:
                        e.append(int(line.split(',')[2]))
                        print(e)
                    for line in f:
                        for i in e:
                            if (low <= i <= high):
                                h.append(line)
                    print(h)

        except Exception as ex:
            print(ex)


