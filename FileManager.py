import os
import msgpack

class FileManager:
    def __init__(self,database_path):
        self._database_path = database_path

    def create_database_file(database_path):
        try:
            with open(database_path, "ab"):
                pass
        except:
            print("Unable to create database file ",database_path)

    def delete_db_file(self):
        try:
            os.remove(self._database_path)
        except:
            print("File ",self._database_path," cannot be found")

    def rename_db_file(_oldFilePath,_newFilePath):
        try:
            os.rename(_oldFilePath,_newFilePath)
        except:
            print("Unable to rename database")

    def add_table(self,table_name):
        database = {}
        if os.path.getsize(self._database_path) > 0:
            database = self.read_from_database()

        database[table_name] = {}

        self.write_to_database(database)

    def return_table(self, table_name):
        return(self.read_from_database()[table_name])

    def rename_table(self, old_name, new_name):
        database = {}
        try:
            database = self.read_from_database()
            try:
                database[new_name] = database.pop(old_name)
            except:
                print("Unable to rename table. ",old_name," is not present on selected database")
        
            self.write_to_database(database)

        except:
            print("Unable to rename table")

    def drop_table(self, table_name):
        database = {}
        database = self.read_from_database()
        try:
            del database[table_name]
        except():
            print("Table ",table_name," not present in database")

        self.write_to_database(database)

    def insert(self, key, value, table_name):
        database = {}
        database = self.read_from_database()
        try:
            database[table_name][key] = value
        except:
            print("Unable to insert into database!")
        self.write_to_database(database)

    def select_by_key(self, key, table_name):
        try:
            return self.read_from_database()[table_name][key]
        except:
            print("Key not present in database")

    def remove_all(self, table_name):
        database = {}
        database = self.read_from_database()
        try:
            database[table_name] = {}
        except:
            print("Unable to remove content from table, no table",table_name)
        self.write_to_database(database)

    def remove_by_key(self, key_name, table_name):
        database = {}
        database = self.read_from_database()
        try:
            del database[table_name][key_name]
        except:
            print("Unable to remove item, invalid key or table")
        self.write_to_database(database)

    def update_by_key(self, key, table_name, value):
        database = {}

        database = self.read_from_database()
        try:
            database[table_name][key] = value
        except:
            print("Unable to update record, invalid table name or key")
        self.write_to_database(database)

    def list_tables(self):
        pass

    def write_to_database(self,database):
        try:
            with open(self._database_path, "wb") as f:
                f.write(msgpack.packb(database, use_bin_type = True))
        except:
            print("Unable to write changes to database")

    def read_from_database(self):
        database = {}
        try:
            with open(self._database_path, "rb") as f:
                database = msgpack.unpackb(f.read(), raw = False)
        except:
            print("Unable to read from database")
        return database
