# gameUIResTool
1.先使用resTool.py工具对uiRename中的图片进行重命名。

2.重命名后的图片会在outplist目录中。以及out目录中。out目录中的图片在界面编辑器中使用，outplist中的图片用来打包pvr图片组。

3.图片重命名结束后，使用UI编辑器开始编辑UI,编辑好之后，导出json格式界面。

4.将编辑器导出的json文件复制到UIJson目录中。

5.运行uiJsonUIDate.py，运行之后，会在UIClass中生成界面对就有C++类代码。将代码复制到游戏项目，作一下简单修可，即可以在项目中使用。

6.将UIJsonOut中的json文件复制到UIJson目录中，并替换原来的文件。再次运行uiJsonUIDate.py。这时会成生界面对应的pvr打包好的图片。
