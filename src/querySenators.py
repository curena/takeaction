import urllib.request
import os
import json

class SenatorInfo:
    def __init__ (self,state):
        url = "https://api.propublica.org/congress/v1/members/senate/" + state + "/current.json"
        secret_key = os.environ.get("SECRET_KEY")
        headers = {"X-API-Key": secret_key}
    
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        
        self.__data = json.loads(data)
    
    def getName(self, number):
        if (self.__data["status"] == "OK"):
            return self.__data["results"][number]["name"]

    def getTwitter(self,number):
        if (self.__data["status"] == "OK"):
            return self.__data["results"][number]["twitter_id"]


if __name__ == "__main__":
    #Print Example
    state = "WY"

    MySenators = SenatorInfo(state)

    print(state + " senators are " + MySenators.getName(0) + " and " + MySenators.getName(1)  + ".")

    print(MySenators.getName(0) + " twitter handle is: " + MySenators.getTwitter(0))