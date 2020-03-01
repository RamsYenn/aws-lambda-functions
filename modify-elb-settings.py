import boto3

client = boto3.client('elbv2')
response = client.modify_load_balancer_attributes(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-east-1:117613187320:loadbalancer/app/ot-api-alb/60569c6e14d2e816',
    Attributes=
    [
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '1800'
        }
    ]
)
