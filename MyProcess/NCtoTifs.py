# -*- coding:utf-8 -*-
import datetime
import os
import multiprocessing as mp
import FileHelper as fh
import arcpy


ncWorkDir=r"F:\CJM\CMFD\P"
TifTargetDir=r"F:\CJM\CMFD\P_tifs"


def func_ncToTif(ncPath):
        dir = os.path.dirname(ncPath)
        targetDir = str(dir).replace(ncWorkDir, TifTargetDir)
        name=os.path.basename(ncPath)
        year=name[-9:-5]
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        print("开始处理:" + ncPath)
        for i in range(0,365):
            day=i+1
            result = os.path.join(targetDir, str(year) +"_"+str(day)+'.tif')
            layername='layer'+str(year)+str(day)
            if not os.path.exists(result):
                arcpy.MakeNetCDFRasterLayer_md(ncPath,"temp","lon","lat",layername,"#","time "+str(i),"BY_INDEX")
                arcpy.CopyRaster_management(layername,result)
                print(os.path.basename(result)+": saved")
        print("finished:" + ncPath)
        # else:
        #     print("passed:" + project_result)
        # arcpy.Clip_management(dir_file_path, "#", clip_result, clipShpPath, "3", "ClippingGeometry")  # 裁剪






if __name__ == '__main__':

    ncfiles=fh.getFiles(ncWorkDir,"nc",True)
    start_time = datetime.datetime.now()
    cpu= mp.cpu_count()
    usecore=cpu
    pool=mp.Pool(usecore)
    pool.map(func_ncToTif, ncfiles)
    end_time = datetime.datetime.now()
    use_time = (end_time - start_time).total_seconds()
    print("Finished: " + "{:.2f}".format(use_time) + " s")


