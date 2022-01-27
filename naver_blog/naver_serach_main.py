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
        self.setWindowTitle("나만의 네이버 검색기")
        self.search_button.clicked.connect(self.showTextlist)
        self.search_button.clicked.connect(self.showTextresult)
        self.search_button.clicked.connect(self.Textlistdel) 
        self.text_list.itemClicked.connect(self.go_text) # 리스트 항목클릭
    
    
    # 검색버튼 클릭시 리스트에딧에 있는 검색어 제거 코드
    def Textlistdel(self):
        self.naver_search_text.clear()        
    
    
    # 리스트항목 클릭시 클릭한 항목을 검색해주는 코드
    def go_text(self):
        a = self.text_list.currentItem().text()
        url1 = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + a
        self.naver_blog_view.load(QUrl(url1))
        
    # 검색 클릭시 리스트에딧에 있는 검색어를 리스트항목에 추가해주는 코드
    def showTextlist(self):
        self.text_list.addItem(self.naver_search_text.text())
    
    # 검색 클릭시 리스트에딧에 있는 검색어 검색 코드
    def showTextresult(self):
        global url1
        url1 = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + self.naver_search_text.text()
        self.naver_blog_view.load(QUrl(url1))
             
        





        
        
     
if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    nSearchWin = NaverSerachblog()


    nSearchWin.show()

    app.exec_()