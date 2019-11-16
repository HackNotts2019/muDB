import os
from FileManager import FileManager

class DatabaseManager:
    
    def __init__(self):
        self._fm = None
    # Database methods #
    def select_database(self,databasePath):
        self._fm = FileManager(databasePath)
    def _create_database(self,databasePath):
        self._fm = FileManager(databasePath)
    def drop_database(self,databasePath): #if you are dropping other than current database
        fm = FileManager(databasePath)
        fm.delete_db_file()
    def close_database(self):
        self._fm._close_db_file() #just to be sure
        self._fm = None #hopefully this does garbage collection in FileManager Class
    def rename_database(self,_oldFilePath,_newFilePath):
        self._fm.rename_db_file(_oldFilePath,_newFilePath)
    def list_tables(self):
        pass
    # Table methods #
    def create_table(self):
        pass
    def drop_table(self):
        pass
    def rename_table(self):
        pass
    # Data manipulation methods #
    def select_all(self):
        pass
    def select_by_key(self):
        pass
    def insert(self):
        pass
    def remove_all(self):
        pass
    def remove_by_key(self):
        pass
    def update_by_key(self):
        pass

