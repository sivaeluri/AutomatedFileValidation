# Automated File Validation   # Windows

Automated File Validation
Project Overview
This project validates an application's output file against input CSV files to ensure correctness. The input consists of two files:
* InstrumentDetails.csv: Contains instrument data.
* PositionDetails.csv: Contains position data.
The output is the PositionReport.csv, which must be validated by comparing it against expected values calculated from the input files.
Setup Instructions
1. Install Python
Ensure that Python 3.8+ is installed on your machine. You can download it from here.
2. Install Dependencies
After Python is installed, navigate to the project directory and install the necessary libraries by running:
bash
CopyEdit
pip install -r requirements.txt
This will install the following dependencies:
* pandas for data manipulation.
* pytest for running the test cases.
* openpyxl for handling Excel files (if needed in the future).
Alternatively, you can manually install them using:
bash
CopyEdit
pip install pandas pytest openpyxl
3. Project Folder Structure
The project is organized as follows:
bash
CopyEdit
AutomatedFileValidation/
??? tests/                 # Folder for test scripts
??? data/                  # Folder for input/output CSV files
??? docs/                  # Folder for documentation
??? README.md              # Instructions for the project
??? requirements.txt       # Dependencies list
4. Prepare the Input Files
The following input files are required to run the tests:
* InstrumentDetails.csv (Place in data/ folder)
* PositionDetails.csv (Place in data/ folder)
5. Prepare the Output File
The application should generate the PositionReport.csv in the data/ folder.

Running the Tests
1. To validate the output file, navigate to the project directory in the terminal/command prompt:
bash
CopyEdit
cd path/to/AutomatedFileValidation
2. Run the tests with the following command:
bash
CopyEdit
pytest tests/test_file_validation.py
3. Test Results:
o If the files match, you’ll see a success message:
CopyEdit
1 passed in 0.12s
o If there is a mismatch, pytest will display the differences.

Understanding the Tests
Test Case: Validate Output File
The test_file_validation.py script performs the following steps:
1. Loads the input files: InstrumentDetails.csv and PositionDetails.csv.
2. Calculates the expected output by merging these files and computing the total price (Quantity * Unit Price).
3. Loads the application's generated PositionReport.csv file.
4. Compares the expected output with the actual output and reports any discrepancies.
Test Failure
If the test fails, pytest will show where the data mismatches occur, helping you debug the issue.

Future Improvements
* Extend the tests to check for additional validation criteria (e.g., data integrity, missing values).
* Add support for handling more complex cases or larger datasets.
* Integrate the tests with a CI/CD pipeline for automated testing.

