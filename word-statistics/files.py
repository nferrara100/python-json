import os


# Find the absolute paths for all selected files.
def get_file_paths(source=None):
    # If no source is provided locate the example data relative to this file.
    if source is None or len(source) == 0:
        script_dir = os.path.dirname(__file__)
        source = [os.path.join(script_dir, "example_data/")]

    files = []

    # Find all the files in the source folder.
    # Loop through source if there are multiple source directories.
    for dir in source:
        abs_dir_path = os.path.abspath(dir)
        try:
            for filename in os.listdir(abs_dir_path):
                # Don't examine files that are not text files so all data is the same.
                if filename[4:] != ".txt":
                    continue
                abs_filename = os.path.join(abs_dir_path, filename)
                files.append(abs_filename)
        # Return a pretty error when a file is not found. Continue looking for other
        # files.
        except FileNotFoundError:
            print(f"Error: {dir} does not exist.")
    return files
