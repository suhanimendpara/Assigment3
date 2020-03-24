import requests


class Pokemon:
    def __init__(self, name):
        """
        Builds a pokemon from the PokeAPI using the name.  Raises exception
        if the pokemon does not exist there.
        :param name:
        """
        poke_json = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(name))
        if poke_json.status_code == 404:
            raise ValueError("Pokemon is bogus.  Try a real one next time.")


def brawl(poke1: Pokemon, poke2: Pokemon, html="results.html",
          record="history.csv"):
    """
    Pits the two pokemon against each other in a battle of wills
    :param poke1: the first combatant
    :type poke1: Pokemon
    :param poke2: the second combatant
    :type poke2: Pokemon
    :param html:  a file to which the results will be written
    :param record: a file to which the results will be written and read
    :return: None
    """
    pass
