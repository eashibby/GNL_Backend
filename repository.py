import os
import pandas as pd
import pyodbc
import gspread
from domain import SignupPlayer
from util import *
from dotenv import load_dotenv
from domain import GNLPlayer
import w3champions as w3c

load_dotenv()

class RepoService():
    def __init__(self):
        self.db_host = os.getenv('SQL_HOST')
        self.db_name = os.getenv('SQL_DB_NAME')
        self.db_players_table = os.getenv('PLAYERS_TABLE')
        self.db_username = os.getenv('SQL_DB_USER')
        self.db_pw = os.getenv('SQL_DB_PW')
        self.conn = pyodbc.connect("DRIVER={SQL SERVER};server=127.0.0.1;port=3306;database=gnl;uid=gnl;pwd=gnl;Encrypt=no")
        
    def executeStatement(self, update_statement, values = None):
        #conn = sqlite3.connect(self.db_path)
        if values is None:
            values = []
        return pd.read_sql_query(update_statement,self.conn, values)

    def syncPlayersWithSpreadsheet(self):
        print("Sync Players with Spreadsheet!")
        players = self.readPlayersSpreadSheet()
        players = w3c.updatePlayersInfo(players)
        data = []
        for player in players: 
            o = [player.id,player.battleTag, player.name,player.discord, player.race, player.mmr, player.team, player.country]
            print("Player dict: ", player.__dict__)
            print("Player arr: " , o)
            data.append(o)
        self.executeStatement(f'''
            declare @id int = ?
            declare @battleTag varchar(100) = ?
            declare @name varchar(100) = ?
            declare @discord varchar(100) = ?
            declare @race varchar(100) = ?
            declare @mmr decimal(10,2) = ?
            declare @team varchar(100) = ?
            declare @country varchar(100) = ?
                
            UPDATE [{self.db_table}] 
            SET id = @id, battleTag = @battleTag, name = @name, discord = @discord, race = @race, mmr = @mmr, team = @team, country = @country
            WHERE id = @id
            
            IF @@ROWCOUNT = 0
                INSERT INTO [{self.db_table}] 
                    (id, battleTag, name, discord, race, mmr, team, country)
                VALUES (@id, @battleTag, @name, @discord, @race, @mmr, @team, @country)
        ''', o)



    def readPlayersSpreadSheet():
        gc = gspread.service_account(filename=os.getenv("SERVICE_ACCOUNT_FILE"))
        sh = gc.open_by_url(os.getenv("GNL_SHEET"))
        players = sh.worksheet(os.getenv("PLAYERS_SHEET")).get_all_records()
        players_list = []
        for player in players:
            players_list.append(
                GNLPlayer(
                    0,
                    player["Bnet"],
                    player["Bnet (no ID)"],
                    player["Discord"],
                    player["Race"],
                    player["MMR"],
                    player["Team Abbr"],
                    player["Country"],
                )
            )

        return players_list
    
    def readMatchupsSpreadSheet():
        gc = gspread.service_account(filename=os.getenv("SERVICE_ACCOUNT_FILE"))
        sh = gc.open_by_url(os.getenv("GNL_SHEET"))
        players = sh.worksheet(os.getenv("PLAYERS_SHEET")).get_all_records()
        players_list = []
        for player in players:
            players_list.append(
                GNLPlayer(
                    0,
                    player["Bnet"],
                    player["Bnet (no ID)"],
                    player["Discord"],
                    player["Race"],
                    player["MMR"],
                    player["Team Abbr"],
                    player["Country"],
                )
            )

        return players_list