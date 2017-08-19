import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------------------')
    print('           JOURNAl APP')
    print('-------------------------------------')
    print()


def run_event_loop():

    print('What do you want to do with your journal')
    cmd = 'init'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, ]A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Goodbye')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)

    for i, entry in enumerate(entries):
        print('* [{}] {}'.format(i, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
