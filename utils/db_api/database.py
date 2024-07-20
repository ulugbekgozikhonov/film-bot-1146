import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connection successful")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error connecting to database: {error}")
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
    
    def create_table(self, create_table_sql):
        self.connect()
        try:
            self.cursor.execute(create_table_sql)
            self.connection.commit()
            print("Table created successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error creating table: {error}")
            
        finally:
            self.close()
    
    def insert_data(self, insert_sql, data):
        self.connect()
        try:
            self.cursor.execute(insert_sql, data)
            self.connection.commit()
            print("Data inserted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error inserting data: {error}")
        finally:
            self.close()
    
    def query_data(self, query_sql):
        self.connect()
        try:
            self.cursor.execute(query_sql)
            records = self.cursor.fetchall()
            return records
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error querying data: {error}")
        finally:
            self.close()
    
    def update_data(self, update_sql, data):
        self.connect()
        try:
            self.cursor.execute(update_sql, data)
            self.connection.commit()
            print("Data updated successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error updating data: {error}")
        finally:
            self.close()
    
    def delete_data(self, delete_sql, data):
        self.connect()
        try:
            self.cursor.execute(delete_sql, data)
            self.connection.commit()
            print("Data deleted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error deleting data: {error}")
        finally:
            self.close()

