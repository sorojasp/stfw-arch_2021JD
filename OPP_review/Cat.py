from Animal import Animal

class Cat(Animal):
    
    __lives:int
    
    def __init__(self, 
                 age:int,
                 colors:list,
                 gender:str,
                 taxonomyc_group: str,
                 type:str,
                 name:str,
                 lives:int,
                 ):
        
        Animal.__init__(self,
                        age,
                        colors,
                        gender,
                        taxonomyc_group,
                        type,
                        name) # The children calls the constructor of the parent class 
        
        self.__lives=lives # set up __lives attribute with lives value
    
    def make_sound(self):
        """[This method is been used to make sound of animal]
        """
        print(f'{self._name} make miauuuuuuuuu')
        
    def loss_life(self):
        """[This method is using to carry account of lives of the cat]
        """
        self.__lives-=1
        
    def get_life(self)-> int:
        """[The method return the lives of the cat]

        Returns:
            int: [Lives of the cat]
        """
        return self.__lives
        

