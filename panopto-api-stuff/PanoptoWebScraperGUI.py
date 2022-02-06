from tkinter import Tk, Button, Label, Entry, StringVar
from PanoptoWebScraper import main
from PIL import Image, ImageTk
from threading import Thread


class UI:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("GUI")
        self.__window.geometry("1280x720")
        self.__window.resizable(0, 0)
        self.__bgCol = "#FFFBF8"
        self.__fgCol = "#FFCC86"
        self.__altCol = "#FF9D2D"
        self.__window.configure(bg=self.__bgCol)
        self.__widgets = []
        self.__fonts = [
            ("Bree Serif", 30, "bold", "underline"),
            ("Bree Serif", 30, "bold"),
            ("Bree Serif", 30),
            ("Bree Serif", 20),
        ]
        self.__domain = StringVar(self.__window, "imperial.cloud.panopto.eu")
        self.__username = StringVar(self.__window, "username")
        self.__password = StringVar(self.__window, "password")
        img = Image.open("PiracyNotice.png")
        img.putalpha(50)
        img = img.resize((1280, 720), Image.BICUBIC)
        self.__piracyNotice = ImageTk.PhotoImage(img)
<<<<<<< HEAD
        self.__place_widget(Label(self.__window, image=self.__piracyNotice, bg=self.__bgCol),
                            1280, 720, 0, 0)
        self.__place_widget(Label(self.__window, text="Part of the Quot-a-Lecture software suite", font=self.__fonts[3],
                                  bg=self.__bgCol),
                            520, 50, 150, 670)
        self.__img = ImageTk.PhotoImage(Image.open("quotalecture.png").resize((150, 150), Image.BICUBIC))
        self.__place_widget(Label(self.__window, image=self.__img, bg=self.__bgCol),
                            150, 150, 0, 570)
        self.__place_widget(Label(self.__window, text="Auto Transcript Extractor", font=self.__fonts[0],
                                  bg=self.__bgCol),
                            500, 60, 400, 0)
        self.__place_widget(Label(self.__window, text="Domain: ", font=self.__fonts[2],
                                  bg=self.__bgCol),
                            160, 60, 45, 110)
        self.__place_widget(Label(self.__window, text="Username: ", font=self.__fonts[2],
                                  bg=self.__bgCol),
                            200, 60, 25, 340)
        self.__place_widget(Label(self.__window, text="Password: ", font=self.__fonts[2],
                                  bg=self.__bgCol),
                            200, 60, 25, 500)
        self.__place_widget(Entry(self.__window, textvariable=self.__domain, font=self.__fonts[2], bg=self.__fgCol),
                            500, 60, 250, 110)
        self.__place_widget(Entry(self.__window, textvariable=self.__username, font=self.__fonts[2], bg=self.__fgCol),
                            500, 60, 250, 340)
        self.__place_widget(Entry(self.__window, textvariable=self.__password, show="*", font=self.__fonts[2],
                                  bg=self.__fgCol),
                            500, 60, 250, 500)
        self.__place_widget(Button(self.__window, text="GO!", font=self.__fonts[1], command=self.__run,
                                   bg=self.__altCol),
                            200, 200, 900, 280)
=======
        self.__place_widget(
            Label(self.__window, image=self.__piracyNotice, bg=self.__bgCol),
            1280,
            720,
            0,
            0,
        )
        self.__place_widget(
            Label(
                self.__window,
                text="Part of the QuotaLecture software suite",
                font=self.__fonts[3],
                bg=self.__bgCol,
            ),
            470,
            50,
            150,
            670,
        )
        self.__img = ImageTk.PhotoImage(
            Image.open("QuotaLecture.png").resize((150, 150), Image.BICUBIC)
        )
        self.__place_widget(
            Label(self.__window, image=self.__img, bg=self.__bgCol), 150, 150, 0, 570
        )
        self.__place_widget(
            Label(
                self.__window,
                text="Auto Transcript Extractor",
                font=self.__fonts[0],
                bg=self.__bgCol,
            ),
            500,
            60,
            400,
            0,
        )
        self.__place_widget(
            Label(
                self.__window, text="Domain: ", font=self.__fonts[2], bg=self.__bgCol
            ),
            160,
            60,
            45,
            110,
        )
        self.__place_widget(
            Label(
                self.__window, text="Username: ", font=self.__fonts[2], bg=self.__bgCol
            ),
            200,
            60,
            25,
            340,
        )
        self.__place_widget(
            Label(
                self.__window, text="Password: ", font=self.__fonts[2], bg=self.__bgCol
            ),
            200,
            60,
            25,
            500,
        )
        self.__place_widget(
            Entry(
                self.__window,
                textvariable=self.__domain,
                font=self.__fonts[2],
                bg=self.__fgCol,
            ),
            500,
            60,
            250,
            110,
        )
        self.__place_widget(
            Entry(
                self.__window,
                textvariable=self.__username,
                font=self.__fonts[2],
                bg=self.__fgCol,
            ),
            500,
            60,
            250,
            340,
        )
        self.__place_widget(
            Entry(
                self.__window,
                textvariable=self.__password,
                show="*",
                font=self.__fonts[2],
                bg=self.__fgCol,
            ),
            500,
            60,
            250,
            500,
        )
        self.__place_widget(
            Button(
                self.__window,
                text="GO!",
                font=self.__fonts[1],
                command=self.__run,
                bg=self.__altCol,
            ),
            200,
            200,
            900,
            280,
        )
>>>>>>> fe-polish
        self.__window.mainloop()

    def __place_widget(self, widget, width, height, x, y, anchor="nw"):
        self.__widgets.append(widget)
        widget.place(anchor=anchor, x=x, y=y, width=width, height=height)

    def __run(self):
        Thread(
            target=main,
            args=(
                self.__domain.get(),
                self.__username.get(),
                self.__password.get(),
                False,
            ),
        ).start()


UI()
