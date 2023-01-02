import boto3
import paramiko
import botocore
import time


try:
    print("Creating ec2 instance!!!!!")
    ec2 = boto3.client('ec2')
    ec2.run_instances(
        ImageId='ami-0b5eea76982371e91',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='new_project',
    )
except Exception as e:
    print(e)
    print('exception thrown')
