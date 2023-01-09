import os
import subprocess


def GetunzipCommand(unzipPath=None):
    if unzipPath:
        return unzipPath
    else:
        return "360zip -X"


def UnzipFile(filePath, targetDir):
    unzipCommand = GetunzipCommand()
    if not os.path.exists(filePath):
        print(filePath, "don't exist")
        return
    if not os.path.exists(targetDir):
        os.makedirs(filePath)

    cmd = unzipCommand+" \""+filePath+"\" \""+targetDir+"\""
    ret = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ret == 0:
        print(filePath, "unzip complete:", ret)
        return True
    else:
        print("error:", ret)
        return False


def UnzipFiles(filePaths, targetDir):
    if not isinstance(filePaths, list) and filePaths:
        filePaths = [filePaths]
    for filePath in filePaths:
        name = os.path.basename(filePath).split('.')[0]
        subTargetDir = targetDir + '\\' + name
        if not os.path.exists(subTargetDir):
            os.makedirs(subTargetDir)
        UnzipFile(filePath, subTargetDir)
    return