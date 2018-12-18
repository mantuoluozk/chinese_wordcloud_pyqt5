# -*- coding: utf-8 -*-

import random
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from os import path

def run(imgpath,txtpath,color):

    # 文本路径名
    text_path = txtpath 

    # 中文字体路径名
    font_path = 'ttf/Hiragino.ttf' 

    # 背景图片路径名
    img_path = imgpath

    # 保存的图片名字
    img_result = 'result.png' 

    # 获取当前文件路径
    p = path.dirname('.')

    # 打开文本
    text = open(path.join(p, text_path),'r', encoding='UTF-8').read()

    # 中文分词
    text = ' '.join(jieba.cut(text))
    print(text[:100])

    # 颜色函数
    def random_color(word, font_size, position, orientation, font_path, random_state):
        s = 'hsl(0, %d%%, %d%%)' % (random.randint(0, 255), random.randint(0, 255))
        print(s)
        return s
        
    if color:   #从图片中生成颜色
        mask = np.array(Image.open(img_path))       #生成对象
        wc = WordCloud(mask=mask, font_path=font_path, mode='RGBA', background_color=None).generate(text)
        image_colors = ImageColorGenerator(mask)
        wc.recolor(color_func=image_colors)
    else:       #随机颜色
        mask = np.array(Image.open(img_path))    #生成对象
        wc = WordCloud(color_func=random_color, mask=mask, font_path=font_path, mode='RGBA', background_color=None).generate(text)

    # 显示词云
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    # 保存到文件
    wc.to_file(path.join(p, img_result))