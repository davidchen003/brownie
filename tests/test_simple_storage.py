from brownie import SimpleStorage, accounts

# test No.1
def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    print(f"Expected value: {expected}")
    print(f"starting_value: {starting_value}")
    # Assert
    assert starting_value == expected


# Test No.2
def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    print(f"Expected value: {expected}")
    print(f"udpated_value: {simple_storage.retrieve()}")
    # Assert
    assert expected == simple_storage.retrieve()
