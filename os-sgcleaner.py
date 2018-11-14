# Copyright (c) 2018 Jean-Louis FEREY.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import shade

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("cloud", help="name of your cloud defined in clouds.yml or in your openstack rc file", type=str)
args=parser.parse_args()

sgNames = set ()
sgUsed = set ()

# Initialize cloud
# Cloud configs are read with os-client-config
cloud = shade.openstack_cloud(cloud=args.cloud)

# Get security group list
for sg in cloud.list_security_groups():
    sgNames.add(sg.name)

# Get server list and get security groups used by each servers
for server in cloud.list_servers():
    for sgUsedByServer in (cloud.get_server(server.id)).security_groups:
        sgUsed.add(sgUsedByServer["name"])

print("These SGs are not used by any servers:")

# from https://stackoverflow.com/questions/3462143/get-difference-between-two-lists/3462160#3462160
for sg in list(sgNames - sgUsed):
    print (sg)
