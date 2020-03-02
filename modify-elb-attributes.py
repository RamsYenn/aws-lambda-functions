import boto3
import json

# get elbv2 client
client = boto3.client('elbv2')

# modify the attributes of loab balancer
response = client.modify_load_balancer_attributes(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-east-1:117613187320:loadbalancer/app/ot-api-alb/60569c6e14d2e816',
    Attributes=[
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '1800'
        }
    ]
)


print(response['ResponseMetadata']['HTTPStatusCode'])
