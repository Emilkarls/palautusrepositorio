import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.team = dict["team"]
        self.games = dict["games"]
    
    def __str__(self):
        return f"{self.name:20} {self.team:4} {self.goals:2} + {self.assists:2} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        nat = filter(lambda p: p.nationality == nationality, players)
        return list(sorted(nat, key = lambda p: p.goals + p.assists, reverse=True))[0:9]

    def get_nationalities(self):
        players = self.reader.get_players()
        nat = set(p.nationality for p in players)
        return list(sorted(nat))