#!/usr/bin/env python

#######################################################################
# coding: utf8
#
#   Copyright (c) 2018 Dell
#   Praveen Nagegowda Nagegowda.Praveen@Dell.com
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
########################################################################

from config import CLOUDIFY_MANAGER_IP, CLOUDIFY_USERNAME, CLOUDIFY_PASSWORD, CLOUDIFY_TENANT
from cloudify_rest_client import CloudifyClient
from prettytable import PrettyTable

# client object to establish connection to cloudify manager
client = CloudifyClient(
    host=CLOUDIFY_MANAGER_IP,
    username=CLOUDIFY_USERNAME,
    password=CLOUDIFY_PASSWORD,
    tenant=CLOUDIFY_TENANT)


class cloudify_operations():

    def get_authtoken(self):
    # get auth token from cloudify manager
        mytoken = client.tokens.get()
        print("\n\n{:*^21s}".format("Token Table"))
        token_table=PrettyTable()
        token_table.field_names = ['Role', 'Token']
        token_table.add_row([mytoken['role'], mytoken['value']])
        print token_table

    def get_blueprint_list(self):
    # get blueprints list
        print("\n\n{:*^21s}".format("Blueprints List"))
        blueprints = client.blueprints.list(_include=['id','created_at'])
        bp_table = PrettyTable()
        bp_table.field_names = ["Blueprint ID", "Created at"]
        for blueprint in blueprints:
            #print blueprint
            bp_table.add_row([blueprint['id'],blueprint['created_at']])
        print bp_table

    def get_deployment_list(self):
    # get deployment list
        print("\n\n{:*^21s}".format("Deployments List"))
        deployments = client.deployments.list(
            _include=['id', 'blueprint_id'],
            _sort=['blueprint_id', '-id'],
            )
        dp_table = PrettyTable()
        dp_table.field_names = ['Deployment', 'Blueprint']
        for deployment in deployments:
            dp_table.add_row([deployment['id'], deployment['blueprint_id']])
        print dp_table

    #def get_events_list(self):
    #    print "Get Events"
    #    events = client.events.list(
    #        _size=4,
    #        _offset=1,
    #        _include=['timestamp'],
    #        ) 
    #    for event in events:
    #        print event

    def get_status(self):
        print "\n\nCloudify Manager Status"
        #status = client.manager.get_status() OVERALL STATUS
        status = client.manager.get_status()['services']
        service_names = [i['display_name'] for i in status]
        service_status = [st['instances'][0]['state'] for st in status]
        status_table= PrettyTable()
        status_table.field_names = ['Service Name', 'Servce Status']
        for i,j in map(None, service_names, service_status):
            status_table.add_row([i,j])
        print status_table
            
    def get_blueprint_by_id(self, blueprint_id):
        try:
            print client.blueprints.get(blueprint_id=blueprint_id)
        except:
            print "Invalid blueprint ID" 
 
    def upload_blueprint(self, blueprint_id, archive_location, yamlFile):
        try:
            client.blueprints._upload(
            blueprint_id=blueprint_id,
            archive_location=archive_location,
            application_file_name=yamlFile,
            )  
            print 'Blueprint uploaded Successfully'
        except:
            print 'Blueprint upload Failed..!!'
            print '\nVerify your archive file location and YAML'
  
    def get_plugins_list(self):
        plugins = client.plugins.list(_include=['id','archive_name'])
        print("\n\n{:*^21s}".format("Plugins List"))
        plugin_table = PrettyTable()
        plugin_table.field_names = ['Plugin ID', 'Plugin Archive Name']
        for plugin in plugins:
            plugin_table.add_row([plugin['id'], plugin['archive_name']])
        print plugin_table
