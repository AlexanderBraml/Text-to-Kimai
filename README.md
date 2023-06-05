# Text-to-Kimai

This script takes a path to a txt file containing manual time records. It then imports all records into Kimai.

The txt file needs to be in a special - but not complicated - syntax, namely:
  - The first line of the file must contain the date of all the records in ISO-format.
  - The next lines are all the time records. They need to be structured like this: starttime - endtime activity name.

A sample file called `SampleTimes.txt` is given.

## Sample Usage

```shell
python3 main.py --url "demo.kimai.org" --user "user" --password "api.pw" --source SampleTimes.txt
```
