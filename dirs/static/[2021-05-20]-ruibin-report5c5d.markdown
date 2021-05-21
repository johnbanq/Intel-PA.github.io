---
layout: page
title: [2021-05-20]-ruibin-report
permalink: /static/ruibin/progress/[2021-05-20]-ruibin-report/
---

[**<-back**](/static/ruibin/progress)  

## What did I do

1. try to extract entity of the input by myself, failed. It is difficult to label the data.  link oral description to the normalizational description. 


2. Azure Health Bot 

    * [Links](https://westeurope.healthbot.microsoft.com/account/test-demo-bemqbrf/scenario-editor/d9c25a7a-28a0-43c2-a955-1c93a8a59752)

    * Advantages
        * API is avaliable
        * user can not only use diagnosis service but also build their own diagnosis tree
        * example   

    * [charge](https://docs.microsoft.com/en-us/azure/health-bot/resources/pricing-details)
        * free, 3000 messages, 200 chances to consult(200 MCU)
        * 500 fixed monthly fee, 10,000 Messages and 1000 MCU

2. useage of the IBM Annotator for clinical data

    * Purpose: extract useful information from patient's sentences. 
    * [Links](https://acd-try-it-out.mybluemix.net/preview)

    * Advantages:
        * API is avaliable

    * Disadvantages:
        * API out is in a mass, user should familiar with their related lables (for example: Insight type, Medical Code, and entity type), so thay can easily extract useful information of patient's input, which has High learning costs
    
    * [charge](https://cloud.ibm.com/catalog/services/annotator-for-clinical-data)
        * free: 3000*1000 characters
        * charge: Item = 1000 characters of input text;
          Customized instance = USD 10,000 per month;
            Up to 24,999 items = $0.12 per item;
            Up to 499,999 items = $0.10 per item;
            500,000 or more = 0.07 USD per item


3. practice the coding for basic nlp algorithms(CBOW,RNN,Attention+RNN,Transformer)


## what I will do next

continue go as we planned


## difficulties of our project

1. most of our collected data are QA, describe their symptom, then ask the doctor what they can do to relieve it, not for what disease they have.
2. https://www.aclweb.org/anthology/2020.emnlp-main.743.pdf









