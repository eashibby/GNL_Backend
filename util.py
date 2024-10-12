def getRaceID (race):
    if not race:
        return
    else:
        if race.lower() == 'random' or race.lower() == 'rd':
           return 0
        elif race.lower() == 'orc' or race.lower() == 'oc':
            return 2
        elif race.lower() == 'nightelf' or race.lower() == 'night elf'  or race.lower() == 'ne':
            return 4
        elif race.lower() == 'undead' or race.lower() == 'ud':
            return 8
        elif race.lower() == 'human' or race.lower() == 'hu':
            return 1

def getRaceName (raceId):
    if raceId is None:
        return
    else:
        if raceId == 0 :
           return 'Random'
        elif raceId == 2:
            return 'Orc'
        elif raceId == 4:
            return 'Night Elf'
        elif raceId == 8:
            return 'Undead'
        elif raceId == 1:
            return 'Human'
        

def determineKOTHBucket(mmr):
    if mmr < 1450:
        return 1
    elif mmr > 1450 and mmr < 1600:
        return 2
    else:
        return 3