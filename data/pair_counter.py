import numpy as np
import pandas

from utils.index import string_to_list


def get_counter_data(df):
    matches_map = np.zeros(shape=(166, 166), dtype=int)
    wins_map = np.zeros(shape=(166, 166), dtype=int)

    team1_pick_column = df["Team1Picks"].to_numpy()
    team2_pick_column = df["Team2Picks"].to_numpy()

    for index, team1_picks_string in enumerate(team1_pick_column):
        team1_champion_list = string_to_list(team1_picks_string)

        team2_picks_string = team2_pick_column[index]
        team2_champion_list = string_to_list(team2_picks_string)
        for champion in team1_champion_list:
            champion = int(champion)
            for enemy_champion in team2_champion_list:
                enemy_champion = int(enemy_champion)
                matches_map[champion][enemy_champion] += 1
                matches_map[enemy_champion][champion] += 1

                if df["Winner"][index] == 1:
                    wins_map[champion][enemy_champion] += 1
                elif df["Winner"][index] == 2:
                    wins_map[enemy_champion][champion] += 1

    matches_df = pandas.DataFrame(matches_map)
    matches_df.to_csv("../csv/CounterMatchesMatrix.csv", index=False, header=False)

    wins_df = pandas.DataFrame(wins_map)
    wins_df.to_csv("../csv/CounterWinsMatrix.csv", index=False, header=False)


def get_counter_winrates(match_map, win_map):
    wr_map = np.zeros(shape=(166, 166), dtype=float)
    for column_index, row in enumerate(match_map.to_numpy()):
        for row_index, num_matches in enumerate(row):
            num_wins = win_map[column_index][row_index]
            if num_matches == 0:
                winrate = 0
            else:
                winrate = num_wins / num_matches
            wr_map[column_index][row_index] = winrate

    winrate_df = pandas.DataFrame(wr_map)
    winrate_df.to_csv("../csv/CounterWinrateMatrix.csv", index=False, header=False)
