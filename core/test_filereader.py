#import filereader
from core.filereader import FileReader

def test_File():
    print("print...")
    a = FileReader("core/1.txt")
    a.read()

def test_File2():
    print("-----s")

test_File()
