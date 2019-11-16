class DatabaseManager:
    # "privates"
    
    #
    def __init__(self,databasePath):
        self._select_database(databasePath)
    # Database methods #
    def _select_database(self,_databasePath):
        pass
    def create_database(self):
        pass
    def drop_database(self):
        pass
    def rename_database(self):
        pass
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

