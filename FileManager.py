import os

def create_database_file(databasePath):
        with open(databasePath, "ab"):
            pass 

class FileManager:
    # "private members"
    #

    def __init__(self,databasePath):
        self.DELIMITER = bytearray((str("i")*128), 'utf-8')
        self._databasePath = databasePath
        self._open_db_file()
    
    def _open_db_file(self):
        self._prepare_db_file()
            
    def _prepare_db_file(self):
        isFileEmpty = False
        with open(self._databasePath, "rb") as f:
            first_char = f.read(1)
            print(first_char)
            if not first_char:
               print ("file is empty") #first character is the empty string..
               isFileEmpty = True
        
        if(isFileEmpty):
            with open(self._databasePath, "ab") as f:
                f.seek(0)
                f.write(self.DELIMITER)
                
    def delete_db_file(self):
        os.remove(self._databasePath)
        
    def rename_db_file(self,_oldFilePath,_newFilePath):
        os.rename(_oldFilePath,_newFilePath)
        self._databasePath = _newFilePath
    


