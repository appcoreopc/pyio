import csv

class CsvFileReader:
    def __init__(self, name):
        self.filename = name

    def read(self, function, chunksize=1024):
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                function(row)

###### how to use it ##########
# x = CsvFileReader("1.csv")
# a = lambda row : print(row)
# x.read(a)
##############################