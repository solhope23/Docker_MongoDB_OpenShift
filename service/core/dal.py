from typing import List, Dict, Any
from pymongo import MongoClient

class MongoDAL:

    def __init__(self, mongo_url: str):
        self._client = MongoClient(mongo_url)
        self._db = self._client.get_database()
        self._col = self._db["people"]

    def add_person(self, name: str) -> None:
        self._col.insert_one({"name": name})

    def list_people(self) -> List[Dict[str, Any]]:
        docs = list(self._col.find({}, {"_id": 0}))
        return docs

    def close(self) -> None:
        self._client.close()