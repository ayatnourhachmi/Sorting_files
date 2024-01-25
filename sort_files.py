import os
import shutil
from datetime import datetime

def sort_files(source_path, destination_path):
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
        month_path = os.path.join(year_path, str(creation_date.month))

        # Create directories if they don't exist
        os.makedirs(extension_path, exist_ok=True)
        os.makedirs(year_path, exist_ok=True)
        os.makedirs(month_path, exist_ok=True)

        # Construct the destination file path
        destination_file_path = os.path.join(month_path, file)

        # Move the file to the destination
        shutil.move(source_file_path, destination_file_path)

        print(f"Moved: {source_file_path} -> {destination_file_path}")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ")
    destination_directory = input("Enter the destination directory path: ")

    sort_files(source_directory, destination_directory)
