import sqlite3

class SQLiteDB ():
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        except sqlite3.Error as e:
            print(e)
        return self.conn

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

class PgSQLDB ():
    pass