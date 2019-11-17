import os
import msgpack

class FileManager:
    def __init__(self,database_path):
        self._database_path = database_path

    def create_database_file(database_path):
        with open(database_path, "ab"):
            pass

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
            with open(self._database_path, "rb") as f:
                database = msgpack.unpackb(f.read(), raw = False)

        database[table_name] = {}

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def return_table(self, table_name):
        with open(self._database_path, "rb") as f:
            return msgpack.unpackb(f.read(), raw = False)[table_name]

    def rename_table(self, old_name, new_name):
        database = {}
        try:
            with open(self._database_path, "rb") as f:
                database = msgpack.unpackb(f.read(), raw = False)
                try:
                    database[new_name] = database.pop(old_name)
                except:
                    print("Unable to rename table. ",old_name," is not present on selected database")
        
            with open(self._database_path, "wb") as f:
                f.write(msgpack.packb(database, use_bin_type = True))

        except:
            print("Unable to rename table")

    def drop_table(self, table_name):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            try:
                del database[table_name]
            except(Exception):
                print("Table ",table_name," not present in database")

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def insert(self, key, value, table_name):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            database[table_name][key] = value

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def select_by_key(self, key, table_name):
        with open(self._database_path, "rb") as f:
            try:
                return msgpack.unpackb(f.read(), raw = False)[table_name][key]
            except:
                print("Key not present in database")

    def remove_all(self, table_name):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            database[table_name] = {}

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def remove_by_key(self, table_name, key_name):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            del database[table_name][key_name]

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def update_by_key(self, key, table_name, value):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            database[table_name][key] = value

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def list_tables(self):
        pass
