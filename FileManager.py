import os
import msgpack

class FileManager:
    def __init__(self,database_path):
        self._database_path = database_path

    def create_database_file(database_path):
        with open(database_path, "ab"):
            pass

    def delete_db_file(self):
        os.remove(self._database_path)

    def rename_db_file(self,_oldFilePath,_newFilePath):
        os.rename(_oldFilePath,_newFilePath)
        self._database_path = _newFilePath

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

    def insert(self, key, value, table_name):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            database[table_name][key] = value

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def list_tables(self):
        pass
