+++
date = "2025-05-25"
title = "Amazon Q CLI: More than chat. Building small game"
slug = "aws-q-cli-game"
tags = [
    "aws",
    "q",
    "q-cli",
    "amplify",
    "game",
    "javascript",
]
categories = [
    "aws",
]
series = ["AWS"]
+++

## From Swift to Java Script

Remember that old project? The one where I spent time with Swift back in 2023, trying to build a simple game about work-life balance? It was an entertaining idea to demonstrate how easily things can go wrong when given only a few options. But like many side projects, it was abandoned because of time constraints and, to be honest, the lack of robust GenAI tools at the time.

Fast-forward to today. I decided to resurrect that concept, but with a twist. This time, I'd leverage the power of Amazon Q CLI and aim for a Node.js/TypeScript implementation. Why the switch? Simplicity and the ease of deploying to the AWS cloud. My goal was a "100% vibe coding experience" – meaning, I'd let Amazon Q do the heavy lifting. No manual code changes, just commands to Q.

I started by feeding Q the old Swift project and its notes, asking it to translate the game into JavaScript.

![Initial Swift Project](/images/posts/aws_amazon_q_cli_game/001_swift.png)

The initial results were impressive. Q managed to port the core logic to JavaScript. There are just maybe a few lines of code in that Swift Project, but Amazon Q able to understand the task and prepare a completely different application. This is not just a “standard” Java 8 to Java 18 upgrade. Here is a platform migration from macOS to Web Application.

![Q generates JavaScript code](/images/posts/aws_amazon_q_cli_game/002_js.png)

Next, I tasked Q with adding tests. It's crucial for Q to be able to run the code, identify issues, and fix them. I always recommend letting GenAI tools be able to test their code.

![Q adding tests](/images/posts/aws_amazon_q_cli_game/003_tests.png)

And here's the migration to JavaScript, completed by Amazon Q. It looks basic, but all the code was migration, and what is more important - project bootstrapping. I don't need to spend time preparing the development environment.

![JavaScript code by Q](/images/posts/aws_amazon_q_cli_game/004_compete_migration_to_js.png)

With the basic game ported, it was time for new features.

![Q adding new features](/images/posts/aws_amazon_q_cli_game/005_addiding_new_features.png)

## ToDo.md as bidirectional communication

While Q was processing, I started a `todo.md` file to queue up more commands and ideas. AI can read files, right? All because of the built-in MCP inside the Q CLI.
Here we could find a set of basic tools:  [https://github.com/aws/amazon-q-developer-cli/blob/main/crates/cli/src/cli/chat/tools/fs_read.rs](https://github.com/aws/amazon-q-developer-cli)  
Oh, I maybe forgot, but yes, Amazon Q Developer CLI is open source. 
Another critical part is the set of MCP servers, which, if you are interesting you could find [here]( https://github.com/awslabs/mcp/tree/main/src).

![Creating a TODO file](/images/posts/aws_amazon_q_cli_game/006_creating_todo_file.png)

It is a bit better to tell Q CLI to use this `todo.md` file. It's hard for these tools to understand which content, for example, needs to be processed in the repository. The codebase could be big.

![Asking Q to use the TODO file](/images/posts/aws_amazon_q_cli_game/007_ask_q_to_use_todo.png)

Exciting "Ah-ha" moment, Q started proposing its ideas and adding them to the `todo.md` file. This created a cool back-and-forth communication channel, all within a simple markdown file. You know, currently we can't speak with the CLI Tool yet, but we can both read and write text files.

![Q suggesting ideas in TODO file](/images/posts/aws_amazon_q_cli_game/008_q_use_todo_and_suggest_ideas.png)

We even got checkboxes working in the to-do list, and Q was smart enough to understand them and mark items as done. This kind of interactive coding is quite something.

![Q using checkboxes in TODO](/images/posts/aws_amazon_q_cli_game/009_add_check_boxes_for_todo.png)

## Deployment to AWS Amplify 

With development progressing nicely, the next logical step was deployment. I decided to feign a bit of AWS unfamiliarity and asked Q for guidance on deploying the app.

![Asking Q how to deploy](/images/posts/aws_amazon_q_cli_game/010_ask_q_how_to_deploy_app.png)

Q suggested AWS Amplify, and the process was surprisingly straightforward. Connecting to GitHub was a breeze.

![Amplify connect to GitHub](/images/posts/aws_amazon_q_cli_game/011_amplify_connect_github.png)

Setting up the app basics in Amplify was also just a few clicks.

![Amplify app basics](/images/posts/aws_amazon_q_cli_game/012_amplify_app_basics.png)

And just like that, the app was deployed, complete with the new features. Amplify handled all the build processes, so no need for manual CI/CD setup.

![Deployed app with new features](/images/posts/aws_amazon_q_cli_game/013_deployed_app_with_new_features.png)

The most fascinating part? Even the commit messages were AI-generated!

![GitHub commits from AI](/images/posts/aws_amazon_q_cli_game/014_github_commits_from_ai.png)

This entire experience showcased that Amazon Q CLI is much more than just a chat interface. It can be a powerful partner in the development lifecycle, from coding and testing to deployment and even project management. It's a glimpse into a new era of software development.

The game itself is here: https://timetectonic.cageyv.dev/  
My goal mostly was to try the autonomous behavior of Q and ability to follow instructions and perform not well described tasks.

## Summary 
- Amazon Q Developer CLI could bring agentic behavior to the terminal as independent from the applications. 
- It is giant progress since the CodeWhisperer era 
- Build-in tools help a lot and let the agent execute many commands.
- Amazon Q Developer CLI could also: debug issues in AWS, check logs, and S3 buckets. With access to the AWS API, it is a very powerful tool. 
