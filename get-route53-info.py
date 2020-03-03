import boto3
import json

client=boto3.client("route53")

response = client.list_resource_record_sets(
    HostedZoneId = "Z3F24SF75VQXPG"
)

for record in response["ResourceRecordSets"]:

 print(response[])