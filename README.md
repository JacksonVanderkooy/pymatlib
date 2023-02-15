# pymatlib

This readme is a work in progress. Currently it's only purpose is so I don't forget how this package works when I inevitably forget it exists for months.

## Installation (Opening Docker)

1) Have docker installed

2) Clone the repo into any empty folder and `cd` into it.

3) run `docker-compose build`
    
    a) If you get an error and you're using WSL in windows, make sure docker desktop is running locally

## Booting container

1) cd into the git repo folder.

2) run `docker-compose run pymat`

3) Once in the container, `cd` into the home directory.

## Usage (Using the Package)

1) Open python

2) run `from pymatbase import *`

3) Done.
## Included Packages

See the code in ./pkg/pymatbase.py

## Included Code

### matplotlib

 - figure()
 - close()
 - xlim()
 - ylim()
 - title()
 - xlabel()
 - ylabel()
 - plot()

### control

 - s (the variable for frequency domain math)

## Custom Functions

 - step(tf)
    - Based on control.step_response(tf)
 - impulse(tf)
    - Based on control.impulse_response(tf)

## Default Settings

 - plt.ion()
    -idk how it works, just that it lets the code keep running when you open a figure.