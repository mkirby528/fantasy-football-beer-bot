from espn_api.football import League
from os import getenv
league: League = League(league_id=1181055176, year=2023,
                        espn_s2=getenv("ESPN_S2"),swid=getenv("ESPN_SWID"))


def get_zero_point_teams(week_number):
    matchups = league.box_scores(week_number)
    zero_point_teams_dict = {}
    for matchup in matchups:
        if matchup.home_team == 0 or matchup.away_team == 0:
            continue
        home_team_zeroes = get_zero_point_players(matchup.home_lineup)
        away_team_zeroes = get_zero_point_players(matchup.away_lineup)
        if len(home_team_zeroes) != 0:
            zero_point_teams_dict[matchup.home_team] = home_team_zeroes
        if len(away_team_zeroes) != 0:
            zero_point_teams_dict[matchup.away_team] = away_team_zeroes
    return (zero_point_teams_dict)


def get_zero_point_players(lineup):
    zero_point_players = []
    
    for player in lineup:
        if player.points <= 0 and player.slot_position not in ("BE", "IR"):
            zero_point_players.append(player.name)
    return zero_point_players



