# File: car.py

class Car:
    def __init__(self, fl_tyre, fr_tyre, bl_tyre, br_tyre):
        self.fl_tyre = [fl_tyre]
        self.fr_tyre = [fr_tyre]
        self.bl_tyre = [bl_tyre]
        self.br_tyre = [br_tyre]
    # store instances of all tyres - individually (lists of tyre objects)
    
    def update(self, fl_tyre, fr_tyre, bl_tyre, br_tyre):
        self.fl_tyre.append(fl_tyre)
        self.fr_tyre.append(fr_tyre)
        self.bl_tyre.append(bl_tyre)
        self.br_tyre.append(br_tyre)

    def get_position(self,position):
        if position == "FL":
            return self.fl_tyre
        elif position == "FR":
            return self.fr_tyre
        elif position == "BL":
            return self.bl_tyre
        else:
            return self.br_tyre

    def get_readings(self, position):
        #implements for loop - iterate through list for that tyre, getting readings and time
        # returns list of readings and time
        relevant_list = self.get_position(position)

        historical_readings = {}
        for item in relevant_list:
            entry = {item.reading_time : {"pressure" : item.pressure,
                                      "tread_depth" : item.tread_depth}
            }
            historical_readings.update(entry)

        return historical_readings

    def get_latest_readings(self):
        #get last item on list in each of the four lists - concatonate into one list 
        list_of_current_tyres = [self.fl_tyre[-1], self.fr_tyre[-1], 
                                 self.bl_tyre[-1], self.br_tyre[-1]]
        
        all_tyres_at_a_glance = {}
        for item in list_of_current_tyres:
            pack_the_tyre = {item.position : {"pressure" : item.pressure,
                                      "tread_depth" : item.tread_depth,
                                      "date_taken" : item.reading_time}}
            all_tyres_at_a_glance.update(pack_the_tyre)

        return all_tyres_at_a_glance
            
    