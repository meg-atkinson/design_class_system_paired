import pytest
from datetime import datetime
from lib.tyre import Tyre

"""
On creating tyre instance
position is one of the four prescribed positions else raise error
"""
def test_tyre_position_exists():
    with pytest.raises(Exception) as e:
        tyre = Tyre("middle", 15.0, 20)
    error_msg = str(e.value)
    assert error_msg == "No such tyre position"


"""
On creating tyre instance
pressure is float else raise error
"""
def test_tyre_pressure_is_float():
    with pytest.raises(Exception) as e:
        tyre = Tyre("FR", 15, 20)
    error_msg = str(e.value)
    assert error_msg == "Pressure must be a float"


"""
On creating tyre instance
tread_depth is int else raise error
"""
def test_tyre_tread_depth_is_int():
    with pytest.raises(Exception) as e:
        tyre = Tyre("FR", 15.0, 20.45)
    error_msg = str(e.value)
    assert error_msg == "Tread depth must be an integer"


"""
On creating tyre instance
tread_depth is int else raise error
"""
def test_attributes():
    tyre = Tyre("FR", 15.0, 14)
    assert tyre.position == "FR"
    assert tyre.pressure == 15.0
    assert tyre.tread_depth == 14
    assert isinstance(tyre.reading_time, datetime) == True

