import os
from FileManager import FileManager,create_database_file

class DatabaseManager:
    
    def __init__(self):
        self._fm = None
    # Database methods #
    def create_database(self,pathName):
        create_database_file(pathName)
    def select_database(self,databasePath):
        self._fm = FileManager(databasePath)
    def drop_database(self,databasePath): #if you are dropping other than current database
        fm = FileManager(databasePath)
        fm.delete_db_file()
    def close_database(self):
        self._fm = None #hopefully this does garbage collection in FileManager Class
    def rename_database(self,_oldFilePath,_newFilePath):
        self._fm.rename_db_file(_oldFilePath,_newFilePath)
    def list_tables(self):
        pass
    # Table methods #
    def create_table(self,table_name,key_size,val_size):
        pass
    def drop_table(self,table_name):
        pass
    def rename_table(self,old_name,new_name):
        pass
    # Data manipulation methods #
    def select_all(self,table_name):
        pass
    def select_by_key(self,key,table_name):
        pass
    def insert(self,key,value,table_name):
        pass
    def remove_all(self,table_name):
        pass
    def remove_by_key(self,table_name,key_name):
        pass
    def update_by_key(self,key,table_name,value):
        pass

