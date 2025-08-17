from fastapi import FastAPI
from dal import MongoDAL

class MyAPI:

    def __init__(self, dal: MongoDAL):
        self.dal = dal
        self.app = FastAPI()
        self._register_routes()

    def _register_routes(self) -> None:
        @self.app.get("/health")
        def health():
            return {"status": "ok"}

        @self.app.post("/people/{name}")
        def add_person(name: str):
            self.dal.add_person(name)
            return {"message": f"{name} added"}

        @self.app.get("/people")
        def list_people():
            return {"people": self.dal.list_people()}