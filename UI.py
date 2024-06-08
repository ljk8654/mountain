from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import textwrap
import map_read
from xmlread import *
import gmail
import spam

main_mountain = {"이름":'', "산 정보" : ''}
class UI:
    def Frame_1(self):
        self.label.append(Label(self.frame[0], text="정보 입력", font=self.TempFont, bg='green'))
        self.label[0].grid(row=0, column=0, sticky='NSEW', columnspan=3)

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
        self.show_saved_button = Button(self.frame[0], text='저장된 산 정보 보기', width= 7, command=self.show_saved_mountains)
        self.show_saved_button.grid(row=3, column=2, columnspan=2, padx=5, pady=5)


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
        self.button3 = Button(self.FOF, image=self.telegram_photo, compound="top")
        self.button4 = Button(self.FOF, image=self.graph_photo,compound='top',command=self.show_graph)
        self.button1.grid(row=0, column=1, sticky='N', padx=5, pady=5)
        self.button2.grid(row=1, column=1, sticky='N', padx=5, pady=5)
        self.button3.grid(row=2, column=1, sticky='N', padx=5, pady=5)
        self.button4.grid(row=3, column=1, sticky='N', padx=5, pady=5)

    def __init__(self):
        self.window = Tk()
        self.window.geometry("830x600")
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

    def select_mountain(self, a):
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
                # 산 정보를 저장
                spam.save_info(selected_mountain["Name"], selected_mountain["Location"],
                               int(float(selected_mountain["Height"])))
        else:
            for label in self.label_2[1:]:
                if self.label_2.index(label) % 2 == 1:
                    label.config(text="결과 없음")

    def open_trail_window(self):
        trail_window = Toplevel(self.window)
        trail_window.geometry("800x300")
        trail_window.title("등산로 정보")
        Label(trail_window, text="\n".join(textwrap.wrap(self.trail, 16)), font=self.TempFont).pack(pady=20)
        trail_info = Text(trail_window, font=self.TempFont, wrap=WORD, height=10, width=40, bg='lightgreen')
        trail_info.pack(pady=20)
        trail_info.insert(END, self.trail_detail)  # Add actual trail information retrieval here

    def send_mail(self, email, window):
        if email:
            gmail.sendMain(
                main_mountain['이름'],
                main_mountain['산 정보'],
                email,
                self.label_2[3].cget("text"),  # 지역명
                self.label_2[5].cget("text").split()[0]  # 해발고도 (숫자만 추출)
            )
            messagebox.showinfo(main_mountain['이름'] + ' 정보', main_mountain['이름'] + ' 정보를 ' + email + '로 보냈습니다!')
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
        m_l = {1:"300~400",2:"400~500",3:"500~600",4:"600~700",5:"700~800",6:"800~900",7:"900~1000",8:"1000~1100",9:"1100~1200",10:"1200~1300",11:"1300초과"}
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
                h_l[4]+= 1
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
            y1 = y0 - 100 * h_l[i]/ max(h_l)
            canvas.create_rectangle(x1, y1, x1 + bar_width, y0, fill='blue')
            canvas.create_text(x1 + bar_width / 2, y0 + 50, text=m_l[i+1], anchor='n', angle=90)
            canvas.create_text(x1 + bar_width / 2, y1 - 10, text=h_l[i], anchor='s')

    def open_email_window(self):
        email_window = Toplevel(self.window)
        email_window.geometry("300x200")
        email_window.title("이메일 입력")
        Label(email_window, text="이메일 주소를 입력하세요:", font=self.TempFont).pack(pady=20)
        self.email_entry = Entry(email_window, width=25, font=self.TempFont)
        self.email_entry.pack(pady=10)
        send_button = Button(email_window, text="보내기",
                             command=lambda: self.send_mail(self.email_entry.get(), email_window))
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


UI()