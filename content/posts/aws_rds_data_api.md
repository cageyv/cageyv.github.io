+++
date = "2024-01-04"
title = "AWS RDS Data API and CloudTrail. Who drop the table?"
slug = "aws-rds-data-api"
tags = [
    "aws",
    "cloudtrail",
    "slack",
]
categories = [
    "aws",
]
series = ["AWS"]
+++

## Introduction
Amazon Web Services (AWS) continually innovates to enhance user experience and efficiency. A prime example of this is the recent update to the RDS Data API, particularly for Amazon Aurora PostgreSQL-Compatible Edition. This update is a game-changer, as it offers users the ability to access Aurora clusters via a secure HTTP endpoint. The key here is the removal of rate limits and the elimination of the need for database drivers and managing connections. 

![Alt text](/images/posts/aws_rds_data_api/image1.png)

## Main Features of the Redesigned Data API
The redesigned Data API is not just an incremental update; it's a significant overhaul aimed at scalability and ease of use. Here's what you need to know:

- **No More Rate Limits**: Initially available for single instance Aurora Serverless v1 clusters with a 1,000 RPS rate limit, the API now imposes no rate limits for ASv2 and Aurora provisioned clusters.
- **Enhanced Scalability and Efficiency**: The API has been redesigned for increased scalability, supporting a wider range of database clusters.
- **Connection Pooling**: One of the most significant benefits is the automatic pooling and sharing of database connections, greatly simplifying application scalability.
- **Backward Compatibility**: For those already using Data API for ASv1, the transition will be smooth thanks to backward-compatible commands.

## AWS CloudTrail Integration: A Leap in Security and Accountability
Integrating the RDS Data API with AWS CloudTrail marks a significant step in database security and operational transparency. CloudTrail captures all API calls as events, including the identity of the API caller, the time of the API call, the source IP address of the API caller, and more. 
And this is a very important part. By using CloudTrail we could get information about who, when and from where executed SQL command.
Could you imagine that you could get information about who execute `DROP TABLE money_transfers` in a mitutes and without aditional tools?
Also CloudTrail is well integrated with GuardDuty, which is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads. 

## Setting Up CloudTrail with RDS Data API and Slack Notifications
Setting up CloudTrail with the RDS Data API and configuring Slack notifications is straightforward. This setup allows you to receive instant updates on your database operations, enhancing your monitoring and response capabilities. For example, you could use [cloudtrail-to-slack](/posts/aws-cloudtrail-to-slack) Terraform Module or any other tool to receive notifications.

## ToDo List
- Enable the RDS Data API for your Aurora Cluster
- Ensure CloudTrail is enabled for your AWS account (if it isn't already).
- Setup Slack notifications for CloudTrail events
- Use the RDS Data API to execute SQL commands
- Surprise your team by sending them their SQL commands

## What else we could do?
Combined with Just in Time (Elevated Access), this could be the best way to manage your database access.
You could allow to execute SQL commands only for specific period of time and only for specific users.

## References
- [Using RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)
- [Logging RDS Data API calls with AWS CloudTrail](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/logging-using-cloudtrail-data-api.html)