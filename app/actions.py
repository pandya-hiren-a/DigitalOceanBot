import time
from config import get_env
from app.utils.dohelper import DoHelper
from app.utils.slackhelper import SlackHelper


class Actions:
    def __init__(self, slackhelper, user_info=None):
        self.user_info = user_info
        self.slackhelper = slackhelper
        self.dohelper = DoHelper()

    def help(self):
        return {
            'text': 'Available Commands: \n `/dostat droplets  e.g. /dostat droplets` \n To get all available droplets`\n'
            ' \n `/dostat restart [droplet_name] e.g. /dostat restart nkn-droplet-client1` \n Restart mentioned droplet \n'
                    ' \n `/dostat status [droplet_name] e.g. /dostat status nkn-droplet-client1` \n Display the status of mentioned droplet \n'
                    ' \n `/dostat help` \n Displays this information \n \n Droplet Bot 1.0'}

    def droplets(self):
        # recipient = self.user_info['user']['id']
        text_details = self.dohelper.get_droplets()
        self.slackhelper.post_message(text_details)
        return None

    def restart_droplet(self, droplet_name):
        # recipient = self.user_info['user']['id']
        text_details = self.dohelper.restart_droplet(droplet_name)
        self.slackhelper.post_message(text_details)
        return None

    def droplet_status(self, droplet_name):
        # recipient = self.user_info['user']['id']
        text_details = self.dohelper.droplet_status(droplet_name)
        self.slackhelper.post_message(text_details)
        return None
