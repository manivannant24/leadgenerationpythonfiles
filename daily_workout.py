#ex 1:
'''n=1
while n<11:
    print(n)
    n=n+1'''
#ex 2:
'''for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
print()'''
#ex 3:
'''g=int(input("enter num"))
while g>=1:
    print(g)
    g=g-1'''
# ex 4:
'''a=2
b=1
t=1
while t<11:
    c=a*b
    print(a,'*',b,'=',c)
    b=b+1
    t=t+1'''
#ex 5:
'''list1 = [10, 20, 30, 40, 50]
for i in range(list1[4],list1[0],-10):
    print(i)'''
#ex 6:
'''def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)'''
#ex 7:
'''def calculation(a, b):
    # Your Code
    
    return(a+b,a-b)


res = calculation(40, 10)
print(res)'''
'''def showEmployee(Ben,900):
    print("Employee name is" + Ben)
    print("Employee salaray is"+ 9000)
showEmployee("Ben", 9000)'''
'''def showEmployee(name,number):
    print("mass"+name +'and'+number )
showEmployee('sri',18000)'''
#print(list(range(2,6,2)))
class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
#print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
print(Bus)



