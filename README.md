# The Elder Scrolls IV: Oblivion - minmaxer's toolkit
## Background
I love this game and decided to properly minmax a character to avoid [the leveling problem](https://en.uesp.net/wiki/Oblivion:Leveling#The_Leveling_Problem).
Copying character information from the game to handwritten notes and tracking progress was tedious and error-prone, so this project was born.
The result is a basic interface written in Python 3 (tested in 3.9.1) which automates the tedious bookkeeping of the process, allowing you to spend more time actually playing the game - or in my case, more time to play and write this code.

Unlike tools like [Oblivion Character Planner](https://github.com/rdoll/ocp), this repo expects you to know what you're doing and simply makes journaling your progress easier, rather than guiding you by the hand.
Therefore a good grasp of the game's mechanics is required.
If you're just starting out check out the required reading section, which points you to the peerless UESP.

## Required reading
- https://en.uesp.net/wiki/Oblivion:Character_Creation
- https://en.uesp.net/wiki/Oblivion:Attributes
- https://en.uesp.net/wiki/Oblivion:Skills
- https://en.uesp.net/wiki/Oblivion:Leveling
- https://en.uesp.net/wiki/Oblivion:Efficient_Leveling
- https://en.uesp.net/wiki/Oblivion:Increasing_Skills
- https://en.uesp.net/wiki/Oblivion:Endurance (especially the Health Gains section)

## Quickstart
There's no proper documentation yet while the system is being finalised but this basically covers everything you need.

Designed to be used from an interactive python session:
```
python3 -i oblivion.py
```
Existing data will automatically be loaded if found.

### Setup
Most people will want to create a class with a name, specialisation, favoured attributes and major skills, then create a character with a race, gender, class and birthsign.
The 21 default classes are included for completeness' sake, however.
```
# create a custom class - use this to follow rest of tutorial
myclass = CharacterClass('Class name','magic',['endurance','luck'],['alchemy','alteration','block','conjuration','hand-to-hand','light armor','marksman'])
c = Character('breton','f',myclass,'apprentice')

# alternative - use a default class
c = Character('imperial','m',default_classes['battlemage'],'lady')
```

### Core usage loop
Python's interactive autocomplete is basically mandatory, e.g. `c.i <TAB> 'someskill')`
```
# print core character info. easy to compare with in-game journal
c.journal()

# print "hidden" information about this level-up so far
c.progressToLevelUp()

# increase a skill when it happens in-game
c.increaseSkill('heavy armor')

# increase a single skill by more than one - useful when catching up or at low levels with rapid increases
c.increaseSkill('armorer',9)
c.progressToLevelUp()

# track training sessions
c.increaseSkill('alchemy',3,True)
c.progressToLevelUp()

# level up - increase tenth major skill and call levelUp
# endurance, intelligence and luck will be automatically detected as the best attributes to raise
# confirm interactively and you're level 2
c.increaseSkill('conjuration',7)
c.levelUp()
yes
c.journal()
c.progressToLevelUp()

# save character to safely quit python - our character will be loaded automatically next time
saveCharacter(c)
```

### Extras
```
# manually specify attributes to increase on level-up. useful when increasing luck
c.levelUp(['strength','agility','luck'])

# show magic skills by mastery level - leave blank for all skills
c.skillLevels('magic')

# show how we're doing in the overall scheme of minmaxing
c.minmax()

# import an existing character at a level greater than 1.
# only works assuming a level up has just taken place

attributes = {'strength': 35, 'intelligence': 80, 'willpower': 100, 'agility': 30, 'speed': 50, 'endurance': 100, 'personality': 40, 'luck': 65}
skills = {'acrobatics': 24, 'alchemy': 50, 'alteration': 88, 'armorer': 55, 'athletics': 43, 'blade': 30, 'block': 53, 'blunt': 11, 'conjuration': 61, 'destruction': 69, 'hand-to-hand': 34, 'heavy armor': 58, 'illusion': 47, 'light armor': 36, 'marksman': 28, 'mercantile': 29, 'mysticism': 54, 'restoration': 55, 'security': 22, 'sneak': 13, 'speechcraft': 26}
health = 298
level = 15
c.override(attributes,skills,health,level)
# make sure everything checks out
c.validate()

# save characters with a different file name to e.g. keep backups or maintain multiple characters
saveCharacter(c,'other filename')

# load a save to undo a mistake or revert lost progress (e.g. you died without saving in-game)
loadCharacter('savename')
# last resort in case we didn't save anything here - undoes all progress this level
c.resetToLastLevel()
```
