# open-notify API Implementation

A simple script to interact with the open-notify API, written in Python 3.7

#### Required Packages:

- requests
- builtins including datetime, re, and sys

#### File Structure:
    . open-notify
    ├── _src    (API interaction functions)
    |   ├── iss_loc_now.py
    |   ├── iss_pass_times.py
    |   └── ppl_in_space.py
    ├── .gitignore
    ├── main.py     (functional script)
    └── README.md
    
#### Usage:

This API implementation can be run as a single script via main.py:

```
python3 main.py loc
python3 main.py pass LAT,LONG
python3 main.py people
```

The package also accepts multiple user inputs in any order and will display results for each separated by a newline. 
For example:

```
python3 main.py loc pass LAT,LONG
```

Results in:

```
The ISS current location at {current UTC} is {LAT,LONG}

The ISS will be overhead ({LAT,LONG}) at {time} for {duration}
```