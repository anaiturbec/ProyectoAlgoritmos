class Tour:
    def __init__(self, tours):
        self.tours = tours



    def op1(self):
        try:
            cost = 30

            dni = input ('Ingrese su DNI: ')
            print()

            total = int(input('Ingrese el numero de personas que tomaran parte en el tour (max 4): '))

            if total > 4 or total < 0:
                raise Exception 
            else:
                if total <= 2:
                    price = cost * total
                elif total == 3:
                    price = (cost * total) - (cost * 0.10)
                elif total == 4:
                    price = (cost * total) - 2 * (cost * 0.10)
           
            
            cupo = 0
            with open('tour1.txt') as f:
                for line in f:
                    cupo += 1
                if (cupo + total) <= 10: 
                    person = 1
                    while person <= total:
                        with open('tour1.txt', 'a') as f:
                            f.write(f'\n{dni} , {price} , {person}')
                            person += 1
                    print(f'''
                    CUPO CONFIRMADO
                    Cedula: {dni}
                    El tour comienza a las 7 AM
                    Monto: {price} 
                    ''')
                else:
                    print('No hay cupos suficientes')
            
        except:
            print('Uno de los datos es incorrecto')

    def op2(self):
        try:
            cost = 100

            dni = input ('Ingrese su DNI: ')
            print()

            total = int(input('Ingrese el numero de personas que tomaran parte en el tour (max 2): '))

            if total > 2 or total < 0:
                raise Exception 
            else:
                if total <= 2:
                    price = cost * total      
           
            
            cupo = 0
            with open('tour2.txt') as f:
                for line in f:
                    cupo += 1
                if (cupo + total) <= 100: 
                    person = 1
                    while person <= total:
                        with open('tour2.txt', 'a') as f:
                            f.write(f'\n{dni} , {price} , {person}')
                            person += 1
                    print(f'''
                    CUPO CONFIRMADO
                    Cedula: {dni}
                    El tour comienza a las 12 PM
                    Monto: {price} 
                    ''')
                else:
                    print('No hay cupos suficientes')

            with open('tour2.txt', 'r') as f:
                data = f.read()
                print(data)

            
        except:
            print('Uno de los datos es incorrecto')

    def op3(self):
        try:

            dni = input ('Ingrese su DNI: ')
            print()

            total = int(input('Ingrese el numero de personas que tomaran parte en el tour: '))
            
            person = 1
            while person <= total:
                with open('tour3.txt', 'a') as f:
                    f.write(f'\n{dni} , {person}')
                    person += 1
            print(f'''
            CUPO CONFIRMADO
            Cedula: {dni}
            El tour comienza a las 6 AM
            ''')
            
            with open('tour3.txt', 'r') as f:
                data = f.read()
                print(data)

            
        except:
            print('Uno de los datos es incorrecto')

    def op4(self):
        try:
            cost = 40

            dni = input ('Ingrese su DNI: ')
            print()

            total = int(input('Ingrese el numero de personas que tomaran parte en el tour (max 4): '))

            if total > 4 or total < 0:
                raise Exception 
            else:
                if total <= 2:
                    price = cost * total
                elif total == 3:
                    price = (cost * total) - (cost * 0.10)
                elif total == 4:
                    price = (cost * total) - 2 * (cost * 0.10)

           
            
            cupo = 0
            with open('tour4.txt') as f:
                for line in f:
                    cupo += 1
                if (cupo + total) <= 15: 
                    person = 1
                    while person <= total:
                        with open('tour4.txt', 'a') as f:
                            f.write(f'\n{dni} , {price} , {person}')
                            person += 1
                    print(f'''
                    CUPO CONFIRMADO
                    Cedula: {dni}
                    El tour comienza a las 7 AM
                    Monto: {price} 
                    ''')
                else:
                    print('No hay cupos suficientes')
            
        except:
            print('Uno de los datos es incorrecto')

note = input(int('Ingrese un numero '))