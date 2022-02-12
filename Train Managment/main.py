from fare import price_c
from View_Booking import view
from update import update
from book_your_ticket import main
from Cancel_booking import delete
from tkinter import *
from PIL import ImageTk, Image
import pymysql

my_pass = ""
my_database = "Qasier's Train"

# ===Connecting to the MySql server===
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()

# ===Creating Window===
root = Tk()
root.title("Qasier's Train")
root.minsize(width=1000, height=800)
root.geometry("0x0")
same = True
n = 0.365

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

# ===Showing Headings===
headingFrame1 = Frame(root, bg="#094757")
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.8)

headingLabel = Label(headingFrame1, text="Welcome to Railway Booking System", bg='#094757', fg='light gray', font=('Bahnschrift SemiBold Condensed', 24))
headingLabel.place(relx=0.13, y=50)

# member functions
# ===Button 1===
btn1 = Button(root,
              text="Book your Ticket",
              bg='#094757',
              fg="light gray",
              font=('Calibri bold', 12),
              command=main
              )
btn1.place(
    relx=0.28,
    rely=0.3,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 2===
btn2 = Button(root,
              text="Cancel Booking",
              bg='#094757',
              fg="light gray",
              font=('Calibri bold', 12),
              command=delete
              )
btn2.place(
    relx=0.28,
    rely=0.7,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 3===
btn3 = Button(root,
              text="Ticket Details",
              bg='#094757',
              fg="light gray",
              font=('Calibri bold', 12),
              command=view
              )
btn3.place(
    relx=0.28,
    rely=0.5,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 4===
btn4 = Button(root,
              text="Calculate Ticket Fare",
              bg='#094757',
              fg="light gray",
              font=('Calibri bold', 12),
              command=price_c
              )
btn4.place(
    relx=0.28,
    rely=0.6,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 5===
btn5 = Button(root,
              text="Update Booking",
              bg='#094757',
              fg="light gray",
              font=('Calibri bold', 12),
              command=update
              )
btn5.place(
    relx=0.28,
    rely=0.4,
    relwidth=0.45,
    relheight=0.1
)

root.mainloop()
