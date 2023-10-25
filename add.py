from mysql.connector import connect, errors
import Exception
import Prac

a = connect(host='localhost', user='root', password = 'root',database = 'sys')
b = a.cursor()


def one():

    sql = 'insert into emp values(%s,%s,%s,%s)'
    try:
        sno = int(input('Enter Serial number of Employee: '))
        name = input('Enter Name of the Employee: ')
        sal = int(input("Enter salary of the Employee: "))
        try:
            if sal < 0:
                raise Exception.SalaryException("Salary Should not be Negative.\n Try Again with Postive Value")
            else:
                address = input("Enter the Address of the Employee: ")
                val = (sno, name, sal, address)
                b.execute(sql, val)
                a.commit()
                print("Thank you! Your Entry is added successfully...")
        except Exception.SalaryException as e:
            print(e)

    except ValueError:
        print('Serial Number Must be Numerical')


def many():
    list = []
    sql = 'insert into emp values (%s,%s,%s,%s)'
    while True:
        try:
            sno = int(input('Enter Serial number of Employee: '))
            name = input('Enter Name of the Employee: ')
            sal = int(input("Enter salary of the Employee: "))
            try:
                if sal < 0:
                    raise Exception.SalaryException("Salary Should not be Negative.\n Try Again with Postive Value")
                address = input("Enter the Address of the Employee: ")
                val = (sno, name, sal, address)
                list.append(val)
                print(list)
                b.executemany(sql, list)
                a.commit()
                s = input("Enter Yes if you want to Add more Entry And Enter No for continue: ")
                if s.lower() == "no":
                    print("Thank you! Your Entries are added successfully...")
                    list.clear()
                    break
            except Exception.SalaryException as e:
                print(e)
        except ValueError:
            print('Serial Number Must be Numerical')

def adding():
    print('1.For Adding Single Record')
    print('2.For Adding Multiple Record')

    c = int(input("Select your choice: "))
    if c == 1:
        print('1. Adding Single Record')
        one()

    elif c == 2:
        print('2. Adding Multiple Record')
        many()

def find():
    sql = ('select * from emp where sno = %s')
    try:
        sno = int(input("Enter the Serial Number of Employee: "))
        if sno not in Prac.f:
            raise Exception.SerialNoException("The Serial Number doesn't exist...")
        try:
            val = (sno,)
        except errors.InternalError:
            print("          You can Continue")
        b.execute(sql, val)
        r = b.fetchone()
        print("============================================")
        print("Sno    Name     Salary    Address")
        print("============================================")
        print(r[0], "    ", r[1], "   ", r[2], "   ", r[3])
    except ValueError:
        print('Serial Number Must be Numerical')
    except Exception.SerialNoException as e:
        print(e)


def findAll():
    sql = 'Select * from emp order by sno asc'
    b.execute(sql)
    r = b.fetchall()
    print("===================================================")
    print("Sno         Name          Salary         Address")
    print("===================================================")
    for i in r:
        print(i[0],"         ",i[1],"        ",i[2],"        ",i[3])

def update():
    print('1.Update Name')
    print('2.Update Salary')
    print('3.Update Address')
    s = int(input("Select the choice : "))
    if s == 1:
        list = []
        sql = 'update emp set name = %s where sno = %s'
        while True:
            print('1.                      Update Name')
            try:
                sno = int(input('Enter the Serial Number of Employee: '))
                try:
                    if sno not in Prac.f:
                        raise Exception.SerialNoException("Invalid Serial Number... Please Go For 5th Option.")
                    else:
                        name = input('Enter the Updated name of the Employee: ')
                        val = (name,sno)
                        list.append(val)
                        print(list)
                        b.executemany(sql,list)
                        a.commit()
                        c = input('Enter "Yes" If you want to update more entry and "No" if you want to continue:  ')
                        if c.lower() == "no":
                            print('Thank you your Entries are updated successfully....')
                            list.clear()
                            break
                except Exception.SerialNoException as u:
                    print(u)
            except ValueError:
                print("Serial Number Must be in Numerical Form...")

    elif s == 2:
        list = []
        sql = 'update emp set sal = %s where sno = %s'
        sql1 = 'select sal from emp WHERE sno = %s'
        while True:
            print('2.                      Update Salary')
            try:
                sno = int(input('Enter the Serial Number of Employee: '))
                val1 = (sno,)
                b.execute(sql1, val1)
                current_sal = b.fetchone()
                sal = int(input('Enter the Updated Salary of the Employee: '))
                new_sal = (sal,)
                try:

                    if new_sal < current_sal:
                        raise Exception.UpdateSalaryException('Updated salary Must be Greater than Current Salary...\n You can try again with Updated salary again...')

                    val = (sal, sno)
                    list.append(val)
                    print(list)
                    b.executemany(sql, list)
                    a.commit()
                    c = input('Enter "Yes" If you want to update more entry and "No" if you want to continue:  ')
                    if c.lower() == "no":
                        print('Thank you your Entries are updated successfully....')
                        list.clear()
                        break
                except Exception.UpdateSalaryException as e:
                    print(e)
            except ValueError:
                print("Serial Number Must be in Numerical Form...")

    elif s == 3:

        list = []
        sql = 'update emp set address = %s where sno = %s'
        while True:
            print('3.                      Update Address')
            try:
                sno = int(input('Enter the Serial Number of Employee: '))
                address = int(input('Enter the updated Address of the Employee: '))
                val = (address, sno)
                list.append(val)
                print(list)
                b.executemany(sql, list)
                a.commit()
                c = input('Enter "Yes" If you want to update more entry and "No" if you want to continue:  ')
                if c.lower() == "no":
                    print('Thank you your Entries are updated successfully....')
                    list.clear()
                    break
            except ValueError:
                print("Serial Number Must be in Numerical Form...")
def deleteR():
    sql = 'delete from emp where sno = %s'
    try:
        sno = int(input("Enter the Serial Number of that Employee you want to delete the entry"))
        c = input("Are you sure you want to Delete this Record?? \n If Yes Enter Yes: ")
        if c.lower() == 'yes':
            b.execute(sql,(sno,))
            a.commit()
            print("Your Entry is deleted....")
        else:
            print('Thank you... \n Please Proceed....')
    except ValueError:
        print('Serial Number Must be in Numeric Form....')
