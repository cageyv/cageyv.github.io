+++
date = "2023-09-30"
title = "scb-to-moneywiz: Import Bank Transactions from SCB Easy (Thailand) to MoneyWiz"
slug = "scb-to-moneywiz"
tags = [
    "opensource",
    "money",
]
categories = [
    "opensource",
]
series = ["opensource"]
+++

## Introduction:
Navigating financial management can be a tricky affair, especially without cutting-edge banking technology. But for users of MoneyWiz, an ingenious script is making life easier. This tool specifically aids in importing SCB Bank transactions, transforming a tedious task into a smooth, automated process.

## The Challenge with SCB Bank:
As we approach the end of 2023, SCB Bank's lack of OpenBanking support means their clients are stuck with transaction statements in PDF format, courtesy of the SCB Easy App. Not exactly convenient for those who need to keep track of their finances regularly. This is where our script steps in, offering a practical solution for MoneyWiz users.

## Conversion from SCB Easy App Statement to MoneyWiz App:
This script's primary function is to facilitate the conversion of transaction data from the SCB Easy App's PDF format into a form compatible with MoneyWiz. It's all about easing the process for MoneyWiz users, helping them save time and manage their finances more efficiently.

![image1](/images/posts/opensource_scb_to_moneywiz/1.png)

## Inspiration and Problem-Solving Approach:
Inspired by the agile and solution-centric startup culture, I realized focusing on features, not perfection, was the key. It was about creating a tool that worked well, fast, and addressed the main pain point – seamlessly importing bank transactions into accounting software.

## Development Journey:
My journey began with a dive into research, where I stumbled upon `tabula-py`, a powerful OCR tool that converts multipage PDF files with tables into a more manageable format. The task was then broken down into manageable steps. The first one - just able to open PDF and make lib works correctly. After that, I had to parse the transactions, differentiate between debits and credits. Finally, I had to generate a MoneyWiz-compatible URL and create a comprehensive CSV file. An essential feature was added: verifying the accuracy of transactions against the PDF total. Surprisingly, the entire script took just 4-5 hours to develop over 3-4 attempts. 

## How it works?
First we have to get PDF statement from SCB Easy App. 
- Open SCB Easy mobile app
- Go to Bank Services -> Account Summary -> Select account and click "Tap to view more details" -> "More Services" -> Request Statement -> Select range -> - - Check Mail Box
At the moment we will get a file per month.

And after that we have to run script:
- Clone git repo
- Install requirements `pip install -r requirements.txt` or `./setup.sh`
- Activate virtualenv `source venv/bin/activate`
- Get the CSV `python3 main.py --password XXXXXX --account TEST --infile ./data/AcctSt_Jul23.pdf --csv --debug`
As account name we have to use account name from MoneyWiz.

The last step is to import CSV file to MoneyWiz.
- Open MoneyWiz
- Go to File  -> Import -> Import from CSV

## Reflection and Future Outlook:
While this script is a temporary fix until SCB Bank embraces OpenBanking, it stands as a perfect example of innovative, quick-fix problem solving that effectively bridges technological gaps.

## About MoneyWiz and SCB Bank:
[MoneyWiz](https://www.wiz.money/) stands out with its adaptability. It's a platform that suits both expert and novice financial managers, offering extensive features in a user-friendly package, allowing you to manage your money your way.

[SCB](https://www.scb.co.th/) Originating as the "Book Club" in 1904 by Prince Jayanta Mongkol, a brother of King Chulalongkorn (Rama V), SCB Bank evolved from an experimental project to "The Siam Commercial Bank" in 1907. This transformation marked a significant step in Thailand's journey towards establishing a robust, independent banking system.

## Conclusion:
For MoneyWiz users who bank with SCB, this script isn't just a tool; it's an essential part of their financial toolkit. It demonstrates how a simple, need-based idea can revolutionize personal finance management.
Also MoneyWiz added that tool to their support page: https://help.wiz.money/en/articles/8358537-3rd-party-data-bank-importers 
Hope that script will help people to save their time.

