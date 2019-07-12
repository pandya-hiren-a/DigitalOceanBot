from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from app.actions import Actions
from flask import request, jsonify

allowed_commands = [
    'droplets'
    'restart'
    'status'
    'help'
]


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')

    @app.route("/dostat", methods=["POST"])
    def dostat():
        command_text = request.data.get('text')
        command_text = command_text.split(' ')
        # slack_uid = request.data.get('user_id')
        slackhelper = SlackHelper()
        # slack_user_info = slackhelper.user_info(slack_uid)
        actions = Actions(slackhelper)

        if command_text[0] not in allowed_commands:
            response_body = {
                'text': 'Invalid Command. Try /dostat help for available commands'}

        if command_text[0] == 'help':
            response_body = actions.help()

        if(command_text[0] in ['droplet', 'droplets']):
            response_body = actions.droplets()

        if(command_text[0] == 'restart'):
            if(command_text[1] == '' or command_text[1] == ' '):
                response_body = {
                    'text': 'Invalid Restart Command. Command format: `/dostat restart droplet_name`'}
            else:
                response_body = actions.restart_droplet(command_text[1])

        if(command_text[0] == 'status'):
            if(command_text[1] == '' or command_text[1] == ' '):
                response_body = {
                    'text': 'Invalid Restart Command. Command format: `/dostat status droplet_name`'}
            else:
                response_body = actions.droplet_status(command_text[1])

        response = jsonify(response_body)
        response.status_code = 200
        return response
    return app
