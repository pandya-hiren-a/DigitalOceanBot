import digitalocean
from os import path
from prettytable import PrettyTable
from config import get_env


class DoHelper:
    def __init__(self):
        self.dataTable = PrettyTable()
        self.dataTable.field_names = ['Droplet Name', 'Droplet IP', 'Status']
        try:
            self.manager = digitalocean.Manager(
                token=get_env('DIGITAL_OCEAN_TOKEN'))
        except:
            print("Problem occurred here")

    def get_droplets(self):
        allDroplets = self.manager.get_all_droplets()
        for droplet in allDroplets:
            self.dataTable.add_row(
                [droplet.name, droplet.ip_address, droplet.status])
        return self.dataTable

    def droplet_status(self, droplet_name):
        droplets = self.manager.get_all_droplets()
        for droplet in droplets:
            if(droplet.name == droplet_name):
                self.dataTable.add_row(
                    [droplet.name, droplet.ip_address, droplet.status])
                return self.dataTable
        return "Error Code - Droplet Not Found"

    def droplet_restart(self, droplet_name):
        droplets = self.manager.get_all_droplets()
        for droplet in droplets:
            if(droplet.name == droplet_name):
                droplet.reboot
                return "Droplet Restarted"
        return "Droplet not found"
