import os
import platform
import subprocess
import cat_service


def print_header():
    print('-----------------------')
    print('      CAT FACTORY')
    print('-----------------------')


def get_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory at {full_path}')
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats..')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = f'lolcat {i}'
        print(f'Downloading cat {name}')
        cat_service.get_cat(folder, name)

    print('done.')

def display_cats(folder):
    if platform.system() == 'Darwin':
        command = 'open'
    elif platform.system() == 'Windows':
        command = 'explorer'
    elif platform.system() == 'Linux':
        command = 'xdg-open'
    else:
        raise AttributeError("We don't supper your os: " + platform.system())

    subprocess.call([command, folder])

def main():
    print_header()

    folder = get_output_folder()
    print(f'Found or created folder: {folder}')

    download_cats(folder)
    display_cats(folder)

if __name__ == "__main__":
    main()
