# Simple Python project to check file sizes
import os, json

class GatherFiles:
    def __init__(self,filename):
        self.filename = filename
        self.BitContents = []
        self.ArraySize = 0
        self.filecontents = ""
        self.HasMadeBit = False
        self.HasReleasedMemory = False
        self.HasRestoredFile = False
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
            self.fileSize = int(self.fileSize/8)
    
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
                self.BitContents.append(ord(i))
                self.ArraySize+=1
            write_file.close()

            self.HasMadeBit = True
    
    def ReleaseMemory(self):
        """Opens and deletes all file information"""
        if self.filecontents != "":
            with open(self.filename,"w") as f:
                f.write("")
                f.close()
            self.fileSize = int(0)
            self.HasReleasedMemory = True
    
    def RestoreFile(self):
        if self.filecontents != "":
            with open(self.filename,"w") as f:
                for i in self.BitContents:
                    f.write(chr(i))
                f.close()
            
            # Getting size again..
            for i in range(len(self.filecontents)):
                self.fileSize += 8
            self.fileSize = int(self.fileSize/8)
            self.HasRestoredFile = True

    def Save(self):
        DATA = {
            "filename": self.filename,
            "size": {
                "bytes":self.fileSize
            },
            "MEMORY":{
                "has_released": self.HasReleasedMemory,
                "has_restored": self.HasRestoredFile   
            }
        }
        with open("info.json","w") as f:
            f.write(json.dumps(
                DATA,
                indent=2,
                sort_keys=True
            ))
            f.close()
    


gf = GatherFiles("main.py")
gf.RepFile()
gf.SetSize()
gf.MakeBit(convert=True)
gf.ReleaseMemory()
gf.RestoreFile()
gf.Save()