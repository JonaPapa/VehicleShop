from enum import Enum

class Color(Enum):
    BLACK = 1
    WHITE = 2
    BLUE = 3
    GREY = 4
    BROWN = 5
    RED = 6

class FuelType(Enum):
    GASOLINE = 1
    DIESEL = 2

class Manufacturer(Enum):
    SKODA = 1
    HONDA = 2
    VW = 3
    BMW = 4
    AUDI = 5

class Transmission(Enum):
    MANUAL = 1
    AUTOMATIC = 2

class VehicleFile(Enum):
    BUY = 1
    RENT = 2