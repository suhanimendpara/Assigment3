from sys import argv

from monsters import Pokemon, brawl

if __name__ == '__main__':
    if len(argv) != 3:
        raise ValueError("Invalid command line arguments.  Must be python3 arena.py [pokemon1] [pokemon2]")

    first_combatant = Pokemon(name=argv[1])
    second_combatant = Pokemon(name=argv[2])

    brawl(first_combatant, second_combatant, html="results.html", record="history.csv")