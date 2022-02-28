import sys
import json
import PyQt5.QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

# UI파일 연결
search_window = uic.loadUiType("naver_search.ui")[0]

    # 네이버 검색 버튼 기능 설정
class Naver_btn(QMainWindow, search_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.naver_btn.clicked.connect(self.search_naver)
        
    def search_naver(self):
        if self.search_btn.isClicked():
            a = self.text_list.currentItem().text()
            url1 = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + a
            self.search_view.load(QUrl(url1))

    # 유튜브 검색 버튼 기능 설정
class Youtube_btn(QMainWindow, search_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.youtube_btn.clicked.connect(self.search_youtube)
    
    def search_youtube(self):
        if self.search_btn.isClicked():
            a = self.text_list.currentItem().text()
            url1 = "https://www.youtube.com/results?search_query=" + a
            self.search_view.load(QUrl(url1))
