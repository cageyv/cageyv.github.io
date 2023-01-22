+++
date = "2023-01-15"
title = "LProbe: A Secure, Open-Source Local Health Check Solution"
slug = "lprobe"
tags = [
    "opensource",
    "security",
    "docker",
    "containers",
]
categories = [
    "opensource",
]
series = ["opensource"]
+++

## LProbe: A One-Stop-Shop Tool for Secure, Local Health Checks  
Even if your app is functioning, that doesn’t always mean it’s working correctly. For you to securely and easily ensure your local container is healthy before the system fails, FivexL developed an open-source automated local health check solution - [LProbe](https://github.com/fivexl/lprobe).  
A vivid example is an eternal timeout: your app doesn’t crash but keeps waiting for a system response. If you receive no alert that there is no response within, let’s say, 30 seconds, you may not notice something is wrong. Here comes a health check to ensure your app is working correctly. 
### What Is a Health Check?  
Health check is a process of checking whether a specific resource inside your local container is working correctly. The command conducts regular health checks within set time intervals and alerts you if the system fails to perform. That’s how LProbe works.  
Suppose you need to validate external systems and find out if your app can access a database or bucket, record something, etc. For you not to miss a problem, LProbe automatically runs the command within a predefined interval to ensure your container is healthy. If it isn’t, try turning it off and on or reload a container.  
  
*A quick reminder: all the further information is relevant for both API and Web Services. LProbe can also cover the majority of needs for both, as it doesn’t cover the needs of an app with no interface at all.*  
### How The Problem Was Solved Before LProbe?  
Today, there are several traditional methods to run health checks: curl or wget commands. Even if you don’t have them, the guides will advise you to install and run them, neglecting all the security precautions.  
In reality, you **undermine your app’s protection** significantly, since wget/curl commands are used in scripts and allow for downloading other utilities for a further attack. If an attacker is inside your file system and it’s not read-only, they will be able to download info from the web and run a code or binary files—all this leaves a **huge opportunity window for an intruder**.  
If you want a more secure option, guides will suggest you write your own code, which takes extra time and effort to integrate and maintain it. **FivexL developed a reliable and well-protected local health check solution - LProbe.** Let’s find out why it’s more convenient and secure compared to existing health check alternatives.  
### Traditional Health Check Methods for Docker, ECS, and Kubernetes (mTLS and Istio cases)  
If you Google how to conduct a local health check, the top results will keep shouting one thing: that wget and curl are your best options. We have conducted research to figure out what is proposed for different local health checks.  
  
**Docker Health Check**   
If you need a command to make docker ensure your container is performing correctly, 99% of guides recommend using a traditional CMD curl or CMD wget, like in this [example](https://docs.docker.com/engine/reference/builder/#healthcheck).
```
HEALTCHECK --interval=5m --timeout=3s \
    CMD curl -f http://localhost/ || exit 1
``` 
In terms of code, you need to pay attention to the output. Set up only two outputs: 0 - for a successful health check, meaning everything is working as it should, and 1 - for an unhealthy status.  
  
**Amazon ECS Health Check**  
[The Amazon ECS Container documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definition_healthcheck) focuses on the same commands and sets out two options to run a health check command:  
- The default one is CMD, which runs directly. It is the only option for containers without a shell.  
- The other one is CMD-SHELL, which runs with the container's default shell.  

Why do we mention this? The documentation only has one example of a CMD-SHELL, and this also uses the curl tool. You could try to search for more information about heath checks for containers in the re:post, but you will still find CMD-SHELL + curl/wget recommendations. Here is one [example](https://repost.aws/questions/QUfrOJiYQERXGAOgHGt1GW-w/container-health-check-for-ecs-task-with-awsvpc-network-mode).  
All this once again proves the fact that curl and wget are now deeply fixated in people's brains.  
  
**Kubernetes  Health Check**  
    Kubernetes has [embedded features](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-http-request) to run health checks with no extra effort. You can initiate it with an HTTP-get-command or run a gRPC liveness probe for Kubernetes v. 1.24. This is no longer an option once you add Istio Sidecar with mTLS because liveness probes take place outside the service mesh.  
  
Here, once again, all the tribute goes to an infamous wget (a standard command probe), exec is run, and you get health check results.  
### Which Health Check Solution Does ChatGPT Suggest?
Even AI can’t find a better option than using insecure commands or third-party tools that are vulnerable to intruders. To prove this, we asked ChatGPT for a health check solution. The FivexL team requested the following:  
*“I want you to act as a Cloud Engineer with a focus on AWS and Container Security. You will give advice about Docker Containers and Dockerfiles and help to create the most secure Dockerfile, and it will not be an empty one. My first request is, "I need a Dockerfile with a HEALTHCHECK instruction in it. Please use the most secure tool or command to run the health check"*  
Here’s what ChatGPT suggested:  
```dockerfile 
FROM alpine:latest
RUN apk add --no-cache curl
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
CMD ["/bin/sh"]
```
This Dockerfile specifies that the health check should run every 30 seconds, with a timeout of 30 seconds and a start period of 5 seconds. It also specifies that the health check should be retried 3 times if it fails. The curl command is used to check the status of the http://localhost/ endpoint. If the curl command returns an error, the health check will fail and the container will be considered unhealthy.  
You can also use other tools or commands to perform the health check, depending on your specific requirements. For example, you might use wget or httpie instead of curl, or you might use a tool like nmap to perform a network scan. Ultimately, the choice of tool or command will depend on your specific needs and the resources that are available within your container.
### A Single Solution for Everyone: LProbe 
Еnterprises usually code their proprietary binary tool and add it to a docker image to run health checks while maintaining a proper security level. Although the code is simple, it requires time to write and maintain it. To do this task once and for all, we at FivexL have created [LProbe — an open-source health check run tool](https://github.com/fivexl/lprobe).   
With a name that originated from “local probe,” LProbe can become a one-stop-shop health check runner for every startup that wants to focus on a core product:  
* Those who do secure containers based on a scratch image without a shell or other utilities
* Those who use ECS 
* Those who use Kubernetes with Istio and have to suffer with a CMD-probe.  

The best thing — it is a ready-made open-source solution to securely run your health checks. It now supports **two protocols**: *HTTP and GRPC*. The latter is designed thanks to the Grpc health probe, added by Google to Kubernetes 1.23. On your request, we can add other protocols like the Apache JServ Protocol.  
In the near future, we plan to further enhance the tool’s functionality to ensure it meets the demands of as many companies as possible. If you have any specific requirements or ideas on how to make LProbe better, feel free to share your feedback.  
We would be glad if you collaborate with us for the sake of secure local health checks. Also, we would appreciate it if you [rate LProbe on GitHub](https://github.com/fivexl/lprobe) to promote trust across the community.

