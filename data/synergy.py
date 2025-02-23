from utils.index import string_to_list


def get_synergy(df, wr_map):
    team1_pick_column = df["Team1Picks"].to_numpy()
    team2_pick_column = df["Team2Picks"].to_numpy()
    synergy_list = []
    for index, team1_picks in enumerate(team1_pick_column):
        team1_wr = get_wr_sum(team1_picks, wr_map)

        team2_picks = team2_pick_column[index]
        team2_wr = get_wr_sum(team2_picks, wr_map)

        synergy = team2_wr - team1_wr
        synergy_list.append(synergy)
    df["Synergy"] = synergy_list


def get_wr_sum(picks, wr_map):
    wr_sum = 0
    player_list = string_to_list(picks)
    for i in range(4):
        j = i + 1
        while j < 5:
            player1 = int(player_list[i])
            player2 = int(player_list[j])
            print(str(player1) in wr_map)
            if player1 in wr_map and player2 in wr_map[player1]:
                wr_sum += wr_map[player1][player2]
            j += 1
    return wr_sum


def get_player_synergy(df, wr_map):
    team1_player_column = df["Team1Players"].to_numpy()
    team2_player_column = df["Team2Players"].to_numpy()
    synergy_list = []
    for index, team1_players in enumerate(team1_player_column):
        team1_wr = get_wr_sum(team1_players, wr_map)

        team2_players = team2_player_column[index]
        team2_wr = get_wr_sum(team2_players, wr_map)

        synergy = team2_wr - team1_wr
        synergy_list.append(synergy)
    df["PlayerSynergy"] = synergy_list
