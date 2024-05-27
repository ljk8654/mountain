from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import textwrap
import xmlread


class UI:
    def Frame_1(self):
        self.label.append(Label(self.frame[0], text="정보 입력", font=self.TempFont, bg='green'))
        self.label[0].grid(row=0, column=0, sticky='NSEW', columnspan=3)

        # Label과 Entry를 좌우로 붙여서 배치
        self.label.append(Label(self.frame[0], text="산 이름", font=self.TempFont))
        self.label[1].grid(row=1, column=0, sticky='WN', padx=(5, 0), pady=5)

        self.entry1 = Entry(self.frame[0], width=15, font=self.TempFont)
        self.entry1.grid(row=1, column=1, sticky='WN', pady=5, padx=5)

        self.label.append(Label(self.frame[0], text="지역명", font=self.TempFont))
        self.label[2].grid(row=2, column=0, sticky='WN', padx=(5, 0), pady=5)

        self.entry2 = Entry(self.frame[0], width=15, font=self.TempFont)
        self.entry2.grid(row=2, column=1, sticky='NW', padx=5, pady=5)

        self.search = Button(self.frame[0], text='검색', width=7, command=self.search_click)
        self.search.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.label.append(Label(self.frame[0], text="검색 결과", font=self.TempFont, bg='green'))
        self.label[3].grid(row=4, column=0, sticky='NSEW', columnspan=3)

        self.listbox_frame = Frame(self.frame[0])
        self.listbox_frame.grid(row=5, column=0, columnspan=3, sticky='WE')
        self.ListBox = Listbox(self.listbox_frame, height=30, width=20)
        self.scrollbar = Scrollbar(self.listbox_frame, orient=VERTICAL, command=self.ListBox.yview)
        self.ListBox.config(yscrollcommand=self.scrollbar.set)
        self.ListBox.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def Frame_2(self):
        self.label_2.append(Label(self.frame[1], text="산 이름", font=self.TempFont, bg='green'))
        self.label_2[0].grid(row=0, column=0, sticky='NSEW', columnspan=3)
        self.label_2.append(Label(self.frame[1], text="결과 없음", font=self.TempFont, bg='lightgreen'))
        self.label_2[1].grid(row=1, column=0, sticky='NSEW', columnspan=3)
        self.label_2.append(Label(self.frame[1], text="주소", font=self.TempFont, bg='green'))
        self.label_2[2].grid(row=2, column=0, sticky='NSEW', columnspan=3)
        self.label_2.append(Label(self.frame[1], text="결과 없음", font=self.TempFont, bg='lightgreen'))
        self.label_2[3].grid(row=3, column=0, sticky='NSEW', columnspan=3)
        self.label_2.append(Label(self.frame[1], text="해발고도", font=self.TempFont, bg='green'))
        self.label_2[4].grid(row=4, column=0, sticky='NSEW', columnspan=3)
        self.label_2.append(Label(self.frame[1], text="결과 없음", font=self.TempFont, bg='lightgreen'))
        self.label_2[5].grid(row=5, column=0, sticky='NSEW', columnspan=3)
        self.label_2.append(Label(self.frame[1], text="정보", font=self.TempFont, bg='green'))
        self.label_2[6].grid(row=6, column=0, sticky='NSEW', columnspan=3)
        self.info_frame = Frame(self.frame[1])
        self.info_frame.grid(row=7, column=0, sticky='NSEW', columnspan=3)

        self.info_text = Text(self.info_frame, font=self.TempFont, wrap=WORD, height=30, width=32, bg='lightgreen')
        self.info_text.grid(row=0, column=0, sticky='NSEW')

        self.scrollbar_2 = Scrollbar(self.info_frame, orient=VERTICAL, command=self.info_text.yview)
        self.info_text.config(yscrollcommand=self.scrollbar_2.set)
        self.scrollbar_2.grid(row=0, column=1, sticky='NS')

        self.info_text.config(state=DISABLED)

    def Frame_3(self):
        self.FOF = Frame(self.frame[2],bg='lightgreen')
        self.FOF.grid(row=1,column=1,sticky='WE')
        self.label_3.append(Label(self.frame[2], text="사진", font=self.TempFont, bg='green'))
        self.label_3[0].grid(row=0, column=0, sticky='NSEW', columnspan=3)
        self.label_3.append(Label(self.frame[2], text="버튼", font=self.TempFont, bg='green'))
        self.label_3[1].grid(row=0, column=1, sticky='NSEW', columnspan=3)

        image1 = Image.open('b1fv.png')
        image1 = image1.resize((300, 200), Image.LANCZOS)
        self.p = ImageTk.PhotoImage(image1)
        self.photo = Label(self.frame[2], image=self.p)
        self.photo.grid(row=1, column=0,padx=(35,0),pady=(20,20))
        self.label_3.append(Label(self.frame[2], text="위치", font=self.TempFont, bg='green'))
        self.label_3[2].grid(row=2, column=0, sticky='NSEW', columnspan=3)

        # 오른쪽에 위치할 버튼들
        self.button1 = Button(self.FOF, text='???')
        self.button2 = Button(self.FOF, text='???')
        self.button3 = Button(self.FOF, text='???')
        self.button1.grid(row=0, column=1, sticky='N', padx=5, pady=5)
        self.button2.grid(row=1, column=1, sticky='N', padx=5, pady=5)
        self.button3.grid(row=2, column=1, sticky='N', padx=5, pady=5)

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")
        self.TempFont = font.Font(size=10, weight='bold', family='Consolas')
        self.label = []
        self.label_2 = []
        self.label_3 = []

        self.frame = []
        self.click_data="?"
        # 예제 데이터
        self.mountains = []
        for mountain in xmlread.mountain_data:
            self.mountains.append(mountain)
        colors = ["lightgreen", "lightgreen", "lightgreen"]
        for i in range(3):
            self.frame.append(Frame(self.window, bg=colors[i]))
            self.frame[i].grid(row=0, column=i, sticky='NSEW')  # 세로로 3분할

        self.Frame_1()
        self.Frame_2()
        self.Frame_3()

        self.window.mainloop()

    def search_click(self):
        # 리스트 박스 초기화
        self.ListBox.delete(0, END)

        # 사용자가 입력한 검색어
        search_name = self.entry1.get()

        # 산 이름이 사용자 입력과 일치하는 산을 리스트 박스에 추가
        for mountain in self.mountains:
            if search_name.lower() in mountain["Name"].lower():
                self.ListBox.insert(END, mountain["Name"])

        # 리스트 박스 클릭 이벤트 처리 함수를 설정
        self.ListBox.bind("<<ListboxSelect>>", self.select_mountain)
    def select_mountain(self,a):
        selected_index = self.ListBox.curselection()

        if selected_index:
            selected_mountain_name = self.ListBox.get(selected_index)

            selected_mountain = next((mountain for mountain in self.mountains if mountain["Name"] == selected_mountain_name), None)
            if selected_mountain:
                self.label_2[1].config(text=selected_mountain["Name"])
                self.label_2[3].config(text=selected_mountain["Location"])
                self.label_2[5].config(text=f"{selected_mountain['Height']} M")
                self.info_text.config(state=NORMAL)
                self.info_text.delete(1.0, END)
                wrapped_description = "\n".join(textwrap.wrap(xmlread.mountain_information(selected_mountain_name), 18))
                self.info_text.insert(END, wrapped_description)
                self.info_text.config(state=DISABLED)
        else:
            for label in self.label_2[1:]:
                if self.label_2.index(label) % 2 == 1:
                    label.config(text="결과 없음")

UI()