# Endpoint Monitor
> Polls endpoints and posts their status on slack

This is a simple python script to monitor endpoints and post in slack based on their status codes.

## Getting started

The following commands will download and run the project. However, you'll need to do the configuration down below first.
```shell
git clone https://github.com/KevinAiken/endpoint-monitor.git
cd endpoint-monitor
pip install -r requirements.txt
python main.py
```

### Configuration
#### Slack Setup
First you'll need to create a Slack App: https://api.slack.com/apps?new_app=1

Add the 'incoming webhook' feature to your app: https://api.slack.com/messaging/webhooks

Make sure the sample curl command works successfully posts a message in your Slack.

#### Config.json

Now you'll need to configure the script by setting up the config.json file. An example is included in the repo.

Set `slackWebhookUrl` to your webhook url.

Add any endpoints you want to poll, expected statuses, and the slack message to send. To avoid sending a message
on certain statuses, set the corresponding message to `""`. 

Every endpoint needs an unknownResponse key and a connection failure key. The unknownResponse message will be sent
if an endpoint returns a status code you did not specifically define in your json.

You can use a message prefix by setting the message prefix field. If you do not want to use the field, set it to "".
An example is `<!channel>`, which will make all of the messages start with `@channel`.

## Licensing
The code in this project is licensed under the GPL license.
