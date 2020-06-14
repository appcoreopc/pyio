#import filereader
from csvreader import CsvFileReader

def test_File():
    print("print...")
    a = CsvFileReader("./3.csv")
    l = lambda row : print(row)
    a.read(l, 5)
    

test_File()
