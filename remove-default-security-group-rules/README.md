# AWS Lambda: Cleanup Default Security Groups

This AWS Lambda function removes all inbound and outbound rules from EC2 security groups named "default" to improve security by restricting unintended access.

## Features
- Identifies all "default" security groups in the account.
- Removes all ingress (inbound) and egress (outbound) rules.
- Automatically triggered by an SNS notification when a new default VPC is created.

## How It Works
1. **Trigger**: An SNS topic sends a notification when a new default VPC is created.
2. **Lambda Execution**:
   - The Lambda function identifies all security groups named "default."
   - It removes all inbound and outbound rules from those security groups.
3. **Result**: Default security groups are stripped of any rules, enhancing security.

## How to Set Up

1. **Create an SNS Topic**:
   - Go to the [Amazon SNS Console](https://console.aws.amazon.com/sns/).
   - Create a new topic (e.g., `NewDefaultVPCTopic`).
   - Set up the appropriate event to publish to this topic when a default VPC is created.

2. **Create the Lambda Function**:
   - Go to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
   - Create a new function using Python 3.x runtime.
   - Paste the code into the editor.

3. **Subscribe the Lambda to the SNS Topic**:
   - On the SNS topic's **Subscriptions** page, add a subscription.
   - Select **AWS Lambda** as the protocol and choose your Lambda function.

4. **Set Permissions**:
   - Attach an IAM role to the Lambda function with the following permissions:
     - `ec2:DescribeSecurityGroups`
     - `ec2:RevokeSecurityGroupIngress`
     - `ec2:RevokeSecurityGroupEgress`
     - `sns:Subscribe`

5. **Test the Function**:
   - Simulate a notification by publishing a message to the SNS topic.
   - Verify the Lambda function is triggered and processes the security groups.

6. **Monitor**:
   - Check the EC2 Security Groups and CloudWatch Logs for results.

## Notes
- **Caution**: This function removes **all rules** from security groups named "default." Ensure you test thoroughly before deploying.
- **Automation**: With the SNS topic trigger, this function automatically handles newly created default security groups.
