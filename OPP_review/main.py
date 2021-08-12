from Animal import Animal
from Cat import Cat
from Writter import Writter

"""#panter:Animal = Animal(45,'black','male','feline','walk','Snow ball')

#panter.drink()
#panter.eat()
    
#print(panter.test_method()) 
#print(panter.age)
    
seniorGato:Cat=Cat(4,['black','white'],'male','feline','walk','Señor Gato',7)   
#seniorGato.drink()
#seniorGato.eat()
seniorGato.make_sound()

seniorGato.loss_life()#6
seniorGato.loss_life()#5
seniorGato.loss_life()#4
seniorGato.loss_life()#3

print(seniorGato.get_life())"""


w: Writter = Writter()


# w.create_file("data.txt")

"""
w.write_new_Line("data.txt","STIVEN ORLANDO ROJAS")
w.write_new_Line("data.txt","Juan")
w.write_new_Line("data.txt","Mateo")
w.write_new_Line("data.txt","Jose")
"""

path: str = "data.txt"
file = open(path, "r")  # save data
print(file)
print(file.read())
w.clear(path)

counter: int = 0
line_to_delete: int = 1


for line in file:
    print(f'Line: {line}')
    if counter != line_to_delete:
        w.write_new_Line("data.txt", line.strip('\n'))
    counter += 1

# w.clear("data.txt")
