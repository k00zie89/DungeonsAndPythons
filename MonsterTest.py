from MonsterLibrary import Squirtle
from Killables import Attack, Monster

def main():
    monster0 = Squirtle()
    m0data =  'Name: ' + monster0.name
    m0data += '\n AC: ' + str(monster0.ac)
    m0data += '\n HP: ' + str(monster0.hp)
    m0data += '\n Speed: ' + str(monster0.speed)
    m0data += '\n Attacks: ' + monster0.mAttacks
    m0data += '\n Abilities: ' + monster0.mAbilities
    m0data += '\n Environment: ' + monster0.mEnvironment
    m0data += '\n Challenge Rating: ' + monster0.mChallengeRating
    m0data += '\n StrMod: ' + monster0.mStr
    m0data += '\n DexMod: ' + monster0.mDex
    m0data += '\n ConMod: ' + monster0.mCon
    m0data += '\n IntMod: ' + monster0.mInt
    m0data += '\n WisMod: ' + monster0.mWis
    m0data += '\n ChaMod: ' + monster0.mCha
    m0data += '\n CurrentHealth: ' + monster0.currentHealth
    
    print(m0data)
    
    

if __name__ == '__main__': main()