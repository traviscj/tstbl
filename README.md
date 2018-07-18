
Often, I have a duration in seconds and want to know how many hours/days/whatever that would be.
Enter `tstbl`:

    ➜ tstbl 123456
    method|frac               |whole
    ------|-------------------|-----
    w     |0.20412698412698413|0
    d     |1.4288888888888889 |1
    h     |34.29333333333334  |10
    m     |2057.6             |17
    s     |123456.0           |36

This quickly tells me that it's 1.42 days or 1 day, 10 hours.

Other times, I have a couple of timestamps:

    ➜ tstbl 12:00:00 13:00:00
    method|frac                |whole
    ------|--------------------|-----
    w     |0.005952380952380952|0
    d     |0.041666666666666664|0
    h     |1.0                 |1
    m     |60.0                |0
    s     |3600.0              |0

## installing

    virtualenv venv
    . venv/bin/activate
    pip3 install --editable .
