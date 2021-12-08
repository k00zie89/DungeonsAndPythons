import sys
from datetime import datetime
from random import randrange

from DiceRoll import DiceRoller
from Encounter import Encounter, Participant
from Killables import Monster, Player
from MonsterLibrary import MonsterLibrary


def main():
    fileNameString = sys.argv[1]
    # players = readPlayerFile(str('./players_test.txt'))
    players = readPlayerFile(str(fileNameString))
    print('Welcome to the rice-fields motherfucker')
    gameOn = True
    while gameOn:
        gameOn = mainMenu(gameOn, players)
    
def mainMenu(gameOn, players):
    print('0.) Print Player Info')
    print('1.) Start Encounter')
    print('2.) Roll a DXX')
    print('3.) Heal ALL Players (long rest)')
    print('4.) Heal Individual Player')
    print('5.) Add New Player Manually')
    print('6.) Exit Game')
    
    choice = input('---> ')
    if   choice == '0': # print player info
        printPlayerInfo(players)
    elif choice == '1': # begin encounter...
        theEncounter = setupEncounter(players)
        theEncounter.runEncounter(players)
    elif choice == '2': # roll dice
        roller = DiceRoller()
        print('What kind of dice to roll?')
        done = False
        while done == False:
            choice = input('----------> ')
            if choice in ('4', '6', '8', '10', '12', '20', '100'):
                intChoice = int(choice)
                result = roller.roll(intChoice)
                print(f'--- Rolled a {result} ---')
                done = True
            else:
                print('Try again...')  
    elif choice == '3': # long rest / heal all players...
        for p in players:
            p.hp = p.currentHealth
            print(f'Player {p.name} healed to {p.currentHealth} HP.')    
    elif choice == '4': # heal individual player
        print('Which player to heal?')
        playersPrinted = 0
        for p in players: # list
            print(f'{playersPrinted}.) {p.name}')
            playersPrinted += 1
        validChoice = False
        while validChoice == False: # who?
            choice = input('---> ')
            try:
                intChoice = int(choice)
                if intChoice >= 0 & intChoice < playersPrinted:
                    print(f'Player {players[intChoice].name} chosen.')
                    validChoice = True
                else:
                    print('Choice out of range.')                
            except:
                print('Invalid entry.')
        validSecondChoice = False
        while validSecondChoice == False: # how much?
            amount = input('By how much? \n---> ')
            try:
                intAmount = int(amount)
                if intAmount >= 0:
                    players[intChoice].currentHealth += intAmount
                    validSecondChoice = True
                    print(f'Healing {players[intChoice].name} by {intAmount}')
                else:
                    print('Need a non-negative amount...')
            except:
                print('Invalid entry. Integer, please...')
    elif choice == '5': # add player manually
        newPlayer = addPlayerManually()
        if newPlayer != None:
            players.append(newPlayer)
            print(f'Player {newPlayer.name} added to the session.')
        else:
            print('Something went wrong.')
        
    elif choice == '6': # end session
        print('Goodbye...')
        writePlayerFile(players)
        gameOn = False
    # room for extra options.........

    else:
        print('Invalid menu choice')
    
    return gameOn
    
def readPlayerFile(filename):
    print('Reading player file....')
    players = []
    with open(filename, 'r') as file:
        for line in file:
            wordCount = 0
            for word in line.split():
                # process word in line
                if   wordCount == 0:
                    pName = word
                elif wordCount == 1:
                    cName = word
                elif wordCount == 2:
                    cRace = word
                elif wordCount == 3:
                    cClass = word
                elif wordCount == 4:
                    cAlignment = word
                elif wordCount == 5:
                    cMaxHealth = int(word)
                elif wordCount == 6:
                    cCurrentHealth = int(word)
                elif wordCount == 7:
                    cArmorClass = int(word)
                elif wordCount == 8:
                    cMoveSpeed = int(word)
                wordCount += 1
            newPlayer = Player(pName,
                               cName,
                               cRace,
                               cClass,
                               cAlignment,
                               cMaxHealth,
                               cCurrentHealth,
                               cArmorClass,
                               cMoveSpeed)
            players.append(newPlayer)
        print("Successful.")    
    return players
    
def writePlayerFile(players):
    print('Saving player data...')
    theTime = datetime.now()
    fileNameString = 'players_' + theTime.strftime("%m.%d_%H.%M")
    print(fileNameString)
    playerData = []
    for p in players:
        playerDataLine = p.pName+' '+p.name+' '+p.cRace+' '+p.cClass+' '+p.cAlignment+' '+str(p.hp)+' '+str(p.currentHealth)+' '+str(p.ac)+' '+str(p.speed)+'\n'
        playerData.append(playerDataLine)
    print(f'Saving player data to file {fileNameString}')
    writtenFile = open(str(fileNameString), 'a')
    writtenFile.writelines(playerData)
    writtenFile.close()

def addPlayerManually():
    print('Wow, much player; such roleplay.')
    c0 = input('Player name: ')
    c1 = input('Character name: ')
    c2 = input('Race: ')
    c3 = input('Class: ')
    c4 = input('Alignment: ')
    c5 = input('Max Health: ')
    c6 = input('Current Health: ')
    c7 = input('Armor Class: ')
    c8 = input('Move Speed: ')
    try:
        thePlayer = Player(c0, c1, c2, c3, c4, int(c5), int(c6), int(c7), int(c8))
        return thePlayer
    except:
        print('Invalid integers for Max / Current Health, Armor Class, or Move Speed')

def printPlayerInfo(players):
    for p in players:
        playerInfoStr =  '-------'             + p.pName.upper() + '-------'
        playerInfoStr += '\n CharacterName: '  + p.name
        playerInfoStr += '\n Race: '           + p.cRace
        playerInfoStr += '\n Class: '          + p.cClass
        playerInfoStr += '\n Alignment: '      + p.cAlignment
        playerInfoStr += '\n Max Health: '     + str(p.hp)
        playerInfoStr += '\n Current Health: ' + str(p.currentHealth)
        playerInfoStr += '\n Armor Class: '    + str(p.ac)
        playerInfoStr += '\n Speed: '          + str(p.speed)
        
        print(playerInfoStr)
    
def setupEncounter(players):
    print('Which players are participating?')
    stillAddingPlayers = True
    participantList    = []
    playersNotYetAdded = []
    for n in players:
        playersNotYetAdded.append(n)
    while stillAddingPlayers:
        currentIndex = 0
        for p in playersNotYetAdded:
            theString  = str(playersNotYetAdded.index(p))
            theString += '.) ' + p.name
            print(theString)
            currentIndex += 1
        print(f'{currentIndex}.) Add ALL Players')
        print(f'{currentIndex + 1}.) Done Adding Players')
        validChoice = False
        while validChoice == False:
            choice = input('---> ')
            try:
                intChoice = int(choice)
                if intChoice in range(currentIndex):
                    validChoice = True
                    chosenPlayer = playersNotYetAdded[intChoice]
                    playersInitiative = input('What is the player\'s initiative? ')
                    validInteger = False
                    while validInteger == False:
                        try:
                            intInitiative = int(playersInitiative)
                            validInteger = True
                        except:
                            print('Invalid choice. Enter an integer. ')
                            playersInitiative = input('What is the player\'s initiative? ')
                    newParticipant = Participant(chosenPlayer, intInitiative)
                    participantList.append(newParticipant)
                    playersNotYetAdded.remove(chosenPlayer)
                elif intChoice == currentIndex:
                    print('Adding all players to encounter...')
                    validChoice = True
                    for p in playersNotYetAdded:
                        playersInitiative = input(f'What is {p.name}\'s initiative? ')
                        validInteger = False
                        while validInteger == False:
                            try:
                                intInitiative = int(playersInitiative)
                                validInteger = True
                            except:
                                print('Invalid choice. Enter an integer. ')
                                players = input(f'What is {p.name}\'s initiative? ')
                        newParticipant = Participant(p, intInitiative)
                        participantList.append(newParticipant)
                    stillAddingPlayers = False
                elif intChoice == (currentIndex + 1):
                    if len(participantList) < 1:
                        print('Must have at least one player added...')
                    else:
                        print('Done adding players...')
                        validChoice = True
                        stillAddingPlayers = False
                        validInteger = True
                else:
                    print('Invalid selection. Pick pick a listed player. ')
            except:
                print('Invalid entry, please enter an integer... ')
        
        if len(playersNotYetAdded) < 1:
            print('All players have been added.')
            stillAddingPlayers = False
            
    print('Moving on with encounter setup...')
    
    goodChoice = False
    while goodChoice == False:
        print('1.) FOREST')
        print('2.) WATER')
        print('3.) DESERT')
        print('4.) TOWN')
        print('5.) ANY')
        choice = input('Where is the encounter taking place?: ')
        if choice in ['1', '2', '3', '4', '5']:
            goodChoice = True
            if choice == '1':
                print('Environment FOREST chosen.')
                envStr = 'FOREST'
            if choice == '2':
                print('Environment WATER chosen.')
                envStr = 'WATER'
            if choice == '3':
                print('Environment DESERT chosen.')
                envStr = 'DESERT'
            if choice == '4':
                print('Environment TOWN chosen.')
                envStr = 'TOWN'
            if choice == '5':
                print('Environment deemed irrelevant.')
                envStr = 'ANY'
        else:
            print('Invalid choice, try again...')
    
    validEntry = False
    while validEntry == False:
        challengeRating = input('What is the difficulty of the encounter? ')
        try:
            intChallengeRating = float(challengeRating)
            if intChallengeRating >= 0:
                validEntry = True
            else:
                print("Need a non-negative value.")
        except:
            print("Must be a number.")
    
    validEntry = False
    while validEntry == False:
        monstersToAdd = input('How many monsters to add?: ')    
        try:
            intMonstersToAdd = int(monstersToAdd)
            if intMonstersToAdd > 0:
                validEntry = True
            else:
                print('Need at least one monster...')
        except:
            print('Please enter an integer.')
    monstersAdded = []
    validEntry = False
    while validEntry == False:
        print('1.) Choose Monster from Library')
        print('2.) Add Random Monster')
        choice = input('---> ')
        if choice in ['1', '2']:
            validEntry = True
            lib = MonsterLibrary()
            while len(monstersAdded) < intMonstersToAdd:
                print(f'Monsters Added: {len(monstersAdded)}')
                print(f'Monsters Remaining to add: {intMonstersToAdd-len(monstersAdded)}')
                if choice == '1':
                    print('Choose from the list below...')
                    lib.printMonsterList(intChallengeRating)
                    validChoice = False
                    while validChoice == False:
                        monsterChoice = input('---> ')
                        monsterChoice = monsterChoice.upper()
                        try:
                            for i, m in lib.monsterLibrary.items():
                                if monsterChoice == i:
                                    validChoice = True
                                    break
                            if validChoice == False:
                                print('Monster not found. Try again.')
                            else:
                                newMonster = lib.chooseMonster(monsterChoice)
                                if newMonster.mChallengeRating <= intChallengeRating:
                                    validMonster = lib.checkMonsterEnvironment(envStr, newMonster)
                                    if validMonster:
                                        print(f'Creating monster - {newMonster.name}...')
                                        monstersAdded.append(newMonster)
                                    else:
                                        print('Monster cannot be added to this encounter (due to environment)')
                                else:
                                    print("Monster chosen is too difficult.")
                        except:
                            print('Invalid entry, select key from list...')
                    if len(monstersAdded) >= intMonstersToAdd:
                        break
                    print(f'Monsters Added: {len(monstersAdded)}')
                    print(f'Monsters Remaining to add: {intMonstersToAdd-len(monstersAdded)}')
                    choice = input('1.) Choose Monster from Library \n2.) Add Random Monster \n---> ')
                if choice == '2':
                    print('Choosing random monsters...')
                    validMonster = False
                    while validMonster == False:
                        newMonster   = lib.addRandomMonster()
                        validMonster = lib.checkMonsterEnvironment(envStr, newMonster)
                    monstersAdded.append(newMonster)
                    if len(monstersAdded) >= intMonstersToAdd:
                        break
                    print(f'Monsters Added: {len(monstersAdded)}')
                    print(f'Monsters Remaining to add: {intMonstersToAdd-len(monstersAdded)}')
                    choice = input('1.) Choose Monster from Library \n2.) Add Random Monster \n---> ')
                if choice not in ['1', '2']:
                    print('Invalid Selection, try again...')
                    print(f'Monsters Added: {len(monstersAdded)}')
                    print(f'Monsters Remaining to add: {intMonstersToAdd-len(monstersAdded)}')
                    choice = input('1.) Choose Monster from Library \n2.) Add Random Monster \n---> ')
        else:
            print('Invalid selection. Try again...')
        for m in monstersAdded:
            init = m.rollInitiative()
            newParticipant = Participant(m, init)
            participantList.append(newParticipant)
            
    theEncounter = Encounter(participantList, envStr)
    return theEncounter
        

if __name__ == '__main__': main()
