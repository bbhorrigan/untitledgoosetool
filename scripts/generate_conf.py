#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Untitled Goose Tool: generate_conf
This script creates a blank configuration file to use.
"""

from goosey.azure_ad_datadumper import AzureAdDataDumper
from goosey.d4iot_dumper import DefenderIoTDumper
from goosey.m365_datadumper import M365DataDumper
from goosey.azure_dumper import AzureDataDumper
from goosey.mde_datadumper import MDEDataDumper

__author__ = "Claire Casalnova, Jordan Eberst, Wellington Lee, Victoria Wallace"
__version__ = "1.2.5"

def create_conf_string(section_name, dumper_class, additional_lines=None):
    s = f'[{section_name}]\n'
    s += '\n'.join([x.lstrip().replace('dump_', '') + '=False' for x in dir(dumper_class) if x.startswith('dump_')])
    s += '\n'
    if additional_lines:
        s += '\n'.join(additional_lines) + '\n'
    s += '\n'
    return s

def write_to_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)

def main():
    auth_s = '[auth]\nusername=\npassword=\nappid=\nclientsecret=\n\n'
    write_to_file('.auth', auth_s)

    config_s = '[config]\ntenant=\nus_government=\nmde_gcc=\nmde_gcc_high=\nexo_us_government=\nsubscriptionid=\nm365=\n\n'
    config_s += '[filters]\ndate_start=\ndate_end=\n\n'
    config_s += create_conf_string('azure', AzureDataDumper)
    config_s += create_conf_string('azuread', AzureAdDataDumper)
    config_s += create_conf_string('m365', M365DataDumper)
    config_s += create_conf_string('mde', MDEDataDumper)
    msgtrc_additional = ['setemailaddress=', 'direction=', 'notifyaddress=', 'originalclientip=', 'recipientaddress=', 'reporttitle=', 'reporttype=', 'senderaddress=']
    config_s += create_conf_string('msgtrc', None, additional_lines=msgtrc_additional)
    
    write_to_file('.conf', config_s)

    d4iotauth_s = '[auth]\nusername=\npassword=\nd4iot_sensor_token=\nd4iot_mgmt_token=\n\n'
    write_to_file('.auth_d4iot', d4iotauth_s)

    d4iot_s = '[config]\nd4iot_sensor_ip=\nd4iot_mgmt_ip=\n\n'
    d4iot_s += create_conf_string('d4iot', DefenderIoTDumper)
    write_to_file('.d4iot_conf', d4iot_s)

if __name__ == "__main__":
    main()
