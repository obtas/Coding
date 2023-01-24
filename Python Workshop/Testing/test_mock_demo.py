from mock_demo import multiplied_rand_num

# pip install pytest-mock

# When running a test tht is mocking an object, we pass in 'mocker'
def test_multiplied_rand_num(mocker):
    # Arrange
    # mocker is the object we are mocking, mock_demo
    # patch is modifying the functionality of this object
    # mocker. patch(file.function,return_value can be anything outside of the bounds too)
    mocker.patch("mock_demo.rand_num", return_value=10)
    
    
    # Act
    result = multiplied_rand_num()
    
    # Assert
    assert result == 20