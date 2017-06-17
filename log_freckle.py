import os
import argparse
import datetime
import pprint

from os.path import join, dirname
from dotenv import load_dotenv

from freckle import FreckleClientV2


def letsfreckle(date, minutes, project, description):
    access_token = os.environ.get("access_token")
    freckle_client = FreckleClientV2(access_token)
    data = {
        "date": date,
        "minutes": minutes,
        "description": "#{}".format(description),
        "project_name": project
    }
    results = freckle_client.log_entry('entries', data=data)
    return results


def format_date(date):
    # check date argument
    try:
        if date.lower() != 'today':
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return date
        else:
            return datetime.datetime.today().date().isoformat()
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD or specify today instead")


def main():
    parser = argparse.ArgumentParser()
    # add positional arguments
    parser.add_argument("date", help="Specify 'today' or date in the format 'yyyy-mm-dd'", type=str)
    parser.add_argument("minutes", help="Time in minutes. 8 hours = 480 minutes", type=int)
    parser.add_argument("project", help="Specify project name e.g Client. Also ensure it's an existing project name", type=str)
    parser.add_argument("description", help="e.g ClientEngagement", type=str)
    args = parser.parse_args()

    # set arguments
    date = format_date(args.date)
    minutes = args.minutes
    project = args.project
    description = args.description

    response = letsfreckle(date, minutes, project, description)

    pprint.pprint(response)


if __name__ == '__main__':
    # load .env variables
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    # execute program
    main()
