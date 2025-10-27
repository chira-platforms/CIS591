#!/usr/bin/env python3
"""
Example usage of the CSV Importer for CIS591

This script demonstrates how to use the CSVImporter class to import and process CSV files.
"""

from csv_importer import CSVImporter


def example_usage():
    """Demonstrate basic CSV import functionality."""
    print("CSV Import Example for CIS591")
    print("=" * 40)
    
    # Create an instance of the CSVImporter
    importer = CSVImporter()
    
    # Import the sample CSV file
    filename = "sample_students.csv"
    print(f"Attempting to import '{filename}'...")
    
    if importer.import_csv(filename):
        print("\n✓ Import successful!")
        
        # Display basic information
        print(f"Imported {importer.get_row_count()} rows with {importer.get_column_count()} columns")
        
        # Show sample data
        print("\n📊 Sample Data:")
        importer.display_sample(3)
        
        # Filter example
        print("\n🔍 Filter Example - Computer Science students:")
        cs_students = importer.filter_data("major", "Computer Science")
        for i, student in enumerate(cs_students[:3]):
            print(f"  {i+1}. {student['name']} (GPA: {student['gpa']})")
        
        # Show summary
        print("\n📈 Data Summary:")
        importer.export_summary()
        
    else:
        print("❌ Import failed!")


if __name__ == "__main__":
    example_usage()