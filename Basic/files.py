# r -> Read
# w -> Write (Creates a file if it doesn't exist, overwrites, and allows writing to the file)
# a -> Add (Write data to the end of the file)
#---#
# r+ -> Read and write
# w+ -> Read, write and created
# a+ -> Write data to the end of the file and created file

# You can add a variable of file url "path"

print("1) Add new name.")
print("2) View list.")

opt = int(input("Select option: "))

if opt == 1 :
    newName = input("Write your name: ")

    names_list = open('client_list', 'a')
    names_list.write(f"{newName} \n")  

    names_list.close()
elif opt == 2:
    last_list = open('client_list', 'r')

    print(last_list.read())   

    last_list.close()
else:
    print("Error, select a just option.")