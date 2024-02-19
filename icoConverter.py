from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

win = tk.Tk()
win.geometry("500x40")
win.title("ICO Converter")

def file_select():
    global files
    files = filedialog.askopenfilenames(initialdir='', title='파일을 선택해주세요.')
    # 이미지 파일이 아닐 경우 에러 메세지 추가
    lbl_system.config(text="\t [System] 변환 버튼을 눌러주세요.")
    btn_file_select.config(bg='#32CD32') ##32CD32 #DAA520
        
def convert2ico():
    icon = Image.open(files[0])
    icon.save(path_filename, format='ICO')
    lbl_system.config(text="\t [System] 변환이 완료되었습니다!")
    btn_convert2ico.config(bg='#32CD32')

btn_file_select = tk.Button(win, text="파일 선택", command=file_select,
                           bg='#567', fg='White', font=('times 9 bold'),
                           relief='raised', width=12, height=5)
btn_file_select.pack(side='left')

btn_convert2ico = tk.Button(win, text="변환", command=convert2ico,
                           bg='#567', fg='White', font=('times 9 bold'),
                           relief='raised', width=12, height=5)
btn_convert2ico.pack(side='left')

lbl_system = tk.Label(win, text='\t [System] 변환할 파일을 선택해주세요.', font=('times 9 bold'))
lbl_system.pack(side='left')

path = os.getcwd()
path_filename = path+"\\icon.ico"

win.mainloop()
