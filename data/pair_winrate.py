import numpy as np
import pandas

from data.columns import PICKS_ARRAY_COLUMNS
from utils.index import string_to_list


def get_pair_data(df):
    matches_map = np.zeros(shape=(166, 166), dtype=int)
    wins_map = np.zeros(shape=(166, 166), dtype=int)

    for column in PICKS_ARRAY_COLUMNS:
        team_pick_column = df[column].to_numpy()

        for index, match in enumerate(team_pick_column):
            champion_list = string_to_list(match)
            for i in range(4):
                j = i+1
                while j < 5:
                    champion1 = int(champion_list[i])
                    champion2 = int(champion_list[j])
                    matches_map[champion1][champion2] += 1
                    matches_map[champion2][champion1] += 1

                    if df["Winner"][index] == 1:
                        wins_map[champion1][champion2] += 1
                        wins_map[champion2][champion1] += 1
                    j += 1

    matches_df = pandas.DataFrame(matches_map)
    matches_df.to_csv("../csv/PairMatchesMatrix.csv", index=False, header=False)

    wins_df = pandas.DataFrame(wins_map)
    wins_df.to_csv("../csv/PairWinsMatrix.csv", index=False, header=False)


def get_winrates(match_map, win_map):
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
    winrate_df.to_csv("../csv/PairWinrateMatrix.csv", index=False, header=False)
