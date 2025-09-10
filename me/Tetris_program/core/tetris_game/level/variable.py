from enum import Enum


class LevelParameter:
    MAX_LEVEL = 10 - 1
    LEVEL_INTERVAL = 20

    # drop_clock, raise_interval uint is ms
    difficult_table = {
        0:  {"drop_clock": 500, "raise_lines": 0, "raise_interval": 7000},
        1:  {"drop_clock": 450, "raise_lines": 0, "raise_interval": 7000},
        2:  {"drop_clock": 450, "raise_lines": 1, "raise_interval": 7000},
        3:  {"drop_clock": 400, "raise_lines": 1, "raise_interval": 6000},
        4:  {"drop_clock": 350, "raise_lines": 1, "raise_interval": 6000},
        5:  {"drop_clock": 300, "raise_lines": 1, "raise_interval": 5000},
        6:  {"drop_clock": 450, "raise_lines": 2, "raise_interval": 7000},
        7:  {"drop_clock": 400, "raise_lines": 2, "raise_interval": 6000},
        8:  {"drop_clock": 300, "raise_lines": 2, "raise_interval": 6000},
        9:  {"drop_clock": 250, "raise_lines": 2, "raise_interval": 5000},
    }

    level_table = {
        0: 0,
        30: 1,
        60: 2,
        90: 3,
        120: 4,
        150: 5,
        180: 6,
        210: 7,
        240: 8,
        270: 9,
    }
