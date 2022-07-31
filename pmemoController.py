import imp
from tkinter import *
import os
from tkinter.filedialog import *
from Pmemo4 import *

top = Tk()
es = ""


# 새파일
def newFile():
    top.title("제목없음- 메모장")
    file = None 
    ta.delete(1.0,END)

# 파일열기
def openFile():
    file = askopenfilename(title = "파일 선택", filetypes = (("텍스트 파일", "*.txt"),("모든 파일", "*.*")))
    top.title(os.path.basename(file) + " - 메모장")
    ta.delete(1.0, END)
    f = open(file,"r")
    ta.insert(1.0,f.read())
    f.close()

# 저장
def saveFile():
    f = asksaveasfile(mode = "w", defaultextension=".txt")
    if f is None:
        return
    ts = str(ta.get(1.0, END))
    f.write(ts)
    f.close()
    
# 잘라내기
def cut():
    global es
    es = ta.get(SEL_FIRST, SEL_LAST)
    ta.delete(SEL_FIRST, SEL_LAST)

# 복사
def copy():
    global es
    es = ta.get(SEL_FIRST, SEL_LAST)

def paste():
    global es
    ta.insert(INSERT, es)

def delete():
    ta.delete(SEL_FIRST, SEL_LAST)

def help():
    he = Toplevel(top)
    he.geometry("200x200")
    he.title("정보")
    lb = Label(he, text = "메모장 버전 1.0\n 파이썬으로 만든 메모장입니다^^")
    lb.pack()