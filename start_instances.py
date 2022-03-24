# Start instances triggered by SNS
import boto3
import time
region = '<region name>'
instances = ['instance id 1','instance id 2']
ec2 = boto3.client('ec2', region_name=region)
client = boto3.client('elbv2', region_name=region)
TargetGroupArn='<ELB Target Group ARN>',
def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('starting your instances: ' + str(instances))
    time.sleep(30)
    for i in instances:
     print(i)
     response = client.register_targets(
     TargetGroupArn='arn:aws:elasticloadbalancing:ap-south-1:123793991769:targetgroup/ASG-LIVEAPI/7f76e32ddcda672f',
     Targets=[
       {
       'Id': str(i),
       },
      ],
     )
print("success")
