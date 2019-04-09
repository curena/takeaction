import urllib.request
import os
import json
import io

class ListOfMembers:
    def __init__ (self):
        url = "https://api.propublica.org/congress/v1/115/senate/members.json"
        secret_key = os.environ.get("SECRET_KEY")
        headers = {"X-API-Key": secret_key}
    
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        
        self.__data = json.loads(data)
    
    def writeToFile(self):
        with io.open("data.txt", 'w') as f:
            json.dump(self.__data, f, ensure_ascii=False, indent=2)



if __name__ == "__main__":
    #Print to file
    myList = ListOfMembers()
    myList.writeToFile()