import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry, Calendar
from PIL import ImageTk, Image

root=tk.Tk()
root.resizable(0,0)
root.title("Calendar Scheduler")
#set background color
root.config(bg='gray')

#function to create pop-up alt text at bottom of window
def image_hover_2(e):
    alt_label.config(text="You're hovering over the Calendar_img.jpg image.")
#function to remove pop-up alt text at bottom of window
def image_hover_leave_2(e):
    alt_label.config(text="")

#import calendar image
calendar= Image.open("Calendar_img.jpg")
#resize image and make label to display new image
resized = calendar.resize((75, 75), Image.ANTIALIAS)
cal_resized = ImageTk.PhotoImage(resized)
label = Label(root, image=cal_resized)
label.grid(row=0, column=2, pady=10)

#image alt text label
alt_label= Label(root, text= "", bd=1, relief=SUNKEN, anchor=SE)
alt_label.place(rely=1.0, relx=1.0, x=0,y=0, anchor=SE)

#bind function to image when hovered over
label.bind("<Enter>", image_hover_2)
label.bind("<Leave>", image_hover_leave_2)

#function to create pop-up alt text at bottom of window
def image_hover(e):
    alt_label.config(text="You're hovering over the Capture.JPG image.")
#function to remove pop-up alt text at bottom of window
def image_hover_leave(e):
    alt_label.config(text="")

#import calendar image
calendar_2= Image.open("Capture.JPG")
#resize image and make label to display new image
resized_2 = calendar_2.resize((75, 75), Image.ANTIALIAS)
cal_resized_2 = ImageTk.PhotoImage(resized_2)
label_2 = Label(root, image=cal_resized_2)
label_2.grid(row=0, column=0, pady=10)

#image alt text label
alt_label= Label(root, text= "", bd=1, relief=SUNKEN, anchor=SE)
alt_label.place(rely=1.0, relx=1.0, x=0,y=0, anchor=SE)

#bind function to image when hovered over
label_2.bind("<Enter>", image_hover)
label_2.bind("<Leave>", image_hover_leave)

#create main label for calendar
calendarLabel = Label(root, text='Calendar', font=('arial',24,'bold'), bg='gray')
calendarLabel.grid(row=0, column=1, columnspan=1)

#create month/year selection label
selectionLabel= Label(root, text="Select month/year and press enter to view calendar",font=('arial',12,'bold'), bg='gray')
selectionLabel.grid(row=1, column=0, columnspan=3, padx=10)

#create a label for the month
monthLabel = Label(root, text="Month", font=('arial',12,'bold'), bg='gray')
monthLabel.grid(row=2, column=0)

#create a label for the year
yearLabel = Label(root, text="Year", font=('arial',12,'bold'), bg='gray')
yearLabel.grid(row=2, column=1)

#create a spin box for the user to select the month
monthSelect = Spinbox(root, from_=1, to=12, width=8, font=('arial', 10, 'bold'))
monthSelect.grid(row=3, column=0, padx=10)
if int(monthSelect.get()) not in range(1,13):
    print("Error")

#create a spin box for the user to select the year
yearSelect = Spinbox(root, from_=2000, to=2100, width=8, font=('arial', 10, 'bold'))
yearSelect.grid(row=3, column=1, padx=10)

# Function that shows the calendar of the selected month/year
def calendar_month():
    cal = Calendar(root, selectmode="day", year=int(yearSelect.get()), month=int(monthSelect.get()), day=1, selectbackground= 'red')
    cal.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def grab_date():
        l1.config(text="Date Selected is " + cal.get_date())

    goButton = Button(root, text="Go", font=('arial', 12, 'bold'), command=lambda: [new_gui(), grab_date()])
    goButton.grid(row=7, column=1, pady=10)
    l1 = Label(root, text="", bg='gray')
    l1.grid(row=8, column=1, pady=20)
    print(str(l1.cget()))


#create an enter button for the user to press once they have selected the month/year
enterButton = Button(root, text="Enter", font=('arial',12,'bold'), command=calendar_month)
enterButton.grid(row=3, column=2, padx=10)

#create a label instructing the user on what to do
instructLabel = Label(root, text="Select a date and press 'Go' to schedule an event", font=('arial', 12, 'bold'), bg='gray')
instructLabel.grid(row=6, column=0, columnspan=3, padx=10)

#function that opens a new window for event scheduling once 'Go' button is pressed
def new_gui():
    new_gui= Toplevel()
    new_gui.config(bg='gray')

    # function to retrieve data from time spinboxes
    def saveTime():
       hour = hourSelect.get()
       minute= int(minSelect.get())
       am_pm= timeframeSelect.get()
       str(print(hour, ":", ("%02d" % (minute)), am_pm))

#function that opens a new window with an event summary
    def eventSave():
       eventSave= Toplevel()
       eventSave.config(bg='gray')

       hour = hourSelect.get()
       minute = int(minSelect.get())
       am_pm = timeframeSelect.get()
       hourLabel= Label(eventSave, text=("At " +(str(hour))+":"+(str("%02d" % (minute)))+(str(am_pm))), font=('arial', 20, 'bold'), bg='gray')
       hourLabel.grid(row=5, column=0)

       title = eventTitle.get()
       description = textbox.get("1.0", END)
       date= ("%02d" % (int(monthSelect.get())), '/' ,(int(yearSelect.get())))

       #create labels stating an event was scheduled
       scheduledLabel= Label(eventSave, text="Event Scheduled",font=('arial', 24, 'bold'), bg='gray')
       scheduledLabel.grid(row=1, column=0)

       scheduledLabel_2= Label(eventSave, text= date, font=('arial', 24, 'bold'), bg='gray')
       scheduledLabel_2.grid(row=1, column=2)


       eventTitleLabel = Label(eventSave, text=("Event Title: "+ str(title)), font=('arial', 20, 'bold'), bg='gray')
       eventTitleLabel.grid(row=2, column=0)

       descLabel= Label(eventSave, text=("Event Description: " + str(description)), font=('arial', 20, 'bold'), bg='gray')
       descLabel.grid(row=3, column=0)

       new_gui.destroy()


    #create label in the new window
    timeLabel= Label(new_gui, text='Select a time: hh/mm/tt', font=("arial",12,"bold"), bg='gray')
    timeLabel.grid(row=1, column=1, columnspan=4)

    #create a spin box to select an hour
    hourSelect = Spinbox(new_gui, from_=00, to=12, width=8,font=('arial',10, 'bold'))
    hourSelect.grid(row=2, column=1, pady=10)

    # create a spin box to select a minute
    minSelect = Spinbox(new_gui, from_=00, to=59, width=8, font=('arial', 10, 'bold'))
    minSelect.grid(row=2, column=2, padx=5, pady=10)

    # create a spin box to select am or pm
    timeframeSelect = Spinbox(new_gui, values=('am', 'pm'), width=8, font=('arial', 10, 'bold'))
    timeframeSelect.grid(row=2, column=3, padx=5, pady=10)

    #create a button to enter the time
    enterTime = Button(new_gui, text="Enter", font=('arial', 12, 'bold'), command=saveTime)
    enterTime.grid(row=2, column=4, padx=10)


    #create a label for the event title entry
    titleLabel = Label(new_gui, text='Event Title:', font=("arial", 12, "bold"), bg='gray')
    titleLabel.grid(row=3, column=1, pady=10, padx=10)

    #create a textbox to enter the title of the event
    eventTitle= Entry(new_gui, width=24, fg='red')
    eventTitle.grid(row=3, column=2, columnspan=2, pady=10, padx=10)
    title = eventTitle


    #create a label for the event description
    descriptionLabel = Label(new_gui, text='Event Description:', font=("arial", 12, "bold"), bg='gray')
    descriptionLabel.grid(row=4, column=0, columnspan=3)
    description = descriptionLabel
    if title and description:
        print(title, description)
    else:
        tk.messagebox.showwarning(title="Error", message="Please fill out required fields")
    #create a textbox to enter a description of the event
    textbox= Text(new_gui,width=36, height=12, fg='red')
    textbox.grid(row=5, column=1, columnspan=4, pady=10)

    #create a button to save the event
    saveButton= Button(new_gui, text='Save Event', font=('arial',12,'bold'), command=eventSave)
    saveButton.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

    #create a button to cancel and return to calendar
    cancelButton= Button(new_gui, text='Nevermind', font=('arial',12,'bold'), command=new_gui.destroy)
    cancelButton.grid(row=6, column=3, columnspan=2, padx=10, pady=10)


root.mainloop()