import pickle

all_races = {
    'altmer': {
        'strength': (30, 30),
        'intelligence': (50, 50),
        'willpower': (40, 40),
        'agility': (40, 40),
        'speed': (30, 40),
        'endurance': (40, 30),
        'personality': (40, 40),
        'luck': (50, 50),
        'magicka': (100, 100),
        'skills': [
            ('alchemy',5),
            ('alteration',10),
            ('conjuration',5),
            ('destruction',10),
            ('illusion',5),
            ('mysticism',10),
        ]
    },
    'argonian': {
        'strength': (40, 40),
        'intelligence': (40, 50),
        'willpower': (30, 40),
        'agility': (50, 40),
        'speed': (50, 40),
        'endurance': (30, 30),
        'personality': (30, 30),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('alchemy',5),
            ('athletics',10),
            ('blade',5),
            ('hand-to-hand',5),
            ('illusion',5),
            ('mysticism',5),
            ('security',10),
            ]
    },
    'bosmer': {
        'strength': (30, 30),
        'intelligence': (40, 40),
        'willpower': (30, 30),
        'agility': (50, 50),
        'speed': (50, 50),
        'endurance': (40, 30),
        'personality': (30, 40),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('acrobatics',5),
            ('alchemy',10),
            ('alteration',5),
            ('light armor',5),
            ('marksman',10),
            ('sneak',10),
    ]
    },
    'breton': {
        'strength': (40, 30),
        'intelligence': (50, 50),
        'willpower': (50, 50),
        'agility': (30, 30),
        'speed': (30, 40),
        'endurance': (30, 30),
        'personality': (40, 40),
        'luck': (50, 50),
        'magicka': (50, 50),
        'skills': [
            ('alchemy',5),
            ('alteration',5),
            ('conjuration',10),
            ('illusion',5),
            ('mysticism',10),
            ('restoration',10),
    ]
    },
    'dunmer': {
        'strength': (40, 40),
        'intelligence': (40, 40),
        'willpower': (30, 30),
        'agility': (40, 40),
        'speed': (50, 50),
        'endurance': (40, 30),
        'personality': (30, 40),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('athletics',5),
            ('blade',10),
            ('blunt',5),
            ('destruction',10),
            ('light armor',5),
            ('marksman',5),
            ('mysticism',5),
    ]
    },
    'imperial': {
        'strength': (40, 40),
        'intelligence': (40, 40),
        'willpower': (30, 40),
        'agility': (30, 30),
        'speed': (40, 30),
        'endurance': (40, 40),
        'personality': (50, 50),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('blade',5),
            ('blunt',5),
            ('hand-to-hand',5),
            ('heavy armor',10),
            ('mercantile',10),
            ('speechcraft',10),
    ]
    },
    'khajiit': {
        'strength': (40, 30),
        'intelligence': (40, 40),
        'willpower': (30, 30),
        'agility': (50, 50),
        'speed': (40, 40),
        'endurance': (30, 40),
        'personality': (40, 40),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('acrobatics',10),
            ('athletics',5),
            ('blade',5),
            ('hand-to-hand',10),
            ('light armor',5),
            ('security',5),
            ('sneak',5),
    ]
    },
    'nord': {
        'strength': (50, 50),
        'intelligence': (30, 30),
        'willpower': (30, 40),
        'agility': (40, 40),
        'speed': (40, 40),
        'endurance': (50, 40),
        'personality': (30, 30),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('armorer',5),
            ('blade',10),
            ('block',5),
            ('blunt',10),
            ('heavy armor',10),
            ('restoration',5),
    ]
    },
    'orc': {
        'strength': (45, 45),
        'intelligence': (30, 40),
        'willpower': (50, 45),
        'agility': (35, 35),
        'speed': (30, 30),
        'endurance': (50, 50),
        'personality': (30, 25),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('armorer',10),
            ('block',10),
            ('blunt',10),
            ('hand-to-hand',5),
            ('heavy armor',10),
    ]
    },
    'redguard': {
        'strength': (50, 40),
        'intelligence': (30, 30),
        'willpower': (30, 30),
        'agility': (40, 40),
        'speed': (40, 40),
        'endurance': (50, 50),
        'personality': (30, 40),
        'luck': (50, 50),
        'magicka': (0, 0),
        'skills': [
            ('athletics',10),
            ('blade',10),
            ('blunt',10),
            ('heavy armor',5),
            ('light armor',5),
            ('mercantile',5),
    ]
    },
    }

all_attributes = [
    'strength',
    'intelligence',
    'willpower',
    'agility',
    'speed',
    'endurance',
    'personality',
    'luck',
    ]

all_skills = [
    'acrobatics',
    'alchemy',
    'alteration',
    'armorer',
    'athletics',
    'blade',
    'block',
    'blunt',
    'conjuration',
    'destruction',
    'hand-to-hand',
    'heavy armor',
    'illusion',
    'light armor',
    'marksman',
    'mercantile',
    'mysticism',
    'restoration',
    'security',
    'sneak',
    'speechcraft',
    ]

all_birthsigns = [
    'apprentice',
    'atronach',
    'lady',
    'lord',
    'lover',
    'mage',
    'ritual',
    'serpent',
    'shadow',
    'steed',
    'thief',
    'tower',
    'warrior',
    ]

skill_attribute_mappings = {
    'acrobatics': 'speed',
    'alchemy': 'intelligence',
    'alteration': 'willpower',
    'armorer': 'endurance',
    'athletics': 'speed',
    'blade': 'strength',
    'block': 'endurance',
    'blunt': 'strength',
    'conjuration': 'intelligence',
    'destruction': 'willpower',
    'hand-to-hand': 'strength',
    'heavy armor': 'endurance',
    'illusion': 'personality',
    'light armor': 'speed',
    'marksman': 'agility',
    'mercantile': 'personality',
    'mysticism': 'intelligence',
    'restoration': 'willpower',
    'security': 'agility',
    'sneak': 'agility',
    'speechcraft': 'personality',
    }

all_specialisations = {
        'combat': [
            'armorer',
            'athletics',
            'blade',
            'block',
            'blunt',
            'hand-to-hand',
            'heavy armor',
            ],
        'magic': [
            'alchemy',
            'alteration',
            'conjuration',
            'destruction',
            'illusion',
            'mysticism',
            'restoration',
            ],
        'stealth': [
            'acrobatics',
            'light armor',
            'marksman',
            'mercantile',
            'security',
            'sneak',
            'speechcraft',
            ]
        }

character_journal_skill_order = []
for x in all_specialisations:
    for y in all_specialisations[x]:
        character_journal_skill_order.append(y)

class CharacterClass:
    def __init__(self, name, specialisation, favoured_attributes, major_skills):
        self.name = name
        if specialisation not in ['combat','magic','stealth']:
            raise RuntimeError('Invalid specialisation')
        self.specialisation = specialisation

        if len(favoured_attributes) != 2 or not all([x in all_attributes for x in favoured_attributes]):
            raise RuntimeError('Invalid favoured attributes')
        self.favoured_attributes = favoured_attributes

        if len(major_skills) != 7 or not all([x in all_skills for x in major_skills]):
            raise RuntimeError('Invalid major skills')
        self.major_skills = major_skills

    def __str__(self):
        return '''Character class {} -
Specialisation = {}
Favoured attributes = {}
Major skills = {}'''.format(self.name,self.specialisation,self.favoured_attributes,self.major_skills)

class Character:
    def __init__(self,race,gender,character_class,birthsign):
        # validate and set race, gender, class
        if race not in all_races:
            raise RuntimeError('Invalid race - in the narrow context of TES4: Oblivion anyway :)')
        self.race = race

        if gender not in ['f','m']:
            raise RuntimeError('Invalid gender - in the narrow context of TES4: Oblivion anyway :)')
        self.gender = gender

        if type(character_class) != CharacterClass:
            raise RuntimeError('Invalid class')
        self.character_class = character_class

        # calculate attributes from race+gender and class
        # also initialise magicka bonus
        if self.gender == 'f':
            self.attributes = {x: all_races[self.race][x][1] for x in all_attributes}
            self.magicka_racial_bonus = all_races[self.race]['magicka'][1]
        elif self.gender == 'm':
            self.attributes = {x: all_races[self.race][x][0] for x in all_attributes}
            self.magicka_racial_bonus = all_races[self.race]['magicka'][0]
        for x in self.character_class.favoured_attributes:
                self.attributes[x] += 5

        # handle birthsign
        if birthsign not in all_birthsigns:
            raise RuntimeError('Invalid birthsign')
        self.birthsign = birthsign
        self.magicka_birthsign_bonus = 0
        if self.birthsign == 'apprentice':
            self.magicka_birthsign_bonus = 100
        elif self.birthsign == 'atronach':
            self.magicka_birthsign_bonus = 150
        elif self.birthsign == 'lady':
            self.attributes['willpower'] += 10
            self.attributes['endurance'] += 10
        elif self.birthsign == 'mage':
            self.magicka_birthsign_bonus = 50
        elif self.birthsign == 'steed':
            self.attributes['speed'] += 20
        elif self.birthsign == 'thief':
            self.attributes['agility'] += 10
            self.attributes['luck'] += 10
            self.attributes['speed'] += 10
        elif self.birthsign == 'warrior':
            self.attributes['endurance'] += 10
            self.attributes['strength'] += 10
        else:
            # nothing which interests us here
            pass

        # initialise health and calculate derived attributes
        self.health = self.attributes['endurance'] * 2
        self.calculateDerivedAttributes()

        # calculate skills from race and class
        self.skills = {x: 5 for x in all_skills}
        for x in self.character_class.major_skills:
            self.skills[x] = 25
        for x in all_specialisations[self.character_class.specialisation]:
            self.skills[x] += 5
        for x in all_races[self.race]['skills']:
            self.skills[x[0]] += x[1]

        # calculate level cap and levelling margin of error (available - required = spare)
        available_major_skill_ups = 0
        self.available_skill_ups = {x:0 for x in all_attributes}
        for x in all_skills:
            ups = (100 - self.skills[x])
            self.available_skill_ups[skill_attribute_mappings[x]] += ups
            if x in self.character_class.major_skills:
                available_major_skill_ups += ups
        self.level_skill_cap = (available_major_skill_ups // 10) + 1
        # don't need to worry about remainders on next line - guaranteed to be divisible by 5
        self.required_attribute_ups = {x:(100 - self.attributes[x])//5 for x in all_attributes[:-1]}
        self.required_attribute_ups['luck'] = (100 - self.attributes['luck'])
        self.spare_skill_ups = {x:self.available_skill_ups[x] - 10*self.required_attribute_ups[x] for x in all_attributes[:-1]}
        self.spare_skill_ups['luck'] =  self.level_skill_cap - self.required_attribute_ups['luck'] - 1
        self.wasted_skill_ups = {x:0 for x in all_attributes}

        # calculate everything else
        self.level = 1
        self.level_up_history = {
                1: {
                    'health': self.health,
                    'skills': self.skills.copy(),
                    'attributes': self.attributes.copy(),
                    }
                }
        self.times_trained_this_level = 0
        self.level_up_progress = 0
        self.level_up_attribute_bonuses = {x:0 for x in all_attributes}
        self.level_up_available = False

    def __str__(self):
        if self.gender == 'f':
            friendly_gender = 'Female'
        elif self.gender == 'm':
            friendly_gender = 'Male'
        return '{} {}, class {}'.format(friendly_gender,self.race.title(),self.character_class.name)

    def increase_skill(self, skill, magnitude=1, trained=False):
        if self.level_up_available:
            raise RuntimeError('Level up first')
        if self.skills[skill] + magnitude > 100:
            raise RuntimeError('Aborting safely - can\'t skill up past 100')
        if trained and self.times_trained_this_level + magnitude > 5:
            raise RuntimeError('Aborting - this exceeds the training limit for this level')

        if skill in self.character_class.major_skills:
            level_up_result = self.level_up_progress + magnitude
            if level_up_result > 10:
                raise RuntimeError('Aborting safely - this increase over-levels by {}'.format(level_up_result - 10))
            self.level_up_progress += magnitude
            self.skills[skill] += magnitude
            self.level_up_attribute_bonuses[skill_attribute_mappings[skill]] += magnitude
            if trained:
                self.times_trained_this_level += magnitude
            if self.level_up_progress == 10:
                # convert number of skill increase to attribute increase bonus
                for x in all_attributes:
                    if self.level_up_attribute_bonuses[x] == 0:
                        self.level_up_attribute_bonuses[x] = 1
                    elif 1 <= self.level_up_attribute_bonuses[x] <= 4:
                        self.level_up_attribute_bonuses[x] = 2
                    elif 5 <= self.level_up_attribute_bonuses[x] <= 7:
                        self.level_up_attribute_bonuses[x] = 3
                    elif 8 <= self.level_up_attribute_bonuses[x] <= 9:
                        self.level_up_attribute_bonuses[x] = 4
                    else:
                        self.level_up_attribute_bonuses[x] = 5
                self.level_up_available = True
                print('Level up available')

        else:
            self.skills[skill] += magnitude
            self.level_up_attribute_bonuses[skill_attribute_mappings[skill]] += magnitude
            if trained:
                self.times_trained_this_level += magnitude

    def calculate_wasted_skill_ups(self):
        # wasted skill ups
        self.wasted_skill_ups = {x:0 for x in all_attributes}
        for x in all_skills:
            self.wasted_skill_ups[skill_attribute_mappings[x]] += self.skills[x] - self.level_up_history[1]['skills'][x]
        # TODO (maybe): relax efficient levelling assumption
        # works for efficient levelling only
        for x in all_attributes[:-1]:
            self.wasted_skill_ups[x] -= (self.attributes[x] - self.level_up_history[1]['attributes'][x]) * 2
        self.wasted_skill_ups['luck'] = (self.level - 1) - (self.attributes['luck'] - self.level_up_history[1]['attributes']['luck'])

    def calculateDerivedAttributes(self):
        # we can't handle health here as it relies on state
        self.magicka = self.attributes['intelligence'] * 2 + self.magicka_birthsign_bonus + self.magicka_racial_bonus
        self.fatigue = self.attributes['strength'] + self.attributes['willpower'] + self.attributes['agility'] + self.attributes['endurance']
        self.encumbrance = self.attributes['strength'] * 5

    def levelUp(self,attributes_to_raise='auto'):
        # checks
        if not self.level_up_available:
            raise RuntimeError('Level up not available - aborting')
        under_100_attributes = [x for x in all_attributes if self.attributes[x] < 100]
        if not under_100_attributes:
            raise RuntimeError('All attributes are 100 - aborting')

        # attributes are available to increase: check how many
        number_of_attributes_to_raise = min(3,len(under_100_attributes))
        # autodetecting attributes to raise
        if attributes_to_raise == 'auto':
            if number_of_attributes_to_raise == len(under_100_attributes):
                attributes_to_raise = under_100_attributes
                print(f'Autodetection succeeded - detected {attributes_to_raise}')
                should_continue = 'yes'
            else:
                candidates = []
                for x in under_100_attributes:
                    if self.level_up_attribute_bonuses[x] == 5:
                        candidates.append(x)
                if len(candidates) == 2:
                    attributes_to_raise = candidates + ['luck']
                    print(f'Autodetection succeeded - detected {attributes_to_raise}')
                    should_continue = input('Are you happy with these attributes? Type \'yes\' to proceed\n')
                elif len(candidates) == 3:
                    attributes_to_raise = candidates
                    print(f'Autodetection succeeded - detected {attributes_to_raise}')
                    should_continue = input('Are you happy with these attributes? Type \'yes\' to proceed\n')
                else:
                    raise RuntimeError('Autodetection failed - please specify attributes manually')
            if should_continue != 'yes':
                raise RuntimeError('Aborting - autodetected attributes rejected. Please specify attributes manually')

        # accepting user input of attributes to raise - check for validity
        elif not all(x in under_100_attributes for x in attributes_to_raise) or len(attributes_to_raise) != number_of_attributes_to_raise:
            raise RuntimeError('Invalid attributes')

        # everything is ok - start level up by increasing attributes
        for x in attributes_to_raise:
            self.attributes[x] += self.level_up_attribute_bonuses[x]
            if self.attributes[x] > 100:
                self.attributes[x] = 100

        # recalculate derived attributes
        self.health += self.attributes['endurance'] // 10
        if 'endurance' in attributes_to_raise:
            self.health += self.level_up_attribute_bonuses['endurance'] * 2
        self.calculateDerivedAttributes()

        # reset various things and finally increment level
        self.times_trained_this_level = 0
        self.level_up_progress = 0
        self.level_up_attribute_bonuses = {x:0 for x in all_attributes}
        self.level_up_available = False
        self.level += 1
        self.calculate_wasted_skill_ups()

        # record character state now that level up has been completed
        self.level_up_history[self.level] = {
            'health': self.health,
            'skills': self.skills.copy(),
            'attributes': self.attributes.copy(),
            }

    def override(self,attributes,skills,health,level):
        # assign blindly, check it's ok later
        self.attributes = attributes
        self.skills = skills
        self.health = health
        self.level = level

        # resets due to uncertainty
        self.level_up_history = {
                1: self.level_up_history[1].copy()
                }
        self.level_up_progress = 0
        self.level_up_attribute_bonuses = {x:0 for x in all_attributes}
        self.level_up_available = False

        # recalculate derived things
        self.calculateDerivedAttributes()
        self.calculate_wasted_skill_ups()

        # record character state now that override has been completed
        self.level_up_history[self.level] = {
            'health': self.health,
            'skills': self.skills.copy(),
            'attributes': self.attributes.copy(),
            }

    def validate(self):
        if self.level_up_progress != 0:
            print('This currently only applies to level up milestones')
            return -1
        # the assumption here is that things set by __init__ are reliable
        warnings = False

        # basic attributes and skills checks
        for x in self.attributes:
            if not 1 <= self.attributes[x] <= 100:
                print('Attributes out of bounds')
                warnings = True
        for x in self.skills:
            if not 1 <= self.skills[x] <= 100:
                print('Skills out of bounds')
                warnings = True

        # check impossible level
        if not 1 <= self.level <= self.level_skill_cap:
            print('Invalid level')
            return 2

        # check for nonsense wasted skill calculation
        for x in self.wasted_skill_ups:
            if self.wasted_skill_ups[x] < 0:
                print('Inefficient levelling detected')
                warnings = True

        # does the level add up with the major skills?
        major_skill_ups = 0
        for x in self.character_class.major_skills:
            major_skill_ups += self.skills[x] - self.level_up_history[1]['skills'][x]

        if self.level - 1 != major_skill_ups//10 or major_skill_ups%10 != 0:
            print('Invalid major skills')
            return 2

        # do the level and attributes stack up?
        efficient_attribute_ups = 0
        for x in all_attributes[:-1]:
            efficient_attribute_ups += (self.attributes[x] - self.level_up_history[1]['attributes'][x])//5
        efficient_attribute_ups += self.attributes['luck'] - self.level_up_history[1]['attributes']['luck']
        if efficient_attribute_ups != (self.level - 1) * 3:
            print('Invalid/inefficient attribute increases detected')
            warnings = True

        # check health for efficiency
        # won't work with starting endurance not divisible by 5
        # - AFAIK this isn't possible, so won't worry for now
        endurance_tracker = self.level_up_history[1]['attributes']['endurance']
        healthcheck = endurance_tracker * 2
        if self.level > 1:
            for x in range(2,self.level + 1):
                if endurance_tracker != 100:
                    endurance_tracker += 5
                    healthcheck += (10 + endurance_tracker//10)
                elif endurance_tracker == 100:
                    healthcheck += 10
                else:
                    # this should never happen
                    print('Something went wrong')
                    return 2
        if healthcheck != self.health:
            print('Invalid/inefficient health')
            warnings = True

        if warnings:
            return 1
        else:
            print('Everything looks good :)')
            return 0

    def resetToLastLevel(self):
        # reset skills and attributes
        self.skills = self.level_up_history[self.level]['skills'].copy()
        self.attributes = self.level_up_history[self.level]['attributes'].copy()

        # recalculate wasted skill ups
        self.calculate_wasted_skill_ups()

        # reset level stuff
        self.times_trained_this_level = 0
        self.level_up_progress = 0
        self.level_up_attribute_bonuses = {x:0 for x in all_attributes}
        self.level_up_available = False

    def progressToLevelUp(self):
        if self.level_up_available:
            print('Go level up!')
            return 1
        print(f'''Working towards level {self.level + 1}
majors          {self.level_up_progress:2}/10
------------------''')
        under_100_attributes = [x for x in all_attributes[:-1] if self.attributes[x] < 100]
        for x in under_100_attributes:
            print(f'{x.upper():16}{self.level_up_attribute_bonuses[x]:2}')
        print(f'''------------------
Times trained    {self.times_trained_this_level}/5''')


    def journal(self):
        # print everything
        print(f'''  ____ _                          _            
 / ___| |__   __ _ _ __ __ _  ___| |_ ___ _ __ 
| |   | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__|
| |___| | | | (_| | | | (_| | (__| ||  __/ |   
 \____|_| |_|\__,_|_|  \__,_|\___|\__\___|_|   
   _                              _ 
  (_) ___  _   _ _ __ _ __   __ _| |
  | |/ _ \| | | | '__| '_ \ / _` | |
  | | (_) | |_| | |  | | | | (_| | |
 _/ |\___/ \__,_|_|  |_| |_|\__,_|_|
|__/                                

LEVEL           {self.level:3}       STRENGTH        {self.attributes['strength']:3}
CLASS{self.character_class.name:>14}       INTELLIGENCE    {self.attributes['intelligence']:3}
SIGN{self.birthsign.title():>15}       WILLPOWER       {self.attributes['willpower']:3}
                          AGILITY         {self.attributes['agility']:3}
HEALTH          {self.health:3}       SPEED           {self.attributes['speed']:3}
MAGICKA         {self.magicka:3}       ENDURANCE       {self.attributes['endurance']:3}
FATIGUE         {self.fatigue:3}       PERSONALITY     {self.attributes['personality']:3}
ENCUMBRANCE     {self.encumbrance:3}       LUCK            {self.attributes['luck']:3}

==================
   MAJOR SKILLS   
==================''')
        for x in character_journal_skill_order:
            if x in self.character_class.major_skills:
                print(f'{x:15}{self.skills[x]:3}')
        print('''==================
   MINOR SKILLS   
==================''')
        for x in character_journal_skill_order:
            if x not in self.character_class.major_skills:
                print(f'{x:15}{self.skills[x]:3}')

    def minmax(self):
        # 1/3 - print skill-up margin of error
        # check which attributes are still being levelled
        under_100_attributes = [x for x in all_attributes if self.attributes[x] < 100]
        # lists are false iff empty
        if under_100_attributes:
            print('''==================
 SKILL UP MARGINS 
==================''')
            for x in under_100_attributes:
                progress = round(50 * (self.wasted_skill_ups[x]/self.spare_skill_ups[x]))
                if progress == 0 and self.wasted_skill_ups[x] > 0:
                    progress = 1
                print(f'''{x.upper()}
{self.wasted_skill_ups[x]:3} {"#"*progress}{"."*(50-progress)} {self.spare_skill_ups[x]:3}''')

        # 2/3 - check fastest route to all attributes (except luck) 100 - "7x100" hereafter
        # only supports +5 +5 +1 strategies for now
        # ASSUMPTION: player has enough levels to get 100s all round
        #
        # remove luck from consideration, as always increased in +5 +5 +1
            print('''
==================
ATTRIBUTE ORDERING
==================''')
        under_100_attributes_no_luck = under_100_attributes.copy()
        if 'luck' in under_100_attributes_no_luck:
            under_100_attributes_no_luck.remove('luck')
        if under_100_attributes_no_luck:
            # find lowest attribute and how many increase are left
            lowest_attribute = min(self.attributes)
            lowest_attribute_increases_remaining = (100 - self.attributes[lowest_attribute])//5
            # get other attributes which need increasing
            other_under_100_attributes = under_100_attributes_no_luck.copy()
            other_under_100_attributes.remove(lowest_attribute)
            # see how many increases they need
            other_increases_remaining = 0
            for x in other_under_100_attributes:
                other_increases_remaining += (100 - self.attributes[x])//5
            # make the judgment - free when others greater than, tight when equal or within 1
            difference = other_increases_remaining - lowest_attribute_increases_remaining
            if difference > 0:
                # there's leeway, let's calculate how much
                print(f'''
Status: OK

Increase attributes in any order, although there are only
{(difference + 1)//2} spare level ups until you need to increase {lowest_attribute.upper()}''')
            elif difference in [-1,0]:
                print(f'''
Status: WARNING

Optimal 7x100 level can still be achieved but you must increase
{lowest_attribute.upper()} (or one at the same level) this level up''')
            else:
                print(f'{lowest_attribute} should be increased but 7x100 will already be reached late.')
        else:
            print('Nothing to consider here!')

        # 3/3 - forecast attributes at max level
        # print level, health, magicka, fatigue, encumbrance
        # skills can always all reach 100. I think but haven't verified that it's always possible for all attributes to reach 100 too
        #
        # calculate optimal health
        # won't work with starting endurance not divisible by 5
        # - AFAIK this isn't possible, so won't worry for now
        endurance_tracker = self.level_up_history[1]['attributes']['endurance']
        max_health = endurance_tracker * 2
        lvl = 1
        while lvl < self.level_skill_cap:
            lvl += 1
            if endurance_tracker != 100:
                endurance_tracker += 5
                max_health += (10 + endurance_tracker//10)
            elif endurance_tracker == 100:
                max_health += 10
        # calculate optimal magicka
        max_magicka = 200 + self.magicka_birthsign_bonus + self.magicka_racial_bonus

        # max fatigue and encumbrance are always the same
        max_fatigue = 400
        max_encumbrance = 500

        print(f'''
==================
 IDEAL STATISTICS 
==================
Level       = {self.level_skill_cap:3}
Health      = {max_health:3}
Magicka     = {max_magicka:3}
Fatigue     = {max_fatigue:3}
Encumbrance = {max_encumbrance:3}''')

        # if no attributes being levelled, we should be done:
        # check that things add up
        if not under_100_attributes:
            if self.level == self.level_skill_cap and self.health == max_health:
                print(''' _   _  ___   ___  ____      _ __   ___ 
| | | |/ _ \ / _ \|  _ \    / \\ \ / / |
| |_| | | | | | | | |_) |  / _ \\ V /| |
|  _  | |_| | |_| |  _ <  / ___ \| | |_|
|_| |_|\___/ \___/|_| \_\/_/   \_\_| (_)

You did it, kid.''')
            else:
                print(':( why did this have to happen?')

    def skillLevels(self, specialisation=None):
        if specialisation is not None and specialisation not in all_specialisations:
            raise RuntimeError('Invalid specialisation')
        # setup
        # initialise mastery levels
        mastery = {
                'master': [],
                'expert': [],
                'journeyman': [],
                'apprentice': [],
                'novice': [],
        }
        # narrow down which skills we're checking
        if specialisation:
            skills_to_check = all_specialisations[specialisation]
        else:
            skills_to_check = all_skills
        # check each skill's mastery level
        for x in skills_to_check:
            if 0 <= self.skills[x] <= 24:
                mastery['novice'].append(x)
            elif 25 <= self.skills[x] <= 49:
                mastery['apprentice'].append(x)
            elif 50 <= self.skills[x] <= 74:
                mastery['journeyman'].append(x)
            elif 75 <= self.skills[x] <= 99:
                mastery['expert'].append(x)
            elif self.skills[x] == 100:
                mastery['master'].append(x)

        # print
        # handle spacing by tracking when we print for the first time
        first = True
        # define headings to use loop
        headings = {
                'master': '----- MASTER -----',
                'expert': '----- EXPERT -----',
                'journeyman': '--- JOURNEYMAN ---',
                'apprentice': '--- APPRENTICE ---',
                'novice': '----- NOVICE -----',
        }
        # here we go
        print('''==================
   SKILL LEVELS   
==================''')
        for level in list(mastery):
            if mastery[level]:
                if first:
                    first = False
                else:
                    print()
                print(headings[level])
                for x in mastery[level]:
                    print(f'{x:15}{self.skills[x]:3}')

def saveCharacter(character,savename='saved-character.pickle'):
    with open(savename,'bw') as f:
        f.write(pickle.dumps(character))

def loadCharacter(savename='saved-character.pickle'):
    global c
    try:
        with open(savename,'br') as f:
            c = pickle.loads(f.read())
        print('Saved character loaded as c')
    except:
        print('No saved character found')

def rebuildCharacter(old_character):
    try:
        level = max(list(old_character.level_up_history))
        new_character = Character(old_character.race,old_character.gender,old_character.character_class,old_character.birthsign)
        new_character.override(old_character.level_up_history[level]['attributes'].copy(),old_character.skills.copy(),old_character.health,level)
        new_character.level_up_history = old_character.level_up_history.copy()
        new_character.times_trained_this_level = old_character.times_trained_this_level
        new_character.skills = old_character.level_up_history[level]['skills'].copy()
        for x in all_skills:
            difference = old_character.skills[x] - new_character.skills[x]
            if difference > 0:
                if difference >= 10 and x in new_character.character_class.major_skills:
                    raise RuntimeError('Invalid input character - character should have levelled up')
                new_character.increase_skill(x,difference)

    except:
        print('Something went wrong')
    return new_character

default_classes = {
        'acrobat': CharacterClass('Acrobat','stealth',['agility','endurance'],['blade','block','acrobatics','marksman','security','sneak','speechcraft']),
        'agent': CharacterClass('Agent','stealth',['agility','personality'],['illusion','acrobatics','marksman','mercantile','security','sneak','speechcraft']),
        'archer': CharacterClass('Archer','combat',['agility','strength'],['armorer','blade','blunt','hand-to-hand','light armor','marksman','sneak']),
        'assassin': CharacterClass('Assassin','stealth',['intelligence','speed'],['blade','alchemy','acrobatics','light armor','marksman','security','sneak']),
        'barbarian': CharacterClass('Barbarian','combat',['speed','strength'],['armorer','athletics','blade','block','blunt','hand-to-hand','light armor']),
        'bard': CharacterClass('Bard','stealth',['intelligence','personality'],['blade','block','alchemy','illusion','light armor','mercantile','speechcraft']),
        'battlemage': CharacterClass('Battlemage','magic',['intelligence','strength'],['blade','blunt','alchemy','alteration','conjuration','destruction','mysticism']),
        'crusader': CharacterClass('Crusader','combat',['strength','willpower'],['athletics','blade','blunt','hand-to-hand','heavy armor','destruction','restoration']),
        'healer': CharacterClass('Healer','magic',['personality','willpower'],['alchemy','alteration','destruction','illusion','restoration','mercantile','speechcraft']),
        'knight': CharacterClass('Knight','combat',['personality','strength'],['blade','block','blunt','hand-to-hand','heavy armor','illusion','speechcraft']),
        'mage': CharacterClass('Mage','magic',['intelligence','willpower'],['alchemy','alteration','conjuration','destruction','illusion','mysticism','restoration']),
        'monk': CharacterClass('Monk','stealth',['agility','willpower'],['athletics','hand-to-hand','alteration','acrobatics','marksman','security','sneak']),
        'nightblade': CharacterClass('Nightblade','magic',['speed','willpower'],['athletics','blade','alteration','destruction','restoration','acrobatics','light armor']),
        'pilgrim': CharacterClass('Pilgrim','stealth',['endurance','personality'],['armorer','block','blunt','light armor','mercantile','security','speechcraft']),
        'rogue': CharacterClass('Rogue','combat',['personality','speed'],['athletics','blade','block','alchemy','illusion','light armor','mercantile']),
        'scout': CharacterClass('Scout','combat',['endurance','speed'],['armorer','athletics','blade','block','alchemy','acrobatics','light armor']),
        'sorcerer': CharacterClass('Sorcerer','magic',['endurance','intelligence'],['heavy armor','alchemy','alteration','conjuration','destruction','mysticism','restoration']),
        'spellsword': CharacterClass('Spellsword','magic',['endurance','willpower'],['blade','block','heavy armor','alteration','destruction','illusion','restoration']),
        'thief': CharacterClass('Thief','stealth',['agility','speed'],['acrobatics','light armor','marksman','mercantile','security','sneak','speechcraft']),
        'warrior': CharacterClass('Warrior','combat',['endurance','strength'],['armorer','athletics','blade','block','blunt','hand-to-hand','heavy armor']),
        'witchhunter': CharacterClass('Witchhunter','magic',['agility','intelligence'],['athletics','alchemy','conjuration','destruction','mysticism','marksman','security']),
        }

loadCharacter()
