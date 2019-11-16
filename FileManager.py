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

    def rename_table(self, old_name, new_name):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            database[new_name] = database.pop(old_name)

        with open(self._database_path, "wb") as f:
            f.write(msgpack.packb(database, use_bin_type = True))

    def drop_table(self, table_name):
        database = {}

        with open(self._database_path, "rb") as f:
            database = msgpack.unpackb(f.read(), raw = False)
            del database[table_name]

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
            return msgpack.unpackb(f.read(), raw = False)[table_name][key]

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
            del database[table_name][key]

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
