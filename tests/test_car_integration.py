import pytest
from datetime import date

from lib.tyre import Tyre
from lib.car import Car

def test_access_attributes_of_one_tyre():
    fl = Tyre("FL", 15.0, 20)
    fr = Tyre("FR", 20.0, 21)
    bl = Tyre("BL", 25.0, 22)
    br = Tyre("BR", 30.0, 23)
    car = Car(fl, fr, bl, br)
    assert car.get_latest_readings() == {
                                        "FL": {"pressure": 15.0, 
                                            "tread_depth": 20, 
                                            "date taken": date.today()},
                                        "FR": {"pressure": 20.0, 
                                            "tread_depth": 21, 
                                            "date taken": date.today()},   
                                        "BL": {"pressure": 25.0, 
                                            "tread_depth": 22, 
                                            "date taken": date.today()}, 
                                        "BR": {"pressure": 30.0, 
                                            "tread_depth": 23, 
                                            "date taken": date.today()}, 
                                            }