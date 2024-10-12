from pip._vendor import requests
import json
import urllib.parse
from domain import SignupPlayer
from util import *
from dotenv import load_dotenv
import os

load_dotenv()

class W3ChampService():
    def __init__(self):
        self.url = os.getenv('W3C_URL')
        self.season = os.getenv('W3C_CURRENT_SEASON')
        self.db_table = os.getenv('SQL_DB_TABLE')

    def get_data(self, name, race):
        quotedName = urllib.parse.quote(name)
        url = self.url +quotedName + '/game-mode-stats?gateWay=20&season=' + self.season
        print("Request URL: " + url)
        content = requests.get(url)
        if (not content):
            print("no content found")
            return
        else:
            print("Content found")
            gamemodes = json.loads(content.text)
            for gamemode in gamemodes:
                print(gamemode)
                if gamemode['gameMode'] == 1 and gamemode['race'] == getRaceID(race):
                    player = SignupPlayer(gamemode['id'],gamemode['playerIds'][0]['battleTag'],gamemode['playerIds'][0]['name'],gamemode['race'], gamemode['mmr'], determineKOTHBucket(gamemode['mmr']))
                    return player
            return

    def updatePlayersInfo(self, players):
        for player in players:
            quotedName = urllib.parse.quote(player.battleTag)
            url = self.url +quotedName
            print("Request URL: " + url)
            content = requests.get(url)
            if (not content):
                raise Exception("Cant find player by BattleTag: " + player.battleTag) 
            else:
                playerInfo = json.loads(content.text)
                player.name = playerInfo['name']
                player.id = playerInfo['playerAkaData']['id']
        return players
