#!/bin/sh

curl -X POST http://172.28.1.1:5000/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://172.28.1.2:5000"}'
curl -X POST http://172.28.1.2:5000/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://172.28.1.3:5000"}'
curl -X POST http://172.28.1.2:5000/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://172.28.1.4:5000"}'
curl -X POST http://172.28.1.3:5000/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://172.28.1.4:5000"}'
curl -X POST http://172.28.1.4:5000/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://172.28.1.5:5000"}'