from Tkinter import *
import sqlite3

Class Hello():
	def __init__(self, master):
		frame=Frame(master, width=80, height=50)
		frame.pack()

		self.text = Label(frame, text="")
		self.text.pack()
		self.text.grid(row=0, sticky=W, pady=10, padx=10)

		self.TextField = Entry(frame, width=45)
		self.TextField.pack()
		self.TextField.grid(row=1, rowspan=2, sticky=W, pady=5, padx = 10)

		self.btn=Button(frame, text='Add note', command=self.add_note)
		self.btn.pack()
		self.btn.grid(row=3, rowspan=2, sticky=W, pady=10, padx=10)

		self.showbtn = Button(frame, text="Show Notes", command=self.show)
		self.showbtn.pack()
		self.showbtn.grid(row=3, rowspan=2, pady=10, padx=80)

		self.content=Listbox(master, width=50)
		self.content.pack()

	def add_note(self):
		if self.TextField.get() == "":
			self.text["text"] = "Please type sumting"
		else:
			item = self.TextField.get()

			conn = sqlite3.connect('phonebook1.db')
			c = conn.cursor()

			c.close()

	def show_notes(self):
		conn = sqlite3.connect('phonebook1.db')
		c =conn.cursor()

		for row in list:
			self.content.insert(END, row)
		c.close()

root=Tk()
application = Hello(root)
root.mainloop()
