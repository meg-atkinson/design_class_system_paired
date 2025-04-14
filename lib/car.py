# File: car.py

class Car:
    def __init__(self, fl_tyre, fr_tyre, bl_tyre, br_tyre):
        self.fl_tyre = [fl_tyre]
        self.fr_tyre = [fr_tyre]
        self.bl_tyre = [bl_tyre]
        self.br_tyre = [br_tyre]
    # store instances of all tyres - individually (lists of tyre objects)

    def get_readings(self, position):
        #implements for loop - iterate through list for that tyre, getting readings and time
        # returns list of readings and time
        pass 

    def get_latest_readings(self):
        #get last item on list in each of the four lists - concatonate into one list 
        pass
    