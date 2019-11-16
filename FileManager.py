import os

class FileManager:
    # "private members"
    #
    def __init__(self,databasePath):
        self._open_db_file(databasePath)
        self._dbFile = None
        self._dbFilePath = databasePath

    def __del__(self):
        self._close_db_file()
    def _open_db_file(self,databasePath):
        if self._dbFile != None:
            self._close_db_file()
        self._dbFile = open(databasePath,"wb+")
        self._dbFilePath = databasePath
            
    def _close_db_file(self):
        if self._dbFile != None:
            self._dbFile.close()
            self._dbFile = None

    def _prepare_db_file(self):
        self._dbFile.write("\n",2)

    def delete_db_file(self):
        self._close_db_file()
        os.remove(self._dbFilePath)
        
    def rename_db_file(self,_oldFilePath,_newFilePath):
        self._close_db_file()
        os.rename(_oldFilePath,_newFilePath)
        self._open_db_file(_newFilePath)
    


