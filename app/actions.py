import time
from config import get_env
from app.utils.dohelper import DoHelper
from app.utils.vuhelper import VuHelper
from app.utils.slackhelper import SlackHelper


class Actions:
    ''' Actions class will be used to perform all digitalocean droplets actions'''

    def __init__(self, slackhelper, user_info=None):
        self.user_info = user_info
        self.slackhelper = slackhelper
        self.dohelper = DoHelper()
        self.vuhelper = VuHelper()

    ''' [/dostat help] will call this function. It shall display all the available commands the bot can handle '''

    def help_do(self):
        return {
            'text': 'Available Commands: \n `/dostat droplets  e.g. /dostat droplets` \n To get all available droplets`\n'
            ' \n `/dostat restart [droplet_name] e.g. /dostat restart nkn-droplet-client1` \n Restart mentioned droplet \n'
                    ' \n `/dostat status [droplet_name] e.g. /dostat status nkn-droplet-client1` \n Display the status of mentioned droplet \n'
                    ' \n `/dostat help` \n Displays this information \n \n DigitalOcean Bot 1.1'}

    ''' [/dostat droplets] command will call this function. It will gather all the available
        droplets and display their name, ipaddresses, and current status in a table'''

    def droplets(self):
        ''' Call digitalocean function to gather the data '''
        text_details = self.dohelper.get_droplets()
        ''' call slack api to post the message to the user on slack '''
        self.slackhelper.post_message(text_details)
        return {'text': 'Command completed successfully. \n \n DigitalOcean Bot 1.1'}

    ''' [/dostat restart {droplet_name}] command will call this function. It will restart the mentioned droplet
        single droplet at the moment. If no droplet name given, bot will show an error with appropriate message '''

    def restart_droplet(self, droplet_name):
        ''' Call digitalocean function to restart the droplet '''
        text_details = self.dohelper.restart_droplet(droplet_name)
        ''' call slack api to post the message to the user on slack '''
        self.slackhelper.post_message(text_details)
        return {'text': 'Command completed successfully. \n \n DigitalOcean Bot 1.1'}

    ''' [/dostat status {droplet_name}] command will call this function and display individual droplet's status '''

    def droplet_status(self, droplet_name):
        ''' Call digitalocean function to gather the data '''
        text_details = self.dohelper.droplet_status(droplet_name)
        ''' call slack api to post the message to the user on slack '''
        self.slackhelper.post_message(text_details)
        return {'text': 'Command completed successfully. \n \n DigitalOcean Bot 1.1'}

    ''' [/vustat help] will call this function. It shall display all the available commands the bot can handle '''

    def help_vu(self):
        return {
            'text': 'Available Commands: \n `/vustat instances  e.g. /vustat instances` \n To get all available instances`\n'
            ' \n `/vustat restart [instance_label] e.g. /vustat restart nkn-vultr-client1-ny` \n Restart mentioned instance \n'
                    ' \n `/vustat status [instance_label] e.g. /vustat status nkn-vultr-client1-ny` \n Display the status of mentioned instance \n'
                    ' \n `/vustat help` \n Displays this information \n \n DigitalOcean Bot 1.2'}

    ''' [/vustat instances] command will call this function. It will gather all the available
        instances and display their label, ipaddresses, and current status in a table'''

    def instances(self):
        ''' Call vultr function to gather the data '''
        text_details = self.vuhelper.get_instances()
        ''' call slack api to post the message to the user on slack '''
        self.slackhelper.post_message(text_details)
        return {'text': 'Command completed successfully. \n \n DigitalOcean Bot 1.2'}

    ''' [/vustat restart {instance_label}] command will call this function. It will restart the mentioned instance
        single instance at the moment. If no instance label given, bot will show an error with appropriate message '''

    def restart_instance(self, instance_label):
        ''' Call vultr function to restart the droplet '''
        text_details = self.vuhelper.instance_reboot(instance_label)
        ''' call slack api to post the message to the user on slack '''
        self.slackhelper.post_message(text_details)
        return {'text': 'Command completed successfully. \n \n DigitalOcean Bot 1.2'}

    ''' [/vustat status {instance_label}] command will call this function and display individual instance's status '''

    def inst_status(self, instance_label):
        ''' Call vultr function to gather the data '''
        text_details = self.vuhelper.instance_status(instance_label)
        ''' call slack api to post the message to the user on slack '''
        self.slackhelper.post_message(text_details)
        return {'text': 'Command completed successfully. \n \n DigitalOcean Bot 1.2'}
