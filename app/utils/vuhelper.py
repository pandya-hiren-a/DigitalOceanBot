from vultr import Vultr
from os import path
from prettytable import PrettyTable
from config import get_env

''' Vultr helper class to perform all api calls to vultr '''


class VuHelper:
    def __init__(self):
        ''' Instantiate all required variables '''
        self.dataTable = PrettyTable()
        self.dataTable.field_names = ['Instance Name', 'Instance IP', 'Status']
        try:
            self.vultr = Vultr(get_env('VULTR_TOKEN'))
        except:
            print("Problem during vultr object initialization")

    def get_instances(self):
        ''' get all the instances from the vultr and use required values within the table '''
        instances = self.vultr.server.list()
        for (id, data) in instances.items():
            self.dataTable.add_row(
                [data['label'], data['main_ip'], data['status']])
        return self.dataTable

    def instance_status(self, instance_label):
        ''' get all available instances and match their labels with user provided label, if matched return the details in the table form '''
        instances = self.vultr.server.list()
        for (id, data) in instances.items():
            if(data['label'] == instance_label):
                self.dataTable.add_row(
                    [data['label'], data['main_ip'], data['status']])
                return self.dataTable
        return "Error Code - Instance Not Found"

    def instance_reboot(self, instance_label):
        ''' get all the available instances and match their labels with provided one,
            if found, send reboot request '''
        instances = self.vultr.server.list()
        for (id, data) in instances.items():
            if(data['label'] == instance_label):
                self.vultr.server.reboot(id)
                return "Instance Rebooted"
        return "Error Code - Instance Not Found"
