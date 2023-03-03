import my_function
import os
my_function.print_options()
option = input()
charges = []
while option != 'x' and option != 'x':
    if option == '1':
        charges.append(my_function.device_charge())
    elif option == '2':
        my_function.save_record(charges)
    elif option == '3':
       my_function.collect_device(charges)
    elif option == '4':
       my_function.view_record(charges)
    elif option == '5':
        my_function.make_enquire(charges)
    else :
        print('the given command doesnt exist..')
    input("print enter to continue...")

    # cls for cleaning the screen
    os.system("cls")
    # asking for input
    my_function.print_options()
    option = input()

