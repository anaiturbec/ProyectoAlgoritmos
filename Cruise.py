class Cruise:
    def __init__(self, name, route, departure, simple_cost, premium_cost, vip_cost, simple_room, premium_room, vip_room, simple_room_hallway, premium_room_hallway, vip_room_hallway, simple_capacity, premium_capacity, vip_capacity, cruises):
        self.name = name
        self.route = route
        self.departure = departure
        self.simple_cost = simple_cost
        self.premium_cost = premium_cost
        self.vip_cost = vip_cost
        self.simple_room = simple_room
        self.premium_room = premium_room
        self.vip_room = vip_room
        self.simple_room_hallway = simple_room_hallway
        self.premium_room_hallway = premium_room_hallway
        self.vip_room_hallway = vip_room_hallway
        self.simple_capacity = simple_capacity
        self.premium_capacity = premium_capacity
        self.vip_capacity = vip_capacity

    def info(self):
        
        print (f''' 
        a. Nombre: {self.name}
        b. Ruta: {self.route}
        c. Fecha de Salida: {self.departure}
        d. Costo de Habitaciones:
            - Sencilla: {self.simple_cost}
            - Premium: {self.premium_cost}
            - VIP: {self.vip_cost}
        e. Informacion sobre Habitaciones:
            - Sencilla: En este piso hay {self.simple_room} habitaciones y {self.simple_room_hallway} pasillos
            - Premium: En este piso hay {self.premium_room} habitaciones y {self.premium_room_hallway} pasillos
            - VIP: En este piso hay {self.vip_room} habitaciones y {self.vip_room_hallway} pasillos
        g. Capacidad por Habitacion:
            - Sencilla: {self.simple_capacity}
            - Premium: {self.premium_capacity}
            - VIP: {self.vip_capacity}
        ''')


