"""
Module to manage the loading and saving of journal
"""
import os


def load(name):
    """
    This method creates or loads journal.

    :param name: This base name of the journal to load.
    :return:  A new journal data structre populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as file:
            for entry in file.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    filename = get_full_pathname(name)
    print('.... saving to: {}'.format(filename))

    with open(filename, 'w') as file:
        for entry in data:
            file.write(entry)
            file.write('\n')


def get_full_pathname(name):
    return os.path.abspath(os.path.join('./journals/', name + '.jrs'))


def add_entry(text, data):
    data.append(text)