+++
date = "2024-05-30"
title = "Getting started with Amazon Bedrock Studio"
slug = "speakup-aws-bedrock-and-accounts"
tags = [
    "aws",
    "bedrock",
    "control-tower",
    "multi-account",    
]
categories = [
    "SpeakUp",
]
series = ["SpeakUp"]
+++

## AWS Sumit Bangkok 2024

The event itself was huge. This year it was special one. AWS will launch Bankgon region in 2025. And this is a awesome news for all of us. Many companies are waiting for this moment. And I was happy to be a part of this event. Miss that one? Don't worry, you can catch up the next one in the next year. 

![FistImage](/images/posts/speakup_aws_bedrock_and_accounts/1.jpg)

## DevLounge and AWS Community Lightening Talks

As is AWS Community Builder I was invited to the DevLounge. It was a great opportunity to share my experience with the community. I was talking about the Amazon Bedrock Studio and how it can be used along with your multi-account environment. 

## Amazon Bedrock Studio and Control Tower

The Amazon Bedrock Studio was renamed to Amazon Bedrock IDE. And it sound better now. 
Amazon Bedrock IDE is a web application designed to simplify prototyping with Amazon Bedrock models and features without the need for a developer environment. Basically you play around in the webpage. It allows you to try many differnt models and see the results. It could be good forprototype applications using Amazon Bedrock models and features like Knowledge Bases or Guardrails, all within the Studio’s no-code interface.
Private Knowledge Bases are a new feature that allows you to create a private knowledge base that is only accessible to your account. This is useful for creating a knowledge base that is specific to your organization and not shared with other accounts. It is very important, that you will control the access to the knowledge base and data will not be shared with other customers and with the whole world.

But during my testing I found that it is simple to use only if we already have AWS IAM Identity Center enabled. 
If we talk about privacy we also talk about permissions and access control. 
And the moment more and more AWS Managed services are integrated with AWS IAM Identity Center. For example: Athena, QuickSight, Managed Grafana, Amazon Q. Amount of the services is growing. And it is good.
If everyhing is already going to AWS IAM Ientity Center it makes us only one step far from AWS Multi Account Strategy.

Ideally I could suggest to create new AWS Account and call it "Management Account". And enable AWS IAM Identity Center there. And then connect all other accounts to this one. It will save you some time in the future. 

All the Bedrock experiments they could be stored as separate AWS Account. Why? Because it is easy to manage the permissions and access control. And it is easy to delete the account if you don't need it anymore. For example you don't like Bedrock anymore and whant just to stop using it. (I hope it will not happen).

Benefits of using multiple AWS accounts:
- Group workloads based on business purpose and ownership
- Apply distinct security controls by environment
- Constrain access to sensitive data
- Promote innovation and agility
- Limit scope of impact from adverse events
- Support multiple IT operating models
- Manage costs
- Distribute AWS Service Quotas and API request rate limits



Full presentation is available [here](https://www.slideshare.net/slideshow/getting-started-with-amazon-bedrock-studio-and-control-tower/269414509).

![FistImage](/images/posts/speakup_aws_bedrock_and_accounts/2.jpg)

## AWS Summit Stocholm 2024

In the same week I travel across the globe and attend another AWS Summit in Stocholm. It was a great event. I was happy to meet many AWS Community Builders and AWS Heroes. Together with Andrey Devyatkin we also attend the AWS Partners Summit. Techically it makes it 3 summits in one week. 
Both events in Stocholm were greate. And if you are in the area, I would recommend to attend. For example it is greate opportunity to meet the AWS team and ask your questions. 

![FistImage](/images/posts/speakup_aws_bedrock_and_accounts/3.jpg)

## AWS User Group Meetup in Las Palmas 2024

After the summits I was invited to the AWS User Group Meetup in Las Palmas. It was a great event. I was talking about the Amazon Bedrock Studio and how it can be used along with your multi-account environment.

![FistImage](/images/posts/speakup_aws_bedrock_and_accounts/4.jpg)
![FistImage](/images/posts/speakup_aws_bedrock_and_accounts/5.jpg)

## Conclusion

These few weeks have been a whirlwind of innovation, knowledge sharing, and connecting with the AWS community worldwide. From the groundbreaking announcements at AWS Summit Bangkok 2024 to the engaging sessions at AWS Summit Stockholm and the vibrant discussions at the AWS User Group Meetup in Las Palmas, each event offered unique opportunities to learn, share, and grow.

Being part of such a dynamic and global community is always inspiring. It’s not just about the technology but also about the people who drive innovation and collaboration. If you missed these events, I highly recommend keeping an eye on upcoming AWS Summits and community meetups—you never know what transformative ideas you might discover or the connections you might make.

Let’s keep building, sharing, and shaping the future of the cloud together!
