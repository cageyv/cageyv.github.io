+++
date = "2022-07-14"
title = "Security Basics in AWS or How To Get Rid of Hardcoded Credential and Reduce Data Leakage Risks with aws-vault"
slug = "aws-vault"
tags = [
    "aws",
    "security",
    "credentials",
    "aws-vault",
]
categories = [
    "aws",
]
series = ["AWS"]
+++

Developers often hardcode credentials on a public or private GitHub repository, ramping up data leakage risks. It’s hardly better to store static credentials in the .aws/credentials folder on a server or a local operator machine. As american cryptographer, writer, and computer security specialist, Bruce Schneier, says:  . "Only amateurs attackWe machines; professionals target people." Therefore, you, not your hardware, is at risk. 

By executing fraudulent software, cybercriminals can easily steal all the data from the folder or a whole directory with your, your friends’, and clients’ credentials. Even the AWS support team is exhausted with constant tickets regarding stolen credentials from public Git repos. Here's why if you commit keys, expect an email in 3-5 minutes saying that the IAM policy has been applied. It means that you can’t get rid of the policy or destroy exposed credentials. 

![FistImage](/images/posts/aws_vault/1.png)

Even such measures don’t solve the problem. According to the [Verizon 2022 Data Breach Investigations Report](https://www.techtarget.com/searchsecurity/news/252520686/Verizon-DBIR-Stolen-credentials-led-to-nearly-50-of-attacks), there’s been an almost 30% increase in stolen credentials, proving it to be a true-and-tried method to gain unauthorized access to an organization for the past five years. In fact, they account for almost half breaches.

![FistImage](/images/posts/aws_vault/2.png)

For the past 12 months, [31,000+](https://outpost24.com/blog/FTSE-100-compromised-credential-study-2022) stolen and leaked credentials were detected for FTSE 100 companies, while almost 40% were disclosed on the underground. The same happened with 1 billion records of Chinese [private citizens’ data](https://www.reuters.com/world/china/hacker-claims-have-stolen-1-bln-records-chinese-citizens-police-2022-07-04/) stolen from the Shanghai police in Summer 2022. All this was possible due to [exposed credentials](https://twitter.com/cz_binance/status/1543905416748359680) on CSDN—the Chinese Software Development Network. 

The worst part — developers can do nothing to prevent the attack even if it’s detected quickly. [Honeypot results](https://www.comparitech.com/blog/information-security/github-honeypot/) showed that it takes 1 minute to find exposed credentials and launch attacks. The entire attack lasts only up to 4 minutes from the moment of exposure.

## Use aws-vault To Securely Store and Access AWS Credentials in a Development Environment 

Aws-vault is a tool that has tackled the problem of stolen credentials for six years already. It stores your IAM credentials in a secure keystore and then generates temporary credentials to expose to your shell and applications. Therefore, the keys are not hard-coded or static, which decreases data leakage risks. Here are four key problems that aws-vault solves:

- **Secures access to products under development.** An engineer who works on a digital solution can run tests without committing keys in public Git repos. Even if you commit your secrets in a private Git repo, you can face security risks. Since no alerts will be sent, you will find out about the incident when your product is in public access—for example, if you are about to begin a presentation, but the access to the solution is blocked.
- **Controls what type of credentials is used.** One common problem a developer faces is not understanding what credential types are used by apps. They can be local, static hardcoded ones, environment variables, containers, EC2 Instance profiles, or ECS Container task roles. Aws-vault populates environment variables but can also emulate EC2 metadata servers and ECS credential servers. 

![FistImage](/images/posts/aws_vault/3.png)

- **Provides seamless access across various apps.** Using several accounts is the norm for developers. Each account has its own access permissions. Without hardcoding, you need to think about where to store credentials and how to distribute them across a team securely. With aws-vault, you don’t need to guard your AWS Multi-Account strategy, thinking about whether to commit keys or not. The tool sends dynamic credentials that expire in a short timeframe, which leaves a reduced window of opportunity for a hacker.
- **Convenient navigation across several apps.** Since your credentials are of the environment type, infrastructure cloud tools using AWS SDK (for example, Terraform) can easily take them and use them to permit you access. If you want to close all sessions, run the exit command. Any app automatically refreshes dynamic credentials as needed. 

## How to Practice With aws-vault

Most likely, currently, your logins and passwords are hardcoded. You may believe that it’s a convenient way to share credentials with your team without passing them over manually. Therefore, your code looks as follows:

![FistImage](/images/posts/aws_vault/4.png)

In this case, your data can be easily stolen and used for malicious purposes. Here’s a brief guide on how to boost your credentials’ security with aws-vault:
- Create an AWS account if you don’t have one. Create an IAM user and define roles. They allow you to access keys used with the API or CLI. Set secret keys, passwords, and action and access permissions.
- If you use several AWS profiles, assume temporary privileges for each. You can learn more about how to do this [here](https://github.com/99designs/aws-vault/blob/master/USAGE.md#using-multiple-profiles). 

Once you are set, you can start generating environment credentials with aws-vault. Suppose you have a **primitive JavaScript-based app** to test. You initiate a command for the vault to take dynamic credentials and add them to development environments for the app to run. With AWS SDK, the JavaScript app will get the credentials. 

![FistImage](/images/posts/aws_vault/5.png)

The process is the same if you want to deliver environmental credentials to a simple docker. Slightly edit a regular docker command, and you will receive environmental credentials.

![FistImage](/images/posts/aws_vault/6.png)

Aws-vault also allows you to **simulate the ESC credential server and ES2 Instance Profile**. For example, if you use the tool to deliver the credentials to **docker-compose**, aws-vault will pretend to be a part of the server responsible for credential transfer. The results in the development environment show that aws-vault launched a local simulation with a specific token just as on ESC. There will be remote credentials, while access key and session tokens aren’t transferred. 

![FistImage](/images/posts/aws_vault/7.png)

![FistImage](/images/posts/aws_vault/8.png)

If you want to simulate ES2 Instance Profile, the tool will run a local proxy. Here, you can’t avoid using root. As a result, you get EC2 metadata credentials. 

![FistImage](/images/posts/aws_vault/9.png)

You can learn more about all the explained examples here: https://github.com/cageyv/aws-vault-examples

## Benefits of aws-vault

Here are the main benefits of using aws-vault 
- **Simple functionality.** It takes only a couple of minutes to start using the tool. Basically, you need to create an account, and set IAM and roles, secret keys, and a password to begin.
- **Security.** Dynamic passwords that expire within a short timeframe don’t pose security threats, even if they are stolen. A cybercriminal can’t steal them, lie low, and then steal your data or app all of a sudden. Besides, if your company uses AWS Single Sign-on (SSO), aws-vault can also use credentials defined by AWS SSO ClI v2. 
- **Convenience.** Thanks to AWS SDK, the whole credential chain is supported by default. You don’t need to add configurations, while the apps will refresh dynamic passwords if they expire during your session.
- **Local testing.** Aws-vault allows you to test the app in the environment where it will be launched before release. You can spot bugs and fix them without deployment or providing access to admins or DevOps.

Another service that allows developing and testing apps offline is [Local Stack](https://localstack.cloud). It comes free and paid and serves as a metal developer that builds an app with AWS locally. Local Stack can simulate a lot of AWS services without access to the cloud to provide a seamless coding experience. The tool has a decent open-source database to speed up the coding process and let you focus on business objectives. The same applies to aws-vault, which facilitates credential transfers, reduces sensitive data leakage risks, and allows you to devote more time to meaningful tasks rather than thinking about how to pass keys without hardcoding them.

