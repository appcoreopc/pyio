import json

class JsonReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self, chunksize=1024):
        try:
            with open(self.filename, "r") as jsonfile:
                jsondata = json.load(jsonfile)
                self.readdata(jsondata)
        except ValueError as e:
            return False
        return True

    def readdata(self, jsondata):
        for jdx in jsondata:
            print(jdx)
            self.readjsondata(jsondata[jdx])

    def readjsondata(self, jsondata):
        for cjdx in jsondata: 
                if isinstance(cjdx, dict):
                    print("more dict")
                elif isinstance(cjdx, list):
                    print("list")
                print(type(cjdx))
                print(cjdx)
