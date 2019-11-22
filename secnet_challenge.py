import boto3

conn = boto3.client('ec2')
resp = conn.create_security_group(GroupName='mywebgroup',
                                  Description='My first security group')
conn.authorize_security_group_ingress(GroupId='sg-08cf1d7c57254906a',
                                      IpProtocol='TCP',
                                      CidrIp='0.0.0.0/0',
                                      FromPort=443,
                                      ToPort=443)
keypair = conn.create_key_pair(KeyName='webkey')
print(keypair['KeyMaterial'])

ec2_conn = boto3.resource('ec2')
instance = ec2_conn.create_instances(ImageId='ami-0d5d9d301c853a04a',
                                   MinCount=1,
                                   MaxCount=1,
                                   SecurityGroups=['mywebgroup'],
                                   KeyName='webkey',
                                   InstanceType='t2.micro')
print(instance)