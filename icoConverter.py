from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class IcoConverter:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x60")
        self.master.title("ICO 변환기")
        
        self.files = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.btn_file_select = tk.Button(self.master, text="파일 선택", command=self.file_select,
                                         bg='#4CAF50', fg='White', font=('Arial', 10, 'bold'),
                                         relief='raised', width=12, height=2)
        self.btn_file_select.pack(side='left', padx=10, pady=10)

        self.btn_convert2ico = tk.Button(self.master, text="변환", command=self.convert2ico,
                                         bg='#2196F3', fg='White', font=('Arial', 10, 'bold'),
                                         relief='raised', width=12, height=2, state=tk.DISABLED)
        self.btn_convert2ico.pack(side='left', padx=10, pady=10)

        self.lbl_system = tk.Label(self.master, text='[System] 변환할 파일을 선택해주세요.', font=('Arial', 10))
        self.lbl_system.pack(side='left', padx=10)

    def file_select(self):
        self.files = filedialog.askopenfilenames(initialdir='', title='파일을 선택해주세요.', 
                                                 filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if self.files:
            self.lbl_system.config(text="[System] 변환 버튼을 눌러주세요.")
            self.btn_file_select.config(bg='#32CD32')
            self.btn_convert2ico.config(state=tk.NORMAL)

    def convert2ico(self):
        if not self.files:
            messagebox.showerror("오류", "먼저 파일을 선택해주세요.")
            return
        
        for i, file in enumerate(self.files):
            icon = Image.open(file)
            filename = f"icon_{i+1}.ico"
            icon.save(filename, format='ICO')
        
        self.lbl_system.config(text="[System] 변환이 완료되었습니다!")
        self.btn_convert2ico.config(bg='#32CD32')
        messagebox.showinfo("완료", f"{len(self.files)}개의 파일이 성공적으로 변환되었습니다.")
        self.btn_convert2ico.config(state=tk.DISABLED)
        self.btn_convert2ico.config(bg='#2196F3')

def main():
    root = tk.Tk()
    app = IcoConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()