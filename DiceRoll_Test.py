from DiceRoll import DiceRoller

def main():
    roller = DiceRoller()
    print(f'Outcome of d4   is: {roller.roll(4)}')
    print(f'Outcome of d6   is: {roller.roll(6)}')
    print(f'Outcome of d8   is: {roller.roll(8)}')
    print(f'Outcome of d10  is: {roller.roll(10)}')
    print(f'Outcome of d12  is: {roller.roll(12)}')
    print(f'Outcome of d20  is: {roller.roll(20)}')
    print(f'Outcome of d100 is: {roller.roll(100)}')
    print(f'Outcome of d13  is: {roller.roll(13)}')
    
    stillGoing = True
    while stillGoing:
        ip = input('Keep going? (y / n) ')
        if ip.lower() == 'y':
            num = input('What kind of dice to roll? ')
            if num == '4':
                print(f'Rolled a {roller.roll(4)}')
            elif num == '6':
                print(f'Rolled a {roller.roll(6)}')
            elif num == '8':
                print(f'Rolled a {roller.roll(8)}')
            elif num == '10':
                print(f'Rolled a {roller.roll(10)}')
            elif num == '12':
                print(f'Rplled a {roller.roll(12)}')
            elif num == '20':
                print(f'Rolled a {roller.roll(20)}')
            elif num == '100':
                print(f'Rolled a {roller.roll(100)}')
            else:
                print('Invalid dice type, try again...')
        elif ip.lower() == 'n':
            stillGoing = False
        else:
            print('Invalid response...')
        
    

if __name__ == "__main__": main()

