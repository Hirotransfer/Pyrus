from enum import Enum


class Level(Enum):
    SYSTEM = 0x00000001
    SENSOR = 0x00000002
    WORLD = 0x00000004
    ACTION = 0x00000008
    INTERCEPT = 0x00000010
    KICK = 0x00000020
    HOLD = 0x00000040
    DRIBBLE = 0x00000080
    PASS = 0x00000100
    CROSS = 0x00000200
    SHOOT = 0x00000400
    CLEAR = 0x00000800
    BLOCK = 0x00001000
    MARK = 0x00002000
    POSITIONING = 0x00004000
    ROLE = 0x00008000
    PLAN = 0x00010000
    TEAM = 0x00020000
    COMMUNICATION = 0x00040000
    ANALYZER = 0x00080000
    ACTION_CHAIN = 0x00100000
    LEVEL_ANY = 0xffffffff

    # unused Levels :\
    LEVEL_00 = 0x00000000
    LEVEL_22 = 0x00200000
    LEVEL_23 = 0x00400000
    LEVEL_24 = 0x00800000
    LEVEL_25 = 0x01000000
    LEVEL_26 = 0x02000000
    LEVEL_27 = 0x04000000
    LEVEL_28 = 0x08000000
    LEVEL_29 = 0x10000000
    LEVEL_30 = 0x20000000
    LEVEL_31 = 0x40000000
    LEVEL_32 = 0x80000000
