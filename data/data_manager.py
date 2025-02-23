import pandas

from data.columns import PLAYER_ARRAY_COLUMNS, TEAM_NAMES_COLUMNS

pandas.options.mode.chained_assignment = None


def get_champions():
    file = open("../csv/champions.csv", "r")
    champion_list = file.read().split(",")
    champion_map = {}

    for index, champion in enumerate(champion_list, start=1):
        champion_map[champion] = index

    return champion_map


def get_teams(dataf):
    team_list = []
    for column in TEAM_NAMES_COLUMNS:
        team_column = list(dataf[column])
        for team in team_column:
            normalized_team = team.lower()
            if normalized_team not in team_list:
                team_list.append(normalized_team)
    team_df = pandas.DataFrame(team_list)
    print(team_df)
    team_df.to_csv(path_or_buf="/csv/Team_Names.csv", sep=";", index=False)


def get_team_map():
    file = open("../csv/Team_Names.csv", "r")
    team_list = file.read().split(";")
    team_map = {}

    for index, team in enumerate(team_list):
        team_map[team] = index

    return team_map


def vectorize_teams(dataframe, column_list, data_map):
    for column_name in column_list:
        column = dataframe[column_name]

        for index, data in enumerate(column):
            if data == "None":
                column[index] = 0
            else:
                if data.lower() in data_map:
                    column[index] = data_map[data.lower()]
                else:
                    map_len = len(data_map)
                    column[index] = map_len
                    data_map[data.lower()] = map_len


def get_players(dataf):
    player_list = []
    for column in PLAYER_ARRAY_COLUMNS:
        players_column = list(dataf[column])
        for team_players in players_column:
            individual_players = team_players.split(",")
            for player in individual_players:
                normalized_player = player.lower()
                if normalized_player not in player_list:
                    player_list.append(normalized_player)
    player_df = pandas.DataFrame(player_list)
    print(player_df)
    player_df.to_csv(path_or_buf="/csv/Player_Names.csv", sep=";", index=False)


def get_player_map():
    file = open("../csv/Player_Names.csv", "r")
    player_list = file.read().split(";")
    player_map = {}

    for index, player in enumerate(player_list):
        player_map[player] = index

    return player_map


def vectorize_data(dataframe, column_list, data_map):
    for column_name in column_list:
        column = dataframe[column_name]

        for column_index, row in enumerate(column):
            data_list = row.split(",")
            for row_index, data in enumerate(data_list):
                if data == "None":
                    data_list[row_index] = 0
                else:
                    if data.lower() in data_map:
                        data_list[row_index] = data_map[data.lower()]
                    else:
                        map_len = len(data_map)
                        data_list[row_index] = map_len
                        data_map[data.lower()] = map_len
            column[column_index] = data_list


def vectorize_champions(dataframe, column_name):
    champions = get_champions()
    column = dataframe[column_name]

    for column_index, row in enumerate(column):
        ban_list = row.split(",")
        for row_index, champion in enumerate(ban_list):
            ban_list[row_index] = 0 if champion == "None" else champions[champion]
        column[column_index] = ban_list


def split_values(dataframe, column_name):
    column = dataframe[column_name].to_numpy()
    new_name = column_name.rstrip("s")

    for column_index, row in enumerate(column):
        values_string = row[1:-1]
        values_list = values_string.split(", ")
        for row_index, value in enumerate(values_list, start=1):
            column_name = f'{new_name}{row_index}'
            dataframe[column_name][column_index] = value
