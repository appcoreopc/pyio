#import filereader
from csvreader import CsvFileReader

def test_File():
    print("print...")
    a = CsvFileReader("./j.csv")
    l = lambda row : print(row)
    a.read(l)
    

test_File()
