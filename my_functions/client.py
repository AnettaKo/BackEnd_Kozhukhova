import requests

class Client():

    backendAddress = "http://localhost:7000/articles"

    @staticmethod
    def addArticle(article):
        result = requests.post(
                Client.backendAddress,
                json=article.dict())
        return result

    @staticmethod
    def getArticleByName(name):
        result = requests.get(Client.backendAddress + "/" + name)
        return result.json()