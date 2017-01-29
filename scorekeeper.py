class scoreboard:
    def initGame(self):
        start = input('Would you like to start a new game?(y/n)')
        if start == "y":
            print ("Ready to go")
 
    def players(self): 
        player1 = input("Enter the name of Player 1:")
        player2 = input("Enter the name of Player 2:") 
        print ("Thank you," + player1 + " will face " + player2)

    def addTally(self):
        scores = [0, 0]
        maxScore = 21
        while True:
            tally = input('Who scored?(p1/p2)')
            if tally == 'p1':
               scores[0] += 1
            if tally == 'p2':
               scores[1] +=1 
            if scores[0] == maxScore:
               print ('player 1 is the winner')
               break
            if scores[1] == maxScore:
               print ('player 2 is the winner')                 
            break


scoreboard.initGame('self')
scoreboard.players('self')
scoreboard.addTally('self')
