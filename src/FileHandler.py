import datetime
import re

from src.APIHandler import Entry


def read_file(file_name: str) -> list[Entry]:
    lines: list[str]
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    date: datetime.datetime = datetime.datetime.fromisoformat(lines[0])
    entries: list[Entry] = []
    for line in lines[1:]:
        split_line = re.split(' - |\s', line, maxsplit=2)
        if len(split_line) != 3:
            raise ValueError(f'The format of the following line is not correct: {line}')
        entry = Entry(split_line[2],
                      datetime.datetime.combine(date, datetime.datetime.strptime(split_line[0], '%H:%M').time()),
                      datetime.datetime.combine(date, datetime.datetime.strptime(split_line[1], '%H:%M').time()))
        entries.append(entry)
    return entries
