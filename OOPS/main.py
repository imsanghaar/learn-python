class House:
    def __init__(self, my_address):
        #Self = {}
        self.address = my_address
        #self = {address: "ABC 123"}
        self.no_of_rooms = 3
         #self = {address: "ABC 123", no_of_rooms: 3}


h1 = House("ABC 123")
print(h1.address)
# print(h1.no_of_rooms)

h2 = House("XYZ 456")
print(h2.address)