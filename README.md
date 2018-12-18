# chinese_wordcloud_pyqt5  
## pyqt5中文词云生成
* 通过调用Wordcloud和jieba这两个库实现中文词云。
* 先调用jieba库进行中文分词，再用Wordcloud生成词云。
* 使用pyqt5生成图形界面  
![image](https://github.com/mantuoluozk/chinese_wordcloud_pyqt5/blob/master/resource/%E7%A8%8B%E5%BA%8F%E6%88%AA%E5%9B%BE.png)
## 环境
* python3
* 安装Wordcloud库，```pip install wordcloud```或conda下```conda install -c conda-forge wordcloud```
* 安装jieba库,```pip install jieba```
* 安装pyqt5,```pip install pyqt5```
## 使用与开发
* codes文件夹中main.py是主函数，调用了function.py实现词云生成功能。
* resource文件夹中是供测试的图片文字。
* 开发时先用pyqt5-tools中的designer.exe设计ui界面,再用pyuic5将.ui文件转为.py文件。
## 链接
* ![jieba中文分词](https://github.com/fxsjy/jieba)
* ![wordcloud库](https://github.com/amueller/word_cloud)
* ![pyqt5中文参考手册](https://maicss.gitbooks.io/pyqt5/)
