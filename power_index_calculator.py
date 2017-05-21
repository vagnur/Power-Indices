from itertools import combinations
from operator import itemgetter
from math import factorial
import collections

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BANZHAF
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def banzhaf(weight, quota):
    """
    Calculator for the banzhaf index of each player.

    Parameters
    ----------
    weight  : list
                Vector with the weights of each player.
    quota   : int
                Necesary weight to win the game.

    Returns
    -------
    list
        Vector of the banzhaf power for each player, where banzhaf_index[i] is
        the banzhaf power for the player i.

    """
    players = name_players(weight)
    coalitions = winning_coalitions(players, quota)

    banzhaf_power = []
    for player in players:
        player_banzhaf = 0.0
        for coalition in coalitions:
            if is_critical(player, players, coalition, quota):
                player_banzhaf += 1
        banzhaf_power.append(player_banzhaf)

    total_power = float(sum(banzhaf_power))
    banzhaf_index = map(lambda x: round((x / total_power), 3), banzhaf_power)

    return banzhaf_index


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
SHAPLEY
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def shapley(weight, quota):
    """
    Calculator for the shapley-shubik index of each player.

    Parameters
    ----------
    weight  : list
                Vector with the weights of each player.
    quota   : int
                Necesary weight to win the game.

    Returns
    -------
    list
        Vector of the shapley-shubik power for each player,
        where shapley_index[i] is the shapley-shubik power for the player i.

    """
    number_of_players = len(weight)
    players = name_players(weight)
    coalitions = winning_coalitions(players, quota)

    SSI = []
    for player in players:
        player_ssi = 0.0
        for coalition in coalitions:
            if is_critical(player, players, coalition, quota):
                player_ssi += float((factorial(number_of_players - len(coalition)) * factorial(len(coalition) - 1))) / factorial(number_of_players)
        SSI.append(player_ssi)
    total_ssi = sum(SSI)

    shapley_index = map(lambda x: round((x / total_ssi), 3), SSI)

    return shapley_index


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HOLLER-PACKEL
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def holler_packel(weight, quota):
    """
    Calculator for the holler-packel index of each player.

    Parameters
    ----------
    weight  : list
                Vector with the weights of each player.
    quota   : int
                Necesary weight to win the game.

    Returns
    -------
    list
        Vector of the holler-packel power for each player,
        where holler_index[i] is the holler-packel power for the player i.

    """
    players = name_players(weight)
    minimal_coalitions = list(winning_minimal_coalitions(players, quota))

    minimal_aparition = []
    for player in players:
        player_in_minimal = 0.0
        for coalition in minimal_coalitions:
            if is_critical(player, players, coalition, quota):
                player_in_minimal += 1.0
        minimal_aparition.append(player_in_minimal)
    total_minimal_aparition = sum(minimal_aparition)

    holler_index = map(lambda x: round((x / total_minimal_aparition), 3),
                       minimal_aparition)

    return holler_index


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DEEGAN-PACKEL
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def deegan_packel(weight, quota):
    """
    Calculator for the deegan-packel index of each player.

    Parameters
    ----------
    weight  : list
                Vector with the weights of each player.
    quota   : int
                Necesary weight to win the game.

    Returns
    -------
    list
        Vector of the deegan-packel power for each player,
        where deegan_index[i] is the deegan-packel power for the player i.

    """
    players = name_players(weight)
    minimal_coalitions = list(winning_minimal_coalitions(players, quota))

    TDPP = []
    for player in players:
        player_tdpp = 0.0
        for coalition in minimal_coalitions:
            if player in coalition:
                player_tdpp += 1.0/len(coalition)
        TDPP.append(player_tdpp)
    total_tdpp = sum(TDPP)

    deegan_index = map(lambda x: round((x / total_tdpp), 3), TDPP)

    return deegan_index


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
JOHNSTON
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def johnston(weight, quota):
    """
    Calculator for the johnston index of each player.

    Parameters
    ----------
    weight  : list
                Vector with the weights of each player.
    quota   : int
                Necesary weight to win the game.

    Returns
    -------
    list
        Vector of the johnston power for each player,
        where johnston_index[i] is the johnston power for the player i.

    """
    players = name_players(weight)
    coalitions = winning_coalitions(players, quota)

    deflectors = []
    for coalition in coalitions:
        total_votes = 0
        for player in coalition:
            total_votes += players[player]
        deflect = []
        for player in players:
            if player in coalition and total_votes-players[player] < quota:
                deflect.append(player)
        deflectors.append(deflect)

    TJP = []
    for player in players:
        player_tjp = 0.0
        for deflect in deflectors:
            if player in deflect:
                player_tjp += (1.0/len(deflect))
        TJP.append(player_tjp)
    total_tjp = sum(TJP)

    johnston_index = map(lambda x: round((x / total_tjp), 3), TJP)

    return johnston_index


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
COMMON

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def _winning_coalitions(players, quota):
    """
    List the winning coalitions of a given game.

    Parameters
    ----------
    players : dictionary
                Name of the the players and their weights.
    quota   : int
                Necesary weight to win the game.

    Yields
    -------
    list
        A winning coalition.

    """
    if quota <= 0:
        for coalition_size in range(len(players)+1):
            for coalition in combinations(players, coalition_size):
                yield coalition
    elif not players:
        pass
    else:
        player_name, player_votes = players[-1]
        players = players[:-1]
        for coalition in _winning_coalitions(players, quota-player_votes):
            yield ((player_name, player_votes),) + coalition
            if sum([votes for (name, votes) in coalition]) >= quota:
                yield coalition


def winning_coalitions(players, quota):
    """
    List the winning coalitions of a given game.

    Parameters
    ----------
    players : dictionary
                Name of the the players and their weights.
    quota   : int
                Necesary weight to win the game.

    Returns
    -------
    list
        Vector of the winning coalitions, each winning coalition list
        the name of the players for what it conforms.

    """
    players = sorted(players.items(), key=itemgetter(1))
    coalitions = _winning_coalitions(players, quota)
    return sorted([sorted([name for (name, votes) in c]) for c in coalitions])


def number_players_search(weights, players, quota):
    """
    Count the quantity of players before they pass the quota.

    Parameters
    ----------
    weight  : list
                Vector with the weights of each player.
    players : dictionary
                Name of the the players and their weights.
    quota   : int
                Necesary weight to win the game.

    Returns
    -------
    int
        Quantity of players.

    """
    total_power = 0
    number_players = 0
    for player in weights:
        total_power += players[player]
        number_players += 1
        if total_power >= quota:
            return number_players


def winning_minimal_coalitions(players, quota):
    """
    List the minimal coalitions that win the game.

    Parameters
    players : dictionary
                Name of the the players and their weights.
    quota   : int
                Necesary weight to win the game.

    Yields
    -------
    list
        A minimal coalition.

    """
    min_to_max_weight = [i[0] for i in sorted(players.items(),
                                              key=itemgetter(1))]

    max_to_min_weight = [i[0] for i in  sorted(players.items(),
                                               key=itemgetter(1),
                                               reverse=True)]

    min_players = number_players_search(max_to_min_weight, players, quota)
    max_players = number_players_search(min_to_max_weight, players, quota)

    for i in range(min_players, max_players + 1):
        potencial_coalitions = combinations(players, i)
        for coalition in potencial_coalitions:
            total_power = 0
            for player in coalition:
                total_power += players[player]
            if total_power == quota:
                yield coalition
            elif total_power > quota:
                flag = 1
                for player in coalition:
                    if not(total_power-players[player] < quota):
                        flag = 0
                        break
                if flag:
                    yield coalition


def name_players(weight):
    """
    Name the players of the game.

    Parameters
    ----------
    weight  : list
                Vector with the weights of each player.

    Returns
    -------
    dictionary
        A name of each player with his power in a dictionary. The
        weight if the player[i] = weight[i].

    """
    players = {}
    counter = 0
    for letter in range(ord('a'), ord('z')+1):
        player_name = chr(letter)
        players[player_name] = weight[counter]
        counter += 1
        if counter == len(weight):
            return collections.OrderedDict(sorted(players.items()))


def is_critical(player, players, coalition, quota):
    """
    Criticality analyzer for a player

    Parameters
    ----------
    player    : string
                    Name of the player that is gonna be analyzed.
    players   : dictionary
                    Name of the the players and their weights.
    coalition : dictionary
                    Vector with the name of the players and their weights,
                    for the winning coalition to analyze.
    quota     : int
                    Necesary weight to win the game.

    Returns
    -------
    bool
        If the total power of the coalition, less the power of the player,
        is less than the quota returns true, otherwise returns false.

    """
    total_power = 0
    for cplayer in coalition:
        if cplayer != player:
            total_power += players[cplayer]
    if total_power < quota:
        return True
    return False
