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
    # TODO (maybe): finish birthsign support
    def __init__(self,race,gender,character_class,birthsign='apprentice'):
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
        # also initialise magicka
        if self.gender == 'f':
            self.attributes = {x: all_races[self.race][x][1] for x in all_attributes}
            self.magicka = all_races[self.race]['magicka'][1]
        elif self.gender == 'm':
            self.attributes = {x: all_races[self.race][x][0] for x in all_attributes}
            self.magicka = all_races[self.race]['magicka'][0]

        for x in self.character_class.favoured_attributes:
                self.attributes[x] += 5

        # calculate derived attributes
        self.health = self.attributes['endurance'] * 2
        self.magicka += self.attributes['intelligence'] * 2
        self.fatigue = self.attributes['strength'] + self.attributes['willpower'] + self.attributes['agility'] + self.attributes['endurance']
        self.encumbrance = self.attributes['strength'] * 5

        # incomplete birthsign logic - apprentice only for now
        self.birthsign = birthsign
        if self.birthsign == 'apprentice':
            self.magicka += 100
        else:
            print('warning - only the apprentice birthsign is implemented for now. skipping')

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
        if 'intelligence' in attributes_to_raise:
            self.magicka += self.level_up_attribute_bonuses['intelligence'] * 2
        self.fatigue = self.attributes['strength'] + self.attributes['willpower'] + self.attributes['agility'] + self.attributes['endurance']
        self.encumbrance = self.attributes['strength'] * 5

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
        # encumbrance
        self.encumbrance = self.attributes['strength'] * 5
        # magicka
        if self.gender == 'f':
            self.magicka = all_races[self.race]['magicka'][1]
        elif self.gender == 'm':
            self.magicka = all_races[self.race]['magicka'][0]
        self.magicka += self.attributes['intelligence'] * 2
        if self.birthsign == 'apprentice':
            self.magicka += 100
        # endurance
        self.fatigue = self.attributes['strength'] + self.attributes['willpower'] + self.attributes['agility'] + self.attributes['endurance']
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
                          WILLPOWER       {self.attributes['willpower']:3}
HEALTH          {self.health:3}       AGILITY         {self.attributes['agility']:3}
MAGICKA         {self.magicka:3}       SPEED           {self.attributes['speed']:3}
FATIGUE         {self.fatigue:3}       ENDURANCE       {self.attributes['endurance']:3}
ENCUMBRANCE     {self.encumbrance:3}       PERSONALITY     {self.attributes['personality']:3}
                          LUCK            {self.attributes['luck']:3}
==================
   MAJOR SKILLS   
==================''')
        for x in character_journal_skill_order:
            if x in self.character_class.major_skills:
                print(f'{x:16}{self.skills[x]:3}')
        print('''==================
   MINOR SKILLS   
==================''')
        for x in character_journal_skill_order:
            if x not in self.character_class.major_skills:
                print(f'{x:16}{self.skills[x]:3}')

    def minmax(self):
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
        # forecast attributes at max level
        # print level, attributes/skills (presumably all 100), health, magicka, fatigue, encumbrance

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
        print(f'''==================
 FINAL STATISTICS 
==================
Max level  = {self.level_skill_cap}
Max health = {max_health}''')

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

loadCharacter()
