import os
import random
import shutil

def transfer_random_files(source_dir, destination_dir, n):
    # Get a list of all files in the source directory
    files = os.listdir(source_dir)
    
    # Ensure we only pick files (ignore subdirectories)
    files = [f for f in files if os.path.isfile(os.path.join(source_dir, f))]
    
    # n should be smaller than total number of files
    n = min(n, len(files))
    
    # Randomly select n files from the list
    selected_files = random.sample(files, n)
    
    # Destination folder
    os.makedirs(destination_dir, exist_ok=True)
    
    # Copy each selected file to the destination directory
    for file_name in selected_files:
        src_path = os.path.join(source_dir, file_name)
        dest_path = os.path.join(destination_dir, file_name)
        shutil.copy(src_path, dest_path)
        print(f'Moved: {file_name} from {source_dir} to {destination_dir}')

    print(f'{n} files have been copied to {destination_dir}')

    return
