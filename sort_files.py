import os
import sys
import shutil
import calendar
from datetime import datetime

def get_month_name(month_number):
    """ Convert the numeric month obtained from the file creation date into its corresponding English name. """
    try:
        month_name = calendar.month_name[month_number]
        return month_name
    except IndexError:
        return "Invalid month number"

def sort_files(source_path, destination_path):
    """ Sort files from source_path to destination_path based on their creation date and file extension. """
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Get a list of files in the source directory
    files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]

    for file in files:
        source_file_path = os.path.join(source_path, file)

        # Get file information
        file_name, file_extension = os.path.splitext(file)
        creation_time = os.path.getctime(source_file_path)
        creation_date = datetime.fromtimestamp(creation_time)

        # Create destination directories based on extension, year, and month
        extension_path = os.path.join(destination_path, file_extension[1:])
        year_path = os.path.join(extension_path, str(creation_date.year))
        month_path = os.path.join(year_path, get_month_name(creation_date.month))

        # Create directories if they don't exist
        os.makedirs(month_path, exist_ok=True)

        # Construct the destination file path
        destination_file_path = os.path.join(month_path, file)

        # Move the file to the destination
        shutil.move(source_file_path, destination_file_path)

        print(f"Moved: {source_file_path} -> {destination_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sort_files.py source_directory destination_directory")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    sort_files(source_directory, destination_directory)
