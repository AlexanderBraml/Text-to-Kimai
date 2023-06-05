import argparse
from os.path import expanduser

from src.APIHandler import add_entries
from src.FileHandler import read_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', help='The url of your kimai instance.', required=True)
    parser.add_argument('--user', help='Your kimai username.', required=True)
    parser.add_argument('--password', help='Your kimai api password, not your regular password.', required=True)

    parser.add_argument('--source', help='A txt file containg the times to import. Must be in the format specified in '
                                         'the README.', required=True)

    args = parser.parse_args()

    entries = read_file(expanduser(args.source))
    add_entries(entries, args.user, args.password, args.url)
