import os

import matplotlib
import requests
from dotenv import load_dotenv
from dateutil.parser import parse

load_dotenv()

PERSONAL_ACCESS_TOKEN = os.getenv('PERSONAL_ACCESS_TOKEN')
ORGANIZATION = os.getenv('ORGANIZATION')
PROJECT = os.getenv('PROJECT')
PIPELINE_ID = os.getenv('PIPELINE_ID')

def get_build_durations():
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT}/_apis/build/builds?definitions={PIPELINE_ID}&$top=30&api-version=7.1"
    params = {
        "statusFilter": "completed",
        "propertyFilters": "startTime,finishTime"
    }
    auth = (PERSONAL_ACCESS_TOKEN, '')
    response = requests.get(url, params=params, auth=auth)
    response.raise_for_status()
    builds = response.json()['value']

    build_durations = []
    for build in builds:
        start_time = parse(build['startTime'])
        finish_time = parse(build['finishTime'])
        duration = (finish_time - start_time).total_seconds() / 60  # duration in minutes
        build_durations.append((finish_time, build['id'], duration))  # store finish_time as datetime object
    return build_durations

    return build_durations

from prettytable import PrettyTable

def display_build_durations(build_durations):
    table = PrettyTable()
    table.field_names = ["Finish Time", "Build ID", "Duration (minutes)"]
    for build in build_durations:
        finish_time = build[0].strftime("%Y-%m-%d %H:%M:%S")  # use stored datetime object
        build_id = build[1]
        duration = build[2]
        table.add_row([finish_time, build_id, duration])
    print(table)

import matplotlib.pyplot as plt

import numpy as np

def plot_build_durations(build_durations):
    finish_times = [build[0] for build in build_durations]
    durations = [build[2] for build in build_durations]

    # Convert finish_times to numbers for trend line calculation
    finish_times_num = matplotlib.dates.date2num(finish_times)

    # Calculate coefficients for the trend line
    z = np.polyfit(finish_times_num, durations, 1)
    p = np.poly1d(z)

    plt.figure(figsize=(10, 6))
    plt.plot(finish_times, durations, marker='o', label='Build durations')
    plt.plot(finish_times, p(finish_times_num), linestyle='--', label='Trend line')
    plt.title('Build Durations Over Time')
    plt.xlabel('Finish Time')
    plt.ylabel('Duration (minutes)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    build_durations = get_build_durations()
    print(build_durations)
    display_build_durations(build_durations)
    plot_build_durations(build_durations)