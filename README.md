# CIS591 - CSV Import Project

This repository contains a Python-based CSV import utility developed for CIS 591. The project provides a robust and user-friendly way to import, analyze, and process CSV files.

## Features

- **CSV Import**: Import CSV files with automatic delimiter detection
- **Error Handling**: Comprehensive error handling for file operations
- **Data Analysis**: Basic data analysis and statistics
- **Filtering**: Filter data by column values
- **Export**: Export data summaries and analysis results
- **Interactive Mode**: Command-line interface for exploring data

## Files

- `csv_importer.py`: Main CSV import module with the CSVImporter class
- `example_usage.py`: Example script demonstrating basic usage
- `sample_students.csv`: Sample CSV file for testing

## Usage

### Basic Usage (Programmatic)

```python
from csv_importer import CSVImporter

# Create importer instance
importer = CSVImporter()

# Import CSV file
if importer.import_csv("your_file.csv"):
    # Display sample data
    importer.display_sample()
    
    # Get statistics
    print(f"Rows: {importer.get_row_count()}")
    print(f"Columns: {importer.get_column_count()}")
    
    # Filter data
    filtered = importer.filter_data("column_name", "value")
```

### Interactive Mode

Run the main script with a CSV file:

```bash
python3 csv_importer.py sample_students.csv
```

Or run without arguments to be prompted for a filename:

```bash
python3 csv_importer.py
```

### Example Usage

Run the example script to see the importer in action:

```bash
python3 example_usage.py
```

## Sample Data

The included `sample_students.csv` contains fictional student data with the following columns:
- student_id: Unique student identifier
- name: Student name
- age: Student age
- major: Academic major
- gpa: Grade Point Average
- year: Academic year (Sophomore, Junior, Senior)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Error Handling

The CSV importer includes robust error handling for:
- File not found errors
- Permission denied errors
- Encoding issues
- CSV parsing errors
- Invalid file formats

## License

This project is for educational purposes as part of CIS 591.
