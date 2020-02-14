#!/usr/bin/python3
# ppl_in_space.py
# written by Nicholas Poet on 2.13.2020

import requests

API_ADDR = 'http://api.open-notify.org/astros.json'


def get_ppl():
    """
    Get the current number of astronauts in space (by craft), and their names if available

    Returns:
        dict: Names of astronauts by craft in the format:
        {"craft1": [person1, person2, ...], "craft2": [p1, ... ] ...}
    """
    resp = requests.get(API_ADDR)
    people = resp.json()

    astros_by_craft = {}
    for entry in people['people']:
        if entry['craft'] not in astros_by_craft:
            astros_by_craft[entry['craft']] = []
        if entry['craft'] in astros_by_craft:
            astros_by_craft[entry['craft']].append(entry['name'])

    return astros_by_craft
