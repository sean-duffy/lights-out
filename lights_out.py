from Tkinter import *
from random import choice, randint

class App:
	def __init__(self):
		self.root = Tk()
		self.root.wm_title('Lights Out')

		self.board = [0]*25
		self.initial_state = [False]*25
		self.values = [False]*25
		self.level = 0

		Frame(self.root).grid(row=0, pady=3)
		self.level_label = Label(self.root)
		self.level_label.grid(row=1)
		self.wrapper = Frame(self.root)
		self.wrapper.grid(row=2, padx=30)
		Frame(self.wrapper).grid(pady=2)

		self.levels = [
		[1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1],
		[0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0],
		[0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1],
		[0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
		[0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1],
		[0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0],
		[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1]
		]

		self.reductions = [
		[1,0,0,0,1],
		[0,1,0,1,0],
		[1,1,1,0,0],
		[0,0,1,1,1],
		[1,0,1,1,0],
		[0,1,1,0,1],
		[1,1,0,1,1]
		]
		
		for row in range(5):
			for col in range(5):
				self.board[row*5+col] = Checkbutton(self.wrapper)
				self.board[row*5+col].grid(row=row+1, column=col)
				self.board[row*5+col].config(command=lambda row=row, col=col: self.switch(row, col))

		self.msg = Label(self.root)
		self.msg.grid(row=3)

		self.action_btn = Button(self.root, text='Reset Game', command=self.reset)
		self.action_btn.grid(row=4)
		Frame(self.root).grid(pady=5)

		self.initialise()
		self.root.mainloop()

	def initialise(self):
		self.action_btn.config(text='Reset Game', command=self.reset)
		level_text = 'Level: ' + str(self.level + 1)
		self.level_label.config(text=level_text)
		for i in range(25):
				self.board[i].config(state='active')
		self.msg.config(text='')
		self.values = [False]*25
		for i in range(25):
			self.board[i].deselect()
		if self.level < 8:
			# load next level
			for n, i in enumerate(self.levels[self.level]):
				if i == 1:
					self.values[n] = True
					self.board[n].select()
		else:
			# generate a new level
			for n, i in enumerate(choice(self.reductions)):
				if i == True:
					self.values[20+n] = True
					self.board[20+n].select()
			for i in range(3):
				self.switch(randint(0, 4), randint(0, 4))
		self.initial_state = self.values[:]
		self.reset()

	def reset(self):
		self.values = [False]*25
		for i in range(25):
			self.board[i].deselect()
			if self.initial_state[i] == True:
				self.board[i].select()
				self.values[i] = True

	def switch(self, row, col):
		self.values[row*5+col] = not self.values[row*5+col]
		if row > 0:
			self.board[(row-1)*5+col].toggle()
			self.values[(row-1)*5+col] = not self.values[(row-1)*5+col]
		if row < 4:
			self.board[(row+1)*5+col].toggle()
			self.values[(row+1)*5+col] = not self.values[(row+1)*5+col]
		if col > 0:
			self.board[row*5+(col-1)].toggle()
			self.values[row*5+(col-1)] = not self.values[row*5+(col-1)]
		if col < 4:
			self.board[row*5+(col+1)].toggle()
			self.values[row*5+(col+1)] = not self.values[row*5+(col+1)]
		self.victory_check()

	def victory_check(self):
		if True not in self.values:
			self.msg.config(text='Well done, you won!')
			self.action_btn.config(text='Next Game', command=self.initialise)
			for i in range(25):
				self.board[i].config(state='disabled')
			self.level += 1

app = App()