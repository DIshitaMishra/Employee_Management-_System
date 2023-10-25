import add
from Exception import OptionException

def pr():
    while True:
        print("\n1. Add Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. Find Record")
        print("5. Find All Records")
        print("6. Exit")
        try:
            choice = int(input('Enter your choice: '))

            if choice < 1 or choice > 6:
                raise OptionException("Option cannot be other than 1-6. Thank You")

            try:
                if choice == 1:
                    print("\n1. Add Record")
                    add.adding()

                elif choice == 2:
                    print("2. Update Record")
                    add.update()

                elif choice == 3:
                    print("3. Delete Record")
                    add.deleteR()

                elif choice == 4:
                    print("4. Find Record")
                    add.find()

                elif choice == 5:
                    print("5. Find All Records")
                    add.findAll()

                elif choice == 6:
                    print("6. Exiting....")
                    break
            except OptionException as e:
                print(e)
        except ValueError:
            print("Select a correct option...")

        

        


        
            


