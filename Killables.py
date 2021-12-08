from DiceRoll import DiceRoller

class KillableType:
    def __init__(self, dudeName):
        self.name  = dudeName # default name to establish universal 'name' attribute
        self.speed = 0        # default speed - universal 'speed' attribute
        self.hp    = 0        # default health - universal 'hp' attribute
        self.ac    = 0        # default armor class - universal 'ac' attribute

class Player(KillableType):
    def __init__(self,
                 playerName,             # roleplayer string arg index 0
                 characterName,          # roleplayee string arg index 1
                 characterRace,          # string            arg index 2
                 characterClass,         # string            arg index 3
                 characterAlignment,     # string            arg index 4
                 characterMaxHealth,     # int               arg index 5
                 characterCurrentHealth, # int               arg index 6
                 characterArmorClass,    # int               arg index 7
                 characterMoveSpeed):    # int               arg index 8
        self.pName         = playerName
        self.cRace         = characterRace
        self.cClass        = characterClass
        self.cAlignment    = characterAlignment
        self.currentHealth = characterCurrentHealth
        self.name          = characterName
        self.hp            = characterMaxHealth
        self.ac            = characterArmorClass
        self.speed         = characterMoveSpeed
        
        self.currentHealth    = characterCurrentHealth
        self.deathSavesPassed = 0
        self.deathSavesFailed = 0
        
    def attack(self):
        print('Attack goes here... ')
        
    def takeDamage(self, amount):
        self.currentHealth -= amount  

class Attack:
    def __init__(self,
                 attackName,         # string
                 attackMod,          # int
                 attackSave,         # int
                 attackSaveType,     # string NONE STR DEX CON INT WIS CHA
                 attackDamage,       # list of Dice counters (4, 6, 8, 10, 12, 20, 100)
                 attackConsequence): # string
        self.name        = attackName
        self.mod         = attackMod
        self.save        = attackSave
        self.saveType    = attackSaveType
        self.damage      = attackDamage
        self.consequence = attackConsequence
    
    def printConsequences(self):
            print(self.consequence)
    
    def calculateDamage(self):
        roller = DiceRoller()
        totalDamage = 0
        
        for dice in self.damage:
            i = self.damage.index(dice)
            if i == 0:
                damage = 0
                for count in range(0, dice):
                    damage += roller.roll(4)
                    count = count
            elif i == 1:
                damage = 0
                for count in range(0, dice):
                    damage += roller.roll(6)
            elif i == 2:
                damage = 0
                for count in range(0, dice):
                    damage += roller.roll(8)
            elif i == 3:
                damage = 0
                for count in range(0, dice):
                    damage += roller.roll(10)
            elif i == 4:
                damage = 0
                for count in range(0, dice):
                    damage += roller.roll(12)
            elif i == 5:
                damage = 0
                for count in range(0, dice):
                    damage += roller.roll(20)
            elif i == 6:
                damage = 0
                for count in range(0, dice):
                    damage += roller.roll(100)
            totalDamage += damage
        return totalDamage
        
class Monster(KillableType):
    
    MONSTER_ENV = ('NOWHERE', 'FOREST', 'WATER', 'DESERT', 'TOWN')
    
    def __init__(self,
                 monsterName,
                 monsterMaxHealth,
                 monsterArmorClass,
                 monsterMoveSpeed,
                 monsterAttacks,     # Attack Class list
                 monsterAbilities,   # string list
                 monsterEnvironment, # MONSTER_ENV list
                 challengeRating = 0,
                 strMod = 0,
                 dexMod = 0,
                 conMod = 0,
                 intMod = 0,
                 wisMod = 0,
                 chaMod = 0):
        self.name             = monsterName
        self.ac               = monsterArmorClass
        self.hp               = monsterMaxHealth
        self.speed            = monsterMoveSpeed
        self.mAttacks         = monsterAttacks
        self.mAbilities       = monsterAbilities
        self.mEnvironment     = monsterEnvironment
        self.mChallengeRating = challengeRating
        self.mStr             = strMod
        self.mDex             = dexMod
        self.mCon             = conMod
        self.mInt             = intMod
        self.mWis             = wisMod
        self.mCha             = chaMod
        
        self.currentHealth    = self.hp
        self.deathSavesPassed = 0
        self.deathSavesFailed = 0
    
    def attack(self, participants):
        # get which attack to use
        print('Select the monster\'s attack...')
        for at in self.mAttacks:
            outStr = str(self.mAttacks.index(at) + 1)
            outStr += '.) ' + at.name
            print(outStr)
        atNum = 0
        validChoice = False
        while validChoice == False:
            answer = input('...? ')
            try:
                atNum = int(answer)
                if atNum == 0:
                    print('Try again...')
                    continue
                elif atNum > 0:
                    if self.mAttacks[atNum - 1].name:
                        print(f'Attack {self.mAttacks[atNum-1].name} chosen. ')
                        validChoice = True
                    else:
                        print('Invalid selection')
                        continue
                else:
                    print('Invalid selection')
                    continue
            except: 
                print('Please enter an integer...')
                continue
        # sanity check
        if atNum != 0: # valid attack choice
            chosenAttack = self.mAttacks[atNum-1]
            roller = DiceRoller()
            # make attack roll
            roll  = roller.roll(20)
            if roll == 20:
                roll = 100 # critical hit
            roll += chosenAttack.mod
            print(f'Attack roll IS!....: {roll} ')
            # select target
            print('Select the monster\'s target...')
            listedParticipants = []
            notAttackedYet = []
            for p in participants:
                if p.dude.name != self.name:
                    notAttackedYet.append(p)
            participantsListed = 0
            for p in participants: # individual targets
                if p.dude.name in listedParticipants:
                    p.dude.name += '-x'
                if p.dude.name != self.name:
                    print(f'{participantsListed}.) {p.dude.name}')
                    listedParticipants.append(p.dude.name)
                participantsListed += 1
            print(f'{participantsListed}.) Multiple Targets...')
            pNum = 0
            validChoice = False
            while validChoice == False: # receive target choice
                answer = input('---> ')
                try:
                    pNum = int(answer)
                    # if pNum >= 0 & pNum < participantsListed:
                    if pNum in range(0, participantsListed, 1):
                        if participants[pNum].dude.name:
                            print(f'Participant {participants[pNum].dude.name} chosen. ')
                            validChoice = True
                        else:
                            print('Invalid selection')
                            continue
                    elif pNum == participantsListed:
                        print('Selecting multiple targets...')
                        validChoice = True
                    else:
                        print('Invalid selection')
                        continue
                except: 
                    print('Please enter an integer...')
                    continue
            if pNum < participantsListed: # single target
                target = participants[pNum]
                if isinstance(target.dude, Monster):
                    print(f'------- {target.dude.name.upper()} being attacked... -------')
                    target.dude.printAbilities()
                # determine hit / miss
                if roll >=90: # range for modifier for crit
                    print('CRITICAL HIT!')
                    if chosenAttack.saveType != 'NONE':
                        if   chosenAttack.saveType == 'STR':
                            save = input('Make a strength save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'DEX':
                            save = input('Make a dexterity save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'CON':
                            save = input('Make a constitution save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'INT':
                            save = input('Make a intelligence save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'WIS':
                            save = input('Make a wisdom save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'CHA':
                            save = input('Make a charisma save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'FAIL':
                            print('Success was never an option, here\'s your consequence: ')
                            chosenAttack.printConsequences()
                        else:
                            print('Invalid save type detected, moving on.')
                            
                    damageDealt = chosenAttack.calculateDamage()
                    damageDealt = 2*damageDealt
                    
                    target.dude.takeDamage(damageDealt)
                    print(f'Dealing {damageDealt} damage to participant {target.dude.name} ')
                    input()
                    
                elif roll > target.dude.ac: # single target as indexed
                    if isinstance(target.dude, Monster):
                        print(f'------- {target.dude.name.upper()} being attacked... -------')
                        target.dude.printAbilities()
                    print('Attack hits...')
                    if chosenAttack.saveType != 'NONE':
                        if   chosenAttack.saveType == 'STR':
                            save = input('Make a strength save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'DEX':
                            save = input('Make a dexterity save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'CON':
                            save = input('Make a constitution save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'INT':
                            save = input('Make a intelligence save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'WIS':
                            save = input('Make a wisdom save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'CHA':
                            save = input('Make a charisma save... ')
                            keepGoing = True
                            while keepGoing:
                                try: 
                                    intSave = int(save)
                                    if intSave >= chosenAttack.save:
                                        print('Save successful...')
                                    else:
                                        print('Save failed...')
                                        chosenAttack.printConsequences()
                                        input()
                                    keepGoing = False
                                except:
                                    print('Invalid response. Integer needed...')
                        elif chosenAttack.saveType == 'FAIL':
                            print('Success was never an option, here\'s your consequence: ')
                            chosenAttack.printConsequences()
                        else:
                            print('Invalid save type detected, moving on.')
                    
                    damageDealt = chosenAttack.calculateDamage()
                    
                    target.dude.takeDamage(damageDealt)
                    print(f'Dealing {damageDealt} damage to participant {target.dude.name} ')
                    input()
                    
                elif roll == target.dude.ac:
                    print('Attack glances just by target, maybe next time!')
                    
                else:
                    print('......NOPE! moving on.')
            elif pNum == participantsListed: # multiple targets
                beingAttacked = []
                doneTargeting = False
                print('Choose your targets: ')
                while doneTargeting == False: # target selection
                    if len(notAttackedYet) == 0:
                        doneTargeting = True
                        print('No more targets to select')
                        break
                    printedTargets = 0
                    for t in notAttackedYet:
                        if t.dude.name != self.name:
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
                                        print('Need at least one target...')
                                else:
                                    print('Selection out of range. Try again.')
                            else:
                                print('Non-negative integer needed.')
                        except:
                            print('Invalid entry. Please enter an integer.')
                for t in beingAttacked:
                    if isinstance(t.dude, Monster):
                        print(f'------- {t.dude.name.upper()} being attacked... -------')
                        t.dude.printAbilities()
                    if roll >= 90:
                        damageCalculated = 2*chosenAttack.calculateDamage()
                        t.dude.takeDamage(damageCalculated)
                        print(f'Dealing {damageCalculated} to {t.dude.name}')
                        if chosenAttack.saveType != 'NONE':
                            if isinstance(t.dude, Monster):
                                print(f'Save type: {chosenAttack.saveType}')
                                save = t.dude.makeSavingThrow()
                                if save >= chosenAttack.save:
                                    print('Target passes the check')
                                else:
                                    chosenAttack.printConsequences()
                            elif isinstance(t.dude, Player):
                                validSave = False
                                while validSave == False:
                                    save = input(f'Make a {chosenAttack.saveType} save...\n---> ')
                                    try:
                                        intSave = int(save)
                                        if intSave >= chosenAttack.save:
                                            print('Save successful...')
                                        else:
                                            print('Save failed...')
                                            chosenAttack.printConsequences()
                                        validSave = True
                                    except:
                                        print('Invalid save value. Enter an integer...')
                            
                    elif roll > t.dude.ac:
                        damageCalculated = chosenAttack.calculateDamage()
                        t.dude.takeDamage(damageCalculated)
                        print(f'Dealing {damageCalculated} to {t.dude.name}')
                        if chosenAttack.saveType != 'NONE':
                            if isinstance(t.dude, Monster):
                                print(f'Save type: {chosenAttack.saveType}')
                                save = t.dude.makeSavingThrow()
                                if save >= chosenAttack.save:
                                    print('Target passes the check')
                                else:
                                    chosenAttack.printConsequences()
                            elif isinstance(t.dude, Player):
                                validSave = False
                                while validSave == False:
                                    save = input(f'Make a {chosenAttack.saveType} save...\n---> ')
                                    try:
                                        intSave = int(save)
                                        if intSave >= chosenAttack.save:
                                            print('Save successful...')
                                        else:
                                            print('Save failed...')
                                            chosenAttack.printConsequences()
                                        validSave = True
                                    except:
                                        print('Invalid save value. Enter an integer...')
                    else:
                        print(f'Attack misses target {t.dude.name}')  
            else:
                print('Invalid choice...')      

    def takeDamage(self, amount):
        self.currentHealth -= amount
    
    def makeSavingThrow(self):
        print('What type of saving throw is to be made? ')
        print('1.) Strength')
        print('2.) Dexterity')
        print('3.) Constituation')
        print('4.) Intelligence')
        print('5.) Wisdom')
        print('6.) Charisma')
        keepGoing = True
        roller = DiceRoller()
        while keepGoing:
            response = input('...? ')
            try:
                responseInt = int(response)
                if responseInt in [1,2,3,4,5,6]:
                    theSave = roller.roll(20)
                    if   responseInt == 1:
                        theSave += self.mStr
                    elif responseInt == 2:
                        theSave += self.mDex
                    elif responseInt == 3:
                        theSave += self.mCon
                    elif responseInt == 4:
                        theSave += self.mInt
                    elif responseInt == 5:
                        theSave += self.mWis
                    elif responseInt == 6:
                        theSave += self.mCha
                    else:
                        print('Unexpected condition...')
                        print(f'Leaving monster save as {theSave}')
                    keepGoing = False
                else:
                    print('Invalid response. Please select an integer from the list...')
                return theSave
            except:
                print('Please enter an integer...')
                
    def rollInitiative(self):
        
        roller = DiceRoller()
        return roller.roll(20) + self.mDex
                
    def printAbilities(self):
        for a in self.mAbilities:
            print(str(a))
    
    
    
    
# TO DO - NPCs follow monster structure, but aren't stored in the Monster Library