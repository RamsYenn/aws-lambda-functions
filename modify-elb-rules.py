import boto3
import json

client = boto3.client('elbv2')
response = client.create_rule(
    ListenerArn="arn:aws:elasticloadbalancing:us-east-1:117613187320:listener/app/ot-api-alb/60569c6e14d2e816/9a24120a182bbed1",
    Conditions=[
        {
            "Field": "host-header",
            "Values": ["ice-test.cloud.sysco.net"],
        }
    ],
    Priority=100,
    Actions=[
        {
            "Type": "forward",
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:117613187320:targetgroup/ot-api/650aa900733cbb38"
        }
    ]
)

print(response)
