class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

customers = [Customer("nomi", "Gold"), Customer("Mary", "Gold")]
print(customers[0].name)
print(customers[1].name)
