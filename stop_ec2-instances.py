import json
import boto3

region = 'us-east-1'

instances = ['i-094edb63e0ee38c81', 'i-02c72edc9efab294b','i-03478c64c9b404aac']

ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('Your EC2 instances have been stopped: '+ str(instances))
