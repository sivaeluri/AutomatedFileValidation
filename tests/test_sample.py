 
import pandas as pd
import pytest

def test_sample():
    """A simple test to check if pandas is working correctly."""
    data = {"ID": [1, 2, 3], "Value": [10, 20, 30]}
    df = pd.DataFrame(data)
    assert df["Value"].sum() == 60  # Test if sum of values is 60

if __name__ == "__main__":
    pytest.main()
