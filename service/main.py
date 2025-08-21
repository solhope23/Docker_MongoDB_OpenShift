import os
from core.api import MyAPI
from core.dal import MongoDAL

mongodb_user = os.getenv("MONGODB_USER")
mongodb_password = os.getenv("MONGODB_PASSWORD")
mongodb_database = os.getenv("MONGODB_DATABASE")

url = f"mongodb://{mongodb_user}:{mongodb_password}@mongodb:27017"

def create_app():
    dal = MongoDAL(url)
    api = MyAPI(dal)
    my_app = api.app

    @my_app.on_event("shutdown")
    def _shutdown():
        dal.close()

    return my_app

app = create_app()