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
                                            "date_taken": date.today()},
                                        "FR": {"pressure": 20.0, 
                                            "tread_depth": 21, 
                                            "date_taken": date.today()},   
                                        "BL": {"pressure": 25.0, 
                                            "tread_depth": 22, 
                                            "date_taken": date.today()}, 
                                        "BR": {"pressure": 30.0, 
                                            "tread_depth": 23, 
                                            "date_taken": date.today()}, 
                                            }
    

def test_returns_list_of_historical_readings():
    fl = Tyre("FL", 15.0, 20)
    fr = Tyre("FR", 20.0, 21)
    bl = Tyre("BL", 25.0, 22)
    br = Tyre("BR", 30.0, 23)
    car = Car(fl, fr, bl, br)
    fl1= Tyre("FL", 11.0, 10)
    fr1 = Tyre("FR", 12.0, 11)
    bl1 = Tyre("BL", 13.0, 12)
    br1 = Tyre("BR", 14.0, 13)
    car.update(fl1, fr1, bl1, br1)

    assert car.get_readings("FL") == {date.today() : {"pressure": 15.0,
                                                      "tread_depth": 20},
                                        date.today() : {"pressure": 11.0,
                                                      "tread_depth": 10}
                                    }
    