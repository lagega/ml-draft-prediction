import datetime

from mwrogue.esports_client import EsportsClient

QUERY_FIELDS = "Team1, Team2, Team1Players, Team2Players, Team1Bans, Team2Bans, Team1Picks, Team2Picks, GameId, " \
               "Team1Score, Team2Score, Team1Dragons, Team2Dragons, Team1Barons, Team2Barons, Team1Towers, " \
               "Team2Towers, Team1Gold, Team2Gold, Team1Kills, Team2Kills, Team1RiftHeralds, Team2RiftHeralds, " \
               "Team1Inhibitors, Team2Inhibitors, Gamelength_Number, Patch, GameId, Winner, Tournament "

api_client = EsportsClient("lol")

date = "2023-09-25"
date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

response_dict = api_client.cargo_client.query(
    tables="ScoreboardGames=SG",
    fields=QUERY_FIELDS,
    where="DateTime_UTC > '2023-01-01 00:00:00'"
)
