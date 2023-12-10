from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
import pymysql
import random
from PIL import ImageTk, Image

my_pass = ""
my_database = "Qasier's Train"

# ===Connecting to the MySql server===
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()


def passenger_details():
    global name_var, age_var, cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing

    name_var_ = name_var.get()
    age_var_ = age_var.get()
    cnic_var_ = cnic_var.get()
    date_var_ = date_var.get()
    class_var_ = class_var.get()
    departure_var_ = departure_var.get()
    txt_destination_ = txt_destination.get()
    txt_timing_ = txt_timing.get()
    fair = 0
    if (departure_var_ == "Rawalpindi" and txt_destination_ == "Lahore") or (txt_destination_ == "Rawalpindi" and departure_var_ == "Lahore"):
        if class_var_ == "Economy":
            fair += 500
        elif class_var_ == "Business":
            fair += 800
    elif (departure_var_ == "Rawalpindi" and txt_destination_ == "Peshawar") or (departure_var_ == "Peshawar" and txt_destination_ == "Rawalpindi"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 700
    elif (departure_var_ == "Rawalpindi" and txt_destination_ == "Karachi") or (departure_var_ == "Karachi" and txt_destination_ == "Rawalpindi"):
        if class_var_ == "Economy":
            fair += 1200
        elif class_var_ == "Business":
            fair += 1600
    elif (departure_var_ == "Rawalpindi" and txt_destination_ == "Quetta") or (departure_var_ == "Quetta" and txt_destination_ == "Rawalpindi"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Rawalpindi" and txt_destination_ == "Sialkot") or (departure_var_ == "Sialkot" and txt_destination_ == "Rawalpindi"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 700
    elif (departure_var_ == "Rawalpindi" and txt_destination_ == "Multan") or (departure_var_ == "Multan" and txt_destination_ == "Rawalpindi"):
        if class_var_ == "Economy":
            fair += 700
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Lahore" and txt_destination_ == "Peshawar") or (departure_var_ == "Peshawar" and txt_destination_ == "Lahore"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Lahore" and txt_destination_ == "Karachi") or (departure_var_ == "Karachi" and txt_destination_ == "Lahore"):
        if class_var_ == "Economy":
            fair += 1000
        elif class_var_ == "Business":
            fair += 1300
    elif (departure_var_ == "Lahore" and txt_destination_ == "Quetta") or (departure_var_ == "Quetta" and txt_destination_ == "Lahore"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Lahore" and txt_destination_ == "Sialkot") or (departure_var_ == "Sialkot" and txt_destination_ == "Lahore"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 600
    elif (departure_var_ == "Lahore" and txt_destination_ == "Multan") or (departure_var_ == "Multan" and txt_destination_ == "Lahore"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 600
    elif (departure_var_ == "Peshawar" and txt_destination_ == "Karachi") or (departure_var_ == "Karachi" and txt_destination_ == "Peshawar"):
        if class_var_ == "Economy":
            fair += 1400
        elif class_var_ == "Business":
            fair += 1700
    elif (departure_var_ == "Peshawar" and txt_destination_ == "Quetta") or (departure_var_ == "Quetta" and txt_destination_ == "Peshawar"):
        if class_var_ == "Economy":
            fair += 900
        elif class_var_ == "Business":
            fair += 1200
    elif (departure_var_ == "Peshawar" and txt_destination_ == "Sialkot") or (departure_var_ == "Sialkot" and txt_destination_ == "Peshawar"):
        if class_var_ == "Economy":
            fair += 600
        elif class_var_ == "Business":
            fair += 900
    elif (departure_var_ == "Peshawar" and txt_destination_ == "Multan") or (departure_var_ == "Multan" and txt_destination_ == "Peshawar"):
        if class_var_ == "Economy":
            fair += 1000
        elif class_var_ == "Business":
            fair += 1300
    elif (departure_var_ == "Karachi" and txt_destination_ == "Quetta") or (departure_var_ == "Quetta" and txt_destination_ == "Karachi"):
        if class_var_ == "Economy":
            fair += 1000
        elif class_var_ == "Business":
            fair += 1300
    elif (departure_var_ == "Karachi" and txt_destination_ == "Sialkot") or (departure_var_ == "Sialkot" and txt_destination_ == "Karachi"):
        if class_var_ == "Economy":
            fair += 1100
        elif class_var_ == "Business":
            fair += 1400
    elif (departure_var_ == "Karachi" and txt_destination_ == "Multan") or (departure_var_ == "Multan" and txt_destination_ == "Karachi"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Quetta" and txt_destination_ == "Sialkot") or (departure_var_ == "Sialkot" and txt_destination_ == "Quetta"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Quetta" and txt_destination_ == "Multan") or (departure_var_ == "Multan" and txt_destination_ == "Quetta"):
        if class_var_ == "Economy":
            fair += 600
        elif class_var_ == "Business":
            fair += 900
    elif (departure_var_ == "Sialkot" and txt_destination_ == "Multan") or (departure_var_ == "Multan" and txt_destination_ == "Sialkot"):
        if class_var_ == "Economy":
            fair += 700
        elif class_var_ == "Business":
            fair += 1000

    if name_var_ == '' or age_var_ == '' or cnic_var_ == '' or date_var_ == '' or class_var_ == '' or departure_var_ == '' or txt_destination_ == '' or txt_timing_ == '':
        messagebox.showerror("Error!", "Field cannot be empty")
    else:
        age_var_ = int(age_var_)
        if age_var_ <= 2:
            fair = fair*0
        elif age_var_ <= 18 and age_var_ > 2:
            fair = fair*(1-0.2)
        elif age_var_ >= 60:
            fair = fair*(1-0.4)
        age_var_ = str(age_var_)
        cur.execute("select * from passenger_detail where cnic = %s", cnic_var_)
        row = cur.fetchone()
        if row is not None:
            messagebox.showerror("Error", "Ticket already booked . If you want to book or another destination cancel previous ticket.")
        else:
            sql = "INSERT INTO `passenger_detail` (`name`,`age`, `CNIC`, `date`,`booking_class`,`departure`,`destination`,`timing`, `fare`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name_var_, age_var_, cnic_var_, date_var_, class_var_, departure_var_, txt_destination_, txt_timing_, fair)
            cur.execute(sql, val)
            con.commit()
            print(cur.rowcount, "record inserted.")
            name_var.set("")
            age_var.set("")
            cnic_var.set("")
            date_var.set("")
            class_var.set("")
            departure_var.set("")
            txt_destination.set("")
            txt_timing.set("")
            messagebox.showinfo("Success!", "Booking Done Successfully")


def main():
    global name_var, age_var, cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing, headingFrame1
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
    name_var = StringVar()
    age_var = StringVar()
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
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.LANCZOS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)

    # We create the image on the canvas1 using .create_image() method.
    # We use .pack() method to organize widgets in blocks before placing them in the parent widget.
    Canvas1.create_image(400, 400, image=img)
    Canvas1.config(bg="#3e271e", width=newImageSizeWidth, heigh=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    # Showing txt
    headingFrame1 = Frame(root, bg="#094757")
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.8)

    # ====== Sign Up ========
    headingLabel = Label(headingFrame1, text="Welcome to Railway Booking System", bg='#094757', fg='light gray',
                         font=('Bahnschrift SemiBold Condensed', 24))
    headingLabel.place(relx=0.125, y=20)

    userName = Label(headingFrame1, text="Name", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(
        relx=0.2,
        y=90)
    txt_userName = Entry(headingFrame1, textvariable=name_var, font=('Calibri', 12)).place(relx=0.2, y=120, width=300)

    age = Label(headingFrame1, text="Age", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2,
                                                                                                           y=150)
    txt_age = Entry(headingFrame1, textvariable=age_var, font=('Calibri', 12)).place(relx=0.2, y=180, width=300)

    CNIC = Label(headingFrame1, text="CNIC", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2,
                                                                                                             y=210)
    txt_cnic = Entry(headingFrame1, textvariable=cnic_var, font=('Calibri', 12)).place(relx=0.2, y=240, width=300)

    Date = Label(headingFrame1, text="Date", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=270)
    txt_date = DateEntry(headingFrame1, textvariable=date_var, selectmode='day', date_pattern='yyyy/mm/dd').place(relx=0.2, y=300, width=300)

    Booking_Class = Label(headingFrame1, text="Booking Class", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=330)
    txt_class = ttk.Combobox(headingFrame1, textvariable=class_var, width=47)
    txt_class['values'] = ['Select', "Economy", "Business"]
    txt_class.place(relx=0.2, y=360)
    txt_class.current(0)

    Departure = Label(headingFrame1, text="Departure", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=390)
    txt_departure = ttk.Combobox(headingFrame1, textvariable=departure_var, width=47)
    txt_departure['values'] = ['Select', "Rawalpindi", "Lahore", "Karachi", "Peshawar", "Quetta", "Multan", "Sialkot"]
    txt_departure.place(relx=0.2, y=420)
    txt_departure.current(0)

    Destination = Label(headingFrame1, text="Destination", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=450)
    txt_destination = ttk.Combobox(headingFrame1, textvariable=txt_destination, width=47)
    txt_destination['values'] = ['Select', "Rawalpindi", "Lahore", "Karachi", "Peshawar", "Quetta", "Multan", "Sialkot"]
    txt_destination.place(relx=0.2, y=480)
    txt_destination.current(0)

    Timing = Label(headingFrame1, text="Time ", bg='#094757', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=510)
    txt_timing = ttk.Combobox(headingFrame1, textvariable=txt_timing, width=47)
    v1 = ['Select', 'Departure : 10AM     Destination : 2PM', 'Departure : 12AM     Destination : 4PM', 'Departure : 2PM     Destination : 6PM', 'Departure : 4PM     Destination : 8PM', 'Departure : 6PM     Destination : 10PM']
    v2 = ['Select', 'Departure : 10AM     Destination : 1PM', 'Departure : 12AM     Destination : 3PM', 'Departure : 2PM     Destination : 5PM', 'Departure : 4PM     Destination : 7PM', 'Departure : 6PM     Destination : 9PM']
    v3 = ['Select', 'Departure : 10AM     Destination : 4PM', 'Departure : 12AM     Destination : 6PM', 'Departure : 2PM     Destination : 8PM', 'Departure : 4PM     Destination : 10PM', 'Departure : 6PM     Destination : 12AM']
    v4 = ['Select', 'Departure : 10AM     Destination : 10PM', 'Departure : 12AM     Destination : 12PM', 'Departure : 2PM     Destination : 2AM', 'Departure : 4PM     Destination : 4AM', 'Departure : 6PM     Destination : 6AM']
    v5 = ['Select', 'Departure : 10AM     Destination : 3PM', 'Departure : 12AM     Destination : 5PM', 'Departure : 2PM     Destination : 7AM', 'Departure : 4PM     Destination : 9AM', 'Departure : 6PM     Destination : 11AM']
    v = [v1, v2, v3, v4, v5]
    r = random.choice(v)
    txt_timing['values'] = r
    txt_timing.place(relx=0.2, y=540)
    txt_timing.current(0)

    # === Confirm Button ===
    confirm = Button(headingFrame1,
                     command=passenger_details,
                     text="Confirm",
                     bg='dark green',
                     fg='light gray').place(relx=0.2, y=590, width=300)

    # ==== root.mainloop ====
    root.mainloop()
