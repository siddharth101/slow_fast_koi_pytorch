import os, shutil, glob
def move_files_validation(category, path1, path2):

    all_files = glob.glob(path1 + '*.png')
    training_files = glob.glob(path2 + '*.png')

    all_files = [i.split('/')[-1] for i in all_files]
    training_files = [i.split('/')[-1] for i in training_files]

    remaining_files = [i for i in all_files if i not in training_files]
    print(len(remaining_files))
    for i in remaining_files:
        shutil.copy(path1 + i, path2.replace('Training', f'Validation'))
    return 