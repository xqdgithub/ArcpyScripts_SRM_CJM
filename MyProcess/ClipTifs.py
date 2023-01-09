# coding=utf-8
import datetime

import arcpy
import os
#from multiprocessing.dummy import Pool as ThreadingPool
import multiprocessing as mp

from FileHelper import *


workDir=r"F:\CJM\HMRFSTP\Clip_Projection"
targetWorkDir=r"F:\CJM\HMRFSTP\Clip_Projection_Clip6"
clipshapePath=r"F:\CJM\boundary\ZiLiuYu_Clip\6\shape.shp"
err=[]

def ClipDir(pool,rootdir):

    targetDir=str(rootdir).replace(workDir,targetWorkDir)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(rootdir)
    dirs=[]
    tifs=[]
    for dir_file in dir_or_files:
        dir_file_path=os.path.join(rootdir,dir_file)
        if os.path.isfile(dir_file_path):
            if dir_file_path.endswith("tif"):
                tifs.append(dir_file_path)
        else:
            dirs.append(dir_file_path)

    pool.map(func_clip,tifs)

    for dir in dirs:
        ClipDir(pool,dir)

def func_clip(tifPath):
        rootdir = os.path.dirname(tifPath)
        targetDir = str(rootdir).replace(workDir, targetWorkDir)
        targetName=GetNameWithoutExtention(tifPath)+"_clipby6"+".tif"
        clip_result = os.path.join(targetDir, targetName)
        try:
            if not os.path.exists(clip_result):
                print("Clipping Start :" + tifPath)
                arcpy.Clip_management(tifPath, "#", clip_result, clipshapePath, "3", "ClippingGeometry")
                print("finished:" + clip_result)
            # arcpy.Clip_management(dir_file_path, "#", clip_result, clipShpPath, "3", "ClippingGeometry")  # 裁剪
            else:
                print(tifPath+":passed")
        except:
            err.append(tifPath)
def Run(pool):
    ClipDir(pool, workDir)
    errPath=os.path.join(targetWorkDir,'err.txt')
    WriteListToFile(errPath,err)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    cpu = mp.cpu_count()
    usecore = cpu
    pool = mp.Pool(usecore)
    Run(pool)
    end_time = datetime.datetime.now()
    use_time = (end_time - start_time).total_seconds()
    print("Finished: " + "{:.2f}".format(use_time) + " s")




