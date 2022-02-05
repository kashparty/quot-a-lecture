

#
# def __init__(self, master, options):
#     self.__window = Toplevel()
#     self.__window.title("Options")
#     self.__window.geometry("360x480")
#     self.__window.resizable(0, 0)
#     self.__option_widgets = []
#     self.__master = master
#     self.__options = options
#     self.__vars = dict()
#     # Never need to reference or delete
#     Label(self.__window, text="Options", font="TkDefaultFont 14 bold").place(anchor="center", relx=0.5, rely=1 / 16,
#                                                                              relwidth=1 / 4, relheight=1 / 16)
#     Separator(self.__window, orient=HORIZONTAL).place(anchor="center", relx=0.5, rely=7 / 32, relwidth=1,
#                                                       relheight=0)
#     Separator(self.__window, orient=VERTICAL).place(anchor="center", relx=1 / 3, rely=0.5, relwidth=0, relheight=9 / 16)
#     Separator(self.__window, orient=HORIZONTAL).place(anchor="center", relx=0.5, rely=25 / 32, relwidth=1,
#                                                       relheight=0)
#     self.__category = StringVar(self.__window)
#     self.__category.set(self.GENERAL)
#     self.__category_drop_down = OptionMenu(self.__window, self.__category, self.GENERAL, self.MAP_CREATION,
#                                            self.NAV_MESH_GENERATION, self.NAV_GRAPH_EDITING, self.PATHFINDING,
#                                            command=self.__category_change)
#     self.__category_drop_down.configure(font="TkDefaultFont 12")
#     self.__category_drop_down.place(anchor="center", relx=0.5, rely=5 / 32, relwidth=7 / 12, relheight=1 / 16)
#     self.__category_change(None)
#
#     self.__apply_button = Button(self.__window, text="Apply", command=self.__apply, bg="light grey",
#                                  font="TkDefaultFont 12")
#     self.__apply_button.place(anchor="center", relx=41 / 48, rely=57 / 64, relwidth=5 / 24, relheight=5 / 32)
#     self.__cancel_button = Button(self.__window, text="Cancel", command=self.__cancel, bg="light grey",
#                                   font="TkDefaultFont 12")
#     self.__cancel_button.place(anchor="center", relx=7 / 48, rely=57 / 64, relwidth=5 / 24, relheight=5 / 32)
#
#     self.__window.mainloop()