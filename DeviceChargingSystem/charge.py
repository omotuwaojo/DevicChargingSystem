class Charge:
    def __init__(self, id, name, description, device_name, payment):
        self.id = id
        self.name = name
        self.description = description
        self.device_name = device_name
        self.payment = payment
# charge dictionary
    def charge_dict(self):
        dictionary = {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'device_name': self.device_name,
        'payment': self.payment
            
        }
        return dictionary
#charge = Charge(12, "ojo", "kijds", "ingsfs", True)
#print(charge.charge_dict())