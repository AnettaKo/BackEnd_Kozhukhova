from pymongo import MongoClient
from bson import ObjectId
from my_functions.classes import Item

client = MongoClient("mongodb+srv://ankozhukhova:mongo4anna.@cluster0.yt7xy1p.mongodb.net/?retryWrites=true&w=majority")

class Wardrobe_database:

    client = client
    database = client.my_wardrobe
    collection = database.articles

    def insert_article(self, article: Item):
        return self.collection.insert_one(article.item_dictionary())

    def get_article_by_name(self, name: str):
        article = self.collection.find_one({"item_name": name})
        if article != None:
            article["_id"] = str(article["_id"])
            article = Item(**article)
        return article

    def get_all_articles(self):
        articles = self.collection.find({})
        list_articles = []
        for article in articles:
            article["_id"] = str(article["_id"])
            list_articles.append(Item(**article))
        return list_articles

    def get_filtered_article(self, param: dict):
    # def get_filtered_article(self, item_class: list|None, season: list|None):
        # articles = self.collection.find({"item_class": {"$in": item_class},
        #                                  "season": {"$in": season}})
        # param = {}
        # if item_class != None:
        #     param["item_class"] = {"$in": item_class}
        # if season != None:
        #     param["season"] = {"$in": season}
        # articles = self.collection.find(param)
        for key, value in param.items():
            if value == None:
                param.pop(key)
            else:
                param[key] = {"$in": value}
        articles = self.collection.find(param)
        list_articles = []
        for article in articles:
            article["_id"] = str(article["_id"])
            list_articles.append(Item(**article))
        return list_articles

    def update_article_by_id(self, id: str, article: Item):
        return self.collection.replace_one({"_id":  ObjectId(id)}, article.item_dictionary())

    def delete_article_by_id(self, id: str):
        return self.collection.delete_one({"_id": ObjectId(id)})

    # def delete_article_by_name(self, name: str):
    #     return self.collection.delete_one({"item_name": name})
    #
    # def update_article_by_name(self, name: str, article: Item):
    #     return self.collection.replace_one({"item_name": name}, article.item_dictionary())
