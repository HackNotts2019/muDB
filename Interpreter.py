from DatabaseManager import DatabaseManager

class Interpreter:
    def __init__(self):
        self._dbm = DatabaseManager()

    def interpret(self, line):
        expressions = [expression for expression in line.split(';') if expression]

        for expression in expressions:
            tokens = self._tokenize(expression)
            self._evaluate(tokens)

    def _tokenize(self, expression):
        return expression.replace('(', ' ( ').replace(')', ' ) ').replace('*', ' * ').split()

    def _evaluate(self, tokens):
        if (tokens[0].upper() == 'USE'):
            self._dbm.select_database(tokens[1])
        elif (tokens[0].upper() == 'CREATE'):
            if (tokens[1].upper() == 'DATABASE'):
                self._dbm.create_database(tokens[2])
            elif (tokens[1].upper() == 'TABLE'):
                self._dbm.create_table(tokens[2], tokens[4], tokens[6])
            else:
                self._syntax_error()
        elif (tokens[0].upper() == 'DROP'):
            if (tokens[1].upper() == 'DATABASE'):
                self._dbm.drop_database(tokens[2])
            elif (tokens[1].upper() == 'TABLE'):
                self._dbm.drop_table(tokens[2])
            else:
                self._syntax_error()
        elif (tokens[0].upper() == 'RENAME'):
            if (tokens[1].upper() == 'DATABASE'):
                self._dbm.rename_database(tokens[2], tokens[3])
            elif (tokens[1].upper() == 'TABLE'):
                self._dbm.rename_table(tokens[2],tokens[3])
            else:
                self._syntax_error()
        elif (tokens[0].upper() == 'LIST'):
            if (tokens[1].upper() == 'TABLES'):
                self._dbm.list_tables()
            else:
                self._syntax_error()
        elif (tokens[0].upper() == 'CLOSE'):
            if (tokens[1].upper() == 'DATABASE'):
                self._dbm.close_database()
            else:
                self._syntax_error()
        elif (tokens[0].upper() == 'SELECT'):
            if (tokens[1] == '*'):
                self._dbm.select_all(tokens[3])
            else:
                self._dbm.select_by_key(tokens[1], tokens[3])
        elif (tokens[0].upper() == 'INSERT'):
            self._dbm.insert(tokens[2], tokens[4], tokens[7])
        elif (tokens[0].upper() == 'UPDATE'):
            self._dbm.update_by_key(tokens[1], tokens[3], tokens[5])
        elif (tokens[0].upper() == 'REMOVE'):
            if (tokens[1] == '*'):
                self._dbm.remove_all(tokens[3])
            else:
                self._dbm.remove_by_key(tokens[1], tokens[3])
        else:
            self._syntax_error()

    def _syntax_error(self):
        print("Error: Incorrect Syntax")
