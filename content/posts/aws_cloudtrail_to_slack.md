+++
date = "2022-07-12"
title = "What Is AWS CloudTrail, and Why Do You Need It"
slug = "aws-cloudtrail-to-slack"
tags = [
    "aws",
    "cloudtrail",
    "slack",
    "terraform",
]
categories = [
    "aws",
]
series = ["AWS"]
+++

Don’t have enough resources to set up a security department but want to stay on top of your AWS CloudTrail events? Find out how the CloudTrail-to-Slack Terraform module by [FivexL](https://fivexl.io/) solves this problem for startups and small teams.

## Terraform Module for AWS CloudTrail — An Effective Security Tool

While large corporations have their own Security Operations Centers (SOCs) responsible for information security and can afford expensive solutions, startups usually don’t have enough resources and time to set up such a luxury. Therefore, they have to look for simple security solutions to protect their data. Understanding the pain of limited resources, FivexL developed the Cloudtrail-to-Slack Terraform Module.

The module works with data gathered from AWS CloudTrail and sends notifications to Slack to keep you updated on what is happening in CloudTrail practically in real-time. Think of it as a surveillance camera that is not constantly monitored but notifies you if something suspicious happens — for example, if a stranger keeps moving near your front or back door. 

### What Is AWS CloudTrail?

Let’s briefly discuss AWS CloudTrail. AWS CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs. More info: [What is CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

Visibility into this type of data is a key element of corporate security, as you can identify who did what, when, where, and how, as well as what resources were used. As a result, you can always stay on top of what is happening in your Amazon Console to fix misconfigurations timely and prevent intrusions. On the one hand, you have all the data to ensure your security, on the other hand, you are still an easy target for cybercriminals. Here are some reasons why:

#### Too Many Events to Keep Track of Manually

Even a startup or a small team will have a lot of logs to monitor. Therefore, you can easily miss an important event worth your attention. For example, you may not notice failed API calls because of a lack of permission, which may indicate incorrect operations setup or intrusion. While in the former case, you merely need to get rid of misconfigurations, in the latter case, you need to prevent a cyber attack that may cost you your business. 

Imagine you are using a root user to login into your Amazon Console. Cybercriminals can steal your static credentials, change a password, and basically steal your data, together with business. We recommend applying Single Sign-on (SSO) or Identity and Access Management (IAM), together with multifactor authentication (MFA). This way, your credentials will expire within a certain period of time, which leaves a short opportunity window for a hacker. 

#### Complicated and Hard-to-Comprehend CloudWatch Notifications 

You can set up notifications from CloudWatch that will send alerts to your email if some suspicious events are recorded. But be ready to devote a lot of time and effort to set them up and comprehend them. 

## Stay on Top of Your CloudTrail Events Easily With CloudTrail-to-Slack Terraform Module

Sending notifications about AWS CloudTrail events to Slack is a useful feature for startups implemented in the Cloudtrail-to-Slack Terraform module by FivexL. We have built a Python-based Lambda that analyzes all the recorded events in CloudTrails and sends notifications to Slack if they’re categorized as suspicious logs according to rules. Delivering Lamda to AWS is already a solved problem and we decided to use the open source module from [Terraform AWS Modules](https://registry.terraform.io/modules/terraform-aws-modules/lambda/aws/latest). So, this is a ready-made flexible CloudTrail-to-Slack Terraform module. You need only to set it up in a couple of seconds, and the following alerts will be sent to your Slack channel:

- Activities done by a root account
- Failed API calls, and suspicious 
- Console logins without MFA
- Sensitive events like IAM, network, and data storage access changes

![FistImage](/images/posts/aws_cloudtrail_to_slack/1.webp)

As a result, you are always aware if something odd is going on in your AWS Console without investing extra time and effort. Chief Cloud Economist at The Duckbill Group, Corey Quinn, who helps companies decrease their AWS bills, mentioned the module in [his podcast dedicated to security awareness training](https://www.lastweekinaws.com/podcast/aws-morning-brief/security-awareness-training-in-five-minutes/): ‘I found a Terraform module that [deploys Lambda](https://github.com/fivexl/Terraform-aws-CloudTrail-to-Slack) to watch CloudTrail and report to Slack - got all that? Good lord - whenever certain things happen. Those things include root logins, console logins without MFA, API calls that failed due to lack of permissions, and more. This might get noisy, but I’d consider deploying at least the big important ones’. This makes the module worth paying attention to. 

Please, note: there is an approximate 5-10 minutes alert delivery delay because the current version is built upon parsing of S3 notifications.

## CloudTrail-to-Slack Terraform Module Features

Besides allowing startups to stay on top of CloudTrail events, the Terraform module grants startups flexibility. Here are the main benefits:

### Adjustable Ready-Made Rules

Startups are known to have little to no time because of limited human resources. To facilitate module setup, there is a set of default rules; they are Python strings that are evaluated during the runtime and designed to return the bool value. The CloudTrail event is flattened prior to processing and should be referenced as an event variable. 

Rules can also be ignored. In this case, an event is ignored by Lambda, and no notification is sent to Slack. “Ignore rules” has the same syntax as default ones. But it is highly recommended to fix alerts instead of ignoring them. This approach should be implemented only when there is no opportunity to fix the alert. Here is how you can do this.

```hcl
locals {
  cloudtrail_ignore_rules = [
      "'userIdentity.accountId' in event and event['userIdentity.accountId'] == '11111111111'",
    ]
}
# we recomend storing hook url in SSM Parameter store and not commit it to the repo
data "aws_ssm_parameter" "hook" {
  name = "/cloudtrail-to-slack/hook"
}
module "cloudtrail_to_slack" {
  source                         = "fivexl/cloudtrail-to-slack/aws"
  version                        = "2.3.0"
  default_slack_hook_url         = data.aws_ssm_parameter.hook.value
  cloudtrail_logs_s3_bucket_name = aws_s3_bucket.cloudtrail.id
  ignore_rules                   = join(",", local.cloudtrail_ignore_rules)
}
```

### Customizing Notifications

You may not want all team members to receive security alerts from the Terraform module. Some may use the information to their advantage, while others may merely be bumped with tons of irrelevant notifications, which disrupts productivity and isn’t affordable for a startup. Here’s why the module gives an opportunity to customize notifications. For example, they can be sent to different Slack channels for different accounts according to the event account ID. 

### User-Defined Rules To Match Events

If the default rules don’t cover all your needs, you can set up user-defined rules to stay in control of what’s going on in CloudTrail. Here’s how to deploy the module with a list of the events that are necessary to track. 

```hcl
data "aws_ssm_parameter" "hook" {
  name = "/cloudtrail-to-slack/hook"
}
locals {
  # CloudTrail events
  cloudtrail = "DeleteTrail,StopLogging,UpdateTrail"
  # EC2 Instance connect and EC2 events
  ec2 = "SendSSHPublicKey"
  # Config
  config = "DeleteConfigRule,DeleteConfigurationRecorder,DeleteDeliveryChannel,DeleteEvaluationResults"
  # All events
  events_to_track = "${local.cloudtrail},${local.ec2},${local.config}"
}

module "cloudtrail_to_slack" {
  source                         = "fivexl/cloudtrail-to-slack/aws"
  version                        = "2.0.0"
  default_slack_hook_url         = data.aws_ssm_parameter.hook.value
  cloudtrail_logs_s3_bucket_name = aws_s3_bucket.cloudtrail.id
  events_to_track                = local.events_to_track
}

resource "aws_cloudtrail" "main" {
  name           = "main"
  s3_bucket_name = aws_s3_bucket.cloudtrail.id
  ...
}
resource "aws_s3_bucket" "cloudtrail" {
  ....
}
```

## Conclusion

The FivexL Cloudtrail-to-Slack Terraform module is a simple tool for you to stay on top of your CloudTrail events and ensure your Amazon Console is secure and properly set up. You can be notified about actions performed by a root account, failed API permissions, and console logins without MFA. Besides this, you can specify which sensitive events you wish to track, set up new rules to extend monitoring beyond default rules, and adjust who receives the notifications. For more info about the Cloudtrail-to-Slack Terraform module, please, check out [FivexL's GitHub](https://github.com/fivexl/terraform-aws-cloudtrail-to-slack).
As a result, startups and small teams can focus on core operations while being sure their data and business are safe. However, if your CloudTrail records too many events, FivexL Terraform Module may be insufficient. 
