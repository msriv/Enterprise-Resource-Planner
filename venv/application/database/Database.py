import os, sqlite3


class Database:
    def __init__(self):

        self.DB_FILENAME = "database/erp.db"
        self.SCHEMA_FILENAME = "database/schema.sql"

        self.db_exists = not os.path.exists(self.DB_FILENAME)

        self.conn = sqlite3.connect(self.DB_FILENAME)
        self.cursor = self.conn.cursor()
        if self.db_exists:
            print('Creating Schema')
            self.schema_file = open(self.SCHEMA_FILENAME, 'r')
            self.schema = self.schema_file.read()
            self.conn.executescript(self.schema)
            print('Schema Built')
        else:
            print('Schema Already Exists')

    def closeConn(self):
        self.conn.close()

    # Query Abstractions
    def fetchOne(self, projection, table, key, value):
        query = "SELECT {0} FROM {1} WHERE {2} = '{3}'".format(projection, table, key, value)
        print(query)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def fetchAll(self, table, projection):
        query = "SELECT {0} FROM {1}".format(projection, table)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetchAll(self, projection, table, key, value):
        query = "SELECT {0} FROM {1} WHERE {2} = '{3}'".format(projection, table, key, value)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insertOne(self, table, values):
        query = 'INSERT INTO {0} VALUES ({1})'.format(table, values)
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
        print("Insert Successful")

    def insertMany(self, tablename, projection, data):
        print("Inserted")

    def deleteOne(self, tablename, key):
        print("Deleted")

    def deleteMany(self, tablename, key):
        print("Deleted")

    def updateOne(self, tablename, column, data):
        print("Deleted")

    def updateMany(self, tablename, column, data):
        print("Deleted")

    # Custom Queries
    def validate(self, key, value):
        query = "SELECT fname FROM User WHERE {0} = '{1}' AND {2} = '{3}'".format(key[0], value[0], key[1], value[1])
        print(query)
        self.cursor.execute(query)
        if len(self.cursor.fetchall()) > 0:
            return True
        else:
            return False

    def business_exists(self, username):
        query = "SELECT * FROM Business WHERE username = '{0}'".format(username)
        self.cursor.execute(query)
        if len(self.cursor.fetchall()) > 0:
            return True
        else:
            return False
