import Tkinter as tk   # python
import Main_fork as mf
import random
from Tkinter import *

TITLE_FONT = ("Helvetica", 18, "bold")


root = Tk()

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
    dice1_count = 0
    dice1 = StringVar()
    dice2_count = 0
    dice2 = StringVar()
    dice3_count = 0
    dice3 = StringVar()
    dice4_count = 0
    dice4 = StringVar()
    dice5_count = 0
    dice5 = StringVar()
    onescount = 0
    ones = StringVar()
    twoscount = 0
    twos = StringVar()
    threescount = 0
    threes = StringVar()
    fourscount = 0
    fours = StringVar()
    fivescount = 0
    fives = StringVar()
    sixescount = 0
    sixes = StringVar()
    threeofakindcount = 0
    threeofakind = StringVar()
    fourofakindcount = 0
    fourofakind = StringVar()
    fullhousecount = 0
    fullhouse = StringVar()
    smallstraightcount = 0
    smallstraight = StringVar()
    largestraightcount = 0
    largestraight = StringVar()
    chancecount = 0
    chance = StringVar()
    yahtzeecount = 0
    yahtzee = StringVar()
    totalscorecount = 0
    totalscore = StringVar()
    totalscore.set(onescount + twoscount + threescount + fourscount + fivescount + sixescount + threeofakindcount + fourofakindcount + fullhousecount + smallstraightcount + largestraightcount + chancecount + yahtzeecount)




    def rollupdate(self):
        global mydice
        mydice = [0, 0, 0, 0, 0]
        mydice = mf.roll()
        self.dice1_count = mydice[0]
        self.dice1.set(self.dice1_count)
        self.dice2_count = mydice[1]
        self.dice2.set(self.dice2_count)
        self.dice3_count = mydice[2]
        self.dice3.set(self.dice3_count)
        self.dice4_count = mydice[3]
        self.dice4.set(self.dice4_count)
        self.dice5_count = mydice[4]
        self.dice5.set(self.dice5_count)

    def updateones(self):
        self.onescount = mf.aces(mydice)
        self.ones.set(self.onescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatetwos(self):
        self.twoscount = mf.twos(mydice)
        self.twos.set(self.twoscount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatethrees(self):
        self.threescount = mf.threes(mydice)
        self.threes.set(self.threescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefours(self):
        self.fourscount = mf.fours(mydice)
        self.fours.set(self.fourscount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefives(self):
        self.fivescount = mf.fives(mydice)
        self.fives.set(self.fivescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatesixes(self):
        self.sixescount = mf.sixes(mydice)
        self.sixes.set(self.sixescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatethreeofakind(self):
        self.threeofakindcount = mf.threeofakind(mydice)
        self.threeofakind.set(self.threeofakindcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefourofakind(self):
        self.fourofakindcount = mf.fourofakind(mydice)
        self.fourofakind.set(self.fourofakindcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefullhouse(self):
        self.fullhousecount = mf.fullhouse(mydice)
        self.fullhouse.set(self.fullhousecount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatesmallstraight(self):
        self.smallstraightcount = mf.smallstraight(mydice)
        self.smallstraight.set(self.smallstraightcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatelargestraight(self):
        self.largestraightcount = mf.largestraight(mydice)
        self.largestraight.set(self.largestraightcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatechance(self):
        self.chancecount = mf.chance(mydice)
        self.chance.set(self.chancecount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updateyahtzee(self):
        self.yahtzeecount = mf.yahtzee(mydice)
        self.yahtzee.set(self.yahtzeecount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def cowplus(self):
        self.cow_count += 1
        self.cow.set(self.cow_count)





    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.cow_count = 1
        self.cow.set(self.cow_count)

        dice1label = tk.Label(self, textvariable=self.dice1, width = "14")
        dice1label.grid(row = 0, column = 0)
        dice2label = tk.Label(self, textvariable=self.dice2, width="14")
        dice2label.grid(row=0, column=1)
        dice3label = tk.Label(self, textvariable=self.dice3, width="14")
        dice3label.grid(row=0, column=2)
        dice4label = tk.Label(self, textvariable=self.dice4, width="14")
        dice4label.grid(row=0, column=3)
        dice5label = tk.Label(self, textvariable=self.dice5, width="14")
        dice5label.grid(row=0, column=4)
        spacelabel = tk.Label(self, text = "", width = "83")
        spacelabel.grid(row = 1, column = 9)
        oneslabel = tk.Label(self, textvariable = self.ones, width = "14")
        oneslabel.grid(row = 2, column = 1)
        oneslabel = tk.Label(self, textvariable = self.twos, width = "14")
        oneslabel.grid(row = 3, column = 1)
        oneslabel = tk.Label(self, textvariable = self.threes, width = "14")
        oneslabel.grid(row = 4, column = 1)
        oneslabel = tk.Label(self, textvariable = self.fours, width = "14")
        oneslabel.grid(row = 5, column = 1)
        oneslabel = tk.Label(self, textvariable = self.fives, width = "14")
        oneslabel.grid(row = 6, column = 1)
        oneslabel = tk.Label(self, textvariable = self.sixes, width = "14")
        oneslabel.grid(row = 7, column = 1)
        oneslabel = tk.Label(self, textvariable = self.threeofakind, width = "14")
        oneslabel.grid(row = 8, column = 1)
        oneslabel = tk.Label(self, textvariable = self.fourofakind, width = "14")
        oneslabel.grid(row = 9, column = 1)
        oneslabel = tk.Label(self, textvariable = self.fullhouse, width = "14")
        oneslabel.grid(row = 10, column = 1)
        oneslabel = tk.Label(self, textvariable = self.smallstraight, width = "14")
        oneslabel.grid(row = 11, column = 1)
        oneslabel = tk.Label(self, textvariable = self.largestraight, width = "14")
        oneslabel.grid(row = 12, column = 1)
        oneslabel = tk.Label(self, textvariable = self.chance, width = "14")
        oneslabel.grid(row = 13, column = 1)
        oneslabel = tk.Label(self, textvariable = self.yahtzee, width = "14")
        oneslabel.grid(row = 14, column = 1)
        totalscorelabel = tk.Label(self, text="Your Total Score Is: ")
        totalscorelabel.grid(row=14, column=4)
        totalscorelabel = tk.Label(self, textvariable=self.totalscore)
        totalscorelabel.grid(row=14, column=5)


        label = tk.Label(self, text="Select a Section", font=5)
        label.grid(row = 1, column = 0)

        buttonMain = tk.Button(self, text="Main Menu", height = "3", width = "14",
                           command=lambda: controller.show_frame("StartPage"))
        buttonRoll = tk.Button(self, text = "Roll", height = "3", width = "14", command = lambda: self.rollupdate())
        buttonScoreOnes = tk.Button(self, text = "Ones", height = "3", width = "14", command = lambda: self.updateones())
        buttonScoreTwos = tk.Button(self, text = "Twos", height = "3", width = "14", command = lambda: self.updatetwos())
        buttonScoreThrees = tk.Button(self, text = "Threes", height = "3", width = "14", command = lambda: self.updatethrees())
        buttonScoreFours = tk.Button(self, text = "Fours", height = "3", width = "14", command = lambda: self.updatefours())
        buttonScoreFives = tk.Button(self, text = "Fives", height = "3", width = "14", command = lambda: self.updatefives())
        buttonScoreSixes = tk.Button(self, text = "Sixes", height = "3", width = "14", command = lambda: self.updatesixes())
        buttonScoreThreeOfAKind = tk.Button(self, text = "Three of a Kind", height = "3", width = "14", command = lambda: self.updatethreeofakind())
        buttonScoreFourOfAKind = tk.Button(self, text = "Four of a Kind", height = "3", width = "14", command = lambda: self.updatefourofakind())
        buttonScoreFullHouse = tk.Button(self, text = "Full House", height = "3", width = "14", command = lambda: self.updatefullhouse())
        buttonScoreSmallStraight = tk.Button(self, text = "Small Straight", height = "3", width = "14", command = lambda: self.updatesmallstraight())
        buttonScoreLargeStraight = tk.Button(self, text = "Large Straight", height = "3", width = "14", command = lambda: self.updatelargestraight())
        buttonScoreChance = tk.Button(self, text = "Chance", height = "3", width = "14", command = lambda: self.updatechance())
        buttonScoreYahtzee = tk.Button(self, text = "Yahtzee", height = "3", width = "14", command = lambda: self.updateyahtzee())



        buttonMain.grid(row = 1, column = 10)
        buttonRoll.grid(row = 0, column = 10)
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
    cow_count = 1
    cow = StringVar()
    dice1_count = 0
    dice1 = StringVar()
    dice2_count = 0
    dice2 = StringVar()
    dice3_count = 0
    dice3 = StringVar()
    dice4_count = 0
    dice4 = StringVar()
    dice5_count = 0
    dice5 = StringVar()
    onescount = 0
    ones = StringVar()
    twoscount = 0
    twos = StringVar()
    threescount = 0
    threes = StringVar()
    fourscount = 0
    fours = StringVar()
    fivescount = 0
    fives = StringVar()
    sixescount = 0
    sixes = StringVar()
    threeofakindcount = 0
    threeofakind = StringVar()
    fourofakindcount = 0
    fourofakind = StringVar()
    fullhousecount = 0
    fullhouse = StringVar()
    smallstraightcount = 0
    smallstraight = StringVar()
    largestraightcount = 0
    largestraight = StringVar()
    chancecount = 0
    chance = StringVar()
    yahtzeecount = 0
    yahtzee = StringVar()
    totalscorecount = 0
    totalscore = StringVar()
    totalscore.set(onescount + twoscount + threescount + fourscount + fivescount + sixescount + threeofakindcount + fourofakindcount + fullhousecount + smallstraightcount + largestraightcount + chancecount + yahtzeecount)

    def rollupdate(self):
        global mydice
        mydice = [0, 0, 0, 0, 0]
        mydice = mf.roll()
        self.dice1_count = mydice[0]
        self.dice1.set(self.dice1_count)
        self.dice2_count = mydice[1]
        self.dice2.set(self.dice2_count)
        self.dice3_count = mydice[2]
        self.dice3.set(self.dice3_count)
        self.dice4_count = mydice[3]
        self.dice4.set(self.dice4_count)
        self.dice5_count = mydice[4]
        self.dice5.set(self.dice5_count)

    def updateones(self):
        self.onescount = mf.aces(mydice)
        self.ones.set(self.onescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatetwos(self):
        self.twoscount = mf.twos(mydice)
        self.twos.set(self.twoscount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatethrees(self):
        self.threescount = mf.threes(mydice)
        self.threes.set(self.threescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefours(self):
        self.fourscount = mf.fours(mydice)
        self.fours.set(self.fourscount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefives(self):
        self.fivescount = mf.fives(mydice)
        self.fives.set(self.fivescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatesixes(self):
        self.sixescount = mf.sixes(mydice)
        self.sixes.set(self.sixescount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatethreeofakind(self):
        self.threeofakindcount = mf.threeofakind(mydice)
        self.threeofakind.set(self.threeofakindcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefourofakind(self):
        self.fourofakindcount = mf.fourofakind(mydice)
        self.fourofakind.set(self.fourofakindcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatefullhouse(self):
        self.fullhousecount = mf.fullhouse(mydice)
        self.fullhouse.set(self.fullhousecount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatesmallstraight(self):
        self.smallstraightcount = mf.smallstraight(mydice)
        self.smallstraight.set(self.smallstraightcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatelargestraight(self):
        self.largestraightcount = mf.largestraight(mydice)
        self.largestraight.set(self.largestraightcount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatechance(self):
        self.chancecount = mf.chance(mydice)
        self.chance.set(self.chancecount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updateyahtzee(self):
        self.yahtzeecount = mf.yahtzee(mydice)
        self.yahtzee.set(self.yahtzeecount)
        self.totalscore.set(
            self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def cowplus(self):
        self.cow_count += 1
        self.cow.set(self.cow_count)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.cow_count = 1
        self.cow.set(self.cow_count)

        dice1label = tk.Label(self, textvariable=self.dice1, width="14")
        dice1label.grid(row=0, column=0)
        dice2label = tk.Label(self, textvariable=self.dice2, width="14")
        dice2label.grid(row=0, column=1)
        dice3label = tk.Label(self, textvariable=self.dice3, width="14")
        dice3label.grid(row=0, column=2)
        dice4label = tk.Label(self, textvariable=self.dice4, width="14")
        dice4label.grid(row=0, column=3)
        dice5label = tk.Label(self, textvariable=self.dice5, width="14")
        dice5label.grid(row=0, column=4)
        spacelabel = tk.Label(self, text="", width="83")
        spacelabel.grid(row=1, column=9)
        oneslabel = tk.Label(self, textvariable=self.ones, width="14")
        oneslabel.grid(row=2, column=1)
        oneslabel = tk.Label(self, textvariable=self.twos, width="14")
        oneslabel.grid(row=3, column=1)
        oneslabel = tk.Label(self, textvariable=self.threes, width="14")
        oneslabel.grid(row=4, column=1)
        oneslabel = tk.Label(self, textvariable=self.fours, width="14")
        oneslabel.grid(row=5, column=1)
        oneslabel = tk.Label(self, textvariable=self.fives, width="14")
        oneslabel.grid(row=6, column=1)
        oneslabel = tk.Label(self, textvariable=self.sixes, width="14")
        oneslabel.grid(row=7, column=1)
        oneslabel = tk.Label(self, textvariable=self.threeofakind, width="14")
        oneslabel.grid(row=8, column=1)
        oneslabel = tk.Label(self, textvariable=self.fourofakind, width="14")
        oneslabel.grid(row=9, column=1)
        oneslabel = tk.Label(self, textvariable=self.fullhouse, width="14")
        oneslabel.grid(row=10, column=1)
        oneslabel = tk.Label(self, textvariable=self.smallstraight, width="14")
        oneslabel.grid(row=11, column=1)
        oneslabel = tk.Label(self, textvariable=self.largestraight, width="14")
        oneslabel.grid(row=12, column=1)
        oneslabel = tk.Label(self, textvariable=self.chance, width="14")
        oneslabel.grid(row=13, column=1)
        oneslabel = tk.Label(self, textvariable=self.yahtzee, width="14")
        oneslabel.grid(row=14, column=1)
        totalscorelabel = tk.Label(self, text="Your Total Score Is: ")
        totalscorelabel.grid(row=14, column=4)
        totalscorelabel = tk.Label(self, textvariable=self.totalscore)
        totalscorelabel.grid(row=14, column=5)

        label = tk.Label(self, text="Select a Section", font=5)
        label.grid(row=1, column=0)

        buttonMain = tk.Button(self, text="Main Menu", height="3", width="14",
                               command=lambda: controller.show_frame("StartPage"))
        buttonRoll = tk.Button(self, text="Roll", height="3", width="14", command=lambda: self.rollupdate())
        buttonScoreOnes = tk.Button(self, text="Ones", height="3", width="14", command=lambda: self.updateones())
        buttonScoreTwos = tk.Button(self, text="Twos", height="3", width="14", command=lambda: self.updatetwos())
        buttonScoreThrees = tk.Button(self, text="Threes", height="3", width="14", command=lambda: self.updatethrees())
        buttonScoreFours = tk.Button(self, text="Fours", height="3", width="14", command=lambda: self.updatefours())
        buttonScoreFives = tk.Button(self, text="Fives", height="3", width="14", command=lambda: self.updatefives())
        buttonScoreSixes = tk.Button(self, text="Sixes", height="3", width="14", command=lambda: self.updatesixes())
        buttonScoreThreeOfAKind = tk.Button(self, text="Three of a Kind", height="3", width="14",
                                            command=lambda: self.updatethreeofakind())
        buttonScoreFourOfAKind = tk.Button(self, text="Four of a Kind", height="3", width="14",
                                           command=lambda: self.updatefourofakind())
        buttonScoreFullHouse = tk.Button(self, text="Full House", height="3", width="14",
                                         command=lambda: self.updatefullhouse())
        buttonScoreSmallStraight = tk.Button(self, text="Small Straight", height="3", width="14",
                                             command=lambda: self.updatesmallstraight())
        buttonScoreLargeStraight = tk.Button(self, text="Large Straight", height="3", width="14",
                                             command=lambda: self.updatelargestraight())
        buttonScoreChance = tk.Button(self, text="Chance", height="3", width="14", command=lambda: self.updatechance())
        buttonScoreYahtzee = tk.Button(self, text="Yahtzee", height="3", width="14",
                                       command=lambda: self.updateyahtzee())

        buttonMain.grid(row=1, column=10)
        buttonRoll.grid(row=0, column=10)
        buttonScoreOnes.grid(row=2, column=0)
        buttonScoreTwos.grid(row=3, column=0)
        buttonScoreThrees.grid(row=4, column=0)
        buttonScoreFours.grid(row=5, column=0)
        buttonScoreFives.grid(row=6, column=0)
        buttonScoreSixes.grid(row=7, column=0)
        buttonScoreThreeOfAKind.grid(row=8, column=0)
        buttonScoreFourOfAKind.grid(row=9, column=0)
        buttonScoreFullHouse.grid(row=10, column=0)
        buttonScoreSmallStraight.grid(row=11, column=0)
        buttonScoreLargeStraight.grid(row=12, column=0)
        buttonScoreChance.grid(row=13, column=0)
        buttonScoreYahtzee.grid(row=14, column=0)

class PageThree(tk.Frame):
    cow_count = 1
    cow = StringVar()
    dice1_count = 0
    dice1 = StringVar()
    dice2_count = 0
    dice2 = StringVar()
    dice3_count = 0
    dice3 = StringVar()
    dice4_count = 0
    dice4 = StringVar()
    dice5_count = 0
    dice5 = StringVar()
    onescount = 0
    ones = StringVar()
    twoscount = 0
    twos = StringVar()
    threescount = 0
    threes = StringVar()
    fourscount = 0
    fours = StringVar()
    fivescount = 0
    fives = StringVar()
    sixescount = 0
    sixes = StringVar()
    threeofakindcount = 0
    threeofakind = StringVar()
    fourofakindcount = 0
    fourofakind = StringVar()
    fullhousecount = 0
    fullhouse = StringVar()
    smallstraightcount = 0
    smallstraight = StringVar()
    largestraightcount = 0
    largestraight = StringVar()
    chancecount = 0
    chance = StringVar()
    yahtzeecount = 0
    yahtzee = StringVar()
    bestmove = StringVar()
    totalscorecount = 0
    totalscore = StringVar()
    totalscore.set(onescount + twoscount + threescount + fourscount + fivescount + sixescount + threeofakindcount + fourofakindcount + fullhousecount + smallstraightcount + largestraightcount + chancecount + yahtzeecount)
    def rollupdate(self):
        global mydice
        mydice = [0, 0, 0, 0, 0]
        mydice = mf.roll()
        self.bestmove.set(mf.bestplays(mydice))
        print "{}".format(self.bestmove)
        self.dice1_count = mydice[0]
        self.dice1.set(self.dice1_count)
        self.dice2_count = mydice[1]
        self.dice2.set(self.dice2_count)
        self.dice3_count = mydice[2]
        self.dice3.set(self.dice3_count)
        self.dice4_count = mydice[3]
        self.dice4.set(self.dice4_count)
        self.dice5_count = mydice[4]
        self.dice5.set(self.dice5_count)

    def updateones(self):
        self.onescount = mf.aces(mydice)
        self.ones.set(self.onescount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)

    def updatetwos(self):
        self.twoscount = mf.twos(mydice)
        self.twos.set(self.twoscount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatethrees(self):
        self.threescount = mf.threes(mydice)
        self.threes.set(self.threescount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatefours(self):
        self.fourscount = mf.fours(mydice)
        self.fours.set(self.fourscount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatefives(self):
        self.fivescount = mf.fives(mydice)
        self.fives.set(self.fivescount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatesixes(self):
        self.sixescount = mf.sixes(mydice)
        self.sixes.set(self.sixescount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatethreeofakind(self):
        self.threeofakindcount = mf.threeofakind(mydice)
        self.threeofakind.set(self.threeofakindcount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatefourofakind(self):
        self.fourofakindcount = mf.fourofakind(mydice)
        self.fourofakind.set(self.fourofakindcount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatefullhouse(self):
        self.fullhousecount = mf.fullhouse(mydice)
        self.fullhouse.set(self.fullhousecount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatesmallstraight(self):
        self.smallstraightcount = mf.smallstraight(mydice)
        self.smallstraight.set(self.smallstraightcount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatelargestraight(self):
        self.largestraightcount = mf.largestraight(mydice)
        self.largestraight.set(self.largestraightcount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updatechance(self):
        self.chancecount = mf.chance(mydice)
        self.chance.set(self.chancecount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def updateyahtzee(self):
        self.yahtzeecount = mf.yahtzee(mydice)
        self.yahtzee.set(self.yahtzeecount)
        self.totalscore.set(self.onescount + self.twoscount + self.threescount + self.fourscount + self.fivescount + self.sixescount + self.threeofakindcount + self.fourofakindcount + self.fullhousecount + self.smallstraightcount + self.largestraightcount + self.chancecount + self.yahtzeecount)
    def cowplus(self):
        self.cow_count += 1
        self.cow.set(self.cow_count)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.cow_count = 1
        self.cow.set(self.cow_count)

        dice1label = tk.Label(self, textvariable=self.dice1, width="14")
        dice1label.grid(row=0, column=0)
        dice2label = tk.Label(self, textvariable=self.dice2, width="14")
        dice2label.grid(row=0, column=1)
        dice3label = tk.Label(self, textvariable=self.dice3, width="14")
        dice3label.grid(row=0, column=2)
        dice4label = tk.Label(self, textvariable=self.dice4, width="14")
        dice4label.grid(row=0, column=3)
        dice5label = tk.Label(self, textvariable=self.dice5, width="14")
        dice5label.grid(row=0, column=4)
        spacelabel = tk.Label(self, text="", width="83")
        spacelabel.grid(row=1, column=9)
        oneslabel = tk.Label(self, textvariable=self.ones, width="14")
        oneslabel.grid(row=2, column=1)
        oneslabel = tk.Label(self, textvariable=self.twos, width="14")
        oneslabel.grid(row=3, column=1)
        oneslabel = tk.Label(self, textvariable=self.threes, width="14")
        oneslabel.grid(row=4, column=1)
        oneslabel = tk.Label(self, textvariable=self.fours, width="14")
        oneslabel.grid(row=5, column=1)
        oneslabel = tk.Label(self, textvariable=self.fives, width="14")
        oneslabel.grid(row=6, column=1)
        oneslabel = tk.Label(self, textvariable=self.sixes, width="14")
        oneslabel.grid(row=7, column=1)
        oneslabel = tk.Label(self, textvariable=self.threeofakind, width="14")
        oneslabel.grid(row=8, column=1)
        oneslabel = tk.Label(self, textvariable=self.fourofakind, width="14")
        oneslabel.grid(row=9, column=1)
        oneslabel = tk.Label(self, textvariable=self.fullhouse, width="14")
        oneslabel.grid(row=10, column=1)
        oneslabel = tk.Label(self, textvariable=self.smallstraight, width="14")
        oneslabel.grid(row=11, column=1)
        oneslabel = tk.Label(self, textvariable=self.largestraight, width="14")
        oneslabel.grid(row=12, column=1)
        oneslabel = tk.Label(self, textvariable=self.chance, width="14")
        oneslabel.grid(row=13, column=1)
        oneslabel = tk.Label(self, textvariable=self.yahtzee, width="14")
        oneslabel.grid(row=14, column=1)
        bestmoveslabel = tk.Label(self, text="Your Best Move Is: ")
        bestmoveslabel.grid(row=14, column=2)
        bestmoveslabel = tk.Label(self, textvariable=self.bestmove)
        bestmoveslabel.grid(row=14, column=3)
        totalscorelabel = tk.Label(self, text="Your Total Score Is: ")
        totalscorelabel.grid(row=14, column=4)
        totalscorelabel = tk.Label(self, textvariable=self.totalscore)
        totalscorelabel.grid(row=14, column=5)


        label = tk.Label(self, text="Select a Section", font=5)
        label.grid(row=1, column=0)

        buttonMain = tk.Button(self, text="Main Menu", height="3", width="14",
                               command=lambda: controller.show_frame("StartPage"))
        buttonRoll = tk.Button(self, text="Roll", height="3", width="14", command=lambda: self.rollupdate())
        buttonScoreOnes = tk.Button(self, text="Ones", height="3", width="14", command=lambda: self.updateones())
        buttonScoreTwos = tk.Button(self, text="Twos", height="3", width="14", command=lambda: self.updatetwos())
        buttonScoreThrees = tk.Button(self, text="Threes", height="3", width="14", command=lambda: self.updatethrees())
        buttonScoreFours = tk.Button(self, text="Fours", height="3", width="14", command=lambda: self.updatefours())
        buttonScoreFives = tk.Button(self, text="Fives", height="3", width="14", command=lambda: self.updatefives())
        buttonScoreSixes = tk.Button(self, text="Sixes", height="3", width="14", command=lambda: self.updatesixes())
        buttonScoreThreeOfAKind = tk.Button(self, text="Three of a Kind", height="3", width="14",
                                            command=lambda: self.updatethreeofakind())
        buttonScoreFourOfAKind = tk.Button(self, text="Four of a Kind", height="3", width="14",
                                           command=lambda: self.updatefourofakind())
        buttonScoreFullHouse = tk.Button(self, text="Full House", height="3", width="14",
                                         command=lambda: self.updatefullhouse())
        buttonScoreSmallStraight = tk.Button(self, text="Small Straight", height="3", width="14",
                                             command=lambda: self.updatesmallstraight())
        buttonScoreLargeStraight = tk.Button(self, text="Large Straight", height="3", width="14",
                                             command=lambda: self.updatelargestraight())
        buttonScoreChance = tk.Button(self, text="Chance", height="3", width="14", command=lambda: self.updatechance())
        buttonScoreYahtzee = tk.Button(self, text="Yahtzee", height="3", width="14",
                                       command=lambda: self.updateyahtzee())

        buttonMain.grid(row=1, column=10)
        buttonRoll.grid(row=0, column=10)
        buttonScoreOnes.grid(row=2, column=0)
        buttonScoreTwos.grid(row=3, column=0)
        buttonScoreThrees.grid(row=4, column=0)
        buttonScoreFours.grid(row=5, column=0)
        buttonScoreFives.grid(row=6, column=0)
        buttonScoreSixes.grid(row=7, column=0)
        buttonScoreThreeOfAKind.grid(row=8, column=0)
        buttonScoreFourOfAKind.grid(row=9, column=0)
        buttonScoreFullHouse.grid(row=10, column=0)
        buttonScoreSmallStraight.grid(row=11, column=0)
        buttonScoreLargeStraight.grid(row=12, column=0)
        buttonScoreChance.grid(row=13, column=0)
        buttonScoreYahtzee.grid(row=14, column=0)

if __name__ == "__main__":
    app = SampleApp()
    app.title("Botzee")
    app.destroy()
    app.mainloop()
