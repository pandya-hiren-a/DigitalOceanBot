import paramiko
import os
import json
from config import get_env

''' SSH Helper class. It shall initialize paramiko client where our commands will be sent '''


class SSHHelper:
    def __init__(self):
        ''' Instantiate paramiko SSHClient object '''
        self.client = paramiko.SSHClient()
        ''' Set the SSH key policy within paramiko '''
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def checkUserPriv(self, host, user, pwd):
        ''' Check what priviledges current user have '''
        stdin, stdout, stderr = self.client.exec_command('sudo -l')
        ''' Check the channel for any command errors '''
        if(stdout.channel.recv_exit_status() == 0):
            return stdout
        else:
            return "Command Failed"
