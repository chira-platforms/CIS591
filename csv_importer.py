#!/usr/bin/env python3
"""
CSV Importer Module for CIS591

This module provides functionality to import and process CSV files with error handling
and data validation capabilities.
"""

import csv
import os
import sys
from typing import List, Dict, Any, Optional


class CSVImporter:
    """A class to handle CSV file importing with error handling and data validation."""
    
    def __init__(self):
        self.data = []
        self.headers = []
        self.filename = None
    
    def import_csv(self, filename: str, delimiter: str = ',', encoding: str = 'utf-8') -> bool:
        """
        Import data from a CSV file.
        
        Args:
            filename (str): Path to the CSV file
            delimiter (str): CSV delimiter character (default: ',')
            encoding (str): File encoding (default: 'utf-8')
            
        Returns:
            bool: True if import successful, False otherwise
        """
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return False
        
        try:
            with open(filename, 'r', encoding=encoding, newline='') as csvfile:
                # Detect delimiter if not specified
                if delimiter == ',':
                    sample = csvfile.read(1024)
                    csvfile.seek(0)
                    sniffer = csv.Sniffer()
                    delimiter = sniffer.sniff(sample).delimiter
                
                reader = csv.DictReader(csvfile, delimiter=delimiter)
                self.headers = reader.fieldnames
                self.data = list(reader)
                self.filename = filename
                
                print(f"Successfully imported {len(self.data)} rows from '{filename}'")
                print(f"Columns: {', '.join(self.headers)}")
                return True
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return False
        except PermissionError:
            print(f"Error: Permission denied accessing '{filename}'.")
            return False
        except UnicodeDecodeError:
            print(f"Error: Unable to decode file '{filename}' with encoding '{encoding}'.")
            return False
        except csv.Error as e:
            print(f"Error: CSV parsing error - {e}")
            return False
        except Exception as e:
            print(f"Error: Unexpected error occurred - {e}")
            return False
    
    def get_data(self) -> List[Dict[str, Any]]:
        """Return the imported data."""
        return self.data
    
    def get_headers(self) -> List[str]:
        """Return the column headers."""
        return self.headers
    
    def get_row_count(self) -> int:
        """Return the number of rows imported."""
        return len(self.data)
    
    def get_column_count(self) -> int:
        """Return the number of columns."""
        return len(self.headers) if self.headers else 0
    
    def display_sample(self, num_rows: int = 5) -> None:
        """
        Display a sample of the imported data.
        
        Args:
            num_rows (int): Number of rows to display (default: 5)
        """
        if not self.data:
            print("No data to display. Import a CSV file first.")
            return
        
        print(f"\nSample data from '{self.filename}':")
        print("-" * 60)
        
        # Display headers
        print(" | ".join(f"{header:15}" for header in self.headers))
        print("-" * 60)
        
        # Display sample rows
        for i, row in enumerate(self.data[:num_rows]):
            values = []
            for header in self.headers:
                value = str(row.get(header, ""))[:15]
                values.append(f"{value:15}")
            print(" | ".join(values))
        
        if len(self.data) > num_rows:
            print(f"... and {len(self.data) - num_rows} more rows")
    
    def filter_data(self, column: str, value: str) -> List[Dict[str, Any]]:
        """
        Filter data by column value.
        
        Args:
            column (str): Column name to filter by
            value (str): Value to filter for
            
        Returns:
            List[Dict[str, Any]]: Filtered data
        """
        if column not in self.headers:
            print(f"Error: Column '{column}' not found in data.")
            return []
        
        filtered = [row for row in self.data if row.get(column, "").lower() == value.lower()]
        print(f"Found {len(filtered)} rows where {column} = '{value}'")
        return filtered
    
    def export_summary(self, output_file: Optional[str] = None) -> None:
        """
        Export a summary of the imported data.
        
        Args:
            output_file (Optional[str]): Output file path (prints to console if None)
        """
        if not self.data:
            print("No data to summarize.")
            return
        
        summary = [
            f"CSV Import Summary",
            f"==================",
            f"Source file: {self.filename}",
            f"Total rows: {len(self.data)}",
            f"Total columns: {len(self.headers)}",
            f"Columns: {', '.join(self.headers)}",
            ""
        ]
        
        # Add column statistics
        for header in self.headers:
            values = [row.get(header, "") for row in self.data]
            non_empty = [v for v in values if v.strip()]
            unique_values = len(set(non_empty))
            
            summary.append(f"Column '{header}':")
            summary.append(f"  - Non-empty values: {len(non_empty)}")
            summary.append(f"  - Unique values: {unique_values}")
            summary.append("")
        
        summary_text = "\n".join(summary)
        
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(summary_text)
                print(f"Summary exported to '{output_file}'")
            except Exception as e:
                print(f"Error writing summary to file: {e}")
        else:
            print(summary_text)


def main():
    """Main function to demonstrate CSV import functionality."""
    importer = CSVImporter()
    
    # Check if filename provided as command line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter CSV filename to import: ").strip()
    
    if importer.import_csv(filename):
        print(f"\nImport successful!")
        importer.display_sample()
        
        # Interactive menu
        while True:
            print("\nOptions:")
            print("1. Display sample data")
            print("2. Show summary")
            print("3. Filter data")
            print("4. Export summary to file")
            print("5. Exit")
            
            choice = input("\nSelect an option (1-5): ").strip()
            
            if choice == '1':
                rows = input("Number of rows to display (default 5): ").strip()
                rows = int(rows) if rows.isdigit() else 5
                importer.display_sample(rows)
            
            elif choice == '2':
                importer.export_summary()
            
            elif choice == '3':
                if importer.get_headers():
                    print(f"Available columns: {', '.join(importer.get_headers())}")
                    column = input("Enter column name to filter by: ").strip()
                    value = input("Enter value to filter for: ").strip()
                    filtered = importer.filter_data(column, value)
                    if filtered:
                        print(f"\nFirst few filtered results:")
                        for i, row in enumerate(filtered[:3]):
                            print(f"Row {i+1}: {row}")
            
            elif choice == '4':
                output_file = input("Enter output filename (or press Enter for console): ").strip()
                importer.export_summary(output_file if output_file else None)
            
            elif choice == '5':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select 1-5.")
    else:
        print("Import failed.")


if __name__ == "__main__":
    main()