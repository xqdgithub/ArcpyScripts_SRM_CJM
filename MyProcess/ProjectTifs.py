# -*- coding:utf-8 -*-
import datetime

import arcpy
import os
#from multiprocessing.dummy import Pool as ThreadingPool
import multiprocessing as mp
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

workDir=r"F:\CJM\CMFD\P_tifs"
targetWorkDir=r"F:\CJM\CMFD\P_Tifs_prj"
prjref=r"F:\CJM\HMRFSTP\PeojectionReference\reference.tif"
# clipshapePath=r"F:\CJM\boundary\yajiangBoundary.shp"

def ReprojectDir(pool,rootdir):
    #arcpy.env.workspace=rootdir
    targetDir=str(rootdir).replace(workDir,targetWorkDir)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(rootdir)

    dirs=[]
    tifs=[]
    err=[]
    for dir_file in dir_or_files:
        dir_file_path=os.path.join(rootdir,dir_file)
        if os.path.isfile(dir_file_path):
            if dir_file_path.endswith("tif"):
                flag=True
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

    pool.map(func_Project,tifs)
    if err:
        print("#################################################################################################");
        print(err)
    for dir in dirs:
        ReprojectDir(pool,dir)

def func_Project(tifPath):
        rootdir = os.path.dirname(tifPath)
        targetDir = str(rootdir).replace(workDir, targetWorkDir)
        project_result = os.path.join(targetDir, os.path.basename(tifPath))
        print("Projection Start:" + tifPath)
        if not os.path.exists(project_result):
            arcpy.ProjectRaster_management(tifPath,project_result,prjref)
            print("finished:" + project_result)
        # else:
        #     print("passed:" + project_result)
        # arcpy.Clip_management(dir_file_path, "#", clip_result, clipShpPath, "3", "ClippingGeometry")  # 裁剪


def Run(pool):
    ReprojectDir(pool, workDir)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    cpu= mp.cpu_count()
    usecore=cpu
    pool=mp.Pool(usecore)

    Run(pool)

    end_time = datetime.datetime.now()
    use_time = (end_time - start_time).total_seconds()
    print("Finished: " + "{:.2f}".format(use_time) + " s")





