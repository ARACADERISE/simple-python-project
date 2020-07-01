# Simple Python project to check file sizes
import os, json

class GatherFiles:
    def __init__(self,filename):
        self.filename = filename
        self.filecontents = ""
        self.HasMadeBit = False
        self.fileSize = 0
    
    def RepFile(self):
        if os.path.isfile(
            os.path.abspath(
                self.filename
            )
        ):
            file_ = open(self.filename,"r").read()
            self.filecontents = file_
    
    def SetSize(self):
        if self.filecontents != "":
            for i in range(len(self.filecontents)):
                self.fileSize += 8
            self.fileSize /= 8
            self.fileSize = int(self.fileSize)
    
    def MakeBit(self,convert=False,end=' '):
        if self.filecontents != "":
            write_file = open(self.filename+"..","w")
            for i in self.filecontents:
                if not convert:
                    write_file.write(ord(i))
                    # print(ord(i))
                else:
                    write_file.write(str(ord(i)))
                    write_file.write("\t")
                    write_file.write(chr(ord(i)))
                    write_file.write(end)
                    # print(ord(i),"\t",chr(ord(i)))
            write_file.close()
            self.HasMadeBit = True
    
    def ReleaseMemory(self):
        """Opens and deletes all file information"""
        file_info = open(self.filename,"rw")
        file_info.write("")
        file_info.close()


gf = GatherFiles("main.py")
gf.RepFile()
gf.SetSize()
gf.MakeBit(convert=True)