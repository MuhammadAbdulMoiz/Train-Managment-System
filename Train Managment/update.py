from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
import pymysql
import random
from PIL import ImageTk, Image

# Enter Table
issueTable = "issued"
bookTable = "books"


def p_detail():
    global cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing

    cnic_var_ = cnic_var.get()
    date_var_ = date_var.get()
    class_var_ = class_var.get()
    departure_var_ = departure_var.get()
    txt_destination_ = txt_destination.get()
    txt_timing_ = txt_timing.get()

    if cnic_var_ == '' or date_var_ == '' or class_var_ == '' or departure_var_ == '' or txt_destination_ == '' or txt_timing_ == '':
        messagebox.showerror("Error!", "Field cannot be empty")

    else:
        cur.execute("select * from passenger_detail where cnic = %s", cnic_var_)
        row = cur.fetchone()
        if row is not None:
            sql = "UPDATE passenger_detail SET CNIC = %s, date = %s, booking_class = %s, departure = %s, destination = %s, timing = %s WHERE CNIC = %s"
            val = (cnic_var_, date_var_, class_var_, departure_var_, txt_destination_, txt_timing_, cnic_var_)
            cur.execute(sql, val)
            con.commit()
            print(cur.rowcount, "Booking updated.")
            cnic_var.set("")
            date_var.set("")
            class_var.set("")
            departure_var.set("")
            txt_destination.set("")
            txt_timing.set("")
            messagebox.showinfo("Info", "Booking,Updated!!!")
        else:
            messagebox.showerror("Error", "No booking to update.")



def update_c():
    global row
    CNIC = cnic_var.get()
    update_sql = "SElECT * FROM passenger_detail WHERE CNIC = %s"
    try:
        cur.execute(update_sql, (CNIC,))
        row = cur.fetchone()
        print(row)
        m_ain()

    except (pymysql.Error, pymysql.Warning):
        messagebox.showerror("Error", "Please check your CNIC")
    cnic_var.set("")


def m_ain():
    global cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing
    # ===Creating Window===
    root = Toplevel()
    root.title("Qasier's Train")
    root.minsize(width=1000, height=800)
    root.maxsize(width=1000, height=800)
    same = True
    n = 0.365

    # declaring string variable
    # for storing name and password
    # ===sign in error===
    cnic_var = StringVar()
    date_var = StringVar()
    class_var = StringVar()
    departure_var = StringVar()
    txt_destination = StringVar()
    txt_timing = StringVar()

    # Adding a background image
    # newImageHeight and newImageWidth contains the adjusted image dimensions.
    background_image = Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)

    # We create the image on the canvas1 using .create_image() method.
    # We use .pack() method to organize widgets in blocks before placing them in the parent widget.
    Canvas1.create_image(400, 400, image=img)
    Canvas1.config(bg="#3e271e", width=newImageSizeWidth, heigh=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    # Showing txt
    headingFrame1 = Frame(root, bg="#094757")
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.65)

    # ====== Sign Up ========
    headingLabel = Label(headingFrame1, text="Welcome to Railway Booking System", bg='#094757', fg='light gray',
                         font=('Bahnschrift SemiBold Condensed', 24))
    headingLabel.place(relx=0.125, y=20)

    CNIC = Label(headingFrame1, text="CNIC", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2,
                                                                                                             y=90)
    txt_cnic = Entry(headingFrame1, textvariable=cnic_var, font=('Calibri', 12)).place(relx=0.2, y=120, width=300)

    Date = Label(headingFrame1, text="Date", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=150)
    txt_date = DateEntry(headingFrame1, textvariable=date_var, selectmode='day').place(relx=0.2, y=180, width=300)

    Booking_Class = Label(headingFrame1, text="Booking Class", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=210)
    txt_class = ttk.Combobox(headingFrame1, textvariable=class_var, width=47)
    txt_class['values'] = ['Select', "Economy", "Business"]
    txt_class.place(relx=0.2, y=240)

    Departure = Label(headingFrame1, text="Departure", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=270)
    txt_departure = ttk.Combobox(headingFrame1, textvariable=departure_var, width=47)
    txt_departure['values'] = ['Select', "Rawalpindi", "Lahore", "Karachi", "Peshawar", "Quetta", "Multan", "Sialkot"]
    txt_departure.place(relx=0.2, y=300)

    Destination = Label(headingFrame1, text="Destination", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=330)
    txt_destination = ttk.Combobox(headingFrame1, textvariable=txt_destination, width=47)
    txt_destination['values'] = ['Select', "Rawalpindi", "Lahore", "Karachi", "Peshawar", "Quetta", "Multan", "Sialkot"]
    txt_destination.place(relx=0.2, y=360)

    Timing = Label(headingFrame1, text="Time ", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=390)
    txt_timing = ttk.Combobox(headingFrame1, textvariable=txt_timing, width=47)
    v1 = ['Select', 'departure time: 10AM \n \t \t \t \t \t \t \t \t destination time: 2PM', 'departure time: 12AM \n \t \t \t \t \t \t \t \t destination time: 4PM', 'departure time: 2PM \n \t \t \t \t \t \t \t \t  destination time: 6PM', 'departure time: 4PM  \n \t \t \t \t \t \t \t \t destination time: 8PM', 'departure time: 6PM \n \t \t \t \t \t \t \t \t destination time: 10PM']
    v2 = ['Select', 'departure time: 10AM \n \t \t \t \t \t \t \t \t destination time: 1PM', 'departure time: 12AM \n \t \t \t \t \t \t \t \t destination time: 3PM', 'departure time: 2PM  \n \t \t \t \t \t \t \t \t destination time: 5PM', 'departure time: 4PM  \n \t \t \t \t \t \t \t \t destination time: 7PM', 'departure time: 6PM \n \t \t \t \t \t \t \t \t destination time: 9PM']
    v3 = ['Select', 'departure time: 10AM \n \t \t \t \t \t \t \t \t destination time: 4PM', 'departure time: 12AM \n \t \t \t \t \t \t \t \t destination time: 6PM', 'departure time: 2PM  \n \t \t \t \t \t \t \t \t destination time: 8PM', 'departure time: 4PM \n \t \t \t \t \t \t \t \t  destination time: 10PM', 'departure time: 6PM \n \t \t \t \t \t \t \t \t destination time: 12AM']
    v4 = ['Select', 'departure time: 10AM \n \t \t \t \t \t \t \t \t destination time: 10PM', 'departure time: 12AM \n \t \t \t \t \t \t \t \t destination time: 12PM', 'departure time: 2PM  \n \t \t \t \t \t \t \t \t destination time: 2AM', 'departure time: 4PM \n \t \t \t \t \t \t \t \t destination time: 4AM', 'departure time: 6PM \n \t \t \t \t \t \t \t \t destination time: 6AM']
    v5 = ['Select', 'departure time: 10AM \n \t \t \t \t \t \t \t \t destination time: 3PM', 'departure time: 12AM \n \t \t \t \t \t \t \t \t destination time: 5PM', 'departure time: 2PM  \n \t \t \t \t \t \t \t \t destination time: 7AM', 'departure time: 4PM \n \t \t \t \t \t \t \t \t destination time: 9AM', 'departure time: 6PM \n \t \t \t \t \t \t \t \t destination time: 11AM']
    v = [v1, v2, v3, v4, v5]
    r = random.choice(v)
    txt_timing['values'] = r
    txt_timing.place(relx=0.2, y=420)

    # === Confirm Button ===
    confirm = Button(headingFrame1,
                     command=p_detail,
                     text="Confirm",
                     bg='dark green',
                     fg='light gray').place(relx=0.2, y=470, width=300)

    # ==== root.mainloop ====
    root.mainloop()


def update():
    global cnic_var, con, cur, root

    root = Toplevel()
    root.title("TMS_Booking Update")
    root.minsize(width=1000, height=800)
    root.geometry("0x0")
    same = True
    n = 0.365

    cnic_var = StringVar()

    my_pass = ""
    my_database = "Qasier's Train"
    # ===Connecting to the MySql server===
    con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
    cur = con.cursor()

    # Adding a background image
    # newImageHeight and newImageWidth contains the adjusted image dimensions.
    background_image = Image.open("lib.jpg")
    [image_size_width, image_size_height] = background_image.size
    new_image_size_width = int(image_size_width*n)
    if same:
        new_image_size_height = int(image_size_height*n)
    else:
        new_image_size_height = int(image_size_height/n)
    background_image = background_image.resize((new_image_size_width, new_image_size_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    canvas1 = Canvas(root)
    canvas1.create_image(400, 400, image=img)
    canvas1.config(bg="#3e271e", width=new_image_size_width, heigh=new_image_size_height)
    canvas1.pack(expand=True, fill=BOTH)

    # ===Heading===
    heading_frame1 = Frame(root, bg='#094757')
    heading_frame1.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    heading_label = Label(heading_frame1, text="Booking Update ", bg='#094757', fg='light gray', font=('Calibri bold', 24))
    heading_label.place(relx=0.3, y=40)

    # ===Book Title===
    lb2 = Label(heading_frame1, text="CNIC : ", bg='#094757', fg='light gray', font=('Calibri bold', 15))
    lb2.place(relx=0.1, rely=0.35, relheight=0.08)

    book_info2 = Entry(heading_frame1, textvariable=cnic_var, font=('Calibri bold', 12))
    book_info2.place(relx=0.25, rely=0.35, relwidth=0.62, relheight=0.08)

    # ===Submit Button===
    submit_btn = Button(root,
                        text="SUBMIT",
                        bg='#094757',
                        fg='light gray',
                        font=('Calibri bold', 12),
                        command=update_c
                        )
    submit_btn.place(
        relx=0.28,
        rely=0.5,
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
        rely=0.5,
        relwidth=0.18,
        relheight=0.08
        )

    root.mainloop()
