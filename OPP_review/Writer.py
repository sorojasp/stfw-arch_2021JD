import os

class Writer:
    
    
    def create_file(self, path: str)-> bool:
        """[Method to create a new file]

        Args:
            path (str): [path of the file]

        Returns:
            bool: [Return true, when the file is created and return false when the file is not created]
        """
        try:
            open(path, mode="x")
            return True
        except FileExistsError:
            print("The file is created")
            return False
        
    def delete(self, path:str)-> bool:
        """[Method that delete a file]

        Args:
            path (str): [path of file]

        Returns:
            bool: [Return True when the file is deleted, and False otherwise]
        """
     
        if os.path.exists(path):
            os.remove(path)
            return True 
        else:
            print("The file does not exist")
            return False
        
    def write_new_Line(self, path:str,text:str)->bool:
        """[This method write a new line in the file]

        Args:
            path (str): [path of the file]
            text (str): [text what you want write in the file]

        Returns:
            bool: [Return true, when the file was successfully written and false when]
        """
        
        if self.check_file_exist(path):
            f = open(path, "a")
            f.write(text+"\n")
            f.close()
            return True
        else:
            print("the file does not exist")
            return False
        
    def check_file_exist(self,path)->bool:
        """[Method to check if the file exists]

        Args:
            path ([type]): [path of file]

        Returns:
            bool: [return True, when the file exist; and return False when the file does not exist]
        """
        
        #if the file not exist = FileNotFoundError
        
        try:
            f = open(path, "rt")
            f.close()
            return True
        except FileNotFoundError:
            print("File not exists")
            return False
        
    def clear(self, path:str)-> bool:
        """[Method to clear a file]

        Args:
            path (str): [path of file]

        Returns:
            bool: [Return True when the file was cleared and False when the file was not cleared] 
        """
        
        try:
            if self.check_file_exist(path):
                file = open(path,"r+")
                file.truncate(0)
                file.close()
                print("File was cleared")
                return True
            else:
                print("File not exists")
                return False
        except Exception as error:
            print(f'error: {error}')
            return False        
            
        