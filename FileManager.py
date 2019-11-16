import os

class FileManager:
    def __init__(self,databasePath):
        self._databasePath = databasePath

    def create_database_file(databasePath):
        with open(databasePath, "ab"):
            pass

    def delete_db_file(self):
        os.remove(self._databasePath)

    def rename_db_file(self,_oldFilePath,_newFilePath):
        os.rename(_oldFilePath,_newFilePath)
        self._databasePath = _newFilePath

    def add_table(self,table_name,key_size,val_size):
        pass

    def list_tables(self):
        pass
