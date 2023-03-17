from tkinter import *
import requests

root = Tk()
Fr_lab = Label(text="Please print id:")
Fr_fra = Frame()
Fr_lab.pack()
Fr_fra.pack()

Fr_lab1 = Label(text="Please print blance:")
Fr_fra1 = Frame()
Fr_lab1.pack()
Fr_fra1.pack()

entry_id = Entry(master=Fr_fra)

entry_balance = Entry(master=Fr_fra1)

entry_id.grid(row=1, column=1)
entry_balance.grid(row=2)
First_fr = Frame()
def send_id():
    id = entry_id.get()
    balance = entry_balance.get()
    setbalnce = "https://coderlog.top/api/goit/?key=yourkey&method=setbalance&user={}&balance={}".format(id, balance)
    requests.get(setbalnce)

    url = "https://coderlog.top/api/goit/?key=yourkey&method=getdata&user={}".format(id)
    res = requests.get(url)
    json = res.json()
    
    for k in json:
        user_id = k['id']
        name = k['name']
        surname = k['surname']
        email = k['email']
        school_group = k['school_group']
        status = k['status']
        balance = k['balance']

    finish_data.config(text="id: {}\nname: {}\nsurname: {}\nemail: {}\ngroup: {}\nstatus: {}\nbalance: {}".format(user_id, name, surname, email, school_group, status, balance))
    print(json)

    if user_id == None:
      finish_data.config(text="Such id not found, try again")


finish_data = Label()
finish_data.pack()

def input_data():

  Last_but = Frame()
  Last_but.pack()
  button = Button(text="Show", master=Last_but,  command=send_id)
  button.pack()

  mainloop()

input_data()