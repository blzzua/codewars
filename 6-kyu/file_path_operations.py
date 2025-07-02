# https://www.codewars.com/kata/5844e0890d3bedc5c5000e54

class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
        
    def extension(self):
        filename = self.filepath.rpartition('/')[-1]
        return filename.rpartition('.')[-1]
        
    def filename(self):
        filename = self.filepath.rpartition('/')[-1]
        return filename.rpartition('.')[0]

    def dirpath(self):
        return self.filepath.rpartition('/')[0] + '/'
