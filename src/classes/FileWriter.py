class FileWriter:
    def __init__(self, filename='output.txt'):
        self.filename = filename
    
    def write(self, data):
        with open(self.filename, 'a') as f:
            f.write(data)
            f.write('\n')
