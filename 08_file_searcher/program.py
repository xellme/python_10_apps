import os
import collections

SearchResult = collections.namedtuple('SearchResult', ['line', 'file', 'text'])


def print_header():
    print('---------------------------')
    print('    FILE SEARCH')
    print('---------------------------')


def get_folder_from_user():
    print('What folder do you want to search? ')
    folder = r'C:\Code space\git\python_10_apps'
    print(folder)
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    print('What text do you want tot search? ')
    text = 'class'
    print(text)
    return text.lower()


def search_file(filename, text):
    print(filename)
    with open(filename, 'r', encoding='utf-8') as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m


def search_folders(folder, text):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if folder.startswith('.') \
                or item.startswith('.')\
                or os.path.splitext(item)[1] in ['.pyc']:
            continue
        elif os.path.isdir(full_item):
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    matches = search_folders(folder, text)

    print()
    print('Results:')
    for m in matches:
        print('----- MATCH --------')
        print(f'file: {m.file}')
        print(f'line: {m.line}')
        print(m.text.strip())


if __name__ == '__main__':
    main()
