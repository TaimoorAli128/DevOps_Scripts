AWS Lambda: Cleanup Default Security Groups

This AWS Lambda function removes all inbound and outbound rules from EC2 security groups named "default" to improve security by restricting unintended access.

Features
- Identifies all "default" security groups in the account.
- Removes all ingress (inbound) and egress (outbound) rules.

How to Set Up

1. Create a Lambda Function:
   - Go to the AWS Lambda Console and create a new function using Python 3.x runtime.
   - Paste the code into the editor.

2. Set Permissions:
   - Attach an IAM role with the following permissions:
     - `ec2:DescribeSecurityGroups`
     - `ec2:RevokeSecurityGroupIngress`
     - `ec2:RevokeSecurityGroupEgress`

3. Test the Function:
   - Add a test event (e.g., `{}`) in the Lambda console and run the function.
   - Verify the results in CloudWatch Logs and EC2 Console.

4. Schedule the Function:
   - Use Amazon EventBridge to run the function on a regular schedule.

Notes
- Test in a non-production environment before deploying.
- Be cautious: This function removes **all** rules from "default" security groups.
