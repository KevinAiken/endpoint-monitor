#!/usr/bin/env python3
"""
A python script that polls endpoints and posts in slack if the endpoints return certain statuses
"""
import time

__author__ = "Kevin Aiken"
__license__ = "GPL-3.0"

import json
import requests


def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    webhook_url = config['slackWebhookUrl']
    interval = config['pollIntervalMinutes']
    message_prefix = config['messagePrefix']

    current_statuses = {}

    # initialize current statuses
    for endpoint in config['endpoints']:
        current_statuses[endpoint['url']] = "Unknown"

    while True:

        print(current_statuses)

        for endpoint in config['endpoints']:
            try:
                response_status_string = str(requests.get(endpoint['url']).status_code)

                try:
                    message = endpoint['responses'][response_status_string]
                except KeyError:
                    message = endpoint['responses']['unknownResponse']

                if message != "" and current_statuses[endpoint['url']] != response_status_string:
                    send_slack_message(webhook_url, f"{message_prefix} {message}")

                current_statuses[endpoint['url']] = response_status_string
            except requests.exceptions.ConnectionError:
                message = endpoint['responses']['connectionFailure']
                if message != "" and current_statuses[endpoint['url']] != "connectionFailure":
                    send_slack_message(webhook_url, f"{message_prefix} {message}")
                current_statuses[endpoint['url']] = "connectionFailure"

        time.sleep(interval * 60)


def send_slack_message(url, message):
    print(f"Sending '{message}' to {url}")
    requests.post(url, json={"text": message})


if __name__ == "__main__":
    main()
