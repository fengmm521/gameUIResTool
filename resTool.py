#-*- coding: utf-8 -*-
import os,sys
import hashlib
import time
import shutil
import json
reload(sys)

imageDir = '/Users/woodcol/Documents/work/tool/resReName'
md5File = 'filemd5.txt'
#获取当前脚本所在路径
def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

#获取工作目录
def getWordDir():
    return imageDir

#读取文件md5
def readOldMd5():
    oldMd5 = {}
    return oldMd5
    
def isFileChange(f):
    md5s = hashlib.md5(f).hexdigest()
    return md5s

#保存md5
def saveNewMd5(md5Dic):
    print md5Dic
    
def getAllPngFile(path):
    jsondir = path
    jsonfilelist = []
    for root, dirs, files in os.walk(jsondir):
        for filex in files:          
            print filex
            name,text = os.path.splitext(filex)
            if cmp(text,".png") == 0:
                jsonArr = []
                rootdir = path
                dirx = root[len(rootdir)+1:]
                pathName = dirx + os.sep + filex
                jsonArr.append(pathName)
                newName = pathName.replace(os.sep,'_')
                (newPath,name) = os.path.split(pathName)
                jsonArr.append(newPath)
                jsonArr.append(newName)
                f = open(root + os.sep + filex,'r')
                fileMd5 = hashlib.md5(f.read()).hexdigest()
                jsonArr.append(fileMd5)
                f.close()
                jsonfilelist.append(jsonArr)
    return jsonfilelist

def saveFileToRes(fileDatList):
    fileSaveRoot = getWordDir() + os.sep + 'out'
    #shutil.rmtree(fileSaveRoot)
    fileReadRoot = getWordDir() + os.sep + 'uiRename'
    for i in range(len(fileDatList)):
        filel = fileDatList[i]
        fileOldPath = fileReadRoot + os.sep + filel[0]
        filepath = fileSaveRoot + os.sep + filel[1]
        filename = filel[2]
        print fileOldPath
        if os.path.exists(filepath) == False:
            os.makedirs(filepath)
        newPath = filepath + os.sep + filename
        print newPath
        if os.path.exists(newPath):
            fo = open(newPath,'r')
            md5o = str(hashlib.md5(fo.read()).hexdigest())
            if cmp(md5o,filel[3]) != 0:
                shutil.copyfile(fileOldPath, newPath)
            else:
                print 'file same'
        else:
            print "file no"
            shutil.copyfile(fileOldPath, newPath)
        
def saveFileToPlist(fileDatList):
    fileSaveRoot = getWordDir() + os.sep + 'outplist'
    #shutil.rmtree(fileSaveRoot)
    fileReadRoot = getWordDir() + os.sep + 'uiRename'
    for i in range(len(fileDatList)):
        filel = fileDatList[i]
        fileOldPath = fileReadRoot + os.sep + filel[0]
        filepath = fileSaveRoot
        filename = filel[2]
        print fileOldPath
        if os.path.exists(filepath) == False:
            os.makedirs(filepath)
        newPath = filepath + os.sep + filename
        print newPath
        if os.path.exists(newPath):
            fo = open(newPath,'r')
            md5o = str(hashlib.md5(fo.read()).hexdigest())
            if cmp(md5o,filel[3]) != 0:
                shutil.copyfile(fileOldPath, newPath)
            else:
                print 'file same'
        else:
            print "file no"
            shutil.copyfile(fileOldPath, newPath)
def main():
    maindir = getWordDir()
    print 'work dir:%s'%(maindir)
    fileList = getAllPngFile(maindir + os.sep + 'uiRename')
    saveFileToRes(fileList)
    saveFileToPlist(fileList)
    print '****file save end! Prease \"Enter\" close the window!****'
    raw_input()
    exit(0)
if __name__ == '__main__':
    main()