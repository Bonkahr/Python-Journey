import os

root = "music"
for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        print('*' * 50)
    print(directories)
    print(files)
    input()
    # for f in files:
    #     print(f'\t {f}')

