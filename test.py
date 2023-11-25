from fastapi.testclient import TestClient
from my_functions.api import app
from my_functions.classes import Item
from my_functions.database import client

def test_acces_to_DB():
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def test_app():

    test_client = TestClient(app)

    test_article = Item(id = "",
                       item_name = "test",
                       item_class = "closes",
                       item_type = "pant",
                       size = "104",
                       season = "winter",
                       color = "red",
                       brand = "kik",
                       price = 0.0,
                       description = "")

    test_article_update = Item(id="",
                        item_name="test1",
                        item_class="closes",
                        item_type="pant",
                        size="104",
                        season="winter",
                        color="red",
                        brand="kik",
                        price=0.0,
                        description="")

    r = test_client.post("/articles", json=test_article.model_dump())
    assert r.status_code == 200

    r = test_client.get("/articles/test")
    assert r.status_code == 200
    article = r.json()
    id = article["_id"]

    r = test_client.put("/articles/" + id, json = test_article_update.model_dump())
    assert r.status_code == 200

    r = test_client.get("/articles/test1")
    assert r.status_code == 200
    article = r.json()
    assert article ["item_name"] == "test1"


    r = test_client.get("/articles/test2")
    assert r.status_code == 200
    article = r.json()
    assert article == None


    r = test_client.delete("/articles/" + id)
    assert r.status_code == 200

    r = test_client.get("/articles/test1")
    assert r.status_code == 200
    article = r.json()
    assert article == None

test_acces_to_DB()
test_app()