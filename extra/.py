class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

c = customer("Nyari", "Gold")
print(c.name, c.membership_type)
