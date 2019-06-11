from pip._vendor.distlib.compat import raw_input

numOfWins = 0

with open("C:\\Users\\yaakov\\Documents\\mco 141\\WorldSeriesWinners.txt") as file:
    wSWinners = list(file)
team = raw_input("select a team\n")
type(team)
for x in range(wSWinners.__len__()):
    if team.lower() == (wSWinners[x].lower().strip()):
        numOfWins += 1
print("the " + team + " have won the world series  {}  times\n".format(numOfWins))
