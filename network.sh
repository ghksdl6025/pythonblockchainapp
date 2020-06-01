#!/bin/sh
'''
This shell script is to control blockchain mockup network.
If the argument is up, script will clean the settings and start new network
If the argument is down, script will close the network
If the argument is connect, script will connect each node.
'''

DIR='./mongodb/data/'
MODE=$1

if [ "$MODE" = "up" ]; then
    if [ "$(ls -A $DIR)" ]; then
        echo "Take action $DIR is not Empty"
        sudo rm -rf $DIR
        mkdir $DIR
        echo "Erase all files in $DIR"
    else
        echo "DIR is already empty"
    fi
    docker-compose up -d --build

elif [ "$MODE" = "down" ]; then
    docker-compose down

elif [ "$MODE" = "connect" ]; then
#     docker exec -it pythonblockchainapp_node1_1 /bin/bash
    curl -X POST http://172.28.1.1:8001/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://172.28.1.2:8002"}'
    curl -X POST http://172.28.1.1:8001/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://172.28.1.3:8003"}'

fi
