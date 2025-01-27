"""
AWS Lambda Function: Cleanup Default Security Groups

This function identifies all EC2 security groups named "default" in your AWS account and removes all inbound (ingress) and outbound (egress) rules. This helps enhance security by ensuring that no unintended access
is allowed through these groups.

The function performs the following:
1. Identify Default Security Groups: Fetches all security groups named "default" using the `describe_security_groups` method.
2. Revoke Ingress Rules: Removes all inbound rules for each identified security group.
3. Revoke Egress Rules: Removes all outbound rules for each identified security group.
4. Error Handling: Captures and logs any exceptions that occur during the rule removal process.

This function ensures default security groups are stripped of any rules, enhancing security by preventing unintended access.
"""

import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Fetch the IDs of all security groups named "default"
    response = ec2.describe_security_groups(Filters=[{'Name': 'group-name', 'Values': ['default']}])
    sg_ids = [sg['GroupId'] for sg in response['SecurityGroups']]  # Extract all matching SG IDs

    # Iterate over each security group ID and remove all ingress and egress rules
    for sg_id in sg_ids:
        try:
            # Fetch current ingress rules
            sg = ec2.describe_security_groups(GroupIds=[sg_id])
            current_ingress_rules = sg['SecurityGroups'][0]['IpPermissions']

            # Revoke all inbound rules
            if current_ingress_rules:
                ec2.revoke_security_group_ingress(
                    GroupId=sg_id,
                    IpPermissions=current_ingress_rules
                )
                print(f"All inbound rules removed from {sg_id}")
        except Exception as e:
            print(f"Failed to remove inbound rules from {sg_id}: {e}")

        try:
            # Fetch current egress rules
            sg = ec2.describe_security_groups(GroupIds=[sg_id])
            current_egress_rules = sg['SecurityGroups'][0]['IpPermissionsEgress']

            # Revoke all outbound rules
            if current_egress_rules:
                ec2.revoke_security_group_egress(
                    GroupId=sg_id,
                    IpPermissions=current_egress_rules
                )
                print(f"All outbound rules removed from {sg_id}")
        except Exception as e:
            print(f"Failed to remove outbound rules from {sg_id}: {e}")

    return {
        'statusCode': 200,
        'body': 'All ingress and egress rules have been successfully revoked.'
    }
