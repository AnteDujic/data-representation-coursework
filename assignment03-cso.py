import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getUrl():
    response = requests.get(url)
    return response.json()

def saveFile():
    with open("cso.json", "wt") as fp:
        print(json.dumps(getUrl()), file=fp)

if __name__ == "__main__":
    #print (getUrl())
    saveFile()