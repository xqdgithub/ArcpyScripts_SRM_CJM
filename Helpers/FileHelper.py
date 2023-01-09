
import os

def getFiles(dir,ext,recurrence=False):
    dirOrFiles=os.listdir(dir)
    res=[]
    for dirOrFile in dirOrFiles:
        path=os.path.join(dir,dirOrFile)
        if os.path.isfile(path):
            if ext and path.endswith(ext):
                res.append(path)
        else:
            if recurrence:
                ans=getFiles(path,ext,recurrence)
                [res.append(a) for a in ans]
    return res

def GetDir(path):
    return os.path.dirname(path)

def GetExtention(path):
    if os.path.isfile(path):
        return os.path.splitext(path)[1]

def GetNameWithoutExtention(path):
    if os.path.isfile(path):
        return str(os.path.basename(path))[0:-GetExtention(path).__len__()]

def WriteListToFile(filePath,listToWrite):
    Note=open(filePath,mode='w')
    for e in listToWrite:
        Note.write(str(e))
    Note.flush()
    Note.close()