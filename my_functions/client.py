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

    @staticmethod
    def updateArticle(article):
        result = requests.put(
            Client.backendAddress + '/' + article.id,
            json=article.dict())
        return result

    @staticmethod
    def deleteArticlebyId(article):
        result = requests.delete(
                Client.backendAddress + '/' + article.id)
        return result