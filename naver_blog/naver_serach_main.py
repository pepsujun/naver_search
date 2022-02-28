from re import A
import sys
import json
import PyQt5.QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic



# UI파일 연결
search_window = uic.loadUiType("naver_search.ui")[0]



class NaverSerachblog(QMainWindow, search_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("통합 검색기")
        self.search_button.clicked.connect(self.showTextlist)
        # self.search_button.clicked.connect(self.showTextresult)
        self.naver_btn.clicked.connect(self.search_naver)
        self.youtube_btn.clicked.connect(self.search_youtube)
        # self.search_button.clicked.connect(self.Textlistdel)
    
    # 유튜브 검색 버튼
    def search_youtube(self):
        self.search_button.clicked.connect(self.youtube)

    def youtube(self):
        print(self.search_text.text())
        url1 = "https://www.youtube.com/results?search_query=" + self.search_text.text()      
        print(url1)
        self.search_view.load(QUrl(url1))

        
    
    # 네이버 검색 버튼
    def search_naver(self):
        self.search_button.clicked.connect(self.naver)

    def naver(self):
        url1 = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + self.search_text.text()
        print(self.search_text.text())
        self.search_view.load(QUrl(url1))    
        




    # 검색버튼 클릭시 리스트에딧에 있는 검색어 제거 코드
    def Textlistdel(self):
        self.search_text.clear()    
        
    # 검색 클릭시 리스트에딧에 있는 검색어를 리스트항목에 추가해주는 코드
    def showTextlist(self):
        self.text_list.addItem(self.search_text.text())
    

    # 검색 클릭시 리스트에딧에 있는 검색어 검색 코드
    def showTextresult(self):
        url1 = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + self.search_text.text()
        self.search_view.load(QUrl(url1))
             
        





        
        
     
if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    nSearchWin = NaverSerachblog()
    

    nSearchWin.show()

    app.exec_()