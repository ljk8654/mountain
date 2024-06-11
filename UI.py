from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import textwrap
import map_read
from xmlread import *
import gmail
import spam
import subprocess
import tkinter.ttk

main_mountain = {"이름": '', "산 정보": ''}


class UI:
    def Frame_1(self):
        self.label.append(Label(self.frame[0], text="정보 입력", font=self.TempFont, bg='green'))
        self.label[0].grid(row=0, column=0, sticky='NSEW', columnspan=4)

        self.label.append(Label(self.frame[0], text="산 이름", font=self.TempFont, bg='lightgreen'))
        self.label[1].grid(row=1, column=0, sticky='WN', padx=(5, 0), pady=5)

        self.entry1 = Entry(self.frame[0], width=15, font=self.TempFont)
        self.entry1.grid(row=1, column=1, sticky='WN', pady=5, padx=5)

        self.label.append(Label(self.frame[0], text="지역명", font=self.TempFont, bg='lightgreen'))
        self.label[2].grid(row=2, column=0, sticky='WN', padx=(5, 0), pady=5)

        self.entry2 = Entry(self.frame[0], width=15, font=self.TempFont)
        self.entry2.grid(row=2, column=1, sticky='NW', padx=5, pady=5)

        # 검색 버튼
        self.search = Button(self.frame[0], text='검색', width=5, command=self.search_click)
        self.search.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky='W')

        # + 버튼 추가
        self.add_button = Button(self.frame[0], text='+', command=self.add_mountain)
        self.add_button.grid(row=3, column=1, padx=5, pady=5, sticky='E')

        self.label.append(Label(self.frame[0], text="검색 결과", font=self.TempFont, bg='green'))
        self.label[3].grid(row=4, column=0, sticky='NSEW', columnspan=4)

        self.listbox_frame = Frame(self.frame[0])
        self.listbox_frame.grid(row=5, column=0, columnspan=4, sticky='WE')
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
        self.FOF = Frame(self.frame[2], bg='lightgreen')
        self.FOF.grid(row=1, column=1, sticky='WE')
        self.label_3.append(Label(self.frame[2], text="사진", font=self.TempFont, bg='green'))
        self.label_3[0].grid(row=0, column=0, sticky='NSEW', columnspan=3)
        self.label_3.append(Label(self.frame[2], text="버튼", font=self.TempFont, bg='green'))
        self.label_3[1].grid(row=0, column=1, sticky='NSEW', columnspan=3)

        image1 = Image.open('mountain01.png')
        image1 = image1.resize((300, 200), Image.LANCZOS)
        self.p = ImageTk.PhotoImage(image1)
        self.photo = Label(self.frame[2], image=self.p)
        self.photo.grid(row=1, column=0, padx=(35, 0), pady=(20, 20))
        self.label_3.append(Label(self.frame[2], text="위치", font=self.TempFont, bg='green'))
        self.label_3[2].grid(row=2, column=0, sticky='NSEW', columnspan=3)

        trail_image = Image.open('trail.png')
        trail_image = trail_image.resize((50, 40), Image.LANCZOS)
        self.trail_photo = ImageTk.PhotoImage(trail_image)

        message_image = Image.open('google.png')
        message_image = message_image.resize((50, 40), Image.LANCZOS)
        self.message_photo = ImageTk.PhotoImage(message_image)

        telegram_image = Image.open('telegram.png')
        telegram_image = telegram_image.resize((50, 40), Image.LANCZOS)
        self.telegram_photo = ImageTk.PhotoImage(telegram_image)

        graph_image = Image.open('graph3.png')
        graph_image = graph_image.resize((50, 40), Image.LANCZOS)
        self.graph_photo = ImageTk.PhotoImage(graph_image)

        self.button1 = Button(self.FOF, image=self.trail_photo, command=self.open_trail_window)
        self.button2 = Button(self.FOF, image=self.message_photo, compound="top", command=self.open_email_window)
        self.button3 = Button(self.FOF, image=self.telegram_photo, compound="top",
                              command=self.on_telegram_button_click)
        self.button4 = Button(self.FOF, image=self.graph_photo, compound='top', command=self.show_graph)
        self.button1.grid(row=0, column=1, sticky='N', padx=5, pady=5)
        self.button2.grid(row=1, column=1, sticky='N', padx=5, pady=5)
        self.button3.grid(row=2, column=1, sticky='N', padx=5, pady=5)
        self.button4.grid(row=3, column=1, sticky='N', padx=5, pady=5)

    def __init__(self):
        self.window = Tk()
        self.window.geometry("830x600")
        self.window.title('명산 정보통')
        self.TempFont = font.Font(size=10, weight='bold', family='Consolas')
        self.label = []
        self.label_2 = []
        self.label_3 = []

        self.frame = []
        self.click_data = "?"
        self.mountains = fetch_mountain_data()  # API에서 산 데이터를 가져옴

        colors = ["lightgreen", "lightgreen", "lightgreen"]
        for i in range(3):
            self.frame.append(Frame(self.window, bg=colors[i]))
            self.frame[i].grid(row=0, column=i, sticky='NSEW')
        self.Frame_1()
        self.Frame_2()
        self.Frame_3()
        self.photo2 = Label(self.frame[2], bg='lightgreen')
        self.photo2.grid(row=3, column=0, padx=(30, 0), pady=(0, 20))
        self.window.mainloop()

    def search_click(self):
        self.ListBox.delete(0, END)
        search_name = self.entry1.get()
        search_area = self.entry2.get()
        if search_name:
            for mountain in self.mountains:
                if search_name.lower() in mountain["Name"].lower():
                    self.ListBox.insert(END, mountain["Name"])
                    # 산 정보를 저장
                    spam.save_info(mountain["Name"], mountain["Location"], int(float(mountain["Height"])))
        elif search_area:
            for mountain in self.mountains:
                if search_area.lower() in mountain["Location"].lower():
                    self.ListBox.insert(END, mountain["Name"])
                    # 산 정보를 저장
                    spam.save_info(mountain["Name"], mountain["Location"], int(float(mountain["Height"])))
        else:
            for mountain in self.mountains:
                self.ListBox.insert(END, mountain["Name"])
                # 산 정보를 저장
                spam.save_info(mountain["Name"], mountain["Location"], int(float(mountain["Height"])))
        self.ListBox.bind("<<ListboxSelect>>", self.select_mountain)

    def search_click(self):
        self.ListBox.delete(0, END)
        search_name = self.entry1.get()
        search_area = self.entry2.get()
        if search_name:
            for mountain in self.mountains:
                if search_name.lower() in mountain["Name"].lower():
                    self.ListBox.insert(END, mountain["Name"])
        elif search_area:
            for mountain in self.mountains:
                if search_area.lower() in mountain["Location"].lower():
                    self.ListBox.insert(END, mountain["Name"])
        else:
            for mountain in self.mountains:
                self.ListBox.insert(END, mountain["Name"])
        self.ListBox.bind("<<ListboxSelect>>", self.select_mountain)

    def open_trail_window(self):

        self.saved_mountains = spam.get_saved_info()
        selected_index = self.ListBox.curselection()
        self.save_mountain_name = self.ListBox.get(selected_index)

        trail_window = Toplevel(self.window, bg='lightgreen')
        trail_window.geometry("440x600")
        trail_window.title("등산로 정보")
        Save_Frame_LEFT = Frame(trail_window, bg='lightgreen')
        Save_Frame_LEFT.grid(row=0, column=0, sticky='NSEW')
        Save_Frame_RIGHT = Frame(trail_window, bg='lightgreen')
        Save_Frame_RIGHT.grid(row=0, column=1, sticky='NSEW')
        Save_Moutain_Name = Label(Save_Frame_LEFT, text="저장된 산", font=self.TempFont, bg='green')
        Save_Moutain_Name.grid(row=0, column=0, padx=(10, 10), sticky="nsew", columnspan=1)

        self.Save_ListBox = Listbox(Save_Frame_LEFT, height=30, width=20)
        self.Save_ListBox.grid(row=1, column=0, padx=10, sticky="nw")
        for mountain in self.saved_mountains:
            self.Save_ListBox.insert(END, f"{mountain['name']}")

        save_mountain_label = Label(Save_Frame_RIGHT, text='산 이름', font=self.TempFont, bg='green')
        save_mountain_label.grid(row=0, column=0, padx=10, sticky="nsew", columnspan=1)

        self.save_mountain_label_info = Label(Save_Frame_RIGHT, text=self.save_mountain_name, font=self.TempFont,
                                              bg='lightgreen')
        self.save_mountain_label_info.grid(row=1, column=0, sticky="nsew", columnspan=1)

        notebook = tkinter.ttk.Notebook(Save_Frame_RIGHT)
        notebook.grid(row=2, column=0, sticky='NSEW', columnspan=1)

        trail_frame = Frame(notebook, bg='lightgreen')
        map_frame = Frame(notebook, bg='lightgreen')

        notebook.add(trail_frame, text='등산로')
        notebook.add(map_frame, text='문화자원')

        wrapped_text = "\n".join(textwrap.wrap(self.trail, 20))
        self.trail_label = Label(trail_frame, text=wrapped_text, font=self.TempFont, bg='lightgreen')
        self.trail_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew", columnspan=1)

        self.POI_label = Label(map_frame, text="\n".join(textwrap.wrap(fetch_POI(self.save_mountain_name), 18)),
                               font=self.TempFont, bg='lightgreen')
        self.POI_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew", columnspan=1)

        trail_info_label = Label(Save_Frame_RIGHT, text='등산로 설명', font=self.TempFont, bg='lightgreen')
        trail_info_label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", columnspan=1)

        info_frame = Frame(Save_Frame_RIGHT, bg='lightgreen')
        info_frame.grid(row=5, column=0, sticky='NSEW', columnspan=3)

        wrapped_text = "\n".join(textwrap.wrap(self.trail_detail, 16))
        self.trail_info = Text(info_frame, font=self.TempFont, wrap=WORD, height=10, width=30, bg='lightgreen')
        self.trail_info.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        save_scrollbar = Scrollbar(info_frame, orient=VERTICAL, command=self.trail_info.yview, bg='lightgreen')
        self.trail_info.config(yscrollcommand=save_scrollbar.set)
        save_scrollbar.grid(row=0, column=1, sticky='NS')
        self.trail_info.insert(END, wrapped_text)

        self.Save_ListBox.bind("<<ListboxSelect>>", self.save_mountain_select)

    def save_mountain_select(self, event):
        selected_index = self.Save_ListBox.curselection()
        selected_mountain_name = self.Save_ListBox.get(selected_index)
        self.save_mountain_name = self.Save_ListBox.get(selected_index)
        self.trail, self.trail_detail = fetch_trail_information(selected_mountain_name)
        wrapped_text = "\n".join(textwrap.wrap(self.trail, 16))
        self.trail_label.config(text=wrapped_text)
        wrapped_text = "\n".join(textwrap.wrap(fetch_POI(self.save_mountain_name), 18))
        self.POI_label.config(text=wrapped_text)
        self.trail_info.config(state=NORMAL)
        self.trail_info.delete(1.0, END)
        wrapped_description = "\n".join(textwrap.wrap(self.trail_detail, 18))
        self.trail_info.insert(END, wrapped_description)
        self.trail_info.config(state=DISABLED)
        self.save_mountain_label_info.config(text=self.save_mountain_name)

    def send_mail(self, email, window, saved_mountains):
        if email:
            mountain_info = ""
            for mountain in saved_mountains:
                mountain_info += (
                    f"<strong>산 이름:</strong> {mountain['name']}<br>"
                    f"<strong>주소:</strong> {mountain['location']}<br>"
                    f"<strong>해발고도:</strong> {mountain['height']} m<br>"
                    f"<strong>산 정보:</strong> {fetch_mountain_information(mountain['name'])}<br><br>"
                )

            # 이메일 보내기
            gmail.sendMain(
                "저장된 산 정보",
                mountain_info,
                email
            )
            messagebox.showinfo('저장된 산 정보', '저장된 산 정보를 ' + email + '로 보냈습니다!')
            window.destroy()
        else:
            messagebox.showerror('오류', '이메일 주소를 입력하세요!')

    def show_graph(self):
        graph_window = Toplevel(self.window)
        graph_window.geometry("400x300")
        graph_window.title("산 높이 그래프")
        canvas = Canvas(graph_window, width=400, height=300)
        canvas.pack()
        bar_width = 20
        x_gap = 10
        x0 = 30
        y0 = 200
        m_l = {1: "300~400", 2: "400~500", 3: "500~600", 4: "600~700", 5: "700~800", 6: "800~900", 7: "900~1000",
               8: "1000~1100", 9: "1100~1200", 10: "1200~1300", 11: "1300초과"}
        h_l = [0] * 11
        for mountain in self.mountains:
            if 300 < float(mountain['Height']) <= 400:
                h_l[0] += 1
            elif 400 < float(mountain['Height']) <= 500:
                h_l[1] += 1
            elif 500 < float(mountain['Height']) <= 600:
                h_l[2] += 1
            elif 600 < float(mountain['Height']) <= 700:
                h_l[3] += 1
            elif 700 < float(mountain['Height']) <= 800:
                h_l[4] += 1
            elif 800 < float(mountain['Height']) <= 900:
                h_l[5] += 1
            elif 900 < float(mountain['Height']) <= 1000:
                h_l[6] += 1
            elif 1000 < float(mountain['Height']) <= 1100:
                h_l[7] += 1
            elif 1100 < float(mountain['Height']) <= 1200:
                h_l[8] += 1
            elif 1200 < float(mountain['Height']) <= 1300:
                h_l[9] += 1
            else:
                h_l[10] += 1

        for i in range(len(h_l)):
            x1 = x0 + i * (bar_width + x_gap)
            y1 = y0 - 100 * h_l[i] / max(h_l)
            canvas.create_rectangle(x1, y1, x1 + bar_width, y0, fill='blue')
            canvas.create_text(x1 + bar_width / 2, y0 + 50, text=m_l[i + 1], anchor='n', angle=90)
            canvas.create_text(x1 + bar_width / 2, y1 - 10, text=h_l[i], anchor='s')

    def open_email_window(self):
        email_window = Toplevel(self.window)
        email_window.geometry("300x200")
        email_window.title("이메일 입력")
        Label(email_window, text="이메일 주소를 입력하세요:", font=self.TempFont).pack(pady=20)
        self.email_entry = Entry(email_window, width=25, font=self.TempFont)
        self.email_entry.pack(pady=10)
        send_button = Button(email_window, text="보내기",
                             command=lambda: self.send_mail(self.email_entry.get(), email_window,
                                                            spam.get_saved_info()))
        send_button.pack(pady=10)

    def show_saved_mountains(self):
        saved_mountains = spam.get_saved_info()
        saved_window = Toplevel(self.window)
        saved_window.title("저장된 산 정보")
        saved_window.geometry("400x300")

        listbox = Listbox(saved_window, width=50, height=15)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(saved_window, orient=VERTICAL, command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        for mountain in saved_mountains:
            mountain_info = f"이름: {mountain['name']}, 위치: {mountain['location']}, 높이: {mountain['height']} m"
            listbox.insert(END, mountain_info)

    def add_mountain(self):
        selected_index = self.ListBox.curselection()
        if selected_index:
            selected_mountain_name = self.ListBox.get(selected_index)
            selected_mountain = next(
                (mountain for mountain in self.mountains if mountain["Name"] == selected_mountain_name), None)

            if selected_mountain:
                # 산 정보를 저장
                spam.save_info(selected_mountain["Name"], selected_mountain["Location"],
                               int(float(selected_mountain["Height"])))
                messagebox.showinfo("저장 완료", f"{selected_mountain['Name']} 정보가 저장되었습니다!")
        else:
            messagebox.showwarning("선택 오류", "저장할 산을 선택하세요.")

    def select_mountain(self, event):
        selected_index = self.ListBox.curselection()
        if selected_index:
            selected_mountain_name = self.ListBox.get(selected_index)
            self.trail, self.trail_detail = fetch_trail_information(selected_mountain_name)
            selected_mountain = next(
                (mountain for mountain in self.mountains if mountain["Name"] == selected_mountain_name), None)
            if selected_mountain:
                self.label_2[1].config(text=selected_mountain["Name"])
                self.label_2[3].config(text=selected_mountain["Location"])
                self.label_2[5].config(text=f"{selected_mountain['Height']} M")
                self.info_text.config(state=NORMAL)
                self.info_text.delete(1.0, END)
                wrapped_description = "\n".join(textwrap.wrap(fetch_mountain_information(selected_mountain_name), 18))
                self.info_text.insert(END, wrapped_description)
                self.info_text.config(state=DISABLED)
                image1 = fetch_mountain_picture(selected_mountain_name)
                if image1:
                    image1 = image1.resize((300, 200), Image.LANCZOS)
                    self.p = ImageTk.PhotoImage(image1)
                    self.photo.config(image=self.p)
                else:
                    image1 = Image.open('mountain01.png')
                    image1 = image1.resize((300, 200), Image.LANCZOS)
                    self.p = ImageTk.PhotoImage(image1)
                    self.photo.config(image=self.p)
                image2 = map_read.update_map(selected_mountain)
                if image2:
                    image2 = image2.resize((300, 300), Image.LANCZOS)
                    self.p2 = ImageTk.PhotoImage(image2)
                    self.photo2.config(image=self.p2)
        else:
            for label in self.label_2[1:]:
                if self.label_2.index(label) % 2 == 1:
                    label.config(text="결과 없음")

    def on_telegram_button_click(self):
        try:
            # noti.py와 teller.py 스크립트 실행
            subprocess.Popen(['python', 'noti.py'])
            subprocess.Popen(['python', 'teller.py'])
            messagebox.showinfo('텔레그램', '텔레그램 챗봇과 연결되었습니다.')
        except Exception as e:
            messagebox.showerror('오류', f'텔레그램 챗봇 연결에 실패했습니다: {e}')


UI()