from decimal import Decimal

def convert_string_to_decimals(value: str) ->Decimal:
    """
    Returns a Decimal Value approximated to Two Decimal Places
    """
    return Decimal("{:.2f}".format(value))

def calculate_expected_returns(amount_invested: Decimal, roi_percentage: Decimal) -> dict:
    expected_capital_gain = amount_invested * (roi_percentage / 100)
    total_returns = amount_invested + expected_capital_gain
    return {
        "expected_capital_gain": convert_string_to_decimals(expected_capital_gain),
        "total_returns": convert_string_to_decimals(total_returns)
        }