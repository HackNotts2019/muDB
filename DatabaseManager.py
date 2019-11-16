import os
from FileManager import FileManager

class DatabaseManager:
    def __init__(self):
        self._fm = None
    # Database methods #
    def create_database(self,pathName):
        FileManager.create_database_file(pathName)

    def select_database(self,databasePath):
        self._fm = FileManager(databasePath)

    def drop_database(self,databasePath):
        fm = FileManager(databasePath)
        fm.delete_db_file()

    def rename_database(self,_oldFilePath,_newFilePath):
        self._fm.rename_db_file(_oldFilePath,_newFilePath)

    def list_tables(self):
        self._fm.list_tables()

    def close_database(self):
        self._fm = None

    # Table methods #
    def create_table(self,table_name):
        self._fm.add_table(table_name)

    def drop_table(self,table_name):
        pass

    def rename_table(self,old_name,new_name):
        pass

    # Data manipulation methods #
    def select_all(self,table_name):
        return self._fm.return_table(table_name)

    def select_by_key(self,key,table_name):
        pass

    def insert(self,key,value,table_name):
        self._fm.insert(key, value, table_name)

    def remove_all(self,table_name):
        pass

    def remove_by_key(self,table_name,key_name):
        pass

    def update_by_key(self,key,table_name,value):
        pass
