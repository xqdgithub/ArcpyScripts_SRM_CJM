
import os


workDir=r""
templetePath=""

def getTemplete(templeteDir):
    dir_or_files = os.listdir(templeteDir)
    exts=[]
    if dir_or_files:
        name = dir_or_files[0].split(".")[0]
    for dir_or_file in dir_or_files:
        exts.append(dir_or_file.replace(name,""))
    return exts

def checkDir(rootdir):
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(rootdir)
    dirs = []
    files = []
    for dir_file in dir_or_files:
        dir_file_path = os.path.join(rootdir, dir_file)
        if os.path.isfile(dir_file_path):
            if dir_file_path.endswith("tif"):
                flag = True
                # name=dir_file.split(".")[0]
                # for ext in[".tif",".tfw",".tif.aux.xml",".xml",".ovr"]:
                #     if not name+ext in dir_or_files:
                #         flag=False
                if flag:
                    tifs.append(dir_file_path)
                else:
                    err.append(dir_file_path)

        else:
            dirs.append(dir_file_path)

    pass



if __name__ == '__main__':
    pass