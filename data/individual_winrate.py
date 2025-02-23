import numpy as np
import pandas

from utils.index import string_to_list


def get_winrates(df):
    matches_list = np.zeros(shape=166, dtype=int)
    wins_list = np.zeros(shape=166, dtype=int)

    team1_pick_column = df["Team1Picks"].to_numpy()
    team2_pick_column = df["Team2Picks"].to_numpy()

    populate_lists(team1_pick_column, df["Winner"], 1, matches_list, wins_list)
    populate_lists(team2_pick_column, df["Winner"], 2, matches_list, wins_list)

    winrate_list = np.zeros(shape=166, dtype=float)
    for index, num_matches in enumerate(matches_list):
        if num_matches == 0:
            pass
        else:
            winrate_list[index] = wins_list[index] / num_matches

    winrate_df = pandas.DataFrame(winrate_list)
    winrate_df.to_csv("../csv/IndividualWinrate.csv", index=False, header=False)


def populate_lists(pick_column, winner_column, winner, match_list, win_list):
    for index, team_picks in enumerate(pick_column):
        team_champion_list = string_to_list(team_picks)
        for champion in team_champion_list:
            champion = int(champion)
            match_list[champion] += 1
            if winner_column[index] == winner:
                win_list[champion] += 1


def add_winrate_to_df():
    df = pandas.read_csv("../csv/ScoreboardCountering.csv", sep=";")
    individual_winrates = pandas.read_csv("../csv/IndividualWinrate.csv").values

    matchup_list = []

    for i in range(len(df.values)):
        team_matchup = 0
        for j in range(1, 6):
            team1_string = f'Team1Pick{j}'
            team2_string = f'Team2Pick{j}'

            champion1 = int(df[team1_string][i]) - 1
            champion2 = int(df[team2_string][i]) - 1

            winrate1 = individual_winrates[champion1][0]
            winrate2 = individual_winrates[champion2][0]

            individual_matchup = winrate2 - winrate1
            team_matchup += individual_matchup

        matchup_list.append(team_matchup)

    df["Matchup"] = matchup_list
    df.to_csv(path_or_buf="../csv/ScoreboardGames8.csv", sep=";", index=False)


add_winrate_to_df()
