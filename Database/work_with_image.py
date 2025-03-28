import sqlite3
import logging
import os

logging.basicConfig(filename="logging.log", filemode="w", format="%(asctime)s %(message)s")
logger = logging.getLogger()

class DB_Util:
    def create_connection(database_name):
        try:
            connection = sqlite3.connect(database=database_name)

            cursor_object = connection.cursor()
            return {
                "connection" : connection,
                "cursor" : cursor_object
            }
        except Exception as e:
            print(f"An exception has occured: {e}")

    def create_table(table_query, cursor_object, connection):
        try:
            cursor_object.execute(table_query)
            connection.commit()
            print("Table has been created")
            return
        except Exception as e:
            print('An exception has occured')

    def insert_into_table(insert_query, cursor_object, connection):
        try:
            cursor_object.execute(insert_query)
            connection.commit()
            print("insert query has been executed")
            return
        except Exception as e:
            print(f'An exception as occured: {e}')
    
    
    def view_query(view_query, cursor_object, connection):
        try:
            cursor_object.execute(view_query)
            connection.commit()
            print("view query has been executed")
            return
        except Exception as e:
            print(f'An exception as occured: {e}')

    

class DB:
    def __init__(self, database):
        logger.info("In this section of code i am trying to initialize database")
        self.database = database

    def get_database(self):
        logger.info(f"In this section of code i am trying to return database")
        return self.database
    
    def create_connection(self, database):
        logger.info(f"In this section of code i am trying to create connection and getting cursor_object")
        object_ = DB_Util.create_connection(database)
        return object_
    
    def create_table(self, table_query, cursor_object, connection):
        logger.info(f"In this section of code i am trying to create table in {self.database} database")
        DB_Util.create_table(table_query, cursor_object, connection)
    
    def insert_into_table(self, insert_query, cursor_object, connection):
        logger.info(f"In this section of code i am trying to return database")
        DB_Util.insert_into_table(insert_query, cursor_object, connection)

    def view_query(self, view_query, cursor_object, connection):
        logger.info(f"In this section of code i am trying to view table")
        DB_Util.view_query(view_query, cursor_object, connection)


db = DB("School.db")

database = db.get_database()
object_ = db.create_connection(database)

connection = object_["connection"]
cursor_object = object_["cursor"]

table_query = str(input("here you have to write create table query: "))
db.create_table(table_query, cursor_object, connection)

insert_query = str(input("\nhere you have to insert row in table: "))
db.insert_into_table(insert_query, cursor_object, connection)

view_query = str(input("here you have to write view query"))
db.view_query(view_query, cursor_object, connection)
