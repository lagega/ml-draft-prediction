PICKS_ARRAY_COLUMNS = [
    "Team1Picks",
    "Team2Picks"
]

BANS_ARRAY_COLUMNS = [
    "Team1Bans",
    "Team2Bans",
]

PLAYER_ARRAY_COLUMNS = [
    "Team1Players",
    "Team2Players"
]

BAN_COLUMNS = [
    "Team1Ban1",
    "Team1Ban2",
    "Team1Ban3",
    "Team1Ban4",
    "Team1Ban5",
    "Team2Ban1",
    "Team2Ban2",
    "Team2Ban3",
    "Team2Ban4",
    "Team2Ban5",
]

PICK_COLUMNS = [
    "Team1Pick1",
    "Team1Pick2",
    "Team1Pick3",
    "Team1Pick4",
    "Team1Pick5",
    "Team2Pick1",
    "Team2Pick2",
    "Team2Pick3",
    "Team2Pick4",
    "Team2Pick5",
]

INDIVIDUAL_CHAMPION_COLUMNS = PICK_COLUMNS + BAN_COLUMNS

TEAM1_PLAYER_COLUMNS = [
    "Team1Player1",
    "Team1Player2",
    "Team1Player3",
    "Team1Player4",
    "Team1Player5",
]

TEAM2_PLAYER_COLUMNS = [
    "Team2Player1",
    "Team2Player2",
    "Team2Player3",
    "Team2Player4",
    "Team2Player5",
]

INDIVIDUAL_PLAYER_COLUMNS = TEAM1_PLAYER_COLUMNS + TEAM2_PLAYER_COLUMNS

TEAM_NAMES_COLUMNS = [
    "Team1",
    "Team2"
]

RELATIONSHIP_COLUMNS = [
    "Synergy",
    "Countering",
    "PlayerSynergy",
    "PlayerCountering"
]

PRE_MATCH_COLUMNS = \
   TEAM_NAMES_COLUMNS + INDIVIDUAL_PLAYER_COLUMNS + INDIVIDUAL_CHAMPION_COLUMNS

FEATURE_COLUMNS = PRE_MATCH_COLUMNS + RELATIONSHIP_COLUMNS

FULL_INFO_COLUMNS = FEATURE_COLUMNS + [
    "Team1Score",
    "Team2Score",
    "Team1Dragons",
    "Team2Dragons",
    "Team1Barons",
    "Team2Barons",
    "Team1Towers",
    "Team2Towers",
    "Team1Gold",
    "Team2Gold",
    "Team1Kills",
    "Team2Kills",
    "Team1RiftHeralds",
    "Team2RiftHeralds",
    "Team1Inhibitors",
    "Team2Inhibitors",
    "Gamelength Number",
]
