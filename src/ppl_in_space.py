# ppl_in_space.py
# written by Nicholas Poet on 2.13.2020

import requests

API_ADDR = "http://api.open-notify.org/astros.json"


def get_ppl():
    """
    Get the current number of astronauts in space (by craft), and their names if available

    Returns:
    dict: Names of astronauts by craft in the format {"craft1": p1, p2 ..., "craft2": p1,  ...}
    """
    resp = requests.get(API_ADDR)
    people = resp.json()
    return people
