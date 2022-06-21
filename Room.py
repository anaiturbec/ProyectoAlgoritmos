import string

class Room:
  def __init__(self, cruises):

      self.cruises = cruises
    

  def r1(self):
    try:
      room_input = input('''  Desea realizar su compra en base a:

            1. Barco 
            2. Destino

        Ingrese la opcion de su preferencia >>>  ''')
      print()
      # Compra en base a barco
      if room_input == '1':
          for i, cruise in enumerate(self.cruises):
              ship = cruise['name']
              print (f'       {i+1}. {ship}')

          print ()
          ship_input = int(input('Ingrese la opción de su preferencia >>> '))
      
      # Compra en base a destino
      elif room_input == '2':
          for i, cruise in enumerate(self.cruises):
              destination = cruise['route']
              print (f'       {i+1}. {destination}')

          print ()
          destination_input = int(input('Ingrese la opción de su preferencia >>> '))
      else:
          print('El dato ingresado es invalido')

      if ship_input == 1 or destination_input == 1:
            file = 'register1.txt'
      elif ship_input == 2 or destination_input == 2:
            file = 'register2.txt'
      elif ship_input == 3 or destination_input == 3:
            file = 'register3.txt'
      elif ship_input == 4 or destination_input == 4:
            file = 'register4.txt'
      else: 
        raise Exception
      
      # Seleccion de cuartos
      room_kind_input = input('''Elija un tipo de habitacion

      1. Simple
      2. Premium
      3. VIP

      Ingrese la opcion de su preferencia >>> ''')
      print()

      # Forma de entrarle a el dato del diccionario que guarda la capacidad por cuarto
      if room_kind_input == '1':
          x = 'simple'
      elif room_kind_input == '2':
          x = 'premium'
      elif room_kind_input == '3':
          x = 'vip'
      else:
          raise Exception
      


      # Oferta de cuartos relacionada a la cantidad de pasajeros que viajan juntos
      if room_input == '1':
          index = ship_input - 1
      elif room_input == '2':
          index = destination_input - 1
      

      travelers = int(input('Ingrese la cantidad de personas que viajaran con nosotros >>> '))
      num = 1
      
      while travelers > (self.cruises[index]['capacity'][x] * num):
          num += 1
      print(f'Debido a la cantidad de personas en su grupo, necesitara {num} habitacion/es de tipo {x}')

      data = 1
      # REGISTRO
      while data <= travelers:  
          print()     
          data_name = input(f'Ingrese el nombre del pasajero {data} >>> ')
          name = []
          name.append(data_name)
          data_dni = int(input(f'Ingrese la cedula del pasajero {data} >>> '))
          dni = []
          dni.append(data_dni)
          age = int(input(f'Ingrese la edad del pasajero {data} >>> '))
          a = []
          a.append(age)

          # SE AGREGA CLIENTE 
          with open('client.txt', 'a') as f:
            f.write(f'\n {data_name} , {data_dni} , {age}')
          
          data+=1

      cost = self.cruises[index]['cost'][x]
      price = cost * num  
      tax = price + (cost * 0.16)
      abc = string.ascii_uppercase
    
      # SE AGREGA GRUPO A CUARTOS
      print()
      hallway = self.cruises[index]['rooms'][x][0]
      room = self.cruises[index]['rooms'][x][1]
          
      for i in range(hallway):
          for j in range(room):
              print(f'{abc[i]}{j+1}  ', end ='', sep = '\t')
          print(' ')
      print()

      for i in range(1, num+1):
        r = []
        room_number = input('Ingrese el cuarto que desea ocupar >>> ').lower()
        
        with open(file, 'r') as f:
          for line in f:
                if room_number not in line.split(',')[0]:
                      info = open(file, 'a')
                      info.write(f'\n {room_number} , {name} , {dni} , {a} , {tax}')
                      r.append(room_number)
    
                      
                else:
                      print('Ese cuarto esta ocupado, seleccione otro')
      print(f'''
      COMPRA EXITOSA
      Habitaciones : {r}
      Tax: {tax}
      ''')
    except:
      print('Uno de los datos ingresados es invalido')
                      




  def r2(self):
    try:
      # barco
      if room_input == '1':
          for i, cruise in enumerate(self.cruises):
              ship = cruise['name']
              print (f'       {i+1}. {ship}')

          print ()
          ship_input = input('Ingrese el barco que tenga el cuarto que desea desocupar >>> ')

      room_name = input('Ingrese el nombre de la habitacion que desea desocupar >>> ')

      if ship_input == '1':
            file = 'register1.txt'
      elif ship_input == '2':
            file = 'register2.txt'
      elif ship_input == '3':
            file = 'register3.txt'
      elif ship_input == '4':
            file = 'register4.txt'
      else:
            raise Exception

      with open(file) as f:
          a = []
          for line in f:
              if room_name not in line.split(',')[0]:
                  a.append(line)
                      
      with open(file, 'w+') as f:
          for i in a:
              f.write(f'\n{i}')

      print('Habitacion desocupada exitosamente!!')
    except:
      print('Uno de los datos ingresados es invalido')

      

  def r3(self):
    try:
      if room_input == '1':
            for i, cruise in enumerate(self.cruises):
                ship = cruise['name']
                print (f'       {i+1}. {ship}')

            print ()
            ship_input = input('Ingrese el barco que tenga el cuarto que desea desocupar >>> ')

      room_name = input('Ingrese el nombre de la habitacion que desea buscar >>> ')

      if ship_input == '1':
            file = 'register1.txt'
      elif ship_input == '2':
            file = 'register2.txt'
      elif ship_input == '3':
            file = 'register3.txt'
      elif ship_input == '4':
            file = 'register4.txt'
      else:
            raise Exception

      with open(file) as f:
          a = []
          for line in f:
              if room_name in line.split(',')[0]:
                  a.append(line)

          for i in a:
            print(f'''
            Habitacion: {a[0]}
            Nombres: {a[1]}
            Cedulas de Grupo: {a[2]}
            Precio: {a[3]}
            ''')
                      
      
    except:
      print('Uno de los dato ingresados es invalido')