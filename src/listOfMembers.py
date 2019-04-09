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
        
        self.__senateData = json.loads(data)
    
    def writeToFile(self):
        with io.open("data.txt", 'w') as f:
            json.dump(self.__senateData, f, ensure_ascii=False, indent=2)
    
    def findStateInfo(self, state):
        self.__stateData = []
        for dict in self.__senateData["results"][0]["members"]:
            if (dict["state"] == state):
                self.__stateData.append(dict)

    def printStateData(self):
        print(self.__stateData)
    
    def getSenatorFirstName(self,number):
        return self.__stateData[number]["first_name"]

    def getSenatorMiddleName(self,number):
        return self.__stateData[number]["middle_name"]

    def getSenatorLastName(self,number):
        return self.__stateData[number]["last_name"]

    def getSenatorPhoneNumber(self,number):
        return self.__stateData[number]["phone"]

if __name__ == "__main__":
    #Print to file
    myList = ListOfMembers()
    myList.findStateInfo("TX")
    myList.printStateData()
    print(myList.getSenatorFirstName(0))
    print(myList.getSenatorPhoneNumber(0))