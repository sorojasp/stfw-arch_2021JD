class Animal:
    
    """[That class is a abstraction of .....]
    """
    __age: float
    __color:list = []
    __gender:str
    __taxonomic_group:str
    __type:str
    _name:str
    
    def __init__(self, 
                 age:str, 
                 color:list, 
                 gender:str, 
                 taxonomic_group:str,
                 type:str,
                 name:str=None
                 ):
        """[summary]

        Args:
           Args:
            age (str): [that attribute set the age of animal]
            color (list): [color of skin]
            gender (str): [male or female]
            taxonomic_group (str): [natural clasification]
            type (str): [can be: 'walk', 'fly', 'swim']
            name (str, optional): [description]. Defaults to None.
        """
        
        self._name=name
        self.__age=age
        self.__color=color
        self.__gender=gender
        self.__type=type
        self.__taxonomic_group=taxonomic_group
        
        
        
    def drink(self)->None:
        """[That method is used when animal have to drink]
        """
        print(f'{self.__name} is drink')
        
    def eat(self)->None:
        """[That method is used when animal have to eat]
        """
        print(f'{self.__name} is eat')
        
    def make_sound(self):
        print(f'{self.__name} is make sound')
        

 
        