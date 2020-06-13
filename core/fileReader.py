class FileReader:
    def __init__(self, name):
        self.filename = name

    def read(self, chunkSize=1024):
        with open(self.filename, "rb") as targetFile:
            for piece in self.read_in_chunks(targetFile, chunkSize):
                print(piece)

    def read_in_chunks(self, file_object, chunkSize):
        while True:
            data = file_object.read(chunkSize)
            if not data:
                break
            yield data

a = FileReader("1.txt")
a.read()
