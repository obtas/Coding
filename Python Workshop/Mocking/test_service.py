from service import *

def test_getOne(mocker):
    # Arrange
    test_data = [(2,15, 1, 'Michael')]
    mocker.patch("db.runQuery", return_value = test_data)
    id = 2
    
    # Act
    result = getOne(2)
    
    # Assert 
    assert result == test_data
    
def test_createPenguin(mocker):
    # Arrange
    #fish = 6
    #dancing = True
    #name = 'Judith'
    test_data = [(85,6,1,'Judith')]
    mocker.patch("db.runQuery", return_value=test_data)
    
    # Act
    #result = createPenguin(fish, dancing, name)
    result = createPenguin(6,True,'Judith')
    
    # Assert
    assert result == test_data