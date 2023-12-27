+++
date = "2024-01-03"
title = "The Multiverse of Hosting a Static HTML File on AWS"
slug = "aws-static-hosting"
tags = [
    "aws",
    "solutions",
]
categories = [
    "aws",
]
series = ["AWS"]
+++

Today, we dive into the versatile and dynamic world of AWS, exploring the numerous avenues for hosting a simple, yet pivotal, web element - the static HTML file. AWS, known for its robust and expansive cloud services, offers a plethora of methods for this seemingly straightforward task. Each method comes with its own set of features and benefits, suitable for various needs and complexities. From the efficient S3 buckets to the comprehensive AWS Amplify, we're covering a spectrum of options that cater to different scales and requirements. So, let's unpack these methods and see how they align with your DevOps strategies, business goals, and IT needs.

![First Image](/images/posts/aws_static_hosting/1.png)

## 1. S3 Bucket + CloudFront CDN
The standard yet powerful choice. Uploading your HTML file to an S3 bucket and integrating it with CloudFront is not just about simplicity; it's about reliability and performance. This method is a staple in the AWS toolkit, favored for its security and scalability.

## 2. EC2 Instance with a Web Server
Deploy an EC2 instance and install a web server software to serve your HTML file. 
For those who need granular control, deploying an EC2 instance with a web server might seem enticing. However, it's often an overkill for hosting a single HTML file, demanding substantial resource allocation and maintenance. It's a classic approach but consider it for more complex hosting needs.

## 3. Lightsail
Lightsail offers a more streamlined experience compared to EC2, yet it inherits similar trade-offs. While it's a viable option for static hosting, its real value lies in its simplicity for small-scale applications, not just individual files.

## 4. Elastic Beanstalk
Elastic Beanstalk simplifies much of the heavy lifting involved in EC2 deployments. It's a feasible solution for those less familiar with containerization, but for a single HTML file, it might be more than what's needed.

## 5. AWS ECS and Fargate
Okay. Probably enough with the EC2-based solutions. Moving into container-based solutions, ECS and Fargate offer scalability and manageability. This approach fits well within modern DevOps practices, although for a single static file, it might be a bit extensive.

## 6. AWS AppRunner
One more from the container family. AppRunner streamlines containerized applications with its integrated CI/CD pipeline, reducing maintenance overhead. However, for straightforward static content hosting, it might introduce unnecessary complexity.

## 7. AWS Lambda with Lambda URL
A neat alternative. Use AWS Lambda to serve static content directly. It's more efficient than an EC2 instance or containers, consuming less energy and resources, though still a bit overkill for simple tasks as simple HTML hosting. And of cource we have to deal with CI/CD.

{{< notice tip >}}
If someone is would like to review the best option and the moment, please just keep scrolling.
{{< /notice >}}

## 8. AWS WAF Static Response
Using AWS WAF for static responses, especially in scenarios like rate limiting, adds an extra layer of user experience enhancement. It's a sophisticated approach that combines security with functionality. This is not a static hosting, but it is possible to respond with static content. And it is require additional setup with ALB, API Gateway, or CloudFront.

## 9. API Gateway
API Gateway's "Mock" response type is an innovative way to serve HTML content, particularly useful in development environments. It's a simple yet effective solution for testing and debugging.

## 10. AWS ALB
Application Load Balancer (ALB) allows for fixed-response actions, enabling you to serve static HTML content. Costly and overcomplicated for simple tasks, but it's possible. Could be usefull in case of request doesn't match any rules and we must have the default response.

There are many combinations of ALB, API Gateway, Labmdas and S3. But we are not going to cover them in this article.
And the last one is the most interesting.

## 11. AWS Amplify

![First Image](/images/posts/aws_static_hosting/2.png)

Amplify stands out as an all-encompassing solution, particularly appealing for projects that go beyond a single HTML file. Its seamless integration with S3, CloudFront, and git-based workflows, combined with CI/CD capabilities, makes it an attractive option for agile development environments and rapid deployment needs.

For a hands-on experience, follow the AWS https://aws.amazon.com/getting-started/hands-on/host-static-website/  tutorial on hosting a static website. It's straightforward and aligns with the AWS free-tier, offering cost-effective solutions. And also could be done in less than 10 minutes.

## Conclusion
Each hosting method on AWS has its distinct advantages and suitability, depending on your project's scale, complexity, and specific requirements. Whether you're optimizing for performance, cost, or ease of use, AWS provides a solution that aligns with your DevOps strategy, business objectives, and technical needs. By understanding these options, you can make informed decisions that drive efficiency and innovation in your organization.


