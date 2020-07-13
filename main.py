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
        else:
            raise Exception(f"Error: File {self.filename} does not exist.\n")
    
    def SetSize(self):
        if self.filecontents != "":
            for i in range(len(self.filecontents)):
                self.fileSize += 8
            self.fileSize = int(self.fileSize/8)
        else:
            print(f"No content in file {self.filename} to gather a standard size.\n")
    
    def MakeBit(self,convert=False,end=' '):
        if self.filecontents != "":
            write_file = open(self.filename+"..","w")
            for i in self.filecontents:
                if not convert:
                    write_file.write(str(ord(i)))
                    write_file.write(end)
                else:
                    write_file.write(str(ord(i)))
                    write_file.write("\t")
                    write_file.write(chr(ord(i)))
                    write_file.write(end)
                self.BitContents.append(ord(i))
                self.ArraySize+=1
            write_file.close()

            self.HasMadeBit = True
        else:
            print(f"No content in file {self.filename} to make into ASCII.\n")
    
    def ReleaseMemory(self):
        """Opens and deletes all file information"""
        if self.filecontents != "":
            with open(self.filename,"w") as f:
                f.write("")
                f.close()
            self.fileSize = int(0)
            os.system("rm -rf {}".format(self.filename))
            self.HasReleasedMemory = True
        else:
            print(f"No content in file {self.filename} to release memory from.\n")
    
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
        else:
            print(f"The file {self.filename} had no memory to restore.\n")

    def Save(self):
        extra = {'New File Name':None}
        byte = {}
        bits = 0
        bytes_ = 0
        for i in self.filecontents:
            bits += 8
            bytes_ = int(bits/8)
            print(i)
            byte[i] = bytes_
           # byte.append(i+'->'+str(bytes_))
        bits = 0
        if not self.fileSize*8 >= 8:
            if not self.filecontents == "":
                for i in self.filecontents:
                    self.fileSize += 8
                self.fileSize = int(self.fileSize/8)
            else:
                print(self.filecontents)
                self.fileSize = None
        if os.path.exists(os.path.abspath(self.filename+'..')):
            extra['New File Name'] = self.filename + '..'
        
        DATA = {
            'filename': self.filename,
            'extra info': extra,
            'size': {
                'bytes':self.fileSize,
                'bits':self.fileSize*8 if not self.fileSize == None else self.fileSize,
                'Byte To Character':byte
            },
            'MEMORY':{
                'has_released': self.HasReleasedMemory,
                'has_restored': self.HasRestoredFile   
            }
        }
        with open("info.json","w") as f:
            f.write(json.dumps(
                DATA,
                indent=2,
                sort_keys=True
            ))
            f.close()
    


gf = GatherFiles(input("File To Open: "))
gf.RepFile()
gf.SetSize()
gf.MakeBit()
gf.ReleaseMemory()
#gf.RestoreFile()
gf.Save()