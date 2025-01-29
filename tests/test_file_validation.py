import pandas as pd
import pytest
import os

# Define file paths
INPUT_DIR = "C:/TechM_Task/AutomatedFileValidation/data/"
OUTPUT_DIR = "C:/TechM_Task/AutomatedFileValidation/data/"
INSTRUMENT_FILE = os.path.join(INPUT_DIR, "InstrumentDetails.csv")
POSITION_FILE = os.path.join(INPUT_DIR, "PositionDetails.csv")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "PositionReport.csv")

def load_csv(file_path):
    """Helper function to load a CSV file as a DataFrame."""
    return pd.read_csv(file_path)

def generate_expected_output(instrument_df, position_df):
    """Generate the expected PositionReport.csv content."""
    merged_df = position_df.merge(
        instrument_df, left_on="InstrumentID", right_on="ID", suffixes=("_Position", "_Instrument")
    )
    merged_df["Total Price"] = merged_df["Quantity"] * merged_df["Unit Price"]
    expected_df = merged_df[["ID_Position", "InstrumentID", "ISIN", "Quantity", "Total Price"]]
    expected_df.rename(columns={"ID_Position": "ID", "InstrumentID": "PositionID"}, inplace=True)
    return expected_df

def test_validate_output_file():
    """Test case to validate the application's output file against expected data."""
    # Load input files
    instrument_df = load_csv(INSTRUMENT_FILE)
    position_df = load_csv(POSITION_FILE)

    # Generate expected output
    expected_df = generate_expected_output(instrument_df, position_df)

    # Load the application's output file
    actual_df = load_csv(OUTPUT_FILE)

    # Compare expected vs actual data
    pd.testing.assert_frame_equal(expected_df, actual_df, check_dtype=False)

if __name__ == "__main__":
    pytest.main()
 
