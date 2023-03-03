""" charging app """
from charge import Charge
import json
def print_options():
    print(".............................")
    print ("   WELCOME TO CHARGING SHOP")
    print(".............................")
    print("     How can we help:    ")
    print("1: Charge Smartphone/Any device")
    print("2: Save record")
    print("3: Collect your device")
    print("4: view record")
    print("5: Make enquire")

# charging function
def input_charging_info():
    id = input("ID: ")
    name = input("name: ")
    description = input("description: ")
    device_name = input("device_name: ")
    payment = input("payment: y for True, n for False ") 
    payment = (payment == "y" or payment != "n")
    return{
        'id':id,
        'name': name,
        'description' : description,
        'device_name' : device_name,
        'payment': payment

   }


def device_charge():
    print("Please enter your device information")
    charge_input =input_charging_info()
    charge =Charge(charge_input['id'], charge_input['name'], charge_input['description'], 
                    charge_input['device_name'], charge_input['payment'])
    print(charge.charge_dict())
    return charge

def save_record(charges):
    json_charges = []
    for charge in charges:
        json_charges.append(charge.charge_dict())
    try:
        file = open("charges.dat","w")
        file.write(json.dumps(json_charges, indent=10))
        print("record successfully saved")
    except:
        print("we had an error saving record")

def find_device(charges, id):
    for index, charge in enumerate(charges):
        if charge.id ==id:
            return index
        return None

def collect_device(charges):
    id = input("enter the id of the collector the device: ")
    index = find_device(charges, id)
    if index != None:
        charges[index].collect = True
        print("Device collected successfully")
    else:
        print("could not find the device you are looking for")

def view_record(charges):
    id = input("Please enter you id: ")
    index = find_device(charges, id)
    if index != None:
        print(charges[index].charge_dict())
    else:
        print("we could not find the device")

def make_enquire(charges):
    print("how can we help u with our services\n please go through the options in the mean")

        

   
