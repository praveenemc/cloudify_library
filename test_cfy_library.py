#!/usr/bin/env python
from cfy_library import cloudify_operations

operations = cloudify_operations()

#GET TOKEN
operations.get_authtoken()

#BLUEPRINTS LIST
operations.get_blueprint_list()

#DEPLOYMENT LIST
operations.get_deployment_list()

#EVENTS LIST
#operations.get_events_list()

#CLOUDIFY STATUS
operations.get_status()

#GET BLUEPRINT DTAILS USING its ID
operations.get_blueprint_by_id('vimsdeployment24sep')

#UPLOAD BLUEPRINT from local path 
operations.upload_blueprint('testBluePrint-2','/home/praveen/test-vims.tar', 'blueprint.yaml')

#PLUGINS LIST
operations.get_plugins_list()
