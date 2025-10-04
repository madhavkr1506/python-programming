import json
from bson import json_util
from pymongo import MongoClient

class ClientConnection:
    def __init__(self, require : bool):
        self.client = None
        self.triggered = False
        self.list_db = []
        self.list_collections = []
        self.work_db = None
        self.work_collection = None
        if require:
            self.trigger_connection()
    
    def trigger_connection(self):
        try:
            self.client = MongoClient("mongodb://:@localhost:27017?authSource=nobel_prize_winner", serverSelectionTimeoutMS=3000)
            if self.client:
                # print(json.dumps(self.client.server_info(), indent=4))
                self.triggered = True
        except Exception as e:
            raise Exception(f"failed to trigger connection: {e}")
        
    def get_nobel_prize_winner_name_in_category(self, category, db_name, collection_name):
        try:
            def find_db_collection():
                if self.triggered:
                    db_list = self.client.list_database_names()
                    for item in db_list:
                        self.list_db.append(item)
                    print(f"found database:\n{self.list_db}")

                    if db_name in self.list_db:
                        self.work_db = db_name
                        db = self.client[db_name]
                        if db is not None:
                            list_collections = db.list_collection_names()
                            for item in list_collections:
                                self.list_collections.append(item)
                            print(f"found collection:\n{self.list_collections}")
                            if collection_name in self.list_collections:
                                self.work_collection = collection_name
                return db if db is not None else -1

            db = find_db_collection()
            if db != -1:
                if self.work_db is not None and self.work_collection is not None:
                    print(f"database name: {self.work_db}\tcollection name: {self.work_collection}")
                    cursor = db[self.work_collection].find({"winners.category": f"{category}"}, {"winners.$": 1, "year": 1, "_id": 0}).limit(10)
                    for doc in cursor:
                        print(f"document: {json.dumps(doc, default=json_util.default, indent=4)}")

        except Exception as e:
            raise Exception(f"failed to fetch nobel prize winner name: {e}")
        
def main():
    try:
        conn = ClientConnection(True)
        conn.get_nobel_prize_winner_name_in_category("chemistry", "nobel_prize_winner", "nobel_prize")
    except Exception as e:
        print(f"Message: {e}")

if __name__ == "__main__":
    main()