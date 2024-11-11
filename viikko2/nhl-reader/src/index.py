from player import Player, PlayerReader, PlayerStats
from rich.console import Console
from rich.prompt import Prompt
from rich import print

def main():
    seasons = [ "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    console = Console()
    while True:
        season = Prompt.ask("Select season", choices = seasons)
        
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        nats = stats.get_nationalities()
        nat = Prompt.ask("Select nationality", choices = nats )
        
        players = stats.top_scorers_by_nationality(nat)

        for player in players:
            print(player)


if __name__ == "__main__":
    main()
