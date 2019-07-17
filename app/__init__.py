from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from app.actions import Actions
from flask import request, jsonify
import requests_cache
import time

''' commands allowed by dostat bot '''
allowed_commands = [
    'droplets'
    'droplet'
    'restart'
    'status'
    'help'
    'instances'
    'instance'
]

''' Cache requests to avoid unnecessary overhead on the server '''
requests_cache.install_cache(
    cache_name='bot_cache', backend='sqlite', expire_after=180)
''' main app entry point '''


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')

    @app.route("/dostat", methods=["POST"])
    def dostat():
        ''' if POST request has been received, gather request body data and perform related actions '''
        command_text = request.data.get('text')
        command_text = command_text.split(' ')
        ''' get SlackHelper object '''
        slackhelper = SlackHelper()
        ''' Get Actions class object '''
        actions = Actions(slackhelper)

        ''' Check if provided command is present in the allowed command or not. '''
        if command_text[0] not in allowed_commands:
            response_body = {
                'text': 'Invalid Command. Try /dostat help for available commands'}

        ''' If the command is help, call help function from the actions class '''
        if command_text[0] == 'help':
            response_body = actions.help_do()

        ''' If the command is 'droplet', call droplets function from the actions class '''
        if(command_text[0] in ['droplet', 'droplets']):
            response_body = actions.droplets()

        ''' If the command is 'restart', first we need to make sure that there is a droplet name present after command
            If not provided, display error, otherwise proceed further with appropriate function call from the actions class '''
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

        ''' Prepare the response, add the response code, and return the object '''
        response = jsonify(response_body)
        response.status_code = 200
        return response

    @app.route("/vustat", methods=["POST"])
    def vustat():
        ''' if POST request has been received, gather request body data and perform related actions '''
        command_text = request.data.get('text')
        command_text = command_text.split(' ')
        ''' get SlackHelper object '''
        slackhelper = SlackHelper()
        ''' Get Actions class object '''
        actions = Actions(slackhelper)

        ''' Check if provided command is present in the allowed command or not. '''
        if command_text[0] not in allowed_commands:
            response_body = {
                'text': 'Invalid Command. Try /vustat help for available commands'}

        ''' If the command is help, call help function from the actions class '''
        if command_text[0] == 'help':
            response_body = actions.help_vu()

        ''' If the command is 'instances', call instances function from the actions class '''
        if(command_text[0] in ['instance', 'instances']):
            response_body = actions.instances()

        ''' If the command is 'restart', first we need to make sure that there is an instance name present after command
            If not provided, display error, otherwise proceed further with appropriate function call from the actions class '''
        if(command_text[0] == 'restart'):
            if(command_text[1] == '' or command_text[1] == ' '):
                response_body = {
                    'text': 'Invalid Restart Command. Command format: `/vustat restart [instance_label]`'}
            else:
                response_body = actions.restart_instance(command_text[1])

        if(command_text[0] == 'status'):
            if(command_text[1] == '' or command_text[1] == ' '):
                response_body = {
                    'text': 'Invalid Restart Command. Command format: `/vustat status [instance_label]`'}
            else:
                response_body = actions.inst_status(command_text[1])

        ''' Prepare the response, add the response code, and return the object '''
        response = jsonify(response_body)
        response.status_code = 200
        return response

    return app
