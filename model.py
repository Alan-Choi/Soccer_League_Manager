import datetime
import uuid
from consts import TeamType
import sqlite3
import consts
from player import Player
from team import Team
from match import Match
from referee import Referee
from schedule import Schedule

class Model:
    
    __DB = consts.DATABASE
    
    def __init__(self, db_dir=None):
        if db_dir:
            self.__conn = sqlite3.connect(db_dir)
        else:
            self.__conn = sqlite3.connect(self.__DB)
        
        self.cursor = self.__conn.cursor()
        # self.initialize_database()
        
    
    def __del__(self):
        self.__conn.close()
        
        
    def commit(self):
        self.__conn.commit()
        
    
    def initialize_database(self) -> None:
        
        self.cursor.execute("""PRAGMA foreign_keys = 1;""")
    
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS player (
            uuid TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            team TEXT,
            date_of_birth TEXT,
            picture TEXT,
            active INTEGER,
            FOREIGN KEY (team) REFERENCES team(uuid) ON DELETE SET NULL ON UPDATE CASCADE
            );""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS team (
            uuid TEXT PRIMARY KEY,
            name TEXT,
            type TEXT,
            active INTEGER
            );""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS match (
            uuid TEXT PRIMARY KEY,
            date TEXT,
            team1 TEXT,
            team2 TEXT,
            score1 INTEGER,
            score2 INTEGER,
            referee TEXT,
            FOREIGN KEY (team1) REFERENCES team(uuid) ON DELETE SET NULL ON UPDATE CASCADE,
            FOREIGN KEY (team2) REFERENCES team(uuid) ON DELETE SET NULL ON UPDATE CASCADE,
            FOREIGN KEY (referee) REFERENCES referee(uuid) ON DELETE SET NULL ON UPDATE CASCADE
            );""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS referee (
            uuid TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            active INTEGER
            );""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS schedule(
            uuid TEXT PRIMARY KEY,
            day TEXT,
            time TEXT
            );""")
    
        self.commit()
        
    
    def create_player(self, player: Player) -> None:
        
        self.cursor.execute("""INSERT INTO player (uuid, first_name, last_name, team, date_of_birth, picture, active) VALUES (?, ?, ?, ?, ?, ?, ?);""", 
                       (player.id, player.first_name, player.last_name, player.team, player.date_of_birth, player.picture, player.active))
        self.commit()
        
    
    def create_team(self, team: Team) -> None:

        self.cursor.execute("""INSERT INTO team (uuid, name, type, active) VALUES (?, ?, ?, ?);""", 
                       (team.id, team.name, team.type.name, team.active))
        self.commit()
        
    
    def create_match(self, match: Match) -> None:
        
        self.cursor.execute("""INSERT INTO match (uuid, date, team1, team2, score1, score2, referee) VALUES (?, ?, ?, ?, ?, ?, ?);""", 
                       (match.id, match.date, match.team1.id, match.team2.id, match.score1, match.score2, match.referee.id))
        self.commit()
        
    
    def create_referee(self, referee: Referee) -> None:

        self.cursor.execute("""INSERT INTO referee (uuid, first_name, last_name, active) VALUES (?, ?, ?, ?);""", 
                       (referee.id, referee.first_name, referee.last_name, referee.active))
        self.commit()
        
    
    def create_schedule(self, schedule: Schedule) -> None:
 
        self.cursor.execute("""INSERT INTO schedule (uuid, day, time) VALUES (?, ?, ?);""", 
                       (schedule.id, schedule.day, schedule.time))
        self.commit()

    def read_players(self) -> list[Player]:
        self.cursor.execute("""SELECT * FROM player;""")
        
        playerList = self.cursor.fetchall()
        
        players = []
        for player in playerList:
            players.append(Player(player[0], player[1], player[2], player[3], player[4], player[5])) 
        
        return players
    
    def read_player_by_id(self, player_id: str) -> list[Player]:

        self.cursor.execute("""SELECT * FROM player WHERE uuid = ?;""", (player_id,))
        
        playerList = self.cursor.fetchall()
        
        players = []
        for player in playerList:
            players.append(Player(player[0], player[1], player[2], player[3], player[4], player[5])) 
                
        return players
        
    def read_team_by_id(self, team_id: str) -> list[Team]:
        
        self.cursor.execute("""SELECT * FROM team WHERE uuid = ?;""", (team_id,))
        
        return self.cursor.fetchall()
    
    def read_match_by_id(self, match_id: str) -> list[Match]:
        db = consts.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM match WHERE uuid = ?;""", (match_id,))
        
        return cursor.fetchall()
    
    def read_referee(self, referee_id: str) -> list[Referee]:
        db = consts.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM referee WHERE uuid = ?;""", (referee_id,))
        
        return cursor.fetchall()
    
    def read_schedule(self, schedule_id: str) -> list[Schedule]:
        db = consts.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM schedule WHERE uuid = ?;""", (schedule_id,))
        
        return cursor.fetchall()
    
    def update_player(self, player: Player) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
        
            cursor.execute("""UPDATE player SET first_name = ?, last_name = ?, team = ?, date_of_birth = ?, active = ? WHERE uuid = ?;""", 
                        (player.first_name, player.last_name, player.team.id, player.date_of_birth, player.active, player.id,))
            conn.commit()
            conn.close()
    
    def upate_team(self, team: Team) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
        
            cursor.execute("""UPDATE team SET name = ?, type = ?, active = ? WHERE uuid = ?;""", 
                        (team.name, team.type.name, team.active, team.id,))
            conn.commit()
            conn.close()
    
    def update_match(self, match: Match) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
        
            cursor.execute("""UPDATE match SET date = ?, team1 = ?, team2 = ?, score1 = ?, score2 = ?, referee = ? WHERE uuid = ?;""", 
                        (match.date, match.team1.id, match.team2.id, match.score1, match.score2, match.referee.id, match.id,))
            conn.commit()
            conn.close()
    
    def update_referee(self, referee: Referee) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
        
            cursor.execute("""UPDATE referee SET first_name = ?, last_name = ?, active = ? WHERE uuid = ?;""", 
                        (referee.first_name, referee.last_name, referee.active, referee.id,))
            conn.commit()
            conn.close()
    
    def delete_player(self, id: str) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""DELETE FROM player WHERE uuid = ?;""", (id,))
            
            conn.commit()
            conn.close()
    
    def delete_team(self, id: str) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""DELETE FROM team WHERE uuid = ?;""", (id,))
            
            conn.commit()
            conn.close()
    
    def delete_match(self, id: str) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""DELETE FROM match WHERE uuid = ?;""", (id,))
            
            conn.commit()
            conn.close()
    
    def delete_referee(self, id: str) -> None:
        db = consts.DATABASE
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""DELETE FROM referee WHERE uuid = ?;""", (id,))
            
            conn.commit()
            conn.close()