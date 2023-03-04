# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:08:27 2023

@author: Administrator
"""

import streamlit as st
#from PIL import Image
#全局配置
st.set_page_config(
    page_title="huajiaCake",    #页面标题
    page_icon=":yum:",        #icon:emoji":rainbow:"
    layout="wide",                #页面布局
    initial_sidebar_state="auto"  #侧边栏
)

###标题

st.markdown('## :blossom:花.家')
st.markdown('可联系：')


# import os
# st.write(os.getcwd())

tab1, tab2, tab3,tab4,tab5= st.tabs(["新品推介","定制蛋糕", "蛋糕卷","茶饮","手工零食",])
with tab1:
    st.markdown('######  巴克斯')
    #image =Image.open('pages/巴克斯.jpg')
    #w, h = image.size
    #image.thumbnail((w//2, h//2))
    image ='pages/巴克斯.jpg'
    st.image(image, caption='')
   
    
   
with tab2:
    tab21, tab22, tab23= st.tabs(["插件蛋糕","水果蛋糕", "手绘蛋糕"])
    with tab21:
       image = 'pages/插件蛋糕-超人.jpg'
       st.image(image, caption='')
       image = 'pages/插件蛋糕-车车.jpg'
       st.image(image, caption='')
    with tab22:
       image = 'pages/水果蛋糕.jpg'
       st.image(image, caption='')
    with tab23:
       image = 'pages/手绘蛋糕-叮当.jpg'
       st.image(image, caption='')

with tab3:
   tab31, tab32, tab33,tab34,tab35,tab36= st.tabs(["浮云卷","爆浆草莓卷", "芒果卷","巧克力卷","香葱肉松卷","盒子蛋糕"])
   with tab31:
      image = 'pages/浮云卷.jpg'
      st.image(image, caption='')
   with tab32:
      image = 'pages/爆浆草莓卷.jpg'
      st.image(image, caption='')
   with tab33:
      image = 'pages/芒果卷.jpg'
      st.image(image, caption='')
   with tab34:
      image = 'pages/巧克力卷.jpg'
      st.image(image, caption='')
   with tab35:
      image = 'pages/香葱肉松卷.jpg'
      st.image(image, caption='') 
   with tab36:
      image = 'pages/盒子蛋糕.jpg'
      st.image(image, caption='')     

      


with tab4:
   tab41, tab42, tab43= st.tabs(["招牌奶茶","草莓椰椰", "生椰拿铁"])
   with tab41:
      image = 'pages/招牌奶茶.jpg'
      st.image(image, caption='')
   with tab42:
      image = 'pages/草莓椰椰.jpg'
      st.image(image, caption='')
   with tab43:
      image = 'pages/生椰拿铁.jpg'
      st.image(image, caption='')
      
with tab5:
   st.markdown('######  麻薯')
   image = 'pages/麻薯.jpg'
   st.image(image, caption='')