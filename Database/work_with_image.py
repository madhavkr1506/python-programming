import sqlite3
import logging
import os

logging.basicConfig(filename="logging.log", filemode="w", format="%(asctime)s %(message)s")
logger = logging.getLogger()

class DB_Util:
    @staticmethod
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
            return None

    @staticmethod
    def create_table(table_query, cursor_object, connection):
        try:
            cursor_object.execute(table_query)
            connection.commit()
            print("Table has been created")
            return
        except Exception as e:
            print('An exception has occured')

    @staticmethod
    def insert_into_table(insert_query, cursor_object, connection, data):
        try:
            cursor_object.execute(insert_query, data)
            connection.commit()
            print("insert query has been executed")
            return
        except Exception as e:
            print(f'An exception as occured: {e}')
    
    @staticmethod
    def view_query(view_query, cursor_object):
        try:
            cursor_object.execute(view_query)
            print("view query has been executed")
            rows = cursor_object.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(f'An exception as occured: {e}')

    

class DB:
    def __init__(self, database):
        logger.info("In this section of code i am trying to initialize database")
        self.database = database

    def get_database(self):
        logger.info(f"In this section of code i am trying to return database")
        return self.database
    
    def create_connection(self):
        logger.info(f"In this section of code i am trying to create connection and getting cursor_object")
        object_ = DB_Util.create_connection(self.database)
        return object_
    
    def create_table(self, table_query, cursor_object, connection):
        logger.info(f"In this section of code i am trying to create table in {self.database} database")
        DB_Util.create_table(table_query, cursor_object, connection)
    
    def insert_into_table(self, insert_query, cursor_object, connection, data):
        logger.info(f"In this section of code i am trying to return database")
        DB_Util.insert_into_table(insert_query, cursor_object, connection, data)

    def view_query(self, view_query, cursor_object):
        logger.info(f"In this section of code i am trying to view table")
        DB_Util.view_query(view_query, cursor_object)


class ImgProcessing:
    def __init__(self, image_path):
        self.image_path = image_path
    
    def get_image_path(self):
        return self.image_path
    
    def process_image(self):
        logger.info("In this section of code i am trying to get image in bytes form")
        image_bytes = ImageProcessing_Util.process_image(self.image_path)
        return image_bytes

class ImageProcessing_Util:
    
    @staticmethod
    def process_image(image_path):
        try:
            with open(image_path, mode='rb') as binary_file:
                bytes_data = binary_file.read()
                return bytes_data
        except FileNotFoundError as file_error:
            print(f"File Not found error: {file_error}")
            return None



db = DB("School.db")

database = db.get_database()
object_ = db.create_connection()

connection = object_["connection"]
cursor_object = object_["cursor"]

table_query = str(input("here you have to write create table query: "))
db.create_table(table_query, cursor_object, connection)

image_path = "C:\\Users\\makumar2502\\Documents\\Database\\Screenshot.png"

image_processing_object = ImgProcessing(image_path)
image_bytes = image_processing_object.process_image()

insert_query = str(input("here you have to write insert query: "))
db.insert_into_table(insert_query, cursor_object, connection, ('screenshot1', image_bytes))

view_query = str(input("here you have to write view query: "))
db.view_query(view_query, cursor_object)
