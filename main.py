# Simple Python project to check file sizes
import os, json
from tqdm import tqdm as t

class GatherFiles:
    def __init__(self,filename):
        self.filename = filename
        self.BitContents = []
        self.ArraySize = 0
        self.filecontents = ""
        self.HasMadeBit = False
        self.HasReleasedMemory = False
        self.HasRestoredFile = False
        self.hasCreatedNewFile = False
        self.fileSize = 0

        # LOADING BAR
        self.LoadingBar = t
    
    def RepFile(self):
        if os.path.isfile(
            os.path.abspath(
                self.filename
            )
        ):
            file_ = open(self.filename,"r").read()
            self.filecontents = file_
            self.hasCreatedNewFile = False
        else:
            with open(os.path.abspath(self.filename),'w') as file:
                file.close()
            self.hasCreatedNewFile = True
            #raise Exception(f"Error: File {self.filename} does not exist.\n")
    
    def SetSize(self):
        if self.filecontents != "":
            if len(self.filecontents) > 4000000:
                print('Loading Large File...\n')

            for i in self.LoadingBar(self.filecontents) if len(self.filecontents) > 4000000 else self.filecontents:
                self.fileSize += 8
            self.fileSize = int(self.fileSize/8)
            #if self.fileSize/1000000 >= 1:
                #self.fileSize = f'{self.fileSize/1000000}mb'
        else:
            print(f"No content in file {self.filename} to gather a standard size.\n")
    
    def MakeBit(self,convert=False,end=' '):
        if self.filecontents != "":
            write_file = open(self.filename+"..","w")
            if len(self.filecontents) > 4000000:
              size = ''
              if self.fileSize >= 1000000:
                size = f'{int(self.fileSize/1000000)}mb'
              else:
                size = f'{self.fileSize}b'
              print(f'Transforming {size} file into ASCII...\n')

            for i in self.LoadingBar(self.filecontents) if len(self.filecontents) > 4000000 else self.filecontents:
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
          size = ''
          if self.fileSize >= 1000000:size = f'{int(self.fileSize/1000000)}mb'
          else: size = f'{self.fileSize}b'
          print(f'Releasing {self.fileSize}')
          self.fileSize = int(0)
          os.system("rm -rf {}".format(self.filename))
          self.HasReleasedMemory = True
        else:
            print(f"No content in file {self.filename} to release memory from.\n")
    
    def RestoreFile(self):
        if self.filecontents != "":
            with open(self.filename,"w") as f:
                if len(self.filecontents) > 4000000:
                    print('Restoring File ASCII contents...\n')
                    
                for i in self.LoadingBar(self.BitContents) if len(self.filecontents) > 4000000 else self.filecontents:
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
            byte[i] = bytes_
           # byte.append(i+'->'+str(bytes_))
        bits = 0
        if not self.fileSize*8 >= 8:
            if not self.filecontents == "":
                for i in self.filecontents:
                    self.fileSize += 8
                self.fileSize = int(self.fileSize/8)
            else:
                self.fileSize = None
        if os.path.exists(os.path.abspath(self.filename+'..')):
            extra['New File Name'] = self.filename + '..'
        
        DATA = {
            'filename' if not self.hasCreatedNewFile else 'Created File Name': self.filename,
            'extra info': extra if extra['New File Name'] != None else 'No Extra Information Informed',
            'size': {
                'bytes':self.fileSize if not self.fileSize > 1000000 else f'{int(self.fileSize/1000000)}mb',
                'bits':self.fileSize*8 if not self.fileSize == None else self.fileSize,
                #'Byte To Character':byte if len(byte) != 0 else 'No Information Informed',
            },
            'MEMORY':{
                'has_released': self.HasReleasedMemory,
                'has_restored': self.HasRestoredFile   
            },
            'New File':self.hasCreatedNewFile
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