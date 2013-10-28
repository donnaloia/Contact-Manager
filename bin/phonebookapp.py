from Tkinter import *
import sqlite3

class Hello():
	def __init__(self, master):
		frame=Frame(master, width=80, height=50)
		frame.pack()

		self.text = Label(frame, text="")
		self.text.pack()
		self.text.grid(row=0, sticky=W, pady=10, padx=10)

		self.TextField = Entry(frame, width=45)
		self.TextField.pack()
		self.TextField.grid(row=1, rowspan=2, sticky=W, pady=5, padx = 10)

		self.btn=Button(frame, text='Add', command=self.add_note)
		self.btn.pack()
		self.btn.grid(row=3, rowspan=2, sticky=W, pady=10, padx=10)

		self.showbtn = Button(frame, text='Update', command=self.show_notes)
		self.showbtn.pack()
		self.showbtn.grid(row=3, rowspan=2, pady=10, padx=20)

		self.delbtn = Button(frame, text='Delete', command=self.del_notes)
		self.delbtn.pack()
		self.delbtn.grid(row=3, rowspan=2, pady=20, padx=30)


		self.content=Listbox(master, width=50)
		self.content.pack()

	def add_note(self):
		if self.TextField.get() == "":
			self.text["text"] = "Please type sumting"
		else:
			item = self.TextField.get()

			conn = sqlite3.connect('phonebook1.db')
			c = conn.cursor()
			conn.execute('''
    	CREATE TABLE IF NOT EXISTS people(name TEXT primary key,
                       age TEXT, phone TEXT, fblink TEXT)''')
			c.execute("insert into people(name) values (?)", (item,))
			conn.commit()
			c.close()
			self.TextField.delete(0, END)

	def show_notes(self):
		conn = sqlite3.connect('phonebook1.db')

		c =conn.cursor()

		conn.execute('''
    	CREATE TABLE IF NOT EXISTS people(name TEXT primary key,
                       age TEXT, phone TEXT, fblink TEXT)''')
		list=c.execute("SELECT * FROM people")
		conn.commit()

		for row in list:
			self.content.insert(END, row)
		c.close()
	
	def del_notes(self):
		pass

root=Tk()
application = Hello(root)
root.mainloop()
