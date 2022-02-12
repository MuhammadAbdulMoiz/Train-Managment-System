from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

my_pass = ""
my_database = "Qasier's Train"

# ===Connecting to the MySql server===
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()

# Enter Table Names here
bookTable = "passenger_detail"


def view():
    root = Toplevel()
    root.title("TMS_View Booking")
    root.attributes('-fullscreen',True)
    root.geometry("0x0")
    same = True
    n = 0.5

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
    heading_frame1.place(relx=0.03, rely=0.13, relwidth=0.95, relheight=0.6)

    heading_label = Label(heading_frame1, text="View Booking", bg='#094757', fg='light gray', font=('Calibri bold', 24))
    heading_label.place(relx=0.42, y=25)

    y = 0.3

    Label(heading_frame1, text="{:<20} {:<5} {:<25} {:<20} {:<20} {:<17} {:<20} {:<82} {:<10}".format('Name', 'Age', 'CNIC', 'Date', 'Booking_Class', 'Departure', 'Destination', 'Time', 'Fare'), font=('Calibri bold', 12), bg='#094757', fg='light Gray').place(
        relx=0.07, rely=0.175)
    Label(heading_frame1, text="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg='#094757',
          fg='light Gray').place(relx=0.05, rely=0.25)
    get_bookings = "select * from " + bookTable
    try:
        cur.execute(get_bookings)
        con.commit()
        for i in cur:
            Label(heading_frame1, text='%-18s%-5s%-15s%-15s%-22s%-20s%-24s%-59s%-3s' % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[8], i[9]), font=('Calibri', 13), bg='#094757', fg='light Gray').place(
                relx=0.07, rely=y)
            y += 0.1
    except (pymysql.Error, pymysql.Warning):
        messagebox.showinfo("Failed to fetch files from database")

    # ===Quit Button===
    quit_btn = Button(root,
                      text="Quit",
                      bg='#094757',
                      fg='light gray',
                      font=('Calibri bold', 12),
                      command=root.destroy
                      )
    quit_btn.place(
        relx=0.4,
        rely=0.9,
        relwidth=0.18,
        relheight=0.08
        )

    root.mainloop()
