import uvicorn
from fastapi import FastAPI, Query
from my_functions.database import Wardrobe_database
from my_functions.classes import Item
from typing import Annotated

app = FastAPI()
db = Wardrobe_database()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/articles")
def getArticles():
    articles = db.get_all_articles()
    return articles

@app.get("/articles/report")
# def getFilteredArticles(item_class: Annotated[list[str] | None, Query()] = None):
def getFilteredArticles(item_class: Annotated[list[str] | None, Query()] = None,
                        item_type: Annotated[list[str] | None, Query()] = None,
                        size: Annotated[list[str] | None, Query()] = None,
                        season: Annotated[list[str] | None, Query()] = None,
                        color: Annotated[list[str] | None, Query()] = None,
                        brand: Annotated[list[str] | None, Query()] = None):
    # articles = db.get_filtered_article(item_class,season)
    param = {}
    if item_class != None:
        param["item_class"] = item_class
    if item_type != None:
        param["item_type"] = item_type
    if size != None:
        param["size"] = size
    if season != None:
        param["season"] = season
    if color != None:
        param["color"] = color
    if brand != None:
        param["brand"] = brand

    # articles = db.get_filtered_article(item_class, season)
    articles = db.get_filtered_article(param)
    return articles

@app.get("/articles/{article_name}")
def getArticleByName(article_name: str):
    article = db.get_article_by_name(article_name)
    return article

@app.post("/articles")
def addArticle(article: Item):
    db.insert_article(article)
    return {"message": "successful"}

@app.put("/articles/{id}")
def updateArticleById(id: str, article: Item):
    db.update_article_by_id(id, article)
    return {"message": "successful"}

@app.delete("/articles/{id}")
def deleteArticleById(id: str):
    db.delete_article_by_id(id)
    return {"message": "successful"}

# @app.delete("/articles/{name}")
# def deleteArticleByName(name: str):
#     db.delete_article_by_name(name)
#     return {"message": "successful"}

class MyProjectBackend():
    @staticmethod
    def startBackend():
        uvicorn.run("my_functions.api:app",
                host='127.0.0.1',
                port=7000,
                reload=True,
                log_level="info")
