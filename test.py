import Tkinter as tk   # python
import Main_fork
import random
from Tkinter import *

TITLE_FONT = ("Helvetica", 18, "bold")


root=Tk()

root.title("Botzee2.0")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(root)
        self.geometry("950x794")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.update()

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select a game Mode", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Play Against A Bot",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Play Against Another Person",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Show Me The Best Cases",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    cow_count=1
    cow = StringVar()
    
    def cowplus(self):
        self.cow_count += 1
        self.cow.set(self.cow_count)
            
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
      
        self.cow_count = 1
        self.cow.set(self.cow_count)
        
        
        spacelabel = tk.Label(self, text = "", width = "83")
        spacelabel.grid(row = 1, column = 2)
        oneslabel = tk.Label(self, textvariable = self.cow, width = "14")
        oneslabel.grid(row = 2, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 3, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 4, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 5, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 6, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 7, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 8, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 9, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 10, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 11, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 12, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 13, column = 1)
        oneslabel = tk.Label(self, text = "4", width = "14")
        oneslabel.grid(row = 14, column = 1)
        
        
        label = tk.Label(self, text="Select a Section", font=5)
        label.grid(row = 1, column = 0)
    
        buttonMain = tk.Button(self, text="Main Menu", height = "3", width = "14",
                           command=lambda: controller.show_frame("StartPage"))
        buttonScoreOnes = tk.Button(self, text = "Ones", height = "3", width = "14", command = self.cowplus)
        buttonScoreTwos = tk.Button(self, text = "Twos", height = "3", width = "14")
        buttonScoreThrees = tk.Button(self, text = "Threes", height = "3", width = "14")
        buttonScoreFours = tk.Button(self, text = "Fours", height = "3", width = "14")
        buttonScoreFives = tk.Button(self, text = "Fives", height = "3", width = "14")
        buttonScoreSixes = tk.Button(self, text = "Sixes", height = "3", width = "14")
        buttonScoreThreeOfAKind = tk.Button(self, text = "Three of a Kind", height = "3", width = "14")
        buttonScoreFourOfAKind = tk.Button(self, text = "Four of a Kind", height = "3", width = "14")
        buttonScoreFullHouse = tk.Button(self, text = "Full House", height = "3", width = "14")
        buttonScoreSmallStraight = tk.Button(self, text = "Small Straight", height = "3", width = "14")
        buttonScoreLargeStraight = tk.Button(self, text = "Large Straight", height = "3", width = "14")
        buttonScoreChance = tk.Button(self, text = "Chance", height = "3", width = "14")
        buttonScoreYahtzee = tk.Button(self, text = "Yahtzee", height = "3", width = "14")

       
        
        buttonMain.grid(row = 1, column = 10)
        buttonScoreOnes.grid(row = 2, column = 0)
        buttonScoreTwos.grid(row = 3, column = 0)
        buttonScoreThrees.grid(row = 4, column = 0)
        buttonScoreFours.grid(row = 5, column = 0)
        buttonScoreFives.grid(row = 6, column = 0)
        buttonScoreSixes.grid(row = 7, column = 0)
        buttonScoreThreeOfAKind.grid(row = 8, column = 0)
        buttonScoreFourOfAKind.grid(row = 9, column = 0)
        buttonScoreFullHouse.grid(row = 10, column = 0)
        buttonScoreSmallStraight.grid(row = 11, column = 0)
        buttonScoreLargeStraight.grid(row = 12, column = 0)
        buttonScoreChance.grid(row = 13, column = 0)
        buttonScoreYahtzee.grid(row = 14, column = 0)
        

class PageTwo(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Playing Against Another Person", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        buttonMain = tk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        buttonScoreOnes = tk.Button(self, text = "Ones")
        buttonScoreTwos = tk.Button(self, text = "Twos")
        buttonScoreThrees = tk.Button(self, text = "Threes")
        buttonScoreFours = tk.Button(self, text = "Fours")
        buttonScoreFives = tk.Button(self, text = "Fives")
        buttonScoreSixes = tk.Button(self, text = "Sixes")
        buttonScoreThreeOfAKind = tk.Button(self, text = "Three of a Kind")
        buttonScoreFourOfAKind = tk.Button(self, text = "Four of a Kind")
        buttonScoreFullHouse = tk.Button(self, text = "Full House")
        buttonScoreSmallStraight = tk.Button(self, text = "Small Straight")
        buttonScoreLargeStraight = tk.Button(self, text = "Large Straight")
        buttonScoreChance = tk.Button(self, text = "Chance")
        buttonScoreYahtzee = tk.Button(self, text = "Yahtzee")
        buttonMain.pack(side = "left")
        buttonScoreOnes.pack(side = "left")
        buttonScoreTwos.pack(side = "left")
        buttonScoreThrees.pack(side = "left")
        buttonScoreFours.pack(side = "left")
        buttonScoreFives.pack(side = "left")
        buttonScoreSixes.pack(side = "left")
        buttonScoreThreeOfAKind.pack(side = "left")
        buttonScoreFourOfAKind.pack(side = "left")
        buttonScoreFullHouse.pack(side = "left")
        buttonScoreSmallStraight.pack(side = "left")
        buttonScoreLargeStraight.pack(side = "left")
        buttonScoreChance.pack(side = "left")
        buttonScoreYahtzee.pack(side = "left")

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Showing The Best Cases", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        buttonMain = tk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        buttonScoreOnes = tk.Button(self, text = "Ones")
        buttonScoreTwos = tk.Button(self, text = "Twos")
        buttonScoreThrees = tk.Button(self, text = "Threes")
        buttonScoreFours = tk.Button(self, text = "Fours")
        buttonScoreFives = tk.Button(self, text = "Fives")
        buttonScoreSixes = tk.Button(self, text = "Sixes")
        buttonScoreThreeOfAKind = tk.Button(self, text = "Three of a Kind")
        buttonScoreFourOfAKind = tk.Button(self, text = "Four of a Kind")
        buttonScoreFullHouse = tk.Button(self, text = "Full House")
        buttonScoreSmallStraight = tk.Button(self, text = "Small Straight")
        buttonScoreLargeStraight = tk.Button(self, text = "Large Straight")
        buttonScoreChance = tk.Button(self, text = "Chance")
        buttonScoreYahtzee = tk.Button(self, text = "Yahtzee")
        buttonMain.pack(side = "left")
        buttonScoreOnes.pack(side = "left")
        buttonScoreTwos.pack(side = "left")
        buttonScoreThrees.pack(side = "left")
        buttonScoreFours.pack(side = "left")
        buttonScoreFives.pack(side = "left")
        buttonScoreSixes.pack(side = "left")
        buttonScoreThreeOfAKind.pack(side = "left")
        buttonScoreFourOfAKind.pack(side = "left")
        buttonScoreFullHouse.pack(side = "left")
        buttonScoreSmallStraight.pack(side = "left")
        buttonScoreLargeStraight.pack(side = "left")
        buttonScoreChance.pack(side = "left")
        buttonScoreYahtzee.pack(side = "left")
      
if __name__ == "__main__":
    app = SampleApp()
    app.title("Botzee")
    app.destroy()
    app.mainloop()

