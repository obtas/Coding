from badcode import *

def test_roll_lots_of_dice(mocker):
    # Use mocking to confirm that it returns 4
    # Arrange
    mocker.patch("random.randint", return_value=4)
    
    # Act
    result = roll_lots_of_dice()
    
    # Assert
    assert result == 4
    
def test_checkrolls(mocker):
    # Arrange
    mocker.patch("random.randint", return_value=10)
    
    # Act
    result = checkrolls()
    
    # Assert
    assert result == "big number!!!"
    
def test_roll_custom_numbers(mocker):
    # Arrange
    numberone = 5
    numbertwo = 3
    mocker.patch("random.randint", return_value=5)
    
    # Act
    result = roll_custom_numbers(numberone, numbertwo)
    
    # Assert
    assert result == 5,3