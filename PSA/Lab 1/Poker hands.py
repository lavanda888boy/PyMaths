# we use the "treys" library to import the tools to work with evaluating poker hands
from treys import Card, Evaluator


# variables for counting each player's wins
wins1 = 0
wins2 = 0
e = Evaluator()

# reading poker hands from the given file
try:
    pokerHands = open('poker.txt', 'r')
    for line in pokerHands:
        player1Hand = list()
        player1Board = list()
        player2Hand = list()
        player2Board = list()

        player1Board.append(Card.new(line[0] + line[1].lower()))
        player1Board.append(Card.new(line[3] + line[4].lower()))
        player1Board.append(Card.new(line[6] + line[7].lower()))
        player1Hand.append(Card.new(line[9] + line[10].lower()))
        player1Hand.append(Card.new(line[12] + line[13].lower()))

        player2Board.append(Card.new(line[15] + line[16].lower()))
        player2Board.append(Card.new(line[18] + line[19].lower()))
        player2Board.append(Card.new(line[21] + line[22].lower()))
        player2Hand.append(Card.new(line[24] + line[25].lower()))
        player2Hand.append(Card.new(line[27] + line[28].lower()))

        if e.evaluate(player1Board, player1Hand) < e.evaluate(player2Board, player2Hand):
            wins1 += 1
        else:
            wins2 += 1
except Exception as e:
    print(e)
finally:
    pokerHands.close()


# printing the results
print(f"The 1-st player won {wins1} times")
print(f"The 2-nd player won {wins2} times")
