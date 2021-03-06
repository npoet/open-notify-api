#!/usr/bin/python3
# iss_pass_times.py
# written by Nicholas Poet on 2.13.2020

import requests
import sys

API_ADDR = 'http://api.open-notify.org/iss-pass.json'


def get_pass(latitude, longitude, altitude=False, number=False):
    """
    Gets the passing information for the ISS at given coordinates. If no optional parameters are
    supplied, get_pass will return the info for the next upcoming pass.

    Params:
        latitude: desired latitude as a value between -80 and 80
        longitude: desired longitude as a value between -180 and 180
        altitude: optional parameter, defaults to false to not be included unless specified as a number
        number: optional parameter, defaults to false to not be included unless specified as a number

    Returns:
        tuple: Time and duration of ISS pass at the given coordinates, in the format:
        (time, duration)
    """
    payload = {"lat": float(latitude), "lon": float(longitude)}

    if altitude:
        payload['alt'] = altitude
    if number:
        payload['n'] = number

    resp = requests.get(API_ADDR, params=payload)
    if resp.status_code != 200:
        print('Error from open-notify: bad request')
        print('Exiting...')
        sys.exit()

    pass_info = resp.json()['response']

    if number:
        return pass_info[0:number]

    return pass_info[0]
