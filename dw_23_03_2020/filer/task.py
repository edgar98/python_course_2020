import pickle


def modify_file(file_name=None):
    if file_name:
        with open(file_name, 'w') as file:
            lines_entered = 0
            while True:
                inp = input(f'Input line {lines_entered + 1} to write: ')
                if inp == 'quit':
                    break
                file.write(inp+'\n')
                lines_entered += 1
        save_metadata(lines_entered, file_name)


def create_file():
    file_name = input('Enter new file name: ')
    open(file_name, 'w').close()
    modify_file(file_name)


def save_metadata(lines_entered, file_name=None):
    if file_name:
        with open(file_name + '_metadata.pkl', 'wb') as meta:
            pickle.dump((file_name, lines_entered), meta)


def load_metadata(file_name=None):
    if file_name:
        with open(file_name + '_metadata.pkl', 'rb') as meta:
            print(pickle.load(meta))


def open_file(file_name=None):
    if not file_name:
        file_name = input('File name to open: ')
    with open(file_name + '_metadata.pkl', 'rb') as meta:
        print(pickle.load(meta))
    with open(file_name, 'r') as file:
        for line in file:
            print(line)
