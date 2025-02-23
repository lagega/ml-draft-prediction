import json

from utils.index import string_to_list


def get_player_pair_data(df):
    matches_dict = {}
    wins_dict = {}

    for i in range(1, 3):
        team_pick_column = df[f'Team{i}Players'].to_numpy()

        for index, match in enumerate(team_pick_column):
            player_list = string_to_list(match)
            while len(player_list) > 1:
                player = player_list.pop()
                for ally in player_list:
                    add_match(player, ally, matches_dict)
                    add_match(ally, player, matches_dict)

                    if df["Winner"][index] == i:
                        add_match(player, ally, wins_dict)
                    elif df["Winner"][index] == 2:
                        add_match(ally, player, wins_dict)

    with open("../csv/PlayerCounterMatches.json", "w") as write_file:
        json.dump(matches_dict, write_file)
        write_file.close()

    with open("../csv/PlayerCounterWins.json", "w") as write_file:
        json.dump(wins_dict, write_file)
        write_file.close()


def get_player_winrates(match_dict, win_dict):
    wr_dict = {}
    for player in win_dict:
        player_wr = {}
        for ally_player in win_dict[player]:
            player_wr[ally_player] = win_dict[player][ally_player] / match_dict[player][ally_player]
        wr_dict[player] = player_wr

    with open("../csv/PlayerSynergy.json", "w") as write_file:
        json.dump(wr_dict, write_file)
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
