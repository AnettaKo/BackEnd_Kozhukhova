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
    def getAllArticles():
        result = requests.get(Client.backendAddress)
        return result.json()

    @staticmethod
    # def getFilteredArticles(item_class):
    def getFilteredArticles(selections: dict):
        param_str = "?"
        for key, value in selections.items():
            # param_str += "item_class=" + item + "&"
            for item in value:
                param_str += key + "=" + item + "&"
        str_len = len(param_str)
        param_str = param_str[0:str_len-1]
        # result = requests.get(Client.backendAddress +"/report" + "?item_class=" + item_class)
        result = requests.get(Client.backendAddress + "/report" + param_str)
        print(result)
        if result.status_code == 200:
            return result.json()
        else:
            return []

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