import boto3

# get elbv2 client
client = boto3.client('elbv2')


def lambda_handler(event, context):

    # get the load balancers ARNs
    elbArns = client.describe_load_balancers()

    try:
        for elb in elbArns['LoadBalancers']:
            client.modify_load_balancer_attributes(
                LoadBalancerArn=elb['LoadBalancerArn'],
                Attributes=[
                    {
                        'Key': 'idle_timeout.timeout_seconds',
                        'Value': '1800'
                    }
                ]
            )
    except Exception as e:
        print(e)
