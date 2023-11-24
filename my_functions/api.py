import uvicorn
from fastapi import FastAPI
from my_functions.database import Wardrobe_database
from my_functions.classes import Item

app = FastAPI()
db = Wardrobe_database()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/articles")
def getArticles():
    articles = db.get_all_articles()
    return articles

@app.get("/articles/{article_name}")
def getArticleByName(article_name: str):
    article = db.get_article_by_name(article_name)
    return article

@app.post("/articles")
def addArticle(article: Item):
    db.insert_article(article)
    return {"message": "successful"}

class MyProjectBackend():
    @staticmethod
    def startBackend():
        uvicorn.run("my_functions.api:app",
                host='127.0.0.1',
                port=7000,
                reload=True,
                log_level="info")
