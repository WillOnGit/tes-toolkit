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
            ('hand to hand',5),
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
            ('hand to hand',5),
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
            ('hand to hand',10),
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
            ('hand to hand',5),
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

class CharacterClass:
    def __init__(self, name, specialisation, favoured_attributes, major_skills):
        self.name = name
        if specialisation not in ['combat','magic','stealth']:
            print('uh oh')
        else:
            self.specialisation = specialisation

        if len(favoured_attributes) != 2 or not all([x in all_attributes for x in favoured_attributes]):
            print('uh oh')
        else:
            self.favoured_attributes = favoured_attributes

        if len(major_skills) != 7 or not all([x in all_skills for x in major_skills]):
            print('uh oh')
        else:
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
            print('uh oh')
        else:
            self.race = race

        if gender not in ['f','m']:
            print('uh oh')
        else:
            self.gender = gender

        if type(character_class) != CharacterClass:
            print('uh oh')
        else:
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
        if birthsign == 'apprentice':
            self.magicka += 100

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
        self.starting_attributes = self.attributes.copy()
        self.starting_skills = self.skills.copy()
        self.level = 1
        self.level_up_history = []
        self.level_up_progress = 0
        self.level_up_attribute_bonuses = {x:0 for x in all_attributes}
        self.level_up_available = False

    def __str__(self):
        if self.gender == 'f':
            friendly_gender = 'Female'
        elif self.gender == 'm':
            friendly_gender = 'Male'
        return '{} {}, class {}'.format(friendly_gender,self.race.title(),self.character_class.name)

    def increase_skill(self, skill, magnitude=1):
        if self.level_up_available:
            raise RuntimeError('Level up first')
        if self.skills[skill] + magnitude > 100:
            raise RuntimeError('Aborting safely - can\'t skill up past 100')

        if skill in self.character_class.major_skills:
            level_up_result = self.level_up_progress + magnitude
            if level_up_result > 10:
                raise RuntimeError('Aborting safely - this increase over-levels by {}'.format(level_up_result - 10))
            self.level_up_progress += magnitude
            self.skills[skill] += magnitude
            self.level_up_attribute_bonuses[skill_attribute_mappings[skill]] += magnitude
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
                self.level_up_history.append('TODO')
                self.level_up_available = True
                print('Level up available')

        else:
            self.skills[skill] += magnitude
            self.level_up_attribute_bonuses[skill_attribute_mappings[skill]] += magnitude

    def level_up(self,attributes='auto'):
        # checks
        if not self.level_up_available:
            raise RuntimeError('Level up not available - aborting')
        if attributes == 'auto':
            candidates = []
            for x in self.level_up_attribute_bonuses:
                if self.level_up_attribute_bonuses[x] == 5:
                    candidates.append(x)
            if len(candidates) == 2:
                attributes = candidates + ['luck']
                print('Autodetection succeeded - detected {}'.format(attributes))
            elif len(candidates) == 3:
                attributes = candidates
                print('Autodetection succeeded - detected {}'.format(attributes))
            else:
                raise RuntimeError('Autodetection failed - please specify attributes manually')
        elif not all(x in all_attributes for x in attributes) or len(attributes) != 3:
            raise RuntimeError('Invalid attributes')

        # everything is ok - start level up by increasing attributes
        for x in attributes:
            self.attributes[x] += self.level_up_attribute_bonuses[x]

        # recalculate derived attributes
        self.health += self.attributes['endurance'] // 10
        if 'endurance' in attributes:
            self.health += self.level_up_attribute_bonuses['endurance'] * 2
        if 'intelligence' in attributes:
            self.magicka += self.level_up_attribute_bonuses['intelligence'] * 2
        self.fatigue = self.attributes['strength'] + self.attributes['willpower'] + self.attributes['agility'] + self.attributes['endurance']
        self.encumbrance = self.attributes['strength'] * 5

        # wasted skill ups
        self.wasted_skill_ups = {x:0 for x in all_attributes}
        for x in all_skills:
            self.wasted_skill_ups[skill_attribute_mappings[x]] += self.skills[x] - self.starting_skills[x]
        # TODO (maybe): relax efficient levelling assumption
        # works for efficient levelling only
        for x in all_attributes[:-1]:
            self.wasted_skill_ups[x] -= (self.attributes[x] - self.starting_attributes[x]) * 2
        # luck differs slightly from override version - we haven't levelled up yet here!
        self.wasted_skill_ups['luck'] = self.level - (self.attributes['luck'] - self.starting_attributes['luck'])

        # reset various things and finally increment level
        self.level_up_progress = 0
        self.level_up_attribute_bonuses = {x:0 for x in all_attributes}
        self.level_up_available = False
        self.level += 1
