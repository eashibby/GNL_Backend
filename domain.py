from dataclasses import dataclass

@dataclass
class SignupPlayer():
    def __init__(self, id, battleTag, name, race, mmr, bucket):
        self.id = id
        self.battleTag = battleTag
        self.name = name
        self.race = race
        self.mmr = mmr
        self.bucket = bucket

    def __str__(self):
        return f"SignupPlayer: id: {self.id}, BattleTag:{self.battleTag}, Name: {self.name}, Race: {self.race}, MMR: {self.mmr}, Bucket: {self.bucket}" 
    

@dataclass
class GNLMatchup():
    def __init__(self, id, stream, time, date, player1, p1_score, p2_score, player2):
        self.id = id
        self.stream = stream
        self.time = time
        self.date = date
        self.player1 = player1
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.player2 = player2

    def __str__(self):
        return f"GNLMatchup: Stream: {self.stream}, Time:{self.time}, Date: {self.date}, Player 1: {self.player1}, Score 1: {self.p1_score}, Score 2: {self.p2_score}, Player 2: {self.player2}" 
    
@dataclass
class GNLPlayer():
    def __init__(self, id, battleTag, name, discord, race, mmr, team, country):
        self.id = id
        self.battleTag = battleTag
        self.name = name
        self.discord = discord
        self.race = race
        self.mmr = mmr
        self.team = team
        self.country = country

    def __str__(self):
        return f"GNLPlayer: id: {self.id}, BattleTag:{self.battleTag}, Discord: {self.discord}, Name: {self.name}, Race: {self.race}, MMR: {self.mmr}, Team: {self.team}, Country: {self.country}" 
    
@dataclass
class GNLTeam():
    def __init__(self, name, icon, players=[]):
        self.name = name
        self.icon = icon
        self.players = players

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        for tPlayer in self.player:
            if(player.id == tPlayer.id) :
                self.players.remove(tPlayer)
    
    def setPlayers(self, players):
        self.players = players

    def removeAllPlayers(self):
        del self.players

    def __str__(self):
        return f"GNLTeam: Name: {self.name} Icon: {self.icon}, Players: {self.players}" 