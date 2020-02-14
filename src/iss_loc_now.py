#!/usr/bin/python3
# iss_loc_now.py
# written by Nicholas Poet on 2.13.2020

import requests

API_ADDR = 'http://api.open-notify.org/iss-now.json'


def get_loc():
    """
    Get the location of the ISS at the current UTC time

    Returns:
        tuple: the location of the ISS containing coordinates in the format (LAT, LONG)
    """
    resp = requests.get(API_ADDR)
    location_info = resp.json()['iss_position']
    return location_info['latitude'], location_info['longitude']
