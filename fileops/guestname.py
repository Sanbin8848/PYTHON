filename = 'guest.txt'

with open(filename,'a') as file_object:
    while True:
        name = input("Please input your name:")
        if name != 'q':
            file_object.write(name+",you are welcome to our home.\n")
        else:
            break






    # guest_name = input("Please input your name:")
    # file_object.write(guest_name)