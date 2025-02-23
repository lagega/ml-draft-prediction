import pandas

from utils.index import string_to_list


def get_counter_index(df, wr_map):
    team1_pick_column = df["Team1Picks"].to_numpy()
    team2_pick_column = df["Team2Picks"].to_numpy()
    countering_list = []
    for index, team1_picks in enumerate(team1_pick_column):
        team2_picks = team2_pick_column[index]

        team1_wr = get_wr_sum(team1_picks, team2_picks, wr_map)
        team2_wr = get_wr_sum(team2_picks, team1_picks, wr_map)

        countering = team2_wr - team1_wr
        countering_list.append(countering)
    df["Countering"] = countering_list


def get_wr_sum(team1_picks, team2_picks, wr_map):
    wr_sum = 0
    team1_champion_list = string_to_list(team1_picks)
    team2_champion_list = string_to_list(team2_picks)
    for champion in team1_champion_list:
        champion = int(champion)
        for enemy_champion in team2_champion_list:
            enemy_champion = int(enemy_champion)
            wr_sum += wr_map[champion][enemy_champion]
    return wr_sum
