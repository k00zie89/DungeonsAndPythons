from Killables import Player, Monster
from DiceRoll  import DiceRoller
from MonsterLibrary import MonsterLibrary

class Participant:
    def __init__(self,
                 killableDude,
                 initiative):
        self.dude = killableDude
        self.init = initiative

class Encounter:
    
    lib = MonsterLibrary()
    
    def __init__(self,
                 participants,
                 environment):
        self.participants = participants
        self.environment  = environment
        
        print('finish setup...')
        # get monster data
        # sort all by initiative
        
    def displayCombatMenu(self):
        validChoice = False
        choice = 0
        print('--- COMBAT MENU ---')
        print('1.) Display Participant Info: ')
        print('2.) Start Turn: ')
        print('3.) Harm Participant ')
        print('4.) Heal Participant ')
        print('5.) Add Player to Encounter ')
        print('6.) Initiate 3rd Party Attack ')
        print('7.) Disengage Combat: ')
        while validChoice == False:
            choice = input('---> ')
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                validChoice = True
            else:
                print('Invalid choice, try again...')
        return int(choice)
        
    def runEncounter(self, players):
        ongoing = True
        monstersRemaining = True
        playersRemaining  = True
        playersNotFighting = []
        for player in players:
            playerInFight = False
            for participant in self.participants:
                if player.name == participant.dude.name:
                    playerInFight = True
            if playerInFight == False:
                playersNotFighting.append(player)
             
        self.participants = self.sortParticipants(True) # verbose TRUE for initial sorting
        while ongoing & monstersRemaining & playersRemaining:
            self.participants = self.sortParticipants(False)
            choice = self.displayCombatMenu()
            if   choice == 1: # display participants
                print('Displaying participant info...')
                self.displayParticipantInfo()
            elif choice == 2: # initiate round of combat
                print('Starting round of combat...')
                # Participant's turn...
                for p in self.participants:
                    print(f'{p.dude.name}\'s turn...')
                    if p.dude.currentHealth > 0: # normal turn
                        stillGoing = True
                        while stillGoing == True:
                            action = self.displayTurnMenu(p.dude)
                            if   action == 1: # attack stuff
                                if   isinstance(p.dude, Player):
                                    self.playerAttack(p.dude)
                                elif isinstance(p.dude, Monster):
                                    p.dude.printAbilities()
                                    p.dude.attack(self.participants)
                            elif action == 2: # end turn
                                print('Ending Turn...')
                                stillGoing = False
                            elif action == 3: # print participants with hp and ac
                                for m in self.participants:
                                    outStr = ''
                                    outStr += m.dude.name + ' - HP: '
                                    outStr += str(m.dude.currentHealth) + ' - AC: '
                                    outStr += str(m.dude.ac)
                                    print(outStr)
                            elif action == 4: # heal participant
                                for m in self.participants:
                                    print(f'{self.participants.index(m)}.) {m.dude.name} - Current Health: {m.dude.currentHealth}')
                                print('Which participant to heal?')
                                validChoice = False
                                while validChoice == False:
                                    choice = input('---> ')
                                    try:
                                        intChoice = int(choice)
                                        if intChoice in range(len(self.participants)+1):
                                            print(f'Healing participant {self.participants[intChoice].dude.name}')
                                            validChoice = True
                                    except:
                                        print('Invalid choice...select an integer from the table.')
                                validSecondChoice = False
                                while validSecondChoice == False:
                                    print('How much HP to restore?')
                                    secondChoice = input('---> ')
                                    try:
                                        intSecondChoice = int(secondChoice)
                                        if intSecondChoice >= 0:
                                            print(f'Healing participant by {intSecondChoice}...')
                                            self.participants[intChoice].dude.currentHealth += intSecondChoice
                                            validSecondChoice = True
                                        else:
                                            print('Must heal by zero or greater HP')
                                    except:
                                        print('Invalid entry. Positive integer please. ')
                                print(f'{self.participants[intChoice].dude.name}\'s health is now {self.participants[intChoice].dude.currentHealth} out of {self.participants[intChoice].dude.hp}')
                            elif action == 5: # harm participant
                                for p in self.participants:
                                    print(f'{self.participants.index(p)}.) {p.dude.name} - Current Health: {p.dude.currentHealth}')
                                print('Which participant to HARM?')
                                validChoice = False
                                while validChoice == False:
                                    choice = input('---> ')
                                    try:
                                        intChoice = int(choice)
                                        if intChoice in range(len(self.participants)+1):
                                            print(f'Harming participant {self.participants[intChoice].dude.name}')
                                            validChoice = True
                                    except:
                                        print('Invalid choice...select an integer from the table.')
                                validSecondChoice = False
                                while validSecondChoice == False:
                                    print('How much pain to inflict?')
                                    secondChoice = input('---> ')
                                    try:
                                        intSecondChoice = int(secondChoice)
                                        if intSecondChoice >= 0:
                                            print(f'Harming participant by {intSecondChoice}...')
                                            self.participants[intChoice].dude.currentHealth -= intSecondChoice
                                            validSecondChoice = True
                                        else:
                                            print('Must KILL by zero or greater HP')
                                    except:
                                        print('Invalid entry. Positive integer please. ')
                                print(f'{self.participants[intChoice].dude.name}\'s health is now {self.participants[intChoice].dude.currentHealth} out of {self.participants[intChoice].dude.hp}')
                                if self.participants[intChoice].dude.currentHealth <= 0:
                                    print(f'{self.participants[intChoice].dude.name} is DEAD...make saving throws when prompted.')
                            elif action == 6: # add new monster
                                self.getMonster()
                            elif action == 7: # 3rd party attack (outside of turn)
                                print('Which participant is attacking?')
                                for m in self.participants:
                                    print(f'{self.participants.index(m)}.) {m.dude.name}')
                                    validChoice = False
                                while validChoice == False:
                                    choice = input('---> ')
                                    try:
                                        intChoice = int(choice)
                                        #if self.participants[intChoice].name:
                                        if intChoice in range(len(self.participants)+1):
                                            validChoice = True
                                            if isinstance(self.participants[intChoice].dude, Player):
                                                self.playerAttack(self.participants[intChoice].dude)
                                            elif isinstance(self.participants[intChoice].dude, Monster):
                                                self.participants[intChoice].dude.printAbilities()
                                                self.participants[intChoice].dude.attack(self.participants)
                                            else:
                                                print('unknown entity...WTF?')
                                        else:
                                            print('Invalid selection.')
                                    except:
                                        print('Please enter an integer or unfuck something else')
                    else: # death save time...
                        print('Roll a death save...')
                        validDeathSave = False
                        while validDeathSave == False:
                            deathSave = input('---> ')
                            try:
                                intDeathSave = int(deathSave)
                                if intDeathSave == 100:
                                    p.dude.deathSavesPassed += 2
                                elif intDeathSave >= 10:
                                    p.dude.deathSavesPassed += 1
                                elif intDeathSave == 1:
                                    p.dude.deathSavesFailed += 2
                                else:
                                    p.dude.deathSavesFailed += 1
                                validDeathSave = True
                            except:
                                print('Invalid entry; please enter an integer.')
                        if p.dude.deathSavesFailed >= 3:
                            print('You dead, homie.')
                            print(f'Removing {p.dude.name} from participant list...')
                            self.participants.remove(p)
                        elif p.dude.deathSavesPassed >= 3:
                            print('You have avoided the icy grip of death.')
                            roller = DiceRoller()
                            amount = roller.roll(6)
                            print(f'Healing {p.dude.name} to {amount} HP...')
                            p.dude.currentHealth = amount
            elif choice == 3: # fuck someone
                for p in self.participants:
                    print(f'{self.participants.index(p)}.) {p.dude.name} - Current Health: {p.dude.currentHealth}')
                print('Which participant to HARM?')
                validChoice = False
                while validChoice == False:
                    choice = input('---> ')
                    try:
                        intChoice = int(choice)
                        if intChoice in range(len(self.participants)+1):
                            print(f'Harming participant {self.participants[intChoice].dude.name}')
                        validChoice = True
                    except:
                        print('Invalid choice...select an integer from the table.')
                validSecondChoice = False
                while validSecondChoice == False:
                    print('How much pain to inflict?')
                    secondChoice = input('---> ')
                    try:
                        intSecondChoice = int(secondChoice)
                        if intSecondChoice >= 0:
                            print(f'Harming participant by {intSecondChoice}...')
                            self.participants[intChoice].dude.currentHealth -= intSecondChoice
                            validSecondChoice = True
                        else:
                            print('Must KILL by zero or greater HP')
                    except:
                        print('Invalid entry. Positive integer please. ')
                print(f'{self.participants[intChoice].dude.name}\'s health is now {self.participants[intChoice].dude.currentHealth} out of {self.participants[intChoice].dude.hp}')
                if self.participants[intChoice].dude.currentHealth <= 0:
                    print(f'{self.participants[intChoice].dude.name} is DEAD...make saving throws when prompted.')
            elif choice == 4: # unfuck someone
                for p in self.participants:
                    print(f'{self.participants.index(p)}.) {p.dude.name} - Current Health: {p.dude.currentHealth}')
                print('Which participant to heal?')
                validChoice = False
                while validChoice == False:
                    choice = input('---> ')
                    try:
                        intChoice = int(choice)
                        if intChoice in range(len(self.participants)+1):
                            print(f'Healing participant {self.participants[intChoice].dude.name}')
                            validChoice = True
                    except:
                        print('Invalid choice...select an integer from the table.')
                validSecondChoice = False
                while validSecondChoice == False:
                    print('How much HP to restore?')
                    secondChoice = input('---> ')
                    try:
                        intSecondChoice = int(secondChoice)
                        if intSecondChoice >= 0:
                            print(f'Healing participant by {intSecondChoice}...')
                            self.participants[intChoice].dude.currentHealth += intSecondChoice
                            validSecondChoice = True
                        else:
                            print('Must heal by zero or greater HP')
                    except:
                        print('Invalid entry. Positive integer please. ')
                print(f'{self.participants[intChoice].dude.name}\'s health is now {self.participants[intChoice].dude.currentHealth} out of {self.participants[intChoice].dude.hp}') 
            elif choice == 5: # add non-combatant player to battle
                if len(playersNotFighting) < 1: # everybody's already here
                    print('All players are in combat; moving on.')
                else: # do it otherwise
                    playerNotFightingCount = 0
                    for pnf in playersNotFighting:
                        outString =  str(playerNotFightingCount)
                        outString += '.) ' + pnf.name
                        print(outString)
                        playerNotFightingCount += 1
                    validChoice = False
                    while validChoice == False:
                        choice = input('Which player to add to the fight?: ')
                        try:
                            intChoice = int(choice)
                            if   intChoice in range(playerNotFightingCount):
                                chosenPlayer = playersNotFighting[intChoice]
                                validChoice = True
                            else:
                                print('Selection out of range.')
                        except:
                            print('Invalid response. Please enter an integer...')
                    validInit = False
                    while validInit == False:
                        print(f'What is {chosenPlayer.name}\'s initiative?')
                        init = input('---> ')
                        try:
                            intInit = int(init)
                            newParticipant = Participant(chosenPlayer, intInit)
                            validInit = True
                        except:
                            print('Invalid response. Please enter an integer...')
                    if newParticipant.dude.name:
                        self.participants.append(newParticipant)
                        playersNotFighting.remove(chosenPlayer)
                        print(f'Player {newParticipant.dude.name} added to the battle.')
                    else:
                        print('Something went wrong...') 
                    self.participants = self.sortParticipants(True)               
            elif choice == 6: # let some fuck oneanother
                print('Which participant is attacking?')
                for m in self.participants:
                    print(f'{self.participants.index(m)}.) {m.dude.name}')
                    validChoice = False
                while validChoice == False:
                    choice = input('---> ')
                    try:
                        intChoice = int(choice)
                        #if self.participants[intChoice].name:
                        if intChoice in range(len(self.participants)+1):
                            validChoice = True
                            if isinstance(self.participants[intChoice].dude, Player):
                                self.playerAttack(self.participants[intChoice].dude)
                            elif isinstance(self.participants[intChoice].dude, Monster):
                                self.participants[intChoice].dude.printAbilities()
                                self.participants[intChoice].dude.attack(self.participants)
                            else:
                                print('unknown entity...WTF?')
                        else:
                            print('Invalid selection.')
                    except:
                        print('Please enter an integer or unfuck something else')
            elif choice == 7: # quit like a bitch
                ongoing = False
                print('Ending Encounter (pussy)...')
            else: # dumb menu choice
                print('Invalid menu choice encountered...unexpected condition.')
            # determine if monsters/players remain in the encounter
            monstersRemaining = False
            playersRemaining  = False
            monsterCount      = 0
            playerCount       = 0
            for el in self.participants:
                if el.dude.currentHealth > 0:
                    if isinstance(el.dude, Monster):
                        monstersRemaining = True
                        monsterCount += 1
                    elif isinstance(el.dude, Player):
                        playersRemaining = True
                        playerCount += 1
            print(f'There are {monsterCount} monsters and {playerCount} players left in the fight.')
            if monsterCount < 1:
                print('All monsters have been killed')
                input('Ending encounter...')
            if playerCount < 1:
                print('All players have been killed')
                input('Party wipe...')
        
    def sortParticipants(self, verbose):
        oldOrder = []
        newOrder = []
        if verbose: print('Initial Participant Ordering:')
        for p in self.participants:
            if verbose: print(f'{p.dude.name} - Initiative: {p.init}')
            oldOrder.append(p)
        while len(oldOrder) > 0:
            highestInitiative = 0
            for o in oldOrder:
                if o.init > highestInitiative:
                    nextParticipant = o
                    highestInitiative = o.init
            for n in newOrder:
                if n.dude.name == nextParticipant.dude.name:
                    nextParticipant.dude.name += '-x'
            newOrder.append(nextParticipant)
            oldOrder.remove(nextParticipant)
            if verbose: print(f'Participant {nextParticipant.dude.name} added to ordering...')
        return newOrder
        
    def displayTurnMenu(self, turntaker):
        print('What shall the player do?')
        print('1.) ATTACK')
        print('2.) Finish Turn')
        print('3.) DM CONTROL - Print current participants with health and AC')
        print('4.) DM CONTROL - Heal Participant')
        print('5.) DM CONTROL - Harm Participant')
        print('6.) DM CONTROL - Add New Monster')
        print('7.) DM CONTROL - Initiate 3rd Party Attack')
        validChoice = False
        while validChoice == False:
            choice = input('---> ')
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                intChoice = int(choice)
                validChoice = True
            else:
                print('Invalid selection. Try again.')
        return intChoice
        
    def displayParticipantInfo(self):
        for p in self.participants:
            if isinstance(p.dude, Player):
                print(f'{p.dude.name}.) AC: {p.dude.ac} - Current Health: {p.dude.currentHealth} - Initiative: {p.init}')
            elif isinstance(p.dude, Monster):
                print(f'{p.dude.name}.) AC: {p.dude.ac} - Current Health: {p.dude.currentHealth} - Initiative: {p.init}')
                for a in p.dude.mAbilities:
                    printStr = '----- ' + a
                    print(printStr)
            else:
                print('Non-Monster NPCs not yet implemented.')
    
    def getMonster(self):
        print('Which monster to add?')
        self.lib.printMonsterList()
        validChoice = False
        while validChoice == False:
            choice = input('---> ')
            try:
                intChoice = int(choice)
                if intChoice >= 0:
                    if intChoice < len(self.lib.monsterLibrary):
                        newMonster = self.lib.chooseMonster(intChoice)
                        validChoice = True
                        roller = DiceRoller()
                        monsterInitiative = roller.roll(20) + newMonster.mDex
                        newParticipant = Participant(newMonster, monsterInitiative)
                        self.participants.append(newParticipant)
                        self.sortParticipants(True)
                    else:
                        print('Choice too large; no such monster.')
                else:
                    print('No negative library indices, smartass...')
            except:
                print('Please enter an integer.')
        print(f'Monster {newMonster.name} added to the fight with initiative {newParticipant.init}')
    
    def getRandomMonster(self):
        print('Getting random monster from library')
        return self.lib.addRandomMonster()
    
    def playerAttack(self, attacker):
        print(f'{attacker.name}, WELCOME to your turn. Who you try\'na fuck with?')
        stillAttacking = True
        while stillAttacking:
            targetCount = 0
            listedParticipants = []
            for target in self.participants: # displaying names with indices for menu
                if target.dude.name in listedParticipants:
                    target.dude.name += '-x'
                    listedParticipants.append(target.dude.name)
                if target.dude.name != attacker.name:
                    print(f'{targetCount}.) {target.dude.name}')
                targetCount += 1
            print(f'{targetCount}.) Attack multiple targets')
            print(f'{targetCount+1}.) Finished Attacking')
            validChoice = False
            while validChoice == False: # choosing target
                choice = input('---> ')
                try:
                    intChoice = int(choice)
                    print(f'you have chosen {intChoice}')
                    if intChoice >= 0 & intChoice < targetCount+2:
                        validChoice = True
                    else:
                        print('Selection out of range...')
                except:
                    print('Invalid selection. Please enter an integer')
            if  intChoice == targetCount: # indicates multiple targets
                beingAttacked = []
                notAttackedYet = []
                for t in self.participants:
                    if t.dude.name != attacker.name:
                        notAttackedYet.append(t)
                doneTargeting = False
                print('Choose your targets: ')
                while doneTargeting == False: # target selection
                    if len(notAttackedYet) == 0:
                        doneTargeting = True
                        print('No more targets to select')
                        break
                    printedTargets = 0
                    for t in notAttackedYet:
                        print(f'{printedTargets}.) {t.dude.name}')
                        printedTargets += 1
                    if len(beingAttacked) > 0:
                        print(f'{printedTargets}.) Done choosing targets')
                    validChoice = False
                    while validChoice == False:
                        choice = input('---> ')
                        try:
                            intChoice = int(choice)
                            if intChoice >= 0:
                                if intChoice < printedTargets:
                                    beingAttacked.append(notAttackedYet[intChoice])
                                    print(f'Participant {notAttackedYet[intChoice].dude.name} added to targets')
                                    notAttackedYet.remove(notAttackedYet[intChoice])
                                    validChoice = True
                                elif intChoice == printedTargets:
                                    if len(beingAttacked) > 0:
                                        print('Moving on to attack phase...')
                                        doneTargeting = True
                                    validChoice = True
                                else:
                                    print('Selection out of range. Try again.')
                            else:
                                print('Non-Negative entry required.')
                        except:
                            print('Invalid entry. Please enter an integer.')
                for t in beingAttacked: # begin attacking each target
                    if isinstance(t.dude, Monster):
                        print(f'------- {t.dude.name.upper()} being attacked... -------')
                        t.dude.printAbilities()
                    print(f'Make an attack roll for {t.dude.name}...')
                    validRoll = False
                    hitTarget = False
                    while validRoll == False:
                        roll = input('---> ')
                        try:
                            intRoll = int(roll)
                            if intRoll <= t.dude.ac:
                                print(f'Missed target {t.dude.name}')
                                hitTarget = False
                                validRoll = True
                            elif intRoll == 100:
                                print(f'CRITICAL HIT on target {t.dude.name}')
                                hitTarget = True
                                validRoll = True
                            else:
                                print(f'Attack hits target {t.dude.name}')
                                hitTarget = True
                                validRoll = True
                        except:
                            print('Invalid entry. Try again with an integer.')
                    if hitTarget == True:
                        validSaveData = False
                        while validSaveData == False:
                            print('Is a saving throw needed? y/N ')
                            saveNeededResponse = input('---> ')
                            if saveNeededResponse.lower() in ['y', 'yes']:
                                if isinstance(t.dude, Player):
                                    print('Determine the outcome of the save with players...')
                                    input('')
                                elif isinstance(t.dude, Monster):
                                    monsterSave = t.dude.makeSavingThrow()
                                    validDC = False
                                    while validDC == False:
                                        dcInput = input('What is the save DC?  ')
                                        try:
                                            intSaveDC = int(dcInput)
                                            if intSaveDC >= 0:
                                                validDC = True
                                                if monsterSave >= intSaveDC:
                                                    print(f'{t.dude.name} passes the save.')
                                                else:
                                                    print(f'{t.dude.name} fails the save...')     
                                        except:
                                            print('Invalid Save DC...')                                                        
                                else: 
                                    print('Unknown entity type...')
                                validSaveData = True
                            elif saveNeededResponse.lower() in ['n', 'no']:
                                print('Moving on to damage...')
                                validSaveData = True
                        print('How much damage is dealt?')
                        validDamage = False
                        while validDamage == False:
                            damage = input('---> ')
                            try:
                                intDamage = int(damage)
                                if intDamage >= 0:
                                    print(f'Dealing {intDamage} to target {t.dude.name}...')
                                    t.dude.currentHealth -= intDamage
                                    validDamage = True
                                else:
                                    print('Must deal non-negative damage...')
                            except:
                                print('Invalid damage entered. Integer needed.')
            elif intChoice == targetCount+1: # done attacking
                print('Finishing turn...')
                stillAttacking = False
            else: # indexed target chosen
                print(f'Attacking chosen participant: {self.participants[intChoice].dude.name} ')
                # do other attack stuff
                if self.participants[intChoice].dude.name == attacker.name: # in case you decided to hurt yourself
                    print('It hurt itself in its confusion!')
                    # get damage and deal it to the dumbass who hit himself
                    validAmount = False
                    while validAmount == False:
                        amount = input('How much did you hurt yourself by? \n---> ')
                        try:
                            intAmount = int(amount)
                            if intAmount >= 0:
                                print(f'Dealing {intAmount} damage to self...')
                                attacker.dude.currentHealth -= intAmount
                                validAmount = True
                            else:
                                print('You can\'t heal yourself like this...')
                        except:
                            print('Invalid entry. Non-negative integer needed')
                    print(f'Attacker health is now at {attacker.dude.currentHealth}')
                else: # if you chose an index that wasn't for yourself (...ie it was LISTED)
                    validAttackRoll = False
                    while validAttackRoll == False:
                        attackRoll = input('What is the player\'s attack roll? \n---> ')
                        try:
                            intAttackRoll = int(attackRoll)
                            if intAttackRoll == 100: # CRIT
                                print('CRITICAL HIT')
                                validAttackRoll = True
                                validSaveNeeded = False
                                while validSaveNeeded == False: # is a saving throw needed?
                                    saveNeeded = input('Is a saving throw needed? (y / N) \n---> ')
                                    if saveNeeded.lower() in ['y', 'n', 'yes', 'no']:
                                        validSaveNeeded = True
                                        if saveNeeded.lower() in ['y', 'yes']: # saving throw needed
                                            if isinstance(self.participants[intChoice].dude, Player): # no need to automate this
                                                print('Determine with the player whether or not the save is successful...')
                                            elif isinstance(self.participants[intChoice].dude, Monster): # monsters make their own saves
                                                save = self.participants[intChoice].dude.makeSavingThrow()
                                                validSaveDiff = False
                                                while validSaveDiff == False: # get save difficulty
                                                    saveDiff = input('What is the save DC? \n---> ')
                                                    try:
                                                        intSaveDiff = int(saveDiff)
                                                        validSaveDiff = True
                                                        if save >= intSaveDiff:
                                                            print('Save is successful, determine damage...')
                                                        else:
                                                            print('Save failed...determine damage...')
                                                    except:
                                                        print('Invalid entry, integer needed...')
                                        else:
                                            print('Determined no save is needed.')
                                            
                                validDamage = False
                                while validDamage == False: # get damage dealt
                                    damage = input('How much damage is dealt? \n---> ')
                                    try:
                                        intDamage = int(damage)
                                        if intDamage >= 0:
                                            print(f'Dealing {intDamage} damage to {self.participants[intChoice].dude.name}')
                                            self.participants[intChoice].dude.currentHealth -= intDamage
                                            validDamage = True
                                        else:
                                            print('Cannot heal a creature with an attack...')
                                    except:
                                        print('Invalid entry. Integer needed.')
                            elif intAttackRoll > self.participants[intChoice].dude.ac: # HIT
                                print('Attack HITS!')
                                validAttackRoll = True
                                validSaveNeeded = False
                                while validSaveNeeded == False: # is a saving throw needed?
                                    saveNeeded = input('Is a saving throw needed? (y / N) \n---> ')
                                    if saveNeeded.lower() in ['y', 'n', 'yes', 'no']:
                                        validSaveNeeded = True
                                        if saveNeeded.lower() in ['y', 'yes']: # saving throw needed
                                            if isinstance(self.participants[intChoice].dude, Player): # no need to automate this
                                                print('Determine with the player whether or not the save is successful...')
                                            elif isinstance(self.participants[intChoice].dude, Monster): # monsters make their own saves
                                                save = self.participants[intChoice].dude.makeSavingThrow()
                                                validSaveDiff = False
                                                while validSaveDiff == False: # get save difficulty
                                                    saveDiff = input('What is the save DC? \n---> ')
                                                    try:
                                                        intSaveDiff = int(saveDiff)
                                                        validSaveDiff = True
                                                        if save >= intSaveDiff:
                                                            print('Save is successful, determine damage...')
                                                        else:
                                                            print('Save failed...determine damage...')
                                                    except:
                                                        print('Invalid entry, integer needed...')
                                        else:
                                            print('Determined no save is needed.')
                                            
                                validDamage = False
                                while validDamage == False: # get damage dealt
                                    damage = input('How much damage is dealt? \n---> ')
                                    try:
                                        intDamage = int(damage)
                                        if intDamage >= 0:
                                            print(f'Dealing {intDamage} damage to {self.participants[intChoice].dude.name}')
                                            self.participants[intChoice].dude.currentHealth -= intDamage
                                            validDamage = True
                                        else:
                                            print('Cannot heal a creature with an attack...')
                                    except:
                                        print('Invalid entry. Integer needed.')
                            else:
                                validAttackRoll = True
                                print('Player\'s attack misses...')
                                input('')
                        except:
                            print('Invalid entry, need an integer.')
                                
                                                
                                                    
        