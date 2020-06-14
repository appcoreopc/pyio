import csv

class CsvFileReader:
    def __init__(self, name):
        self.filename = name
    
    def read(self, chunksize=1024):
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)


x = CsvFileReader("1.csv")
x.read()