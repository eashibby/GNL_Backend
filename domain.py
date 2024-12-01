from dataclasses import dataclass


@dataclass
class GNLPlayerMatchup:
    def __init__(
        self, id, uuid, stream, time, date, player1, p1_score, p2_score, player2
    ):
        self.id = id
        self.uuid = uuid
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
class GNLUser:
    def __init__(self, id, uuid, battleTag, name, discord, race, mmr, country):
        self.id = id
        self.uuid = uuid
        self.battleTag = battleTag
        self.name = name
        self.discord = discord
        self.race = race
        self.mmr = mmr
        self.country = country

    def __str__(self):
        return f"GNLPlayer: id: {self.id}, BattleTag:{self.battleTag}, Discord: {self.discord}, Name: {self.name}, Race: {self.race}, MMR: {self.mmr}, Country: {self.country}"


@dataclass
class GNLTeam:
    def __init__(self, id, uuid, name, icon, season, players=[]):
        self.id = id
        self.uuid = uuid
        self.name = name
        self.icon = icon
        self.players = players
        self.season = season

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        for tPlayer in self.player:
            if player.id == tPlayer.id:
                self.players.remove(tPlayer)

    def setPlayers(self, players):
        self.players = players

    def clearPlayers(self):
        del self.players

    def setSeason(self, season):
        self.season = season

    def __str__(self):
        return f"GNLTeam: Name: {self.name} Icon: {self.icon}, Players: {self.players}"


@dataclass
class GNLTeamMatchup:
    def __init__(
        self, id, uuid, week, team1, team2, season, score_t1=0, score_t2=0, matches=[]
    ):
        self.id = id
        self.uuid = uuid
        self.score_t2 = score_t2
        self.week = week
        self.score_t1 = score_t1
        self.team1 = team1
        self.team2 = team2
        self.matches = matches
        self.season = season

    def __str__(self):
        return f"GNLTeamMatchup: UUID: {self.uuid}, Week:{self.week}, Team 1: {self.team1.name}, Score Team 1: {self.score_t1}, Team 2: {self.team2.name}, Score Team 2: {self.score_t2}"


@dataclass
class GNLSeason:
    def __init__(self, id, uuid, name, winner):
        self.id = id
        self.uuid = uuid
        self.name = name
        self.winner = winner

    def setWinner(self, winner):
        self.winner = winner

    def __str__(self):
        return f"GNLMatchup: Stream: {self.stream}, Time:{self.time}, Date: {self.date}, Player 1: {self.player1}, Score 1: {self.p1_score}, Score 2: {self.p2_score}, Player 2: {self.player2}"
