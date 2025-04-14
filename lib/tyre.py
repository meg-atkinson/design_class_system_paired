#File tyre.py
from datetime import date

class Tyre:
    def __init__(self, position, pressure, tread_depth):
        #store various attributes of the tyre
        # self.position
        # self.pressure
        # self.tread_depth
        # self.reading_time
        valid_positions = ["FL", "FR", "BL", "BR"]
        if position.upper() not in valid_positions:
            raise Exception("No such tyre position")
        if not isinstance(pressure, float):
            raise Exception("Pressure must be a float")
        if not isinstance(tread_depth, int):
            raise Exception("Tread depth must be an integer")

        self.position = position
        self.pressure = pressure
        self.tread_depth = tread_depth
        self.reading_time = date.today()


    
