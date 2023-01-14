+++
date = "2023-01-12"
title = "Where no Windows Machine? Luck of space? Travel a lot? Let's use AWS as is Cloud Gaming platform"
slug = "aws-cloudgaming"
tags = [
    "aws",
    "ec2",
    "cloudgaming",
    "terraform",
]
categories = [
    "aws",
]
series = ["AWS"]
+++

## Why Could Gaming? What is the Problem?
Usually, for PC gaming, it is required to have a nice and fresh PC. But time does not stand still; there are many things that change us. The simplest one is that our PCs just get old, and we can't run new titles at high specs anymore, just because of hardware limitations.
What's next? If we are going to update our setup, this means a huge upfront cost. We have to pay right now or make a commitment to pay (such as credit) for a high-end PC. And you know what? After a while, it will get old too. I went through that cycle years ago, when I played a lot more than I do today. Every 2-3 years, I just needed to buy a new PC. At the same time, it is bad for the environment, because we just can't make proper hardware utilization.
Another thing is the OS and hardware architecture. My first PC was on Windows 95, and I stuck with the Windows platform for a while until the Windows 7 age. Next, I used Ubuntu up to 20.04. And finally, I came to MacOS. Why did I do it? Because my life changed, different work, different lifestyle, and of course, different PCs.
So, if we return to the problem: old games, which were created for Windows x32, can't be run on new MacOS ARM. Even Rosetta can't do it.
With Cloud Gaming, we could run ANY PC game. And if, for example, you are going to move to another apartment, to another town, or another country, should you bring your huge hi-end PC with you? Or will it act as an anchor for you?
More than 10 years ago, I decided to switch to laptops and make my life more flexible. And of course, if you are a hardcore gamer, with cloud gaming, you could bring your games on vacation.

## Which options do we have?
Option one: Switch to consoles? No way. Or better put, gaming consoles give us a different type of experience. And of course, they are still huge items in the bag.
Cloud gaming. There are many options for how to play in the cloud. If you don't want to do anything by yourself and the game you like is popular, please go to Geforce NOW or Amazon Luna. But if your game, for example, is not yet released (Early Access) or otherwise too old for major cloud gaming providers, let's see what we can do.

## Self builded Cloud Gaming PC
There are several projects that offer Cloud PC Renting. But in that case, you also have to bring your games with you. For me, it sounds a bit scary. I have to log in to my very old Steam account in some place that I don't actually control. Also, they require to pay in advance (monthly or annually). Let's be serious. We are going to play one or two game sessions or maybe just run our favorite game from the past once, and that's it. So, I mean there is no reason to top up a fixed amount or pay a monthly subscription, which we could forget to stop. And that's when AWS comes to us.
AWS EC2 offers pay-as-you-go pricing, and we could pay per minute in the cloud. 

## More useful information 
- Create and activate AWS Account https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/  
- Increase your account quotas and get instance with GPU https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-limit/ 
  - AWS Regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ 
  - AWS EC2 Types: https://aws.amazon.com/ec2/instance-types/ (Go to Accelerated Computing)
  - Short how to: Open "Service Quotas" -> "Amazon Elastic Compute Cloud (Amazon EC2)" -> Put "L-DB2E81BA" or "On-Demand G and VT instances" in the search bar -> Request quota increase -> "Change quota value: <Desired max number of vCPU> or 8". Note: It could require up to 48h, be ready for that.
- Create instance from basic Windows image: https://aws.amazon.com/blogs/compute/use-amazon-ec2-for-cost-efficient-cloud-gaming-with-pay-as-you-go-pricing/
- Use parsec app: https://www.richardneililagan.com/posts/create-game-server-aws-parsec/ 
- NVIDIA Gaming PC - Windows Server 2019: https://aws.amazon.com/marketplace/pp/prodview-xrrke4dwueqv6  
- Link how to create EC2 in AWS: https://medium.com/tensoriot/cloud-gaming-on-amazon-web-services-4be806c0051b 

## Which way I choose?
Actually, I tested many ways in blog posts above, 
but in the end, I'm using `NVIDIA Gaming PC - Windows Server 2019` + Microsoft RDP client 
There are some useful settings on client side
![FistImage](/images/posts/aws_cloudgaming/1.png)

Setup is pretty simple:
- Run Terraform code https://github.com/cageyv/terraform-aws-ec2-cloud-gaming 
- Wait ~10-12 min 
- Open AWS Console, go to EC2 instance
- Decrypt password with ec2.pem private key (complete unsecure way, please save your secrets in Secret Manager)
- Get RDP File 
- Connect, format EBS, update NVIDIA drivers (optional), install Steam or etc
- Play
- In the end of game session, don't forget to stop your instance manually or with Terraform

Also, I know about EC2 Spot Instances a lot, you could check a [blog post](/posts/aws-ec2-spot/) about it. 
But I don't want any interruptions in my 1h game session, but in case of your plans is playing longer, than yes try spots.
And yes, Terraform code example support both On-Demand and Spot variants.

