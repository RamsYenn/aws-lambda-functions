import boto3
import json
import os

# get elbv2 client
client = boto3.client('elbv2')

# get the list of load balancer Arn from elb-arn.json
workDir = os.getcwd()
prop = json.loads(open(workDir+'\elb-arn.json').read())

for arn in prop['loabBalancers']:

    # modify the idle timeout value 
    response = client.modify_load_balancer_attributes(
        LoadBalancerArn=arn,
        Attributes=[
            {
                'Key': 'idle_timeout.timeout_seconds',
                'Value': '1800'
            }
        ]
    )

    print(arn+'-'+str(response['ResponseMetadata']['HTTPStatusCode']))
