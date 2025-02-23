import json

from utils.index import string_to_list


def get_counter_data(df, file_path):
    matches_dict = {}
    wins_dict = {}

    team1_player_column = df["Team1Players"].to_numpy()
    team2_player_column = df["Team2Players"].to_numpy()

    for index, team1_players_string in enumerate(team1_player_column):
        team1_player_list = string_to_list(team1_players_string)

        team2_players_string = team2_player_column[index]
        team2_player_list = string_to_list(team2_players_string)
        for player in team1_player_list:
            for enemy_player in team2_player_list:

                add_match(player, enemy_player, matches_dict)
                add_match(enemy_player, player, matches_dict)

                if df["Winner"][index] == 1:
                    add_win(player, enemy_player, wins_dict)
                elif df["Winner"][index] == 2:
                    add_win(enemy_player, player, wins_dict)

    with open(file_path, "w") as write_file:
        json.dump(matches_dict, write_file)
        write_file.close()

    with open(file_path, "w") as write_file:
        json.dump(wins_dict, write_file)
        write_file.close()


def add_match(player1, player2, matches_dict):
    if player1 in matches_dict:
        player_dict = matches_dict[player1]
        if player2 in player_dict:
            player_dict[player2] += 1
        else:
            player_dict[player2] = 1
    else:
        matches_dict[player1] = {player2: 1}


def add_win(winner, loser, wins_dict):
    if winner in wins_dict:
        player_dict = wins_dict[winner]
        if loser in player_dict:
            player_dict[loser] += 1
        else:
            player_dict[loser] = 1
    else:
        wins_dict[winner] = {loser: 1}


def get_counter_winrates(match_dict, win_dict, file_path):
    wr_dict = {}
    for player in win_dict:
        player_wr = {}
        for enemy_player in win_dict[player]:
            player_wr[enemy_player] = win_dict[player][enemy_player] / match_dict[player][enemy_player]
        wr_dict[player] = player_wr

    with open(file_path, "w") as write_file:
        json.dump(wr_dict, write_file)
        write_file.close()
