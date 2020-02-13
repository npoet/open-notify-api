# main.py
# written by Nicholas Poet on 2.13.2020

from datetime import datetime
import * from src
import sys


def main():
    if len(sys.argv) > 4:
        print("Too many arguemnts provided, please use any combination of 'loc', 'pass', and 'people'.\nExiting...")
        return
    if 'loc' in sys.argv:
        time = datetime.utcnow()
        coordinates = get_loc()
        print(f'The ISS current location at {time} is {coordinates}\n')
    if 'pass' in sys.argv:
        #TODO
    if 'people' in sys.argv:
        # TODO

    return


if __name__ == '__main__':
    main()
