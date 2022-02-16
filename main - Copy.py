from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
from random import choice
import threading

quiz = [
	["How heavy is a teaspoon of a neutron star?", ["5 billion tons", "5 thousand tons", "150 kilograms"]],
	["How many states of matter are there?", ["22", "4", "15"]],
	["What's the largest living structure on Earth?", ["Great Barrier Reef", "Blue Whale", "Amazon Forest"]],
]
numList = list(range(len(quiz)))

root = Tk()
root.title("UniScience")
root.geometry("1280x800")
root.iconbitmap("uniscience-logo.png")

logo = ImageTk.PhotoImage(Image.open("uniscience-logo.png"))

def enter_screen():
	for widget in root.winfo_children():
		widget.destroy()
	titleLabel = Label(root, text="UniScience", font=("Roboto 30"))
	titleLabel.configure(foreground="purple")
	titleLabel.pack(pady=(130, 0))

	logoLabel = Label(image=logo)
	logoLabel.pack()

	startButton = Button(root, text="Start Guessing", command=start_game, font=("Roboto", 12))
	startButton.pack()

def check_answer(answerNum):
	if answerNum == 0 or answerNum == 10 or answerNum == 20:
		successThread = threading.Thread(target=lambda: playsound(u"C:\\Users\\dora\\OneDrive\\Documents\\DORA - PERSONAL\\Applications\\Rise\\success-sound-effect.mp3"))
		successThread.start()
		if answerNum == 0:
			answerButton_00.config(bg="green")
		elif answerNum == 10:
			answerButton_10.config(bg="green")
		elif answerNum == 20:
			answerButton_20.config(bg="green")
	else:
		failThread = threading.Thread(target=lambda: playsound(u"C:\\Users\\dora\\OneDrive\\Documents\\DORA - PERSONAL\\Applications\\Rise\\fail-sound.mp3"))
		failThread.start()
		if answerNum == 1:
			answerButton_01.config(bg="red")
			answerButton_00.config(bg="green")
		elif answerNum == 2:
			answerButton_02.config(bg="red")
			answerButton_00.config(bg="green")
		elif answerNum == 11:
			answerButton_11.config(bg="red")
			answerButton_10.config(bg="green")
		elif answerNum == 12:
			answerButton_12.config(bg="red")
			answerButton_10.config(bg="green")
		elif answerNum == 21:
			answerButton_21.config(bg="red")
			answerButton_20.config(bg="green")
		elif answerNum == 22:
			answerButton_22.config(bg="red")
			answerButton_20.config(bg="green")

def retry_the_game():
	for question in range(len(quiz)):
		for answer in range(len(quiz[question][1])):
			globals()[f"answerButton_{question}{answer}"].config(bg="white")
	
def start_game():
	for widget in root.winfo_children():
		widget.destroy()

	titleLabel = Label(root, text="UniScience", font=("Roboto 30"))
	titleLabel.configure(foreground="purple")
	titleLabel.pack(pady=20)


	questionLabel_0 = Label(root, text=quiz[0][0], font=("Roboto 15"))
	questionLabel_0.pack(pady=10)

	global answerButton_00
	answerButton_00 = Button(root, text=quiz[0][1][0], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(0))
	global answerButton_01
	answerButton_01 = Button(root, text=quiz[0][1][1], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(1))
	global answerButton_02
	answerButton_02 = Button(root, text=quiz[0][1][2], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(2))

	randomNumList = list(range(3))

	randomNum = choice(randomNumList)
	randomNumList.remove(randomNum)
	globals()[f"answerButton_0{randomNum}"].pack(pady=5)
	
	randomNum = choice(randomNumList)
	randomNumList.remove(randomNum)
	globals()[f"answerButton_0{randomNum}"].pack(pady=5)
	
	randomNum = choice(randomNumList)
	globals()[f"answerButton_0{randomNum}"].pack(pady=5)
	

	questionLabel_1 = Label(root, text=quiz[1][0], font=("Roboto 15"))
	questionLabel_1.pack(pady=10)

	global answerButton_10
	answerButton_10 = Button(root, text=quiz[1][1][0], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(10))
	global answerButton_11
	answerButton_11 = Button(root, text=quiz[1][1][1], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(11))
	global answerButton_12
	answerButton_12 = Button(root, text=quiz[1][1][2], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(12))

	randomNumList = list(range(3))
	
	randomNum = choice(randomNumList)
	randomNumList.remove(randomNum)
	globals()[f"answerButton_1{randomNum}"].pack(pady=5)
	
	randomNum = choice(randomNumList)
	randomNumList.remove(randomNum)
	globals()[f"answerButton_1{randomNum}"].pack(pady=5)
	
	randomNum = choice(randomNumList)
	globals()[f"answerButton_1{randomNum}"].pack(pady=5)


	questionLabel_2 = Label(root, text=quiz[2][0], font=("Roboto 15"))
	questionLabel_2.pack(pady=10)

	global answerButton_20
	answerButton_20 = Button(root, text=quiz[2][1][0], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(20))
	global answerButton_21
	answerButton_21 = Button(root, text=quiz[2][1][1], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(21))
	global answerButton_22
	answerButton_22 = Button(root, text=quiz[2][1][2], font=("Roboto 12"), relief=GROOVE, command=lambda: check_answer(22))

	randomNumList = list(range(3))
	
	randomNum = choice(randomNumList)
	randomNumList.remove(randomNum)
	globals()[f"answerButton_2{randomNum}"].pack(pady=5)
	
	randomNum = choice(randomNumList)
	randomNumList.remove(randomNum)
	globals()[f"answerButton_2{randomNum}"].pack(pady=5)
	
	randomNum = choice(randomNumList)
	globals()[f"answerButton_2{randomNum}"].pack(pady=5)


	retryButton = Button(root, text="Retry", font=("Roboto 14"), command=retry_the_game)
	retryButton.pack(pady=30)
	backButton = Button(root, text="Back", font=("Roboto 14"), command=enter_screen)
	backButton.pack()


enter_screen()

root.mainloop()	