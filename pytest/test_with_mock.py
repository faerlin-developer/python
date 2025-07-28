import pytest

from main import fetch_page
from main import long_running_task
from main import process_payment


def test_fetch(mocker):
    # Create mock response
    response = mocker.Mock
    response.status_code = 200

    # Create mock client
    client = mocker.Mock()
    client.get.return_value = response

    # Call target function
    response = fetch_page(client)

    # Verify response
    assert response.status_code == 200
    client.get.assert_called_once_with("https://google.com")


def test_long_running_task(mocker):
    mocker.patch("time.sleep", return_value=None)
    result = long_running_task()
    assert result == "Task Complete"


def test_process_payment_with_side_effects(mocker):
    # Create mocks
    payment_gateway = mocker.Mock()
    payment_gateway.charge.side_effect = ["Success", ValueError("Insufficient funds")]

    # Expect success for first call
    result = process_payment(payment_gateway, 100)
    assert result == "Payment processed successfully"

    # Expect failure for second call
    with pytest.raises(ValueError, match="Insufficient funds"):
        process_payment(payment_gateway, 200)

    assert payment_gateway.charge.call_count == 2
