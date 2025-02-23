from utils.index import string_to_list


def get_counter_index(df, wr_dict):
    team1_player_column = df["Team1Players"].to_numpy()
    team2_player_column = df["Team2Players"].to_numpy()
    countering_list = []
    for index, team1_players in enumerate(team1_player_column):
        team2_players = team2_player_column[index]

        team1_wr = get_wr_sum(team1_players, team2_players, wr_dict)
        team2_wr = get_wr_sum(team2_players, team1_players, wr_dict)

        countering = team2_wr - team1_wr
        countering_list.append(countering)
    df["PlayerCountering"] = countering_list


def get_wr_sum(team1_players, team2_players, wr_dict):
    wr_sum = 0
    team1_player_list = string_to_list(team1_players)
    team2_player_list = string_to_list(team2_players)
    for player in team1_player_list:
        for enemy_player in team2_player_list:
            if player in wr_dict and enemy_player in wr_dict[player]:
                wr_sum += wr_dict[player][enemy_player]
    return wr_sum
