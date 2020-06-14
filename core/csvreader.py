import csv

class CsvFileReader:
    def __init__(self, name):
        self.filename = name

    def read(self, function, chunksize=1000):
        chunk = []
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for i, l in enumerate(reader):
                if (i % chunksize == 0 and i > 0):
                    print("----------------")
                    function(chunk)
                    print("----------------")
                    del chunk[:] 
                chunk.append(l)
                    



###### how to use it ##########
# x = CsvFileReader("1.csv")
# a = lambda row : print(row)
# x.read(a)
##############################