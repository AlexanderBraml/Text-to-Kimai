import datetime
from dataclasses import dataclass

import requests as requests


@dataclass
class Entry:
    activity: str
    start_time: datetime.datetime
    end_time: datetime.datetime


def add_entries(entries: list[Entry], user: str, token: str, url: str) -> None:
    for entry in entries:
        add_entry(entry, user, token, url)


def add_entry(entry: Entry, user: str, token: str, url: str) -> None:
    headers = {
        'X-AUTH-USER': user,
        'X-AUTH-TOKEN': token,
    }
    try:
        activity_id, project_id = task_ids(url, user, token, entry.activity)
    except ValueError:
        activity_id, project_id = None, None
    if activity_id is None or project_id is None:
        print(f'Could not find id of activity {entry.activity}! Please insert {entry} manually.')
    else:
        data = {
            "begin": entry.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            "end": entry.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            "project": project_id,
            "activity": activity_id
        }
        response = requests.post(url + '/api/timesheets', headers=headers, data=data)
        if response.status_code != 200:
            raise Exception(f'Post request for {entry} failed. Error code {response.status_code}')


def task_ids(url: str, user: str, token: str, activity: str) -> tuple[int, int]:
    headers = {
        'X-AUTH-USER': user,
        'X-AUTH-TOKEN': token,
    }
    params = {
        'size': 999999,
    }

    response = requests.get(url + '/api/activities', headers=headers, params=params)
    result = response.json()

    for entry in result:
        if entry['name'] == activity:
            return entry['id'], entry['project']

    raise ValueError(f'Id of activity {activity} cannot be found.')
