import os

print("running")

if __name__ == '__main__':
    data_directory = os.getenv('DATA_DIRECTORY')
    source_file = os.getenv('INPUT_FILE')
    file_path = data_directory + '/' + source_file
    print("reading " + file_path)