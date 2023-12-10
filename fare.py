from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql

my_pass = ""
my_database = "Qasier's Train"

# ===Connecting to the MySql server===
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()


def price():
    dep = dep_info.get()
    des = dest_info.get()

    if (dep == "Rawalpindi" and des == "Lahore") or (des == "Rawalpindi" and dep == "Lahore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "500          800", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Rawalpindi" and des == "Peshawar") or (dep == "Peshawar" and des == "Rawalpindi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "400          700", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Rawalpindi" and des == "Karachi") or (dep == "Karachi" and des == "Rawalpindi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1200          1600", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Rawalpindi" and des == "Quetta") or (dep == "Quetta" and des == "Rawalpindi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Rawalpindi" and des == "Sialkot") or (dep == "Sialkot" and des == "Rawalpindi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "400          700", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Rawalpindi" and des == "Multan") or (dep == "Multan" and des == "Rawalpindi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "700          1100", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Lahore" and des == "Peshawar") or (dep == "Peshawar" and des == "Lahore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Lahore" and des == "Karachi") or (dep == "Karachi" and des == "Lahore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1000          1300", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Lahore" and des == "Quetta") or (dep == "Quetta" and des == "Lahore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Lahore" and des == "Sialkot") or (dep == "Sialkot" and des == "Lahore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "400          600", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Lahore" and des == "Multan") or (dep == "Multan" and des == "Lahore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "400          600", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Peshawar" and des == "Karachi") or (dep == "Karachi" and des == "Peshawar"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1400          1700", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Peshawar" and des == "Quetta") or (dep == "Quetta" and des == "Peshawar"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "900          1200", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Peshawar" and des == "Sialkot") or (dep == "Sialkot" and des == "Peshawar"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "600          900", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Peshawar" and des == "Multan") or (dep == "Multan" and des == "Peshawar"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1000          1300", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Karachi" and des == "Quetta") or (dep == "Quetta" and des == "Karachi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1000          1300", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Karachi" and des == "Sialkot") or (dep == "Sialkot" and des == "Karachi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1100          1400", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Karachi" and des == "Multan") or (dep == "Multan" and des == "Karachi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Quetta" and des == "Sialkot") or (dep == "Sialkot" and des == "Quetta"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Quetta" and des == "Multan") or (dep == "Multan" and des == "Quetta"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "600          900", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Sialkot" and des == "Multan") or (dep == "Multan" and des == "Sialkot"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "700          1000", bg='#094757', fg='light Gray', font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)

def price_c():
    global root, dep_info, dest_info, heading_frame1

    root = Toplevel()
    root.title("Library_Issue Book")
    root.minsize(width=1000, height=800)
    root.geometry("0x0")
    same = True
    n = 0.365

    dep_info = StringVar()
    dest_info = StringVar()

    # Adding a background image
    # newImageHeight and newImageWidth contains the adjusted image dimensions.
    background_image = Image.open("lib.jpg")
    [image_size_width, image_size_height] = background_image.size
    new_image_size_width = int(image_size_width * n)
    if same:
        new_image_size_height = int(image_size_height * n)
    else:
        new_image_size_height = int(image_size_height / n)
    background_image = background_image.resize((new_image_size_width, new_image_size_height), Image.LANCZOS)
    img = ImageTk.PhotoImage(background_image)

    canvas1 = Canvas(root)
    canvas1.create_image(400, 400, image=img)
    canvas1.config(bg="#3e271e", width=new_image_size_width, heigh=new_image_size_height)
    canvas1.pack(expand=True, fill=BOTH)

    # ===Heading===
    heading_frame1 = Frame(root, bg='#094757')
    heading_frame1.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    heading_label = Label(heading_frame1, text="Fare Calculation", bg='#094757', fg='light gray', font=('Calibri bold', 24))
    heading_label.place(relx=0.3, y=35)

    # Departure
    lb1 = Label(heading_frame1, text="Departure : ", bg='#094757', fg='light Gray', font=('Calibri', 14))
    lb1.place(relx=0.1, rely=0.3)
    inf1 = ttk.Combobox(heading_frame1, textvariable=dep_info, width=47)
    inf1['values'] = ['Select', "Rawalpindi", "Lahore", "Karachi", "Peshawar", "Quetta", "Multan", "Sialkot"]
    inf1.place(relx=0.3, rely=0.3, relwidth=0.60)
    inf1.current(0)

    # Destination
    lb2 = Label(heading_frame1, text="Destination : ", bg='#094757', fg='light Gray', font=('Calibri', 14))
    lb2.place(relx=0.1, rely=0.4)
    inf2 = ttk.Combobox(heading_frame1, textvariable=dest_info, width=47)
    inf2['values'] = ['Select', "Rawalpindi", "Lahore", "Karachi", "Peshawar", "Quetta", "Multan", "Sialkot"]
    inf2.place(relx=0.3, rely=0.4, relwidth=0.60)
    inf2.current(0)

    lb3 = Label(heading_frame1, text="Fare", bg='#094757', fg="light gray", font=('Calibri bold', 14)).place(relx=0.1, rely=0.5)

    # ===Issue Button===
    issue_btn = Button(root,
                       text="SUBMIT",
                       bg='#094757',
                       fg='light gray',
                       font=('Calibri bold', 12),
                       command=price
                       )
    issue_btn.place(
        relx=0.28,
        rely=0.53,
        relwidth=0.18,
        relheight=0.08
    )
    # ===Quit Button===
    quit_btn = Button(root,
                      text="Quit",
                      bg='#094757',
                      fg='light gray',
                      font=('Calibri bold', 12),
                      command=root.destroy
                      )
    quit_btn.place(
        relx=0.53,
        rely=0.53,
        relwidth=0.18,
        relheight=0.08
    )

    root.mainloop()
