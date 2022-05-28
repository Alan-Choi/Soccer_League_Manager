from asyncio import constants
import sqlalchemy
import sqlite3
import model
import view
import constants


class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
    
    def initialize_database() -> None:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""PRAGMA foreign_keys = 1;""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS player (
            uuid TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            team TEXT,
            date_of_birth TEXT,
            active INTEGER,
            FOREIGN KEY (team) REFERENCES team(name) ON DELETE SET NULL ON UPDATE CASCADE
            );""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS team (
            uuid TEXT PRIMARY KEY,
            name TEXT,
            type TEXT,
            active INTEGER
            );""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS match (
            uuid TEXT PRIMARY KEY,
            date TEXT,
            team1 TEXT,
            team2 TEXT,
            score1 INTEGER,
            score2 INTEGER,
            referee TEXT,
            FOREIGN KEY (team1) REFERENCES team(name) ON DELETE SET NULL ON UPDATE CASCADE,
            FOREIGN KEY (team2) REFERENCES team(name) ON DELETE SET NULL ON UPDATE CASCADE,
            FOREIGN KEY (referee) REFERENCES referee(name) ON DELETE SET NULL ON UPDATE CASCADE
            );""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS referee (
            uuid TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            active INTEGER
            );""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS schedule(
            uuid TEXT PRIMARY KEY,
            day TEXT,
            time TEXT
            );""")
        
        conn.commit()
        
        conn.close()
        
    def create_player(self, player: model.Player) -> None:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""INSERT INTO player (uuid, first_name, last_name, team, date_of_birth, active) VALUES (?, ?, ?, ?, ?, ?);""", 
                       (player.id, player.first_name, player.last_name, player.team.id, player.date_of_birth, player.active))
        conn.commit()
        conn.close()
    
    def create_team(self, team: model.Team) -> None:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""INSERT INTO team (uuid, name, type, active) VALUES (?, ?, ?, ?);""", 
                       (team.id, team.name, team.type, team.active))
        conn.commit()
        conn.close()
    
    def create_match(self, match: model.Match) -> None:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""INSERT INTO match (uuid, date, team1, team2, score1, score2, referee) VALUES (?, ?, ?, ?, ?, ?, ?);""", 
                       (match.id, match.date, match.team1.id, match.team2.id, match.score1, match.score2, match.referee.id))
        conn.commit()
        conn.close()
    
    def create_referee(self, referee: model.Referee) -> None:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""INSERT INTO referee (uuid, first_name, last_name, active) VALUES (?, ?, ?, ?);""", 
                       (referee.id, referee.first_name, referee.last_name, referee.active))
        conn.commit()
        conn.close()
    
    def create_schedule(self, schedule: model.Schedule) -> None:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""INSERT INTO schedule (uuid, day, time) VALUES (?, ?, ?);""", 
                       (schedule.id, schedule.day, schedule.time))
        conn.commit()
        conn.close()
    
    def read_player(self, player_id: str) -> list:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM player WHERE uuid = ?;""", (player_id,))
        
        return cursor.fetchall()
        
    def read_team(self, team_id: str) -> list:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM team WHERE uuid = ?;""", (team_id,))
        
        return cursor.fetchall()
    
    def read_match(self, match_id: str) -> list:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM match WHERE uuid = ?;""", (match_id,))
        
        return cursor.fetchall()
    
    def read_referee(self, referee_id: str) -> list:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM referee WHERE uuid = ?;""", (referee_id,))
        
        return cursor.fetchall()
    
    def read_schedule(self, schedule_id: str) -> list:
        db = constants.DATABASE
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM schedule WHERE uuid = ?;""", (schedule_id,))
        
        return cursor.fetchall()
