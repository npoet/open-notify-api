#!/usr/bin/python3
# main.py
# written by Nicholas Poet on 2.13.2020

from datetime import datetime
import re
from src.iss_loc_now import get_loc
from src.iss_pass_times import get_pass
from src.ppl_in_space import get_ppl
import sys


def main():
    # main argument parsing
    if 'loc' in sys.argv:
        time = datetime.utcnow()
        coordinates = get_loc()
        print(f'The ISS current location at {time} is {coordinates}.\n')

    if 'pass' in sys.argv:
        index = sys.argv.index('pass')
        coords = sys.argv[index + 1]
        coords = coords.split(",")
        pass_info = get_pass(coords[0], coords[1])
        time = datetime.fromtimestamp(pass_info['risetime'])
        duration = pass_info['duration']
        print(f'The ISS will be overhead {coords[0], coords[1]} at {time} for {duration} seconds.\n')

    if 'people' in sys.argv:
        astros = get_ppl()
        vessels = list(astros.keys())
        for i in range(len(vessels)):
            print(f'The {vessels[i]} currently has {len(astros[vessels[i]])} people on board.')
            names = astros[vessels[i]]
            print(f"Their names are {', '.join(names[0:-1])}, and {names[-1]}\n")

    # sanity checks
    if 'loc' not in sys.argv and 'pass' not in sys.argv and 'people' not in sys.argv:
        print('Invalid command line option(s), please use any combination of "loc", "pass LAT,LONG", and "people".')
        return
    for entry in sys.argv:
        if entry != 'main.py' and entry != 'loc' and entry != 'pass' and entry != 'people' \
                and not bool(re.match(r"[+-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?[0-9]+)?", entry)):
            print(f'Invalid command line option "{entry}", '
                  'please use any combination of "loc", "pass LAT,LONG", and "people".')
            return

    return


if __name__ == '__main__':
    main()
