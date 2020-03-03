import boto3
import json
import os

client = boto3.client('elbv2')

response1 = client.describe_listeners(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-east-1:117613187320:loadbalancer/app/ot-api-alb/60569c6e14d2e816')

for listeners in response1['Listeners']:
    arn = listeners['ListenerArn']
    port = listeners['Port']
    # print(arn+'-'+str(port))
    if (port == 443):
        print(arn)
        response2 = client.describe_rules(ListenerArn=arn)
        # print(response2)
        workDir = os.getcwd()
        elbrules = json.loads(open(workDir+'\elbrules-stg.json').read())
        rulePriority = 1;

        for rule in elbrules:

            response = client.create_rule(
                ListenerArn=arn,
                Conditions=[
                    {
                        "Field": "host-header",
                        "Values": [rule],
                    }
                ],
                Priority=rulePriority,
                Actions=[
                    {
                        "Type": "forward",
                        "TargetGroupArn": elbrules[rule]
                    }
                ]
            )
            rulePriority = rulePriority+1
            print("Rule "+rule+" created")
