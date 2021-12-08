from Killables import KillableType, Monster, Attack
import random
    
    # Constructor order:
    # Creature name
    # Max Health
    # Armor Class
    # Move Speed
    # Attack Set
    # Ability Set
    # Environment Set
    # Challenge Rating
    # Modifiers in Order: Str Dex Con Int Wis Cha defaulted to zero
class MonsterLibrary:
    
    monsterLibrary = {
        'A1':('Animated Armor', '1'),
        'B1':('Banshee', '4'),
        'B2':('Bilwis', '1'),
        'B3':('Black Dragon Wyrmling', '2'),
        'B4':('Bone Devil', '9'),
        'C1':('Carrion Crawler', '2'),
        'C2':('Centaur', '2'),
        'C3':('Chain Devil', '8'),
        'D1':('Dark Guard', '4'),
        'D2':('Doom Golem', '10'),
        'E1':('Ettercap', '2'),
        'E2':('Exploding Toad', '0.25'),
        'F1':('FacelessMaster', '6'),
        'F2':('FacelessMinion', '3'),
        'F3':('Fey Spider', '2'),
        'G1':('Goliath LongLegs', '7'),
        'I1':('Imp', '1'),
        'I2':('Intellect Devourer', '3'),
        'J1':('Jinmenju', '9'),
        'L1':('Litch Lord', '21'),
        'L2':('Living Shade', '0.25'),
        'M1':('Mimic', '2'),
        'N1':('Neophron', '8'),
        'N2':('Nothic', '2'),
        'P1':('Pishacha Demon', '3'),
        'R1':('Rug of Smothering', '2'),
        'S1':('Shadow Ooze', '3'),
        'S2':('Shadow Skeleton', '2'),
        'S3':('Shambling Mound', '5'),
        'S4':('Spectator', '3'),
        'S5':('Spined Devil', '2'),
        'V1':('Villager - Basic', '1'),
        'V2':('Villager - Plus', '3'),
        'V3':('Villager - Elite', '5'),
        'W1':('Weirding Scroll', '0.5'),
        'W2':('Will o\' Wisp', '2'),
        'Z1':('Zoog', '0')
    }
    
    libraryIndices = [
        'A1', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'F1', 'F2', 'F3', 'G1', 'I1', 'I2', 'J1', 'L1', 'L2', 'M1', 'N1', 'N2', 'P1', 'R1', 'S1', 'S2', 'S3', 'S4', 'S5', 'V1', 'V2', 'V3', 'W1', 'W2', 'Z1'
    ]
    
    def chooseMonster(self, selection):
        if self.monsterLibrary[selection]:
            print('Creating new monster...')
            if   selection == 'A1':
                monster = self.AnimatedArmor()
            elif selection == 'B1':
                monster = self.Banshee()
            elif selection == 'B2':
                monster = self.Bilwis()
            elif selection == 'B3':
                monster = self.BlackDragonWyrmling()
            elif selection == 'B4':
                monster = self.BoneDevil()
            elif selection == 'C1':
                monster = self.CarrionCrawler()
            elif selection == 'C2':
                monster = self.Centaur()
            elif selection == 'C3':
                monster = self.ChainDevil()
            elif selection == 'D1':
                monster = self.DarkGuard()
            elif selection == 'D2':
                monster = self.DoomGolem()
            elif selection == 'E1':
                monster = self.Ettercap()
            elif selection == 'E2':
                monster = self.ExplodingToad()
            elif selection == 'F1':
                monster = self.FacelessMaster()
            elif selection == 'F2':
                monster = self.FacelessMinion()
            elif selection == 'F3':
                monster = self.FeySpider()
            elif selection == 'G1':
                monster = self.GoliathLonglegs()
            elif selection == 'I1':
                monster = self.Imp()
            elif selection == 'I2':
                monster = self.IntellectDevourer()
            elif selection == 'J1':
                monster = self.Jinmenju()
            elif selection == 'L1':
                monster = self.LitchLord()
            elif selection == 'L2':
                monster = self.LivingShade()
            elif selection == 'M1':
                monster = self.Mimic()
            elif selection == 'N1':
                monster = self.Neophron()
            elif selection == 'N2':
                monster = self.Nothic()
            elif selection == 'P1':
                monster = self.PishachaDemon()
            elif selection == 'R1':
                monster = self.RugOfSmothering()
            elif selection == 'S1':
                monster = self.ShadowOoze()
            elif selection == 'S2':
                monster = self.ShadowSkeleton()
            elif selection == 'S3':
                monster = self.ShamblingMound()
            elif selection == 'S4':
                monster = self.Spectator()
            elif selection == 'S5':
                monster = self.SpinedDevil()
            elif selection == 'V1':
                monster = self.VillagerBasic()
            elif selection == 'V2':
                monster = self.VillagerPlus()
            elif selection == 'V3':
                monster = self.VillagerElite()
            elif selection == 'W1':
                monster = self.WeirdingScroll()
            elif selection == 'W2':
                monster = self.Will_o_Wisp()
            elif selection == 'Z1':
                monster = self.Zoog()
            else:
                print(f"Unknown selection: {selection}")
                return None        
        return monster
    
    # A1
    class AnimatedArmor(Monster):        
        libraryIndex = 'A1'
    
        def __init__(self):
            slam = Attack('Slam - single target', 4, 0, 'NONE', [0,1,0,0,0,0,0], 'NONE')
            Monster.__init__(self, 'Animated Armor', 33, 18, 25, [slam], 
                            ['Multi-Attack', 
                             'Magic Susceptibility reduced', 
                             'False Appearance (like a suit of armor)', 
                             'Immune: Poison, Psychic, Blindness, Charmed, Deafness, Fear, Paralysis'], 
                            ['FOREST', 'WATER', 'TOWN'],
                            1,
                            2, 0, 1, -5, -4, -5)
    
    # B1
    class Banshee(Monster):
        libraryIndex = 'B1'
        
        def __init__(self):
            corruptingTouch  = Attack('Corrupting Touch - single target', 4, 0, 'NONE', [0,3,0,0,0,0,0], 'NONE')
            horrifyingVisage = Attack('Horrifying Visage - effect', 100, 13, 'WIS', [0,0,0,0,0,0,0], 'Frightened for 1 minute or until DC-13 WIS passed')
            wail   = Attack('Wail - area of effect (all in range)', 100, 100, 'CON', [0,0,0,0,0,0,0], 'Drop to zero or take 3d6 (when DC-13 CON passed)')
            Monster.__init__(self, 'Banshee', 58, 12, 40, [corruptingTouch, horrifyingVisage, wail], 
                            ['Dark Vision',
                            'Detect Life',
                            'Incorporeal Movement',
                            'Immune:Cold-Necrotic-Poison-Charm-Grappled-Paralyzed-Prone'],
                            ['TOWN', 'DESERT', 'FOREST', 'WATER', 'NONE', 'ANY'],
                            4,
                            -5, 2, 0, 1, 0, 3)
  
    # B2
    class Bilwis(Monster):
    
       libraryIndex = 'B2'
        
       def __init__(self):
           slam      = Attack('Slam - single target', 5, 0, 'NONE', [1,0,2,0,0,0,0], 'NONE')
           whirlwind = Attack('Whirlwind - 5ft radius', 100, 100, 'STR', [0,0,0,0,0,0,0], 'DC12 - Strength...4d6 if fail, half if successful')
           Monster.__init__(self, 'Bilwis', 49, 13, 40, [slam, whirlwind],
                           ['DarkVision', 
                            'Air Form'],
                           ['TOWN', 'DESERT', 'FOREST'],
                           1,
                           1, 3, 0, 0, 1, 3)
    
    # B3
    class BlackDragonWyrmling(Monster):
    
       libraryIndex = 'B3'
        
       def __init__(self):
           bite       = Attack('Bite - single target', 4, 0, 'NONE', [1,0,0,1,0,0,0], 'NONE')
           acidBreath = Attack('Acid Breath - 15ft line', 100, 100, 'DEX', [0,0,0,0,0,0,0], 'DC11 - DEX take 5d8 or half')
           Monster.__init__(self, 'Black Dragon Wyrmling', 33, 17, 30, [bite, acidBreath], 
                           ['Dark Vision', 
                            'Blind Sight', 
                            'Amphibious', 
                            'Immune to Acid'],
                           ['TOWN', 'DESERT', 'FOREST', 'WATER'],
                           2,
                           2, 2, 1, 0, 0, 1)
    
    # B4  
    class BoneDevil(Monster):
    
       libraryIndex = 'B4'
        
       def __init__(self):
           claw  = Attack('Claw - single target', 8, 0, 'NONE', [0,1,1,0,0,0,0], 'NONE')
           sting = Attack('Sting - single target', 8, 14, 'CON', [0,1,2,2,0,0,0], 'Poisoned for 1 minute')
           Monster.__init__(self, 'Bone Devil', 142, 19, 40, [claw, sting], 
                           ['Devil\'s Sight',
                            'Magic Resistance',
                            'Multi-Attack',
                            'Immune to Fire and Poison',
                            'Resistant to cold and damage from nonmagical / unsilvered weapons'],
                           ['TOWN', 'FOREST', 'DESERT'],
                           9,
                           4, 3, 4, 1, 2, 3)
    
    # C1
    class CarrionCrawler(Monster):
    
       libraryIndex = 'C1'
        
       def __init__(self):
           bite      = Attack('Bite - single target', 4, 0, 'NONE', [2,0,0,0,0,0,0], 'NONE')
           tentacles = Attack('Tentacles - single target', 8, 13, 'CON', [2,0,0,0,0,0,0], 'Poisoned and Paralyzed for 1 minute or until DC13 - CON passed')
           Monster.__init__(self, 'Carrion Crawler', 51, 13, 30, [bite, tentacles], 
                           ['Keen Smell (Advantage on Wisdom Checks using smell)',
                            'Spider Climb',
                            'Multi-Attack',
                            'Dark Vision'],
                           ['TOWN', 'FOREST'],
                           2,
                           2, 1, 3, -5, 1, -3)
    
    # C2
    class Centaur(Monster):
    
       libraryIndex = 'C2'
        
       def __init__(self):
           pike    = Attack('Pike - single target', 6, 0, 'NONE', [0,1,0,1,0,0,0], 'NONE')
           hooves  = Attack('Hooves - single target', 6, 0, 'NONE', [1,2,0,0,0,0,0], 'NONE')
           longbow = Attack('Longbow - single target', 4, 0, 'NONE', [1,0,1,0,0,0,0], 'NONE')
           Monster.__init__(self, 'Centaur', 45, 12, 50, [pike, hooves, longbow], 
                           ['Multi-Attack',
                            'Pike and Hooves or 2 Longbow (attack sequence)',
                            'If charging opponent using pike, extra 3d6'],
                           ['FOREST', 'DESERT'],
                           2,
                           4, 2, 2, -1, 1, 0)
    
    # C3
    class ChainDevil(Monster):
    
       libraryIndex = 'C3'
        
       def __init__(self):
           chain         = Attack('Chain - single target', 8, 100, 'STR', [0,3,0,0,0,0,0], 'Grappled until DC14 - STR; restrained and takes 2d6 piercing each turn')
           unNervingMask = Attack('Unnerving Mask - single target', 100, 14, 'WIS', [0,0,0,0,0,0,0], 'Looks like creature\'s beloved departed one; frightened until end of turn')
           Monster.__init__(self, 'Chain Devil', 85, 16, 30, [chain, unNervingMask], 
                           ['Devil\'s Sight',
                            'Magic Resistance',
                            'Multi-Attack',
                            'Immune to fire and poison',
                            'Resistant to cold and weapons not magical or silvered'],
                           ['TOWN', 'DESERT'],
                           8,
                           4, 2, 4, 0, 1, 2)
    
    # D1
    class DarkGuard(Monster):
    
       libraryIndex = 'D1'
        
       def __init__(self):
           greatSword    = Attack('Great Sword - single target', 5, 0, 'NONE', [0,2,0,0,0,0,0], 'NONE')
           eldritchBlast = Attack('Eldritch Blast - line of effect', 5, 0, 'NONE', [0,0,0,1,0,0,0], 'NONE')
           strengthDrain = Attack('Strength Drain - single target', 4, 100, 'STR', [1,2,0,0,0,0,0], 'Victim Strength reduced by 1d4; if falls to zero DEATH. Otherwise, until rested')
           shieldBash    = Attack('Sheild Bash - single target', 5, 15, 'CON', [1,1,0,0,0,0,0], 'Victim knocked prone')
           Monster.__init__(self, 'Dark Guard', 35, 13, 25, [greatSword, eldritchBlast, shieldBash, strengthDrain], 
                           ['Devil\'s Sight',
                            'Telepathy',
                            'Amorphous',
                            'Shadow Stealth'],
                           ['TOWN'],
                           4,
                           3, 1, 3, -1, 4, 3)
    
    # D2
    class DoomGolem(Monster):
    
       libraryIndex = 'D2'
        
       def __init__(self):
           bite     = Attack('Bite - single target', 11, 0, 'NONE', [0,0,1,3,0,0,0], 'NONE')
           doomClaw = Attack('Doom Claw - single target', 11, 0, 'NONE', [0,4,1,0,0,0,0], 'NONE')
           fearAura = Attack('Fear Aura - all in range', 100, 15, 'WIS', [0,0,0,0,0,0,0], 'Frightened until next turn')
           windOfBoreas = Attack('Wind of Boreas - all in range', 100, 100, 'CON', [0,0,0,0,0,0,0], 'DC16 - CON...11d6 cold or half')
           Monster.__init__(self, 'Doom Golem', 153, 17, 30, [bite, doomClaw, fearAura, windOfBoreas], 
                           ['Multi-Attack',
                            'Only harmed by magical weapons',
                            'Immutable Form',
                            'Magic Resistance',
                            'Immune to Cold, Poison, Psychic',
                            'Dark Vision'],
                           ['FOREST', 'DESERT', 'TOWN'],
                           10,
                           7, 1, 3, -4, 0, -5)
    
    # E1
    class Ettercap(Monster):
    
       libraryIndex = 'E1'
        
       def __init__(self):
           bite = Attack('Bite - single target', 4, 0, 'NONE', [0,1,1,0,0,0,0], 'NONE')
           claw = Attack('Claw - single target', 4, 0, 'NONE', [3,0,0,0,0,0,0], 'NONE')
           web  = Attack('Web  - single target', 4, 11, 'STR', [0,0,0,0,0,0,0], 'Restrained in thick spider-webbng until DC11-STR passed')
           Monster.__init__(self, 'Ettercap', 44, 13, 30, [bite, claw, web], 
                           ['Dark Vision',
                            'Spider Climb',
                            'Web Sense',
                            'Web Walker',
                            'Multi-Attack'],
                           ['TOWN', 'FOREST', 'DESERT'],
                           2,
                           2, 2, 1, -2, 1, -1)
    
    # E2
    class ExplodingToad(Monster):
    
       libraryIndex = 'E2'
        
       def __init__(self):
           bite = Attack('Bite - single target', 3, 0, 'NONE', [2,0,0,0,0,0,0], 'NONE')
           Monster.__init__(self, 'Exploding Toad', 2, 12, 20, [bite], 
                           ['Amphibious',
                            'Ranged attacks have disadvantage',
                            'Can choose to take fire damage, otherwise are immune',
                            'When killed, explodes! all in 10ft radius make DC11 - DEX save or take 3d6 fire damage'],
                           ['FOREST', 'WATER'],
                           1/4,
                           -5, 1, 0, -3, -1, -4)
    
    # F1
    class FacelessMaster(Monster):
    
       libraryIndex = 'F1'
        
       def __init__(self):
           icyGrasp      = Attack('Icy Grasp', 4, 15, 'CON', [0,2,0,0,0,0,0], 'Terrified with additional 1d6 cold damage')
           piercingGaze  = Attack('Piercing Gaze', 3, 13, 'INT', [2,0,0,0,0,0,0], 'Disadvantage for next minute')
           command       = Attack('Command', 100, 13, 'WIS', [0,0,0,0,0,0,0], 'Must obey single-word command')
           eldritchBlast = Attack('Eldritch Blast - line of effect', 5, 0, 'NONE', [0,0,0,1,0,0,0], 'NONE')           
           Monster.__init__(self, 'Faceless Master', 40, 16, 40, [icyGrasp, piercingGaze, command, eldritchBlast], 
                           ['True Sight', 'Immune to cold, necrotic', 'Resistant to all non-magical weapons', 'OmniLingual', 'Telepathic', 'Multiattack'],
                           ['TOWN', 'FOREST', 'WATER', 'DESERT'],
                           6,
                           -1, 4, 3, 5, 1, -3)
    
    # F2
    class FacelessMinion(Monster):
        
        libraryIndex = 'F2'
        
        def __init__(self):
            icyGrasp      = Attack('Icy Grasp', 4, 11, 'CON', [0,2,0,0,0,0,0], 'Terrified with additional 1d6 cold damage')
            shadowSpear   = Attack('Shadow Spear', 4, 11, 'CON', [0,0,1,0,0,0,0], 'Additional 2d4 cold damage')
            eldritchBlast = Attack('Eldritch Blast - line of effect', 5, 0, 'NONE', [0,0,0,1,0,0,0], 'NONE')           
            Monster.__init__(self, 'Faceless Minion', 40, 16, 40, [icyGrasp, shadowSpear, eldritchBlast], 
                            ['True Sight', 'Immune to cold, necrotic', 'Resistant to all non-magical weapons', 'Functional mute'],
                            ['TOWN', 'FOREST', 'WATER', 'DESERT'],
                            3,
                            -1, 4, 3, 3, 1, -3)
    
    # F3
    class FeySpider(Monster):
    
       libraryIndex = 'F3'
        
       def __init__(self):
           bite           = Attack('Bite', 2, 10, 'CON', [0,1,0,0,0,0,0], 'Extra 1d4 poison damage')
           smack          = Attack('Smack', 4, 10, 'CON', [2,0,0,0,0,0,0], 'Knocked prone')
           web            = Attack('Web', 6, 100, 'DEX', [0,0,0,0,0,0,0], 'Entangled in a thick string of web - DC 16 STR to escape')
           reelAndConsume = Attack('Reel - Consume (webbed target)', 100, 100, 'CON', [0,0,0,0,0,0,0], 'DC 16 CON or death')
           Monster.__init__(self, 'Fey Spider', 15, 12, 30, [bite, smack, web, reelAndConsume], 
                           ['Climb',
                            'True Sight',
                            'Terrain Master'],
                           ['environments'],
                           2,
                           2, 6, 4, 2, 2, -6)
    
    # G1
    class GoliathLonglegs(Monster):
    
       libraryIndex = 'G1'
        
       def __init__(self):
           bite = Attack('Bite - single target', 7, 100, 'CON', [1,0,1,0,0,0,0], '2d8 poison or half if DC15-CON passed; if dropped to zero, 1 hour of paralysis after stabilization')
           leg  = Attack('Leg - single target', 7, 0, 'NONE', [1,1,0,0,0,0,0], 'NONE')
           paralyticWeb = Attack('Paralytic Web - single target', 5, 15, 'CON', [0,0,0,0,0,0,0], 'Paralyzed and webbed; action DC15-STR to break free. Webbing MAY be attacked')
           reel   = Attack('Reel - webbed targets', 100, 100, 'CON', [0,0,0,0,0,0,0], 'Pulled 30 feet toward GLL; if within 10ft, bonus action to BITE')
           Monster.__init__(self, 'Goliath Longlegs', 162, 16, 20, [bite, leg, paralyticWeb, reel], 
                           ['Immune to Poison / Charm / Fright',
                            'Dark Vision',
                            'Multi-Attack',
                            'Expansive - smaller creatures can travel through safely',
                            'False Appearance (trees)',
                            'Forest Camoflauge (adv on stealth checks)',
                            'Vulnerable Legs: 20+ damage/turn loses leg. if < 4 legs, DC13 CON or knocked prone'],
                           ['FOREST'],
                           7,
                           4, 2, 3, -3, 1, -4)
    
    # I1
    class Imp(Monster):
    
       libraryIndex = 'I1'
        
       def __init__(self):
           stingBite    = Attack('Sting / Bite', 5, 100, 'CON', [2,0,0,0,0,0,0], '3d10 poison or half if DC11 - CON passed')
           invisibility = Attack('Inivisibility', 100, 100, 'INT', [0,0,0,0,0,0,0], 'Magically turns invisible until concentration broken')
           Monster.__init__(self, 'Imp', 10, 13, 40, [stingBite, invisibility], 
                           ['Dark Vision',
                           'Devil\'s Sight',
                           'Shape Changer: Rat / Raven / Spider / Beast',
                           'Resistant: Cold, Bldg, Piercing, Slsh, Nonmagical Weapons, Fire, Poison'],
                           ['FOREST', 'DESERT', 'WATER', 'TOWN'],
                           1,
                           -2, 3, 1, 0, 1, 2)
    
    # I2
    class IntellectDevourer(Monster):
    
       libraryIndex = 'I2'
        
       def __init__(self):
           claw            = Attack('Claw - single target', 4, 0, 'NONE', [3,0,0,0,0,0,0], 'NONE')
           devourIntellect = Attack('Devour Intellect - single target', 100, 12, 'INT', [0,0,0,0,0,0,0], 'Take 2d10 psychic damage - then roll 3d6. If higher than int score, become incapacitated')
           bodyThief       = Attack('Body Thieve - incapacitated target', 100, 100, 'INT', [0,0,0,0,0,0,0], 'Incapacitated creature is under control of the devourer until HP becomes 0')
           Monster.__init__(self, 'Intellect Devourer', 21, 12, 40, [claw, devourIntellect, bodyThief], 
                           ['Blind Sight',
                            'Telepathy',
                            'Detect Sentience',
                            'Multi-Attack'],
                           ['TOWN', 'FOREST'],
                           3,
                           -2, 2, 1, 1, 0, 0)
    
    # J1
    class Jinmenju(Monster):
    
       libraryIndex = 'J1'
        
       def __init__(self):
           root           = Attack('Root - single target', 7, 0, 'NONE', [1,4,0,2,0,0,0], 'NONE')
           mirthfulMiasma = Attack('Mirthful Miasma - radius', 100, 100, 'CON', [0,0,0,0,0,0,0], 'Puff of purple gas... DC16 - CON or incapacitated with laughter for 1 minute')
           Monster.__init__(self, 'Jinmenju', 126, 14, 0, [root, mirthfulMiasma], 
                           ['Multi-Attack',
                            'Immune to Bldg, Prc, nonmagic Slsh, Exhaustion, Prone',
                            'Laughing Fruit - DC16 WIS or fall prone (laughter)'],
                           ['FOREST', 'TOWN'],
                           9,
                           3, -5, 4, 3, -1, 6)
    
    # L1
    class LitchLord(Monster):
    
       libraryIndex = 'L1'
        
       def __init__(self):
           unholySmite        = Attack('Unholy Smite - only action per turn', 5, 17, 'WIS', [0,2,2,0,0,0,0], 'Charmed for 1 minute; defends the litch until DC17-WIS or duration passed')
           damnation          = Attack('Damnation - single target', 100, 17, 'WIS', [0,0,0,0,0,0,0], 'Threatened with eternal damnation. DC17-WIS repeatable: FRIGHTENED for up to 1 minute')
           guidance           = Attack('Guidance - 1 willing creature', 100, 'WIS', '100', [0,0,0,0,0,0,0], 'Add 1d4 to any ability check (touch range)')
           mending            = Attack('Mending - not really an attack', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Repair Damage to Object')
           sacredFlame        = Attack('Sacred Flame', 100, 17, 'DEX', [0,0,0,0,0,0,0], '1d8 fire + radiant damage')
           thaumatergy        = Attack('Thaumatergy - existing stimuli', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Amplify sounds / lights / flame / etc')
           command            = Attack('Command - single target', 100, 17, 'WIS', [0,0,0,0,0,0,0], 'Whisper 1 word command; if failed save, must obey (non-harmful command)')
           detectMagic        = Attack('Detect Magic', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Magic Detected; range 30ft')
           goodEvilProtection = Attack('Protection from Good and Evil - touched target', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Touched creature has resistance and protection from choice of entity types')
           sanctuary          = Attack('Sanctuary - self', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Attacker passes DC17-WIS or chooses new target')
           blindnessDeafness  = Attack('Blindness / Deafness', 100, 17, 'CON', [0,0,0,0,0,0,0], 'Creature blinded / deafened until DC17-CON passed')
           holdPerson         = Attack('Hold Person', 100, 17, 'WIS', [0,0,0,0,0,0,0], 'Paralyzed until DC17-WIS passed (or one minute)')
           silence            = Attack('Silence', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'For < 10 minutes, no sound can be created in a 20ft sphere; no thunder damage or verbal component spells either.')
           animateDead        = Attack('Animate Dead', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Creates undead servant (out of any bones or corpse in sight)')
           dispelMagic        = Attack('Dispel Magic', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Dispel effect of any level 3 or lower spell; if higher, DC10+spell level WIS check')
           spiritGuardian     = Attack('Spirit Guardian', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Wall of spirits protect you (<10 min); creatures entering / starting turn inside 15ft take 3d8 necrotic')
           banishment         = Attack('Banishment', 100, 17, 'CHA', [0,0,0,0,0,0,0], 'Banished to another plane of existence for 1 minute; incapacitated')
           freedomOfMovement  = Attack('Freedom of Movement - willing target', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Target unaffected by difficult terrain; if grappled, can use 5ft move speed to free itself')
           guardianOfFaith    = Attack('Guardian of Faith', 100, 100, 'WIS', [0,0,0,0,0,0,0], 'Large spectral guardian with gleaming sword/shield appears; creatures in that space make DC17-DEX 20 radiant damage or half')
           flameStrike        = Attack('Flame Strike', 100, 100, 'DEX', [0,0,0,0,0,0,0], '10ft radius column of divine fire falls; DC17 DEX save. 4d6 fire 4d6 radiant on failure, else half.')
           Monster.__init__(self, 'Litch Lord', 91, 14, 30, [unholySmite, damnation, guidance, mending, sacredFlame, thaumatergy, command, detectMagic, goodEvilProtection, sanctuary, blindnessDeafness, 
                                                             holdPerson, silence, animateDead, dispelMagic, spiritGuardian, banishment, freedomOfMovement, guardianOfFaith, flameStrike], 
                           ['True Sight',
                            'Resistant: cold, lightning, necrotic',
                            'Immune: poison, non-magical weapons',
                            'Cannot be charmed, exhausted, frightened, paralyzed, or poisoned',
                            'Levitate: can levitate up to 20ft and remain there; no duration or concentration',
                            'Turn Resistance: advantage on saving throws against any effect that turns undead',
                            'Legendary Resistance: can choose to succeed up to 3 failed saves'],
                           ['TOWN', 'FOREST', 'DESERT'],
                           21,
                           1, 1, 2, 1, 5, 3)
    
    # L2
    class LivingShade(Monster):
    
       libraryIndex = 'L2'
        
       def __init__(self):
           shadowTouch = Attack('Shadow Touch - single target', 4, 0, 'NONE', [2,0,0,0,0,0,0], 'NONE')
           Monster.__init__(self, 'Living Shade', 18, 12, 40, [shadowTouch], 
                           ['Amorphous',
                            'Dark Vision',
                            'Shadow Stealth',
                            'Sunlight Sensitivity'],
                           ['TOWN', 'FOREST'],
                           1/4,
                           -2, 2, 0, -1, 0, 1)
    
    # M1
    class Mimic(Monster):
    
       libraryIndex = 'M1'
        
       def __init__(self):
           bite      = Attack('Bite - single target', 5, 0, 'NONE', [1,0,2,0,0,0,0], 'NONE')
           pseudopod = Attack('Pseudopod - single target', 5, 100, 'STR', [1,0,1,0,0,0,0], 'Victim subject to \'adhesive\' ability')
           Monster.__init__(self, 'Mimic', 58, 12, 15, [bite, pseudopod], 
                           ['Shape Changer',
                            'False Appearance',
                            'Grappler (advantage against creatures adhered)',
                            'Adhesive (DC13 - STR or grappled with disadvantage on save)'],
                           ['TOWN', 'FOREST', 'DESERT'],
                           2,
                           3, 1, 2, -3, 1, -1)
    
    # N1
    class Neophron(Monster):
    
       libraryIndex = 'N1'
        
       def __init__(self):
           bite = Attack('Bite - single target', 7, 16, 'DEX', [1,0,0,2,0,0,0], 'SWALLOWED - 4d6 each turn. On death, becomes Ghast. if 20 damage taken in a turn, regurgitated')
           claw = Attack('Claw - single target', 7, 16, 'CON', [1,2,0,0,0,0,0], 'Poisoned until end of next turn')
           Monster.__init__(self, 'Neophron', 114, 16, 40, [bite, claw], 
                           ['Immune to poison',
                            'Dark Vision',
                            'Multi-Attack',
                            'Shape Changer: Giant Vulture',
                            'Magic Resistance',
                            'Resistant to Cold / Fire / Lightning / Bludg / Pierc/ Slash'],
                           ['FOREST', 'DESERT', 'TOWN'],
                           8,
                           4, 3, 5, -1, 3, 2)
    
    # N2
    class Nothic(Monster):
    
       libraryIndex = 'N2'
        
       def __init__(self):
           claw         = Attack('Claw - single target', 4, 0, 'NONE', [1,1,0,0,0,0,0], 'NONE')
           rottingGaze  = Attack('Rotting Gaze - single target', 100, 12, 'CON', [0,0,0,0,0,0,0], 'Victim takes 3d10 necrotic damage')
           weirdInsight = Attack('Weird Insight', 100, 100, 'CHA', [0,0,0,0,0,0,0], 'If this save fails against the Nothic\'s WIS check, 1 secret immediately learned')
           Monster.__init__(self, 'Nothic', 45, 15, 30, [claw, rottingGaze, weirdInsight], 
                           ['Multi-Attack',
                            'True Sight',
                            'Keen Sight - advantage on wisdom checks relying on sight'],
                           ['TOWN', 'FOREST'],
                           2,
                           2, 3, 3, 1, 0, -1)
    
    # P1
    class PishachaDemon(Monster):
    
       libraryIndex = 'P1'
        
       def __init__(self):
           bite              = Attack('Bite - single target', 5, 0, 'NONE', [1,0,2,0,0,0,0], 'NONE')
           claw              = Attack('Claw - single target', 5, 0, 'NONE', [1,2,0,0,0,0,0], 'NONE')
           demonicPossession = Attack('Demonic Possession - single target', 100, 13, 'WIS', [0,0,0,0,0,0,0], 'Possessed by Pishacha Demon. 3d6 rounds of sporratic movements, then dormant. Wait 1d4 hours then repeat DC13 WIS save. If still possessed after long rest, PERMANENT MADNESS')
           Monster.__init__(self, 'Pishacha Demon', 55, 13, 30, [bite, claw, demonicPossession], 
                           ['Dark Vision',
                            'Telepathy',
                            'Multi-Attack',
                            'Shape Changer: Wolf / Tiger'],
                           ['TOWN', 'FOREST', 'DESERT'],
                           3,
                           3, 2, 1, 0, 3, -2)
    
    # R1
    class RugOfSmothering(Monster):
    
       libraryIndex = 'R1'
        
       def __init__(self):
           smother = Attack('Smother - single target', 100, 13, 'STR', [0,0,0,0,0,0,0], 'Stuck until DC-13 STR passed; takes same damage at start of each turn (1d4 + 2d6)')
           Monster.__init__(self, 'Rug of Smothering', 33, 18, 25, [smother], 
                           ['Anti-Magic Susceptibiltiy',
                            'False Appearance',
                            'Damage Transfer (half to targets wrapped inside)',
                            'Immune to Poison / Psychic / Blindness / Charmed / Deafness / Fear / Paralysis'],
                           ['TOWN'],
                           2,
                           3, 2, 0, -5, -4, -5)
    
    # S1
    class ShadowOoze(Monster):
    
       libraryIndex = 'S1'
        
       def __init__(self):
           pseudopod = Attack('Pseudopod - single target', 5, 0, 'NONE', [2,3,0,0,0,0,0], 'NONE')
           snuffOut  = Attack('Snuff Out - single light source', 100, 100, 'CON', [0,0,0,0,0,0,0], 'Extinguishes any targeted light within 60 feet')
           Monster.__init__(self, 'Shadow Ooze', 76, 8, 20, [pseudopod, snuffOut], 
                           ['Amorphous',
                            'Spider Climb',
                            'Blind Sight',
                            'Aura of Darkness (destroys all light w/in 30 feet)',
                            'Multi-Attack'],
                           ['TOWN', 'FOREST', 'DESERT'],
                           3,
                           3, -2, 4, -4, -2, -4)
    
    # S2
    class ShadowSkeleton(Monster):
    
       libraryIndex = 'S2'
        
       def __init__(self):
           scimitar    = Attack('Scimitar', 5, 0, 'NONE', [0,1,1,0,0,0,0], 'NONE')
           fingerDarts = Attack('Finger Darts', 5, 12, 'CON', [1,1,0,0,0,0,0], 'Surrounded by shady aura until extinguished by DC12 - CON (by any player); scimitar deals extra 2d6')
           Monster.__init__(self, 'Shadow Skeleton', 52, 13, 30, [scimitar, fingerDarts], 
                           ['Dark Vision',
                            'Multi-Attack',
                            'Omnilingual'],
                           ['TOWN', 'FOREST', 'DESERT', 'WATER'],
                           2,
                           0, 3, 2, -1, 0, -1)
    
    # S3
    class ShamblingMound(Monster):
    
       libraryIndex = 'S3'
        
       def __init__(self):
           slam   = Attack('Slam - single target', 7, 0, 'NONE', [1,0,2,0,0,0,0], 'NONE')
           engulf = Attack('Engulf - grappled from previous slam', 100, 100, 'CON', [0,0,0,0,0,0,0], 'Beginning of Mound\'s turn: if Fail DC14 - CON take 2d8+4')
           Monster.__init__(self, 'Shambling Mound', 136, 15, 20, [slam, engulf], 
                           ['Resistant to Cold and Fire',
                            'Immune to Lightning, Blindness, Deafness, Exhaustion',
                            'Blind Sight',
                            'Absorbs Lightning Damage',
                            'Multi-Attack: 2 slams grappled and uses engulf if hit'],
                           ['FOREST', 'WATER'],
                           5,
                           4, -1, 3, -3, 0, -3)
    
    # S4
    class Spectator(Monster):
    
       libraryIndex = 'S4'
        
       def __init__(self):
           bite    = Attack('Bite', 1, 0, 'NONE', [0,1,0,0,0,0,0], 'NONE')
           eyeRay1 = Attack('Eye Ray - Confusion', 1, 13, 'WIS', [0,0,0,0,0,0,0], 'Confused until end of next turn')
           eyeRay2 = Attack('Eye Ray - Parayze', 1, 13, 'CON', [0,0,0,0,0,0,0], 'Paralyzed for 1 minute or until DC13-CON passed')
           eyeRay3 = Attack('Eye Ray - Fear', 1, 13, 'WIS', [0,0,0,0,0,0,0], 'Frightened for 1 minute or until DC13-WIS passed')
           eyeRay4 = Attack('Eye Ray - WOUND', 1, 100, 'CON', [0,0,0,0,0,0,0], '3d10 or half if DC13 - CON passed')
           Monster.__init__(self, 'Spectator', 39, 14, 30, [bite, eyeRay1, eyeRay2, eyeRay3, eyeRay4], 
                           ['Dark Vision',
                            'Spell Reflection: target other creature when not hit'],
                           ['TOWN', 'DESERT', 'FOREST'],
                           3,
                           -1, 2, 2, 1, 2, 0)
    
    # S5
    class SpinedDevil(Monster):
    
       libraryIndex = 'S5'
        
       def __init__(self):
           bite  = Attack('Bite', 2, 0, 'NONE', [2,0,0,0,0,0,0], 'NONE')
           fork  = Attack('Fork', 2, 0, 'NONE', [0,1,0,0,0,0,0], 'NONE')
           spine = Attack('Tail Spine', 4, 0, 'NONE', [1,1,0,0,0,0,0], 'NONE')
           Monster.__init__(self, 'Spined Devil', 22, 13, 40, [bite, fork, spine], 
                           ['Devil\'s Sight',
                            'Flyby (no attacks of opportunity)',
                            'Limited Spines (12...)',
                            'Multi-Attack',
                            'Magic Resistance (adv on saves)'],
                           ['FOREST', 'DESERT', 'WATER', 'TOWN'],
                           2,
                           0, 2, 1, 0, 2, -1)
    
    # V1
    class VillagerBasic(Monster):
    
       libraryIndex = 'V1'
        
       def __init__(self):
           shortSword   = Attack('Short Sword', 2, 0, 'NONE', [0,1,0,0,0,0,0], 'NONE')
           Monster.__init__(self, 'Villager - Basic', 15, 10, 25, [shortSword], 
                           ['Advantage while around any other villagers',
                            'Passes all wisdom checks'],
                           ['TOWN'],
                           1,
                           0, 2, 1, -1, 100, -1)
    
    # V2
    class VillagerPlus(Monster):
    
       libraryIndex = 'V2'
        
       def __init__(self):
           longSword   = Attack('Long Sword', 4, 0, 'NONE', [1,0,1,0,0,0,0], 'NONE')
           fireBomb    = Attack('Fire Bomb', 6, 100, 'DEX', [0,0,2,0,0,0,0], 'DEX save 12 takes half damage - else full damage and on fire')
           Monster.__init__(self, 'Villager +', 20, 14, 30, [longSword, fireBomb], 
                           ['ability Advantage while around any elites',
                            'Passes all wisdom checks',
                            'Intimidation - CHA save 12 or disadvantage'],
                           ['TOWN'],
                           3,
                           2, 2, 4, 0, 100, 2)
    
    # V3
    class VillagerElite(Monster):
    
       libraryIndex = 'V3'
        
       def __init__(self):
           greatAxe   = Attack('Great Axe', 6, 0, 'NONE', [1,0,0,0,1,0,0], 'NONE')
           fireBurst  = Attack('Fire Burst', 6, 100, 'DEX', [0,0,2,0,0,0,0], 'On fire, big bang, much ouch unless DC 14 DEX save (else half damage)')
           bigFist    = Attack('Big \'ol FIST', 4, 14, 'CON', [0,2,0,0,0,0,0], 'Knocked prone and dazed')
           Monster.__init__(self, 'Villager ELITE', 30, 17, 30, [greatAxe, fireBurst, bigFist], 
                           ['Passes all wisdom checks',
                            'Intimidation - CHA save 12 or disadvantage'],
                           ['TOWN'],
                           5,
                           6, -1, 4, -2, 100, 2)
    
    # W1
    class WeirdingScroll(Monster):
    
       libraryIndex = 'W1'
        
       def __init__(self):
           lightTendril = Attack('Tendril of Light', 5, 0, 'NONE', [0,2,0,0,0,0,0], 'consequence')
           dominate     = Attack('Dominate', 100, 13, 'WIS', [0,0,0,0,0,0,0], 'Charmed for 1 hour. Obey Scroll\'s command to the best of their ability. DC13 WIS to check whenever damage is taken')
           Monster.__init__(self, 'Weirding Scroll', 27, 10, 10, [lightTendril, dominate], 
                           ['Blind Sight',
                            'Omnilingual',
                            'Antimagic Susceptibility',
                            'False Appearance'],
                           ['TOWN', 'DESERT'],
                           1/2,
                           -5, 0, 2, 3, 0, -1)
    
    # W2
    class Will_o_Wisp(Monster):
    
       libraryIndex = 'W2'
        
       def __init__(self):
           shock        = Attack('Shock', 4, 0, 'NONE', [0,0,2,0,0,0,0], 'NONE')
           consumeLife  = Attack('Consume Life (on targets with 0 hp)', 100, 10, 'CON', [0,0,0,0,0,0,0], 'Target is DEAD if fails; whisp regains 10 hp')
           invisibility = Attack('Invisibility', 100, 100, 'NONE', [0,0,0,0,0,0,0], 'Wisp becomes invisible until attacks or consumes life')
           Monster.__init__(self, 'Will o\' Wisp', 22, 19, 50, [shock, consumeLife, invisibility], 
                           ['Dark Vision',
                            'Variable Illumination: 5-20 feet',
                            'Immune: Ltng / Exh / Grpl / Prz / Psn / Prone / Restrained / Unconscious'],
                           ['FOREST', 'TOWN'],
                           2,
                           -5, 9, 0, 1, 2, 0)
    
    # Z1
    class Zoog(Monster):
    
       libraryIndex = 'Z1'
        
       def __init__(self):
           bite = Attack('Bite', 5, 0, 'NONE', [1,0,0,0,0,0,0], 'NONE')
           Monster.__init__(self, 'Zoog', 5, 13, 30, [bite], 
                           ['Dark Vision'],
                           ['TOWN', 'FOREST'],
                           0,
                           -4, 3, 1, 0, 0, -1)
    
    ##################################################################################################################
    #class MonsterName(Monster):
    #
    #   libraryIndex = '(letter-number)'
    #    
    #   def __init__(self):
    #       attackName   = Attack('AttackName', attackMod, attackSave, 'saveType', [0,0,0,0,0,0,0], 'consequence')
    #       Monster.__init__(self, 'creatureName', health, AC, speed, [attackList], 
    #                       ['abilities'],
    #                       ['environments'],
    #                       0,
    #                       0, 0, 0, 0, 0, 0)
    ##################################################################################################################
    
    
    def printMonsterList(self, challenge=1):
        print('Monster List...')
        monstersPrinted = 0
        for i, m in self.monsterLibrary.items():
            if float(m[1]) <= challenge:
                print(f'{i}.) {m[0]} - {m[1]}')
                monstersPrinted += 1
            else:
                pass
        if monstersPrinted > 0:
            return
        else:
            print("No monsters meet the needed criteria. Fatal error setting up encounter.")
            exit()
            
    def addRandomMonster(self, challenge=1):
        print('Random Monster...')
        top = len(self.libraryIndices)
        validMonster = False
        while not validMonster:
            randomChoice = random.randrange(0, top, 1)
            newMonster = self.chooseMonster(self.libraryIndices[randomChoice])
            if (newMonster.mChallengeRating <= challenge):
                validMonster = True
            else:
                print("Too hard, trying again.")
        return newMonster
    
    def checkMonsterEnvironment(self, env, monster):
        envValid = False
        for e in monster.mEnvironment:
            if env == e:
                envValid = True
            elif env == 'ANY':
                envValid = True
        return envValid
    