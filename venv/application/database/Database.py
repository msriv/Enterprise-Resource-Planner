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

    def getAll(self):
        self.cursor.execute("SELECT * FROM User;")
        print(self.cursor.fetchall())

    def insertOne(self, tablename, columns, data):
        print("Inserted")

    def insertMany(self, tablename, columns, data):
        print("Inserted")

    def deleteOne(self, tablename, key):
        print("Deleted")

    def deleteMany(self, tablename, key):
        print("Deleted")

    def updateOne(self, tablename, column, data):
        print("Deleted")

    def updateMany(self, tablename, column, data):
        print("Deleted")