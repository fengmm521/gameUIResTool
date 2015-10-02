#-*- coding: utf-8 -*-
import os
import sys
import shutil
#import hashlib
import json
from PIL import Image
reload(sys)
sys.setdefaultencoding('utf8')
#used for cocos2dx 3.2
#Json界面文件输出文件夹
jsonOut = 'UIJsonOut'
#界面中使用到的图片
UsedImageFile = 'usedImageFile'
#Json界面文件输入文件夹
jsonIn = 'UIJson'
#plist图片文件夹
plistDir = 'outplist'
#界面class文件输出文件夹
UIClassDir = 'UIClass'
#test 文件输出
UIClassTestDir = 'TestUIClass'
#项目所在文件夹
projectDir = ''

uiAllImage = 'outplist'

UINameFront = ''

tpcmd = '/Applications/TexturePacker.app/Contents/MacOS/TexturePacker'#'texturepacker'

#获取当前脚本所在路径
def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def getProjectUIClassPath():
    return projectDir + os.sep + 'classes'+ os.sep +'com' + os.sep +'ui'

def getProjectUIJsonPath():
    return projectDir + os.sep +'Resources'+ os.sep +'ui'

#获取所有界面的json文件列表
def getAllJsonUIFile(path,fromatx = ".ExportJson"):
    jsondir = path
    jsonfilelist = []
    for root, _dirs, files in os.walk(jsondir):
        for filex in files:          
            #print filex
            name,text = os.path.splitext(filex)
            if cmp(text,fromatx) == 0:
                jsonArr = []
                rootdir = path
                dirx = root[len(rootdir):]
                pathName = dirx +os.sep + filex
                jsonArr.append(pathName)
                (newPath,_name) = os.path.split(pathName)
                jsonArr.append(newPath)
                jsonArr.append(name)
                jsonfilelist.append(jsonArr)
    return jsonfilelist

#获取json中用到的图片资源
def getJsonResImageList(JsonF):
    #print JsonF
    imagelist = []
    return imagelist

#查看文件是否在plist中已打包
def testImageInPlist(fileName):
    if os.path.exists(fileName):
        return True
    else:
        print "no heave Image:%s"%(fileName)
        return False

#查看文件是否在ＵＩ编辑资源中
def testImageInUIRes(filePath):
    if os.path.exists(filePath):
        return True
    else:
        print 'no heave Image in Res:%s'%(filePath)
        return False

#查看美术是否有作这个UI文件
def testImageInBase(fileName):
    if os.path.exists(fileName):
        return True
    else:
        print 'no heave Image In base:%s'%(fileName)
        return False

def listAddNewImage(listx,imlist):
    listx.extend(imlist)
    newLi = []
    while len(listx) > 0:
        x = listx.pop(0)
        fl = False
        for n in newLi:
            if cmp(str(n),str(x)) == 0:
                fl = True
        if not fl:
            newLi.append(x)
    listx.extend(newLi)


def conventJsonWidgetTree(wtree,root,roottype):
    outWtree = wtree
    allUsedImageList = []
    #['type':'Button','name':'','path':'','typepath':'','image':{}]
    #['type':'CheckBox','name':'','path':'','image':[],'isHeaveImage':0]
    childTreePath = {
                     'Button':[],
                     'CheckBox':[],
                     'ImageView':[],
                     'LabelAtlas':[],
                     'LabelBMFont':[],
                     'LoadingBar':[],
                     'Slider':[],
                     'Label':[],
                     'TextField':[],
                     'Panel':[],
                     'ScrollView':[],
                     'ListView':[],
                     'PageView':[]
                     }
    if cmp(outWtree['classname'],'Button') == 0:
        buttonx = {}
        buttonx['type'] = 'Button'
        buttonx['name'] = outWtree['options']['name']
        buttonx['path'] = root
        buttonx['typepath'] = roottype
        buttonx['image'] = {'disabledData':outWtree['options']['disabledData']['path'],'normalData':outWtree['options']['normalData']['path'],'pressedData':outWtree['options']['pressedData']['path']}
        buttonx['font'] = outWtree['options']['fontName']
        if outWtree['options']['disabledData']['path'] != None:
            tmpp = str(outWtree['options']['disabledData']['path'])
            outWtree['options']['disabledData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['disabledData']['path']])
        if outWtree['options']['normalData']['path'] != None:
            tmpp = str(outWtree['options']['normalData']['path'])
            outWtree['options']['normalData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['normalData']['path']])
        if outWtree['options']['pressedData']['path'] != None:
            tmpp = str(outWtree['options']['normalData']['path'])
            outWtree['options']['pressedData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['pressedData']['path']])
        childTreePath['Button'].extend([buttonx])
    elif cmp(outWtree['classname'],'CheckBox') == 0:
        checkboxx = {}
        checkboxx['type'] = 'CheckBox'
        checkboxx['name'] = outWtree['options']['name']
        checkboxx['path'] = root
        checkboxx['typepath'] = roottype
        checkboxx['image'] = {'backGroundBoxData':outWtree['options']['backGroundBoxData']['path'],'backGroundBoxDisabledData':outWtree['options']['backGroundBoxDisabledData']['path'],'backGroundBoxSelectedData':outWtree['options']['backGroundBoxSelectedData']['path'],'frontCrossData':outWtree['options']['frontCrossData']['path'],'frontCrossDisabledData':outWtree['options']['frontCrossDisabledData']['path']}
        if checkboxx['image']['backGroundBoxData'] != None:
            tmpp = str(checkboxx['image']['backGroundBoxData'])
            outWtree['options']['backGroundBoxData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['backGroundBoxData']['path']])
        if checkboxx['image']['backGroundBoxDisabledData'] != None:
            tmpp = str(checkboxx['image']['backGroundBoxDisabledData'])
            outWtree['options']['backGroundBoxDisabledData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['backGroundBoxDisabledData']['path']])
        if checkboxx['image']['backGroundBoxSelectedData'] != None:
            tmpp = str(checkboxx['image']['backGroundBoxSelectedData'])
            outWtree['options']['backGroundBoxSelectedData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['backGroundBoxSelectedData']['path']])
        if checkboxx['image']['frontCrossData'] != None:
            tmpp = str(checkboxx['image']['frontCrossData'])
            outWtree['options']['frontCrossData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['frontCrossData']['path']])
        if checkboxx['image']['frontCrossDisabledData'] != None:
            tmpp = str(checkboxx['image']['frontCrossDisabledData'])
            outWtree['options']['frontCrossDisabledData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['frontCrossDisabledData']['path']])
        childTreePath['CheckBox'].extend([checkboxx])
    elif cmp(outWtree['classname'],'ImageView') == 0:
        imagex = {}
        imagex['type'] = 'ImageView'
        imagex['name'] = outWtree['options']['name']
        imagex['path'] = root
        imagex['typepath'] = roottype
        imagex['image'] = {'fileNameData':outWtree['options']['fileNameData']['path']}
        if imagex['image']['fileNameData'] != None:
            tmpp = str(imagex['image']['fileNameData'])
            outWtree['options']['fileNameData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['fileNameData']['path']])
            #print outWtree['options']['fileNameData']['path']
        childTreePath['ImageView'].extend([imagex])
    elif cmp(outWtree['classname'],'LabelAtlas') == 0:
        labelatlax = {}
        labelatlax['type'] = 'LabelAtlas'
        labelatlax['name'] = outWtree['options']['name']
        labelatlax['path'] = root
        labelatlax['typepath'] = roottype
        labelatlax['image'] = {'charMapFileData':outWtree['options']['charMapFileData']['path']}
        if labelatlax['image']['charMapFileData'] != None:
            tmpp = str(labelatlax['image']['charMapFileData'])
            outWtree['options']['charMapFileData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['charMapFileData']['path']])
        childTreePath['LabelAtlas'].extend([labelatlax])
    elif cmp(outWtree['classname'],'LabelBMFont') == 0:
        labelbmfx = {}
        labelbmfx['type'] = 'LabelBMFont'
        labelbmfx['name'] = outWtree['options']['name']
        labelbmfx['path'] = root
        labelbmfx['typepath'] = roottype
        labelbmfx['image'] = {'fileNameData':outWtree['options']['fileNameData']['path']}
        if labelbmfx['image']['fileNameData'] != None:
            tmpp = str(labelbmfx['image']['fileNameData'])
            outWtree['options']['fileNameData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['fileNameData']['path']])
        childTreePath['LabelBMFont'].extend([labelbmfx])
    elif cmp(outWtree['classname'],'LoadingBar') == 0:
        loadingbarx = {}
        loadingbarx['type'] = 'LoadingBar'
        loadingbarx['name'] = outWtree['options']['name']
        loadingbarx['path'] = root
        loadingbarx['typepath'] = roottype
        loadingbarx['image'] = {'textureData':outWtree['options']['textureData']['path']}
        if loadingbarx['image']['textureData'] != None:
            tmpp = str(loadingbarx['image']['textureData'])
            outWtree['options']['textureData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['textureData']['path']])
        childTreePath['LoadingBar'].extend([loadingbarx])
    elif cmp(outWtree['classname'],'Slider') == 0:
        sliderx = {}
        sliderx['type'] = 'Slider'
        sliderx['name'] = outWtree['options']['name']
        sliderx['path'] = root
        sliderx['typepath'] = roottype
        sliderx['image'] = {'ballDisabledData':outWtree['options']['ballDisabledData']['path'],'ballNormalData':outWtree['options']['ballNormalData']['path'],'ballPressedData':outWtree['options']['ballPressedData']['path'],'barFileNameData':outWtree['options']['barFileNameData']['path'],'progressBarData':outWtree['options']['progressBarData']['path']}
        if sliderx['image']['ballDisabledData'] != None:
            tmpp = str(sliderx['image']['ballDisabledData'])
            outWtree['options']['ballDisabledData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['ballDisabledData']['path']])
        if sliderx['image']['ballNormalData'] != None:
            tmpp = str(sliderx['image']['ballNormalData'])
            outWtree['options']['ballNormalData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['ballNormalData']['path']])
        if sliderx['image']['ballPressedData'] != None:
            tmpp = str(sliderx['image']['ballPressedData'])
            outWtree['options']['ballPressedData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['ballPressedData']['path']])
        if sliderx['image']['barFileNameData'] != None:
            tmpp = str(sliderx['image']['barFileNameData'])
            outWtree['options']['barFileNameData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['barFileNameData']['path']])
        if sliderx['image']['progressBarData'] != None:
            tmpp = str(sliderx['image']['progressBarData'])
            outWtree['options']['progressBarData']['path'] = tmpp.replace('/','_')
            listAddNewImage(allUsedImageList,[outWtree['options']['progressBarData']['path']])
        childTreePath['Slider'].extend([sliderx])
    elif cmp(outWtree['classname'],'Label') == 0:
        labelx = {}
        labelx['type'] = 'Label'
        labelx['name'] = outWtree['options']['name']
        labelx['path'] = root
        labelx['typepath'] = roottype
        labelx['font'] = outWtree['options']['fontName']
        childTreePath['Label'].extend([labelx])
    elif cmp(outWtree['classname'],'TextField') == 0:
        textfieldx = {}
        textfieldx['type'] = 'TextField'
        textfieldx['name'] = outWtree['options']['name']
        textfieldx['path'] = root
        textfieldx['typepath'] = roottype
        textfieldx['font'] = outWtree['options']['fontName']
        childTreePath['TextField'].extend([textfieldx])
    elif cmp(outWtree['classname'],'Panel') == 0:
        panelx = {}
        panelx['type'] = 'Panel'
        panelx['name'] = outWtree['options']['name']
        panelx['path'] = root
        panelx['typepath'] = roottype
        if outWtree['options']['backGroundImageData'] != None:
            panelx['image'] = {'backGroundImageData':outWtree['options']['backGroundImageData']['path']}
            if panelx['image']['backGroundImageData'] != None:
                tmpp = str(panelx['image']['backGroundImageData'])
                outWtree['options']['backGroundImageData']['path'] = tmpp.replace('/','_')
                listAddNewImage(allUsedImageList,[outWtree['options']['backGroundImageData']['path']])
        childTreePath['Panel'].extend([panelx])
    elif cmp(outWtree['classname'],'ScrollView') == 0:
        scrollviewx = {}
        scrollviewx['type'] = 'ScrollView'
        scrollviewx['name'] = outWtree['options']['name']
        scrollviewx['path'] = root
        scrollviewx['typepath'] = roottype
        if outWtree['options']['backGroundImageData'] != None:
            scrollviewx['image'] = {'backGroundImageData':outWtree['options']['backGroundImageData']['path']}
            if scrollviewx['image']['backGroundImageData'] != None:
                tmpp = str(scrollviewx['image']['backGroundImageData'])
                outWtree['options']['backGroundImageData']['path'] = tmpp.replace('/','_')
                listAddNewImage(allUsedImageList,[outWtree['options']['backGroundImageData']['path']])
        childTreePath['ScrollView'].extend([scrollviewx])
    elif cmp(outWtree['classname'],'ListView') == 0:
        listviewx = {}
        listviewx['type'] = 'ListView'
        listviewx['name'] = outWtree['options']['name']
        listviewx['path'] = root
        listviewx['typepath'] = roottype
        if outWtree['options']['backGroundImageData'] != None:
            listviewx['image'] = {'backGroundImageData':outWtree['options']['backGroundImageData']['path']}
            if listviewx['image']['backGroundImageData'] != None:
                tmpp = str(listviewx['image']['backGroundImageData'])
                outWtree['options']['backGroundImageData']['path'] = tmpp.replace('/','_')
                listAddNewImage(allUsedImageList,[outWtree['options']['backGroundImageData']['path']])
        childTreePath['ListView'].extend([listviewx])
    elif cmp(outWtree['classname'],'PageView') == 0:
        pageviewx = {}
        pageviewx['type'] = 'PageView'
        pageviewx['name'] = outWtree['options']['name']
        pageviewx['path'] = root
        pageviewx['typepath'] = roottype
        if outWtree['options']['backGroundImageData'] != None:
            pageviewx['image'] = {'backGroundImageData':outWtree['options']['backGroundImageData']['path']}
            if pageviewx['image']['backGroundImageData'] != None:
                tmpp = str(pageviewx['image']['backGroundImageData'])
                outWtree['options']['backGroundImageData']['path'] = tmpp.replace('/','_')
                listAddNewImage(allUsedImageList,[outWtree['options']['backGroundImageData']['path']])
        childTreePath['PageView'].extend([pageviewx])
    else:
        print 'get unknow child'
        
    if len(outWtree['children']) > 0:
        #print len(outWtree['children'])
        chcnildrenNew = []
        for cx in range(len(outWtree['children'])):
            wctree = outWtree['children'][cx]
            outchWtree,chTreePath,imagelist = conventJsonWidgetTree(wctree,root+'+'+wctree['options']['name'],roottype + '+' + wctree['classname'])
            childTreePath['Button'].extend(chTreePath['Button'])
            childTreePath['CheckBox'].extend(chTreePath['CheckBox'])
            childTreePath['ImageView'].extend(chTreePath['ImageView'])
            childTreePath['LabelAtlas'].extend(chTreePath['LabelAtlas'])
            childTreePath['LabelBMFont'].extend(chTreePath['LabelBMFont'])
            childTreePath['LoadingBar'].extend(chTreePath['LoadingBar'])
            childTreePath['Slider'].extend(chTreePath['Slider'])
            childTreePath['Label'].extend(chTreePath['Label'])
            childTreePath['TextField'].extend(chTreePath['TextField'])
            childTreePath['Panel'].extend(chTreePath['Panel'])
            childTreePath['ScrollView'].extend(chTreePath['ScrollView'])
            childTreePath['ListView'].extend(chTreePath['ListView'])
            childTreePath['PageView'].extend(chTreePath['PageView'])
            chcnildrenNew.append(outchWtree)
            listAddNewImage(allUsedImageList,imagelist)
        outWtree['children'] = chcnildrenNew
    return outWtree,childTreePath,allUsedImageList


def createClassFile(dic,className,filePath,plistcount):
    ddic = dic
    pName = UINameFront + className
    #print ddic
#     'Button':[],
#                      'CheckBox':[],
#                      'ImageView':[],
#                      'LabelAtlas':[],
#                      'LabelBMFont':[],
#                      'LoadingBar':[],
#                      'Slider':[],
#                      'Label':[],
#                      'TextField':[],
#                      'Panel':[],
#                      'ScrollView':[],
#                      'ListView':[],
#                      'PageView':[]
    outh = ''
    outh += '''//
//  %s.h
//  game4
//
//  Created by Junpeng Zhang on 2/3/15.
//  本代码由工具生成
//
//资源加载适合cocos2d-x 3.2版本的cocostuido 1.6 for windows
//

#ifndef __game4__%s__
#define __game4__%s__

#include "cocos2d.h"
#include "ui/CocosGUI.h"
#include "editor-support/cocostudio/CocoStudio.h"
#include "BaseUILayer.h"

USING_NS_CC;
using namespace ui;
using namespace cocostudio;
class %s : public BaseUILayer
{
protected:
    %s();
public:
    virtual ~%s();
    virtual void close(); //界面关闭
    //获取下次初始化界面时的参数数据,Ref可以是　　cocos2d字典(__Dictionary)，数组(__Array)，或者字符串(__String),或者其他继承自Ref的对象
    virtual cocos2d::Ref* getUIConfData();
    static %s* createFromManger(Ref* dat);
    static %s* create();
    static %s* create(int uiID);
    virtual void onEnter();
    virtual void onExit();
    virtual bool init();
    Layout* m_rootLayout;
    
'''%(pName,pName,pName,pName,pName,pName,pName,pName,pName)
#button
    if len(ddic['Button']) > 0:
        outh += '//button\n'
    for bx in ddic['Button']:
        bname = bx['name']
        bpath = bx['path']
        btypePath = bx['typepath']
        print bname
        outh += '    Button* m_%sBtn;'%(bname)
        outh += ' //%s,%s\n'%(bpath,btypePath)
#CheckBox
    if len(ddic['CheckBox']) > 0:
        outh += '//CheckBox\n'
    for cbox in ddic['CheckBox']:
        cname = cbox['name']
        cpath = cbox['path']
        ctypepath = cbox['typepath']
        outh += '    CheckBox* m_%sChbox;'%(cname)
        outh += ' //%s,%s\n'%(cpath,ctypepath)
        outh += '    void checkBox%sSelected();\n'%(cname)
        outh += '    void checkBox%sUnSelected();\n'%(cname)
#ImageView
    if len(ddic['ImageView']) > 0:
        outh += '//ImageView\n'
    for ima in ddic['ImageView']:
        iname = ima['name']
        ipath = ima['path']
        itypePath = ima['typepath']
        outh += '    ImageView* m_%sImage;'%(iname)
        outh += ' //%s,%s\n'%(ipath,itypePath)
#LabelAtlas
    if len(ddic['LabelAtlas']) > 0:
        outh += '//LabelAtlas\n'
    for lab in ddic['LabelAtlas']:
        lname = lab['name']
        lpath = lab['path']
        ltypePath = lab['typepath']
        outh += '    LabelAtlas* m_%slabA;'%(lname)
        outh += ' //%s,%s\n'%(lpath,ltypePath)
#LoadingBar
    if len(ddic['LoadingBar']) > 0:
        outh += '//LoadingBar\n'
    for lob in ddic['LoadingBar']:
        loname = lob['name']
        lopath = lob['path']
        lotypepath = lob['typepath']
        outh += '    LoadingBar* m_%sLoadbar;'%(loname)
        outh += ' //%s,%s\n'%(lopath,lotypepath)
        outh += '    void setLoadingBar%sPencent(int pencent);\n'%(loname)
#Slider
    if len(ddic['Slider']) > 0:
        outh += '//Slider\n'
    for sl in ddic['Slider']:
        sname = sl['name']
        spath = sl['path']
        stypepath = sl['typepath']
        outh += '    Slider* m_%sSlider;'%(sname)
        outh += ' //%s,%s\n'%(spath,stypepath)
#Label
    if len(ddic['Label']) > 0:
        outh += '//TextLabel\n'
    for te in ddic['Label']:
        tename = te['name']
        tepath = te['path']
        tetypepath = te['typepath']
        outh += '    Text* m_%sText;'%(tename)
        outh += ' //%s,%s\n'%(tepath,tetypepath)
#TextField
    if len(ddic['TextField']) > 0:
        outh += '//TextField\n'
    for fi in ddic['TextField']:
        finame = fi['name']
        fipath = fi['path']
        fitypepath = fi['typepath']
        outh += '    TextField* m_%sTextInput;'%(finame)
        outh += ' //%s,%s\n'%(fipath,fitypepath)
        outh += '    std::string m_%sStrValue;//输入框中的值\n'%(finame)
        outh += '    void textField%sTouchEvent(Ref* obj, TextField::EventType type);\n'%(finame)
        
#Panel
    if len(ddic['Panel']) > 1:
        outh += '//Panel\n'
        for pa in ddic['Panel']:
            paname = pa['name']
            papath = pa['path']
            patypepath = pa['typepath']
            if cmp(patypepath,'Panel') != 0:
                outh += '    Layout* m_%sLayout;'%(paname)
                outh += ' //%s,%s\n'%(papath,patypepath)
                outh += '    void initLayout%s();\n'%(paname)
#ScrollView
    if len(ddic['ScrollView']) > 0:
        outh += '//ScrollView\n'
    for scr in ddic['ScrollView']:
        scname = scr['name']
        scpath = scr['path']
        sctypepath = scr['typepath']
        outh += '    ScrollView* m_%sScrollView;'%(scname)
        outh += ' //%s,%s\n'%(scpath,sctypepath)
        outh += '    void initScrollView%s();\n'%(scname)
        outh += '    void scrollView%sEvent(Ref *pSender,ScrollView::EventType type);\n'%(scname)
#ListView
    if len(ddic['ListView']) > 0:
        outh += '//ListView\n'
    for liv in ddic['ListView']:
        livname = liv['name']
        livpath = liv['path']
        livtypepath = liv['typepath']
        outh += '    ListView* m_%sListView;'%(livname)
        outh += ' //%s,%s\n'%(livpath,livtypepath)
        outh += '    int m_prePress%s;\n'%(livname)
        outh += '    std::vector<int> m_list%sDataVect'%(livname)
        outh += '    void initListView%s();\n'%(livname)
        outh += '    void setPanel%sItemHide();'%(livname)
        outh += '    void setListView%sItem(Widget* w,int n);//初始化子控件\n'%(livname)
        outh += '    void listScrollView%sEvent(Ref *pSender, ui::ScrollView::EventType type);//滚动图层回调函数,控制滑块\n'%(livname)
        outh += '    void listView%sEvent(Ref *pSender, ui::ListView::EventType type);\n'%(livname)
#PageView
    if len(ddic['PageView']) > 0:
        outh += '//PageView'
    for pag in ddic['PageView']:
        pagname = pag['name']
        pagpath = pag['path']
        pagtypepath = pag['typepath']
        outh += '    PageView* m_%sPageView;'%(pagname)
        outh += ' //%s,%s\n'%(pagpath,pagtypepath)
        outh += '    int m_pagView%sSele;\n'%(pagname)
        outh += '    std::vector<int> m_pageView%sDataVect;\n'%(pagname)
        outh += '    void initPageView%s();\n'%(pagname)
        outh += '    void setPageView%sItem(Widget* w,int n);//初始化子控件\n'%(pagname)
        outh += '    void pageView%sEvent(Ref *pSender,ui::PageView::EventType type);\n'%(pagname)

    if len(ddic['Button']) > 0:
        outh += '\n'
        outh += '    void onTouchEvent(cocos2d::Ref *pSender, Widget::TouchEventType type);\n'
        outh += '    void onWidgetTouchBeigen(cocos2d::Ref *pSender);\n'
        outh += '    void onWidgetTouchMove(cocos2d::Ref *pSender);\n'
        outh += '    void onWidgetTouchEnd(cocos2d::Ref *pSender);\n'
        outh += '    void onWidgetTouchCanceled(cocos2d::Ref *pSender);\n\n'
    
    if len(ddic['CheckBox']) > 0:
        outh += '\n'
        outh += '    void checkBoxEvent(Ref *pSender,CheckBox::EventType type);\n'    
        outh += '    void onCheckBoxSelectEvent(Ref *pSender);\n'
        outh += '    void onCheckBoxUnSelectEvent(Ref *pSender);\n'
    if len(ddic['Slider']) > 0:
        outh += '\n'
        outh += '    void  sliderEvent(Ref *pSender, Slider::EventType type);\n'
    outh +='''
private:
    int m_uiID;
    
};

#endif /* defined(__game4__%s__) */
    '''%(pName)
    
    outcpp = ''
    outcpp +='''//
//  %s.cpp
//  game4
//
//  Created by Junpeng Zhang on 2/3/15.
//  本代码由工具生成
//资源加载适合cocos2d-x 3.2版本的cocostuido 1.6 for windows
//

#include "%s.h"
#include "strHash.h"
////
////  strHash.h
////  game1
////  使用结构体来进行游戏属性存储会比较方便快捷
//// C++11新特性
////  Created by 俊盟科技1 on 8/26/14.
////
////
////为了使用字符串作为switch的case分支，这里加了些方法
//
//#ifndef game1_strHash_h
//#define game1_strHash_h
//#include "cocos2d.h"
//using namespace std;
//
//typedef std::uint64_t hash_t;
//
//constexpr hash_t prime = 0x100000001B3ull;
//constexpr hash_t basis = 0xCBF29CE484222325ull;
//
//hash_t hash_(char const* str);
////{
////    hash_t ret{basis};
////    
////    while(*str){
////        ret ^= *str;
////        ret *= prime;
////        str++;
////    }
////    
////    return ret;
////}
//
//constexpr hash_t hash_compile_time(char const* str, hash_t last_value = basis)
//{
//    return *str ? hash_compile_time(str+1, (*str ^ last_value) * prime) : last_value;
//}
//
//constexpr unsigned long long operator "" _hash(char const* p, size_t)
//{
//    return hash_compile_time(p);
//}
//
///*字符串作为case例子
//void simple_switch(char const* str)
//{
//    using namespace std;
//    switch(hash_(str)){
//        case "first"_hash:
//            cout << "1st one" << endl;
//            break;
//        case "second"_hash:
//            cout << "2nd one" << endl;
//            break;
//        case "third"_hash:
//            cout << "3rd one" << endl;
//            break;
//        default:
//            cout << "Default..." << endl;
//    }
//}
// */

#define kSoundButton "sound/Click_Button.wav"

USING_NS_CC;
using namespace ui;
using namespace std;
%s::%s()
{
    
}
%s::~%s()
{
    
}
cocos2d::Ref* %s::getUIConfData()
{
    __String* str = __String::createWithFormat("%%d",m_uiID);
    return str;
}
%s* %s::createFromManger(Ref* dat)
{
    %s* tmp = new %s();
    if(tmp){
        tmp->autorelease();
        __String* st = dynamic_cast<__String*>(dat);
        tmp->m_uiID = st->intValue();
        tmp->m_uiName = "%s";
        tmp->init();
        return tmp;
    }else{
        return nullptr;
    }
}
%s* %s::create(int uiID)
{
    %s* tmp = new %s();
    if(tmp){
        tmp->autorelease();
        tmp->m_uiID = uiID;
        tmp->m_uiName = "%s";
        tmp->init();
        return tmp;
    }else{
        return nullptr;
    }
}
%s* %s::create()
{
    %s* tmp = new %s();
    if(tmp){
        tmp->autorelease();
        tmp->m_uiName = "%s";
        tmp->init();
        return tmp;
    }else{
        return nullptr;
    }
    
}
// on "init" you need to initialize your instance
bool %s::init()
{
    //////////////////////////////
    // 1. super init first
    if ( !Layer::init() )
    {
        return false;
    }
'''%(pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName,pName)
    outcpp +=  '\n'
    plistnames = []
    if plistcount > 0:
        for x in range(plistcount):
            strtmp01 = className + str(x)
            plistnames.append(strtmp01)
            outcpp += '    SpriteFrameCache::getInstance()->addSpriteFramesWithFile(uiplist/%s);\n'%(strtmp01 + '.plist')
    
    outcpp += '    m_rootLayout = dynamic_cast<ui::Layout*>(GUIReader::getInstance()->widgetFromJsonFile(\"ui/%s\"));\n'%(filePath)
#     print ddic['Button']
    if len(ddic['Button']) > 0:  
        outcpp += '    //Button\n'
        for bc1 in range(len(ddic['Button'])):
            bc1name = ddic['Button'][bc1]['name']
            bc1path = ddic['Button'][bc1]['path']
            bc1typepath = ddic['Button'][bc1]['typepath']
            #print bc1typepath
            if cmp(bc1typepath,"Panel+Button") == 0: 
                outcpp += '    m_%sBtn = dynamic_cast<ui::Button*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(bc1name,bc1name)
                outcpp += '    m_%sBtn->addTouchEventListener(CC_CALLBACK_2(%s::onTouchEvent, this));\n'%(bc1name,pName)
            elif cmp(bc1typepath,'Panel+Panel+Button') == 0 or cmp(bc1typepath,'Panel+ListView+Button') == 0 or cmp(bc1typepath,'Panel+ScrollView+Button') or cmp(bc1typepath,'Panel+PageView+Button') == 0:
                splittmp = bc1path.split('+')  
                outcpp += '    Widget* tmpx%s = Helper::seekWidgetByName(m_rootLayout, \"%s\");\n'%(splittmp[1],splittmp[1])
                outcpp += '    Button* p_Btn%s = dynamic_cast<ui::Button*>(Helper::seekWidgetByName(tmpx%s, \"%s\"));\n'%(bc1name,splittmp[1],bc1name)
                outcpp += '    p_Btn%s->setTag(%d);\n'%(bc1name,bc1)
                outcpp += '    p_Btn%s->addTouchEventListener(CC_CALLBACK_2(%s::onTouchEvent, this));\n'%(bc1name,pName)
            else:
                outcpp += '    m_%sBtn = dynamic_cast<ui::Button*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(bc1name,bc1name)
                outcpp += '    m_%sBtn->addTouchEventListener(CC_CALLBACK_2(%s::onTouchEvent, this));\n'%(bc1name,pName)
    outcpp += '\n'
#     print ddic['CheckBox']
    if len(ddic['CheckBox']) > 0:
        outcpp += '    //CheckBox\n'
        for ch1 in range(len(ddic['CheckBox'])):
            chbox1 = ddic['CheckBox'][ch1]
            ch1name = chbox1['name']
            _ch1path = chbox1['path']
            _ch1typepath = chbox1['typepath']
            outcpp += '    m_%sChbox = dynamic_cast<CheckBox*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(ch1name,ch1name)
            outcpp += '    m_%sChbox->addEventListener(std::bind(&%s::checkBoxEvent,this,std::placeholders::_1,std::placeholders::_2));\n'%(ch1name,pName)
            outcpp += '\n'
#     print ddic['ImageView']
    if len(ddic['ImageView']) > 0:
        outcpp += '    //ImageView\n'
        for i1 in range(len(ddic['ImageView'])):
            image1 = ddic['ImageView'][i1]
            imname = image1['name']
            impath = image1['path']
            imtypepath = image1['typepath']
            if cmp(imtypepath,'Panel+ImageView') == 0:
                outcpp += '    m_%sImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(imname,imname)
            elif cmp(imtypepath,'Panel+Panel+ImageView') == 0 or cmp(imtypepath,'Panel+ListView+ImageView') == 0 or cmp(imtypepath,'Panel+ScrollView+ImageView') or cmp(imtypepath,'Panel+PageView+ImageView') == 0:
                splittmpi = impath.split('+')
                outcpp += '    Widget* tmpx%s = Helper::seekWidgetByName(m_rootLayout, \"%s\");\n'%(splittmpi[1],splittmpi[1])
                outcpp += '    ImageView* p_image%d = dynamic_cast<ui::ImageView*>(Helper::seekWidgetByName(tmpx%s, \"%s\"));\n'%(i1,splittmpi[1],imname)
            else:
                outcpp += '    m_%sImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(imname,imname)
#     print ddic['LabelAtlas']
    if len(ddic['LabelAtlas']) > 0:
        outcpp += '    //LabelAtlas\n'
        for l1 in range(len(ddic['LabelAtlas'])):
            labeAtl1 = ddic['LabelAtlas'][l1]
            l1name = labeAtl1['name']
            _l1path = labeAtl1['path']
            _l1typepath = labeAtl1['typepath']
            outcpp += '    m_%slabA = dynamic_cast<LabelAtlas*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(l1name,l1name)
#     print ddic['LoadingBar']
    if len(ddic['LoadingBar']) > 0:
        outcpp += '\n    //LoadingBar\n'
        for b1 in range(len(ddic['LoadingBar'])):
            lbar1 = ddic['LoadingBar'][b1]
            lb1name = lbar1['name']
            lb1path = lbar1['path']
            lb1typepath = lbar1['typepath']
            if cmp(lb1typepath,'Panel+LoadingBar') == 0:
                outcpp += '    m_%sLoadbar = dynamic_cast<LoadingBar*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(lb1name,lb1name)
                outcpp += '    m_%sLoadbar->setPercent(50);\n\n'%(lb1name)
            elif cmp(lb1typepath,'Panel+Panel+LoadingBar') == 0 or cmp(lb1typepath,'Panel+ListView+LoadingBar') == 0 or cmp(lb1typepath,'Panel+ScrollView+LoadingBar') or cmp(lb1typepath,'Panel+PageView+LoadingBar') == 0:
                splittmpl = lb1path.split('+')
                outcpp += '    Widget* tmpx%s = Helper::seekWidgetByName(m_rootLayout, \"%s\");\n'%(splittmpl[1],splittmpl[1])
                outcpp += '    LoadingBar* p_loadbar%d = dynamic_cast<ui::LoadingBar*>(Helper::seekWidgetByName(tmpx%s, \"%s\"));\n'%(b1,splittmpl[1],lb1name)
                outcpp += '    p_loadbar%d->setPercent(50);\n\n'%(b1)
            else:
                outcpp += '    m_%sLoadbar = dynamic_cast<LoadingBar*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(lb1name,lb1name)
                outcpp += '    m_%sLoadbar->setPercent(50);\n\n'%(lb1name)
#     print ddic['Slider']
    if len(ddic['Slider']) > 0:
        outcpp += '\n    //Slider\n'
        for s1 in range(len(ddic['Slider'])):
            slider1 = ddic['Slider'][s1]
            s1name = slider1['name']
            _s1path = slider1['path']
            _s1typepath = slider1['typepath']
            outcpp += '    m_%sSlider = dynamic_cast<Slider*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(s1name,s1name)
            outcpp += '    m_%sSlider->addEventListener(CC_CALLBACK_2(%s::sliderEvent, this));\n\n'%(s1name,pName)
#     print ddic['Label']
    if len(ddic['Label']) > 0:
        outcpp += '    //Label\n'
        for lx1 in range(len(ddic['Label'])):
            label1 = ddic['Label'][lx1]
            lx1name = label1['name']
            lx1path = label1['path']
            lx1typepath = label1['typepath']
            if cmp(lx1typepath,'Panel+Label') == 0:
                outcpp += '    m_%sText = dynamic_cast<Text*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(lx1name,lx1name)
            elif cmp(lx1typepath,'Panel+Panel+Label') == 0 or cmp(lx1typepath,'Panel+ListView+Label') == 0 or cmp(lx1typepath,'Panel+ScrollView+Label') or cmp(lx1typepath,'Panel+PageView+Label') == 0:
                splittmpt = lx1path.split('+')
                outcpp += '    Widget* tmpx%s = Helper::seekWidgetByName(m_rootLayout, \"%s\");\n'%(splittmpt[1],splittmpt[1])
                outcpp += '    m_%sText = dynamic_cast<Text*>(Helper::seekWidgetByName(tmpx%s, \"%s\"));\n'%(lx1name,splittmpt[1],lx1name)
            else:
                outcpp += '    m_%sText = dynamic_cast<Text*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(lx1name,lx1name)
#     print ddic['TextField']
    if len(ddic['TextField']) > 0:
        outcpp += '    //TextField\n'
        for tx1 in range(len(ddic['TextField'])):
            textf1 = ddic['TextField'][tx1]
            tx1name = textf1['name']
            _tx1path = textf1['path']
            _tx1typepath = textf1['typepath']
            outcpp += '    m_%sTextInput = dynamic_cast<TextField*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(tx1name,tx1name)
            outcpp += '    m_%sTextInput->addEventListener(CC_CALLBACK_2(%s::textField%sTouchEvent,this));\n\n'%(tx1name,pName,tx1name)
#     print ddic['Panel']
    if len(ddic['Panel']) > 1:
        outcpp += '    //Panel\n'
        for p1 in range(len(ddic['Panel'])):
            panel1 = ddic['Panel'][p1]
            p1name = panel1['name']
            _p1path = panel1['path']
            p1typepath = panel1['typepath']
            if cmp(p1typepath,'Panel') != 0:
                outcpp += '    m_%sLayout = dynamic_cast<Layout*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(p1name,p1name)
                outcpp += '    this->initLayout%s();\n'%(p1name)
#     print ddic['ScrollView']
    if len(ddic['ScrollView']) > 0:
        outcpp += '    //ScrollView\n'
        for sc1 in range(len(ddic['ScrollView'])):
            scroll1 = ddic['ScrollView'][sc1]
            sc1name = scroll1['name']
            _sc1path = scroll1['path']
            _sc1typepath = scroll1['typepath']
            outcpp += '    m_%sScrollView = dynamic_cast<ScrollView*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(sc1name,sc1name)
            outcpp += '    m_%sScrollView->addEventListener(CC_CALLBACK_2(%s::scrollView%sEvent,this));\n'%(sc1name,pName,sc1name)
            outcpp += '    this->initScrollView%s();\n\n'%(sc1name)
#     print ddic['ListView']
    if len(ddic['ListView']) > 0:
        outcpp += '    //ListView\n'
        for lv1 in range(len(ddic['ListView'])):
            listview1 = ddic['ListView'][lv1]
            lv1name = listview1['name']
            _lv1path = listview1['path']
            _lv1typepath = listview1['typepath']
            outcpp += '    m_prePress%s = -1;\n'%(livname)
            outcpp += '    m_%sListView = dynamic_cast<ListView*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(lv1name,lv1name)
            outcpp += '    m_%sListView->addEventListener(CC_CALLBACK_2(%s::listView%sEvent, this));\n'%(lv1name,pName,lv1name)
            outcpp += '    m_%sListView->addEventListener(CC_CALLBACK_2(%s::scrollView%sEvent, this));\n'%(lv1name,pName,lv1name)
            outcpp += '    this->initListView%s();\n'%(lv1name)
#     print ddic['PageView']
    if len(ddic['PageView']) > 0:
        outcpp += '    //PageView\n'
        for pg1 in range(len(ddic['PageView'])):
            pageview1 = ddic['PageView'][pg1]
            pg1name = pageview1['name']
            _pg1path = pageview1['path']
            _pg1typepath = pageview1['typepath']
            outcpp += '    m_pagView%sSele = -1;\n'%(pg1name)
            outcpp += '    m_%sPageView = dynamic_cast<PageView*>(Helper::seekWidgetByName(m_rootLayout, \"%s\"));\n'%(pg1name,pg1name)
            outcpp += '    m_%sPageView->addEventListener(std::bind(&%s::pageView%sEvent,this,std::placeholders::_1,std::placeholders::_2));\n'%(pg1name,pName,pg1name)
            outcpp += '    this->initPageView%s();\n'%(pg1name)
            
    outcpp += '\n'
    outcpp +='''
    this->addChild(m_rootLayout);
    return true;
}
'''
    outcpp +='''
void %s::close()
{
    this->removeFromParent();
}
'''%(pName)
#     print ddic['Button']
#         outh += '    void onTouchEvent(cocos2d::Ref *pSender, Widget::TouchEventType type);\n'
#         outh += '    void onWidgetTouchBeigen(cocos2d::Ref *pSender);\n'
#         outh += '    void onWidgetTouchMove(cocos2d::Ref *pSender);\n'
#         outh += '    void onWidgetTouchEnd(cocos2d::Ref *pSender);\n'
#         outh += '    void onWidgetTouchCanceled(cocos2d::Ref *pSender);\n\n'
    if len(ddic['Button']) > 0:
        outcpp += '//buttonEvent\n'
        outcpp +='''
void %s::onTouchEvent(cocos2d::Ref *pSender, Widget::TouchEventType type)
{
    //按下、移动、结束、取消
   // string buttonname = btntmp->getName();
    switch (type)
    {
        case Widget::TouchEventType::ENDED:
        {
            this->onWidgetTouchEnd(pSender);
        }
            break;
        case Widget::TouchEventType::BEGAN:
        {
            this->onWidgetTouchBeigen(pSender);
        }
            break;
        case Widget::TouchEventType::MOVED:
        {
            this->onWidgetTouchMove(pSender);
        }
            break;
        case Widget::TouchEventType::CANCELED:
        {
            this->onWidgetTouchCanceled(pSender);
        }
            break;
        default:
            break;
    }

}
'''%(pName)
        outcpp +='''
void %s::onWidgetTouchBeigen(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
'''%(pName)
        for b2 in range(len(ddic['Button'])):
            btn2 = ddic['Button'][b2]
            b2name = btn2['name']
            outcpp += '        case \"%s\"_hash:\n'%(b2name)
            outcpp += '        {\n\n        }\n'
            outcpp += '            break;\n'
        outcpp +='''        default:
            break;
    }
}
'''
        outcpp +='''
void %s::onWidgetTouchMove(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
'''%(pName)
        for b2 in range(len(ddic['Button'])):
            btn2 = ddic['Button'][b2]
            b2name = btn2['name']
            outcpp += '        case \"%s\"_hash:\n'%(b2name)
            outcpp += '        {\n\n        }\n'
            outcpp += '            break;\n'
        outcpp +='''        default:
            break;
    }
}
'''
        outcpp +='''
void %s::onWidgetTouchEnd(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
'''%(pName)
        for b2 in range(len(ddic['Button'])):
            btn2 = ddic['Button'][b2]
            b2name = btn2['name']
            outcpp += '        case \"%s\"_hash:\n'%(b2name)
            outcpp += '        {\n\n        }\n'
            outcpp += '            break;\n'
        outcpp +='''        default:
            break;
    }
}
'''
        outcpp +='''
void %s::onWidgetTouchCanceled(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
'''%(pName)
        for b2 in range(len(ddic['Button'])):
            btn2 = ddic['Button'][b2]
            b2name = btn2['name']
            outcpp += '        case \"%s\"_hash:\n'%(b2name)
            outcpp += '        {\n\n        }\n'
            outcpp += '            break;\n'
        outcpp +='''        default:
            break;
    }
}
'''
#     print ddic['CheckBox']
# outh += '    void checkBox%sSelected();\n'%(cname)
# outh += '    void checkBox%sUnSelected();\n'%(cname)
# outh += '    void onCheckBoxSelectEvent(Ref *pSender);\n'
# outh += '    void onCheckBoxUnSelectEvent(Ref *pSender);\n'
    if len(ddic['CheckBox']) > 0:
        outcpp += '//CheckBox\n'
        outcpp += '''void %s::checkBoxEvent(Ref *pSender,ui::CheckBox::EventType type)
{
    CocosDenshion::SimpleAudioEngine::getInstance()->playEffect(kSoundButton);
    if (type == CheckBox::EventType::SELECTED) {
        this->onCheckBoxSelectEvent(pSender);
    }else{//UNSELECTED
        this->onCheckBoxUnSelectEvent(pSender);
    }
}
'''%(pName)
        outcpp += ''' void %s::onCheckBoxSelectEvent(Ref *pSender)
{
    CheckBox* btntmp = dynamic_cast<CheckBox*>(pSender);
    switch(hash_(btntmp->getName().c_str())){
'''%(pName)
        for ch2 in range(len(ddic['CheckBox'])):
            check2 = ddic['CheckBox'][ch2]
            ch2name = check2['name']
            outcpp += '        case \"%s\"_hash:\n'%(ch2name)
            outcpp += '        {\n'
            outcpp += '            this->checkBox%sSelected();\n'%(ch2name)
            outcpp += '        }\n'
            outcpp += '            break;\n'
        outcpp +='''        default:
            break;
        }
}
'''
        outcpp += ''' void %s::onCheckBoxUnSelectEvent(Ref *pSender)
{
    CheckBox* btntmp = dynamic_cast<CheckBox*>(pSender);
    switch(hash_(btntmp->getName().c_str())){
'''%(pName)
        for ch2 in range(len(ddic['CheckBox'])):
            check2 = ddic['CheckBox'][ch2]
            ch2name = check2['name']
            outcpp += '        case \"%s\"_hash:\n'%(ch2name)
            outcpp += '        {\n'
            outcpp += '            this->checkBox%sUnSelected();\n'%(ch2name)
            outcpp += '        }\n'
            outcpp += '            break;\n'
        outcpp +='''        default:
            break;
        }
}
'''
        for ch2 in range(len(ddic['CheckBox'])):
            check2 = ddic['CheckBox'][ch2]
            ch2name = check2['name']
            outcpp += 'void %s::checkBox%sSelected()\n'%(pName,ch2name)
            outcpp += '{\n\n}\n'
            outcpp += 'void %s::checkBox%sUnSelected()\n'%(pName,ch2name)
            outcpp += '{\n\n}\n'
#     print ddic['ImageView']
#     print ddic['LabelAtlas']
#     print ddic['LoadingBar']
# void setLoadingBar%sPencent(int pencent);\n
    if len(ddic['LoadingBar']) > 0:
        outcpp += '//LoadingBar\n'
        for lo3 in range(len(ddic['LoadingBar'])):
            loadbar3 = ddic['LoadingBar'][lo3]
            lo3name = loadbar3['name']
            outcpp += 'void %s::setLoadingBar%sPencent(int pencent)\n'%(pName,lo3name)
            outcpp += '{\n'
            outcpp += '    m_%sLoadbar->setPercent(pencent);\n'%(loname)
            outcpp += '}\n'
#     print ddic['Slider']
    if len(ddic['Slider']) > 0:
        outcpp += '//Slider\n'
        outcpp += '''void  %s::sliderEvent(Ref *pSender, Slider::EventType type)
{
    if (type == Slider::EventType::ON_PERCENTAGE_CHANGED)
    {
        Slider* slider = dynamic_cast<Slider*>(pSender);    //滑块在15到85之间滑动；
        switch(hash_(slider->getName().c_str())){
'''%(pName)
        for sl3 in range(len(ddic['Slider'])):
            slider3 = ddic['Slider'][sl3]
            sl3name = slider3['name']
            outcpp += '            case \"%s\"_hash:\n'%(sl3name)
            outcpp += '            {\n\n'
            outcpp += '            }\n'
        outcpp += '''            default:
                break;
        }
    }
}
'''
#     print ddic['Label']
#     print ddic['TextField']
    if len(ddic['TextField']) > 0:
        outcpp += '//TextField'
        for tf3 in range(len(ddic['TextField'])):
            textfile3 = ddic['TextField'][tf3]
            tf3name = textfile3['name']
            outcpp += '''void %s::textField%sTouchEvent(Ref* obj, TextField::EventType type)
{
    switch (type) {
        case TextField::EventType::ATTACH_WITH_IME://开启输入
        {
            
        }
            break;
        case TextField::EventType::DETACH_WITH_IME://关闭输入
        {
'''%(pName,tf3name)
            outcpp += '            m_%sStrValue = m_%sTextInput->getStringValue();//输入框中的值\n'%(tf3name,tf3name)
            outcpp +='''
        }
            break;
        case TextField::EventType::INSERT_TEXT://插入新文本
        {
            
        }
            break;
        case TextField::EventType::DELETE_BACKWARD://删除文本
        {
            
        }
            break;
        default:
            break;
    }
}
'''
#     print ddic['Panel']
    if len(ddic['Panel']) > 1:
        outcpp += '//Panel\n'
        for pa3 in ddic['Panel']:
            pa3name = pa3['name']
            pa3typepath = pa['typepath']
            if cmp(pa3typepath,'Panel') != 0:
                outcpp += 'void %s::initLayout%s()\n'%(pName,pa3name)
                outcpp += '{\n\n}\n'
#     print ddic['ScrollView']
    if len(ddic['ScrollView']) > 0:
        outcpp += '//ScrollView\n'
        for sc3 in range(len(ddic['ScrollView'])):
            scroll3 = ddic['ScrollView'][sc3]
            sc3name = scroll3['name']
            sc3path = scroll3['path']
            sc3typepath = scroll3['typepath']
            outcpp += ' //%s,%s\n'%(sc3path,sc3typepath)
            outcpp += 'void %s::initScrollView%s()\n'%(pName,sc3name)
            outcpp += '''{
            
}
'''
            outcpp += 'void %s::scrollView%sEvent(Ref *pSender,ScrollView::EventType type)\n'%(pName,sc3name)
            outcpp += '''{
    switch (type) {
        case ui::ScrollView::EventType::SCROLLING:        //滚动过程中有好多次响应；
        {
//             Point  pt=m_scrollView->getInnerContainer()->getPosition();
//             Size  size=m_scrollView->getInnerContainer()->getContentSize();
//             
//             float  percentScroll=(size.height+pt.y)/size.height*70;
//             m_slider->setPercent(percentScroll); 
        }
            break;
        case ui::ScrollView::EventType::SCROLL_TO_TOP:     //到达顶点，只是一次响应；
        {
            //m_slider->setPercent(14);//设置滑动条位置
        }
            break;
            
        case ui::ScrollView::EventType::SCROLL_TO_BOTTOM:    //到达底点；
        {
            //m_slider->setPercent(86);
        }
            break;
        case ui::ScrollView::EventType::SCROLL_TO_LEFT: //横向时到达左边
        {
        
        }
            break;
        case ui::ScrollView::EventType::SCROLL_TO_RIGHT: //横向时到达右边
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_TOP: //顶部回弹事件
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_BOTTOM: //底部回弹事件
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_LEFT: //左边回弹事件
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_RIGHT: //右边回弹事件
        {
        
        }
            break;
        default:
            break;
    }
}
'''
#     print ddic['ListView']
    if len(ddic['ListView']) > 0:
        outcpp += '//ListView\n'
        for li3 in range(len(ddic['ListView'])):
            listview3 = ddic['ListView'][li3]
            li3name = listview3['name']
            li3path = listview3['path']
            li3typepath = listview3['typepath']
            outcpp += '//%s,%s\n'%(li3path,li3typepath)
#             outh += '    ListView* m_%sListView;'%(livname)
#             outh += ' //%s,%s\n'%(livpath,livtypepath)
#             outh += '    std::vector<int> m_list%sDataVect'%(livname)
            outcpp += 'void %s::initListView%s()\n'%(pName,li3name)
            outcpp += '''{
            m_list%sDataVect.clear();
}
'''%(li3name)
            outcpp += 'void %s::setListView%sItem(Widget* w,int n)//初始化子控件\n'%(pName,li3name)
            outcpp += '''{

}
'''
            outcpp += 'void %s::listScrollView%sEvent(Ref *pSender, ui::ScrollView::EventType type)//滚动图层回调函数,控制滑块\n'%(pName,li3name)
            outcpp += '''{
    switch (type) {
        case ui::ScrollView::EventType::SCROLLING:        //滚动过程中有好多次响应；
        {
//             Point  pt=m_scrollView->getInnerContainer()->getPosition();
//             Size  size=m_scrollView->getInnerContainer()->getContentSize();
//             
//             float  percentScroll=(size.height+pt.y)/size.height*70;
//             m_slider->setPercent(percentScroll); 
        }
            break;
        case ui::ScrollView::EventType::SCROLL_TO_TOP:     //到达顶点，只是一次响应；
        {
            //m_slider->setPercent(14);//设置滑动条位置
        }
            break;
            
        case ui::ScrollView::EventType::SCROLL_TO_BOTTOM:    //到达底点；
        {
            //m_slider->setPercent(86);
        }
            break;
        case ui::ScrollView::EventType::SCROLL_TO_LEFT: //横向时到达左边
        {
        
        }
            break;
        case ui::ScrollView::EventType::SCROLL_TO_RIGHT: //横向时到达右边
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_TOP: //顶部回弹事件
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_BOTTOM: //底部回弹事件
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_LEFT: //左边回弹事件
        {
        
        }
            break;
        case ui::ScrollView::EventType::BOUNCE_RIGHT: //右边回弹事件
        {
        
        }
            break;
        default:
            break;
    }
}   
'''
            outcpp += 'void %s::listView%sEvent(Ref *pSender, ui::ListView::EventType type);\n'%(pName,li3name)
            outcpp += '''{
    ListView* plistView = static_cast<ListView*>(pSender);
    if(!listView){
        log("ScrollView  is  NULL"); 
        return;
    }
    switch (type) {
        case ui::ListView::EventType::ON_SELECTED_ITEM_END :    //点击结束；
        {
            ssize_t  n=plistView->getCurSelectedIndex();      //n对应着
            this->setPanel%sItemShow(n);                           // 显示底；
            if(n!=m_prePress){   //隐藏前一项的底；
                this->setPanel%sItemHide();  
            }    
            m_prePress%s=n;                                 //前一项的索引；
        }
            break;
        case ui::ListView::EventType::ON_SELECTED_ITEM_START :    //点选开始时；
        {
            ssize_t  n=plistView->getCurSelectedIndex();      //n对应着m_equip;
        }
            break;
        default:
            break;
    }

'''%(li3name,li3name,li3name)
            outcpp += '''void %s::setPanel%sItemShow(int n)
{
    Layout* tmpItem = m_%sListView->getItem(n);
}
'''%(pName,li3name,li3name)
            outcpp += '''void %s::setPanel%sItemHide()
{
    Layout* tmpItem = m_%sListView->getItem(m_prePress%s);
} 
'''%(pName,li3name,li3name,li3name)
#     print ddic['PageView']
    if len(ddic['PageView']) > 0:
        outcpp += '//PageView\n'
        for pa3 in range(len(ddic['PageView'])):
            pageview3 = ddic['PageView'][pa3]
            pa3name = pageview3['name']
            outcpp += 'void %s::initPageView%s()\n'%(pName,pa3name)
            outcpp += '''{
    m_pageView%sDataVect.clear();
    m_pagView%sSele = 0;
}
'''%(pa3name,pa3name)
            outcpp += 'void %s::setPageView%sItem(Widget* w,int n)//初始化子控件\n'%(pName,pa3name)
            outcpp +='''{
    Layout tmpout = dynamic_cast<Layout*>(w);
}
'''
            outcpp += 'void %s::pageView%sEvent(Ref *pSender,ui::PageView::EventType type)\n'%(pName,pa3name)
            outcpp +='''{
    switch (type)
    {
        case PageView::EventType::TURNING:
        {
            PageView* pageView = dynamic_cast<PageView*>(pSender);
             m_pagView%sSele = (int)pageView->getCurPageIndex();
        }
            break;
        default:
            break;
    }
}
'''%(pa3name)
    outcpp += '''
void %s::onEnter()
{
    Layer::onEnter();
    
}
void %s::onExit()
{
'''%(pName,pName)
    for plx in plistnames:
        outcpp += '''    SpriteFrameCache::getInstance()->removeSpriteFramesFromFile("uiplist/%s.plist");\n'''%(plx)
        outcpp += '''    Director::getInstance()->getTextureCache()->removeTextureForKey("uiplist/%s.png");\n'''%(plx)

    outcpp +='''
    Layer::onExit();
}
'''
    return outcpp,outh

def conventJsonToProject(JsonF):
    outJson = JsonF
    outJson['textures'] = []
    outJson['texturesPng'] = []
    outWtree,childTreePath,imagelist = conventJsonWidgetTree(outJson['widgetTree'],outJson['widgetTree']['options']['name'],outJson['widgetTree']['classname'])
    outJson['widgetTree'] = outWtree
    #print imagelist
    #print childTreePath
    return outJson,childTreePath,imagelist



def getJsonDic(filePath):
    f = open(filePath,'r')
    tmp = json.loads(f.read())
    f.close()
    return tmp

def saveJsonDic(jsonDic,savePath):
    print jsonDic
    strjson = json.dumps(jsonDic,ensure_ascii=False)
    #strjson.replace(u'迷你简准圆','mnjzy')
    #strjson.replace(u'长城特圆体','cctyt')
    f = open(savePath,'w')
    f.write(strjson)
    f.close()

def saveClassFile(cpp,h,name):
    maindi = cur_file_dir()
    cppPath = maindi + os.sep + UIClassDir + os.sep + UINameFront + name + '.cpp'
    hPath = maindi + os.sep + UIClassDir + os.sep + UINameFront + name + '.h'
    fcpp = open(cppPath,'w')
    fcpp.write(cpp)
    fcpp.close()
    fh = open(hPath,'w')
    fh.write(h)
    fh.close()
    
def saveTestClass(nameList):
    maindi = cur_file_dir()
    fpath = maindi + os.sep + UIClassTestDir + os.sep + 'TestUIClass.cpp'
    outstr = ''
    for n in range(len(nameList)):
        strtmp = nameList[n]
        outstr += '#include \"UI%s.h\"\n'%(strtmp)
    outstr += '\n#define kUICount %d'%(len(nameList))
    outstr += '\n\n\n'
    outstr += '''    switch (uiCount) {
'''
    for n in range(len(nameList)):
        strtmp = nameList[n]
        outstr += '''        case %d:
        {
            this->removeChild(thenLayer);
            
            UI%s* test = UI%s::create();
            this->addChild(test,0);
            thenLayer = test;
        }
            break;
'''%(n+1,strtmp,strtmp)
    outstr += '''        default:
            break;
    }
'''
    f = open(fpath,'w')
    f.write(outstr)
    f.close()
    
    
def isHeaveImage(imgx):
    if os.path.exists(imgx):
        return True
    else:
        return False
    
def packageUsedUIImage(uiimgs,outname):
    allImage = ''
    for im in uiimgs:
        imgpath = cur_file_dir() + os.sep + plistDir + os.sep + im
        allImage += imgpath + ' '
    outpath = cur_file_dir() + os.sep + "uiplist"
    cmdstr = tpcmd + " " + allImage + " --data " + outpath + os.sep + outname + "{n}.plist" +\
           " --sheet " + outpath + os.sep + outname + "{n}.pvr.ccz" +\
           " --opt RGBA8888 --dither-fs-alpha" +\
           " --max-width 1024 --max-height 1024 --multipack --pack-mode Best"
    os.system(cmdstr)
    
def saveUIUsedImageFileName(imagelist,savePath,dirname):
    imagelisttmp = imagelist
    f = open(savePath + os.sep + dirname+'.txt','w')
    if os.path.exists(savePath + os.sep + dirname):
        shutil.rmtree(savePath + os.sep + dirname)
    os.mkdir(savePath + os.sep + dirname)
    nofindImg = []
    findImg = []
    saveplistpath = savePath + os.sep + dirname
    for i in imagelisttmp:
        strtmp = i + '\n'
        f.write(strtmp)
        imagefilePath = cur_file_dir() + os.sep + uiAllImage + os.sep + i
        #print imagefilePath
        if os.path.exists(imagefilePath):
            dstimg = savePath + os.sep + dirname + os.sep + i
            shutil.copyfile(imagefilePath, dstimg)
            findImg.append(i)
        else:
            print i
            nofindImg.append(i)
    f.close()
    #打包界面使用到的图片,在界面加载时加载,界面关闭时释放
    packageUsedUIImage(findImg,dirname)
    if len(nofindImg) > 0:
        frro = open(savePath + os.sep + dirname+os.sep + 'noImageErro.txt','w')
        for ero in nofindImg:
            frro.write(ero)
            frro.write('\n')
        frro.close()
    #界面打包之后的包文件数量
    plistfilecount = 0
    for px in range(10):
        pathne = cur_file_dir() + os.sep + "uiplist" + os.sep + dirname +"%d.plist"%(px)
        if os.path.exists(pathne):
            plistfilecount += 1
        else:
            break
    print "UI %s plist count=%d"%(dirname,plistfilecount)
    return plistfilecount
def readProjectUIClassFile():
    clasfilemap = {}
    cppfs = getAllJsonUIFile(cur_file_dir() + os.sep + 'Classes',fromatx = ".cpp")
    for cs in cppfs:
        clasfilemap[cs[2]] = cur_file_dir() + os.sep + 'Classes' + cs[0]
    return clasfilemap

def addPlistRead(strclass,classname,uiname,pcount):
    addstr = ""
    if pcount > 0:
        addstr += "\n\tplistCount = %d;\n"%(pcount)
        for x in range(pcount):
            addstr += '''\tSpriteFrameCache::getInstance()->addSpriteFramesWithFile("uiplist/%s%d.plist");\n'''%(uiname,x)
    strt = strclass
    fcp = strt.find('''m_rootLayout = dynamic_cast<ui::Layout*>(GUIReader::getInstance()->widgetFromJsonFile(''')
    print fcp
    isfind = 0
    if fcp > 0:
        isfind = 1
        strt = strt[0:fcp] + addstr + '\t'+ strt[fcp:]
    elif fcp < 0:
        rfcp = strt.find('''m_pNode = GUIReader::getInstance()->widgetFromJsonFile(''')
        if rfcp > 0:
            isfind = 1
            strt = strt[0:rfcp] + addstr + '\t'+ strt[rfcp:]
    if isfind == 1:
        fcfile = open( cur_file_dir() + os.sep + 'classchangeout' + os.sep + classname + '.cpp','w')
        fcfile.write(strt)
        fcfile.close()

#主方法
def main():
    maindir = cur_file_dir()
    print maindir
    oldjsonlist = getAllJsonUIFile(maindir + os.sep + jsonIn)
    print oldjsonlist
    if os.path.exists(maindir + os.sep + jsonOut):
        shutil.rmtree(maindir + os.sep + jsonOut)
    os.mkdir(maindir + os.sep + jsonOut)
    if os.path.exists(maindir + os.sep + UIClassDir):
        shutil.rmtree(maindir + os.sep + UIClassDir)
    os.mkdir(maindir + os.sep + UIClassDir)
    if os.path.exists(maindir + os.sep + UIClassTestDir):
        shutil.rmtree(maindir + os.sep + UIClassTestDir)
    os.mkdir(maindir + os.sep + UIClassTestDir)
    plistpath = cur_file_dir() + os.sep + "uiplist"
    if os.path.exists(plistpath):
        shutil.rmtree(plistpath)
    os.mkdir(plistpath)
    classNameList = []
    imageusedcount = {}#图片在那些界面中使用到
    uiUsedImagemap = {}#界面中使用到的图片
    allheaveImages = getAllJsonUIFile(maindir + os.sep + uiAllImage,".png")#所有存在的图片
    imagesize = {}#图片的面积
    uiclassfile = readProjectUIClassFile()#所有界面相关的.cpp文件
    for imh in allheaveImages:
        imgpathtmp = maindir + os.sep + uiAllImage + os.sep + imh[0]
        imgfile=Image.open(imgpathtmp)
        (w,h) = imgfile.size
        mianji = w*h
        imagesize[imh[0]] = mianji
    for n in range(len(oldjsonlist)):
        jsonpath = maindir + os.sep + jsonIn + os.sep + oldjsonlist[n][0]
        jsonDic = getJsonDic(jsonpath)
        outJson,chTreePath,imagelist = conventJsonToProject(jsonDic)
        #print imagelist
        for imx in imagelist:
            if imageusedcount.has_key(imx):
                imageulist = imageusedcount[imx]
                imageulist[0] += 1
                imageulist[1].append(oldjsonlist[n][2])
                imageusedcount[imx] = imageulist
            else:
                imageulist = [1,[oldjsonlist[n][2]]]
                imageusedcount[imx] = imageulist
        plistcount = saveUIUsedImageFileName(imagelist,maindir + os.sep + UsedImageFile,oldjsonlist[n][2])
        classfiletmp = ""
        classname = ''
        if uiclassfile.has_key(UINameFront+oldjsonlist[n][2]):
            cppfilestr = open(uiclassfile[UINameFront+oldjsonlist[n][2]],'r')
            classname = UINameFront+oldjsonlist[n][2]
            classfiletmp = cppfilestr.read()
            cppfilestr.close()
        elif uiclassfile.has_key('Ui'+oldjsonlist[n][2]):
            print uiclassfile['Ui'+oldjsonlist[n][2]]
            cppfilestr = open(uiclassfile['Ui'+oldjsonlist[n][2]],'r')
            classname = 'Ui'+oldjsonlist[n][2]
            classfiletmp = cppfilestr.read()
            cppfilestr.close()
        elif uiclassfile.has_key('ui'+oldjsonlist[n][2]):
            cppfilestr = open(uiclassfile['ui'+oldjsonlist[n][2]],'r')
            classname = 'ui'+oldjsonlist[n][2]
            classfiletmp = cppfilestr.read()
            cppfilestr.close()
        addPlistRead(classfiletmp,classname,oldjsonlist[n][2],plistcount)
        uiUsedImagemap[oldjsonlist[n][2]] = imagelist
        saveJsonDic(outJson, maindir + os.sep + jsonOut + os.sep + oldjsonlist[n][0])
        filePath = oldjsonlist[n][0]
        outCpp,outH = createClassFile(chTreePath,oldjsonlist[n][2],filePath,plistcount)
        saveClassFile(outCpp,outH,oldjsonlist[n][2])
        classNameList.append(oldjsonlist[n][2])
    saveTestClass(classNameList)
    allimglist = imageusedcount.keys()
    fimgcount = open(maindir + os.sep + UsedImageFile +os.sep + 'usedImageCount.txt','w')
    for imk in allimglist:
        imktlist = imageusedcount[imk]
        strtmpx = imk + '\t'
        if imagesize.has_key(imk):
            strtmpx += str(imagesize[imk]) + '\t'
        else:
            strtmpx += '0' + '\t'
        strtmpx +=str(imktlist[0]) +'\t' + str(imktlist[1])
        strtmpx +='\n'
        fimgcount.write(strtmpx)
    fimgcount.close()
    readProjectUIClassFile()
    #print imagesize
if __name__ == '__main__':
    main()