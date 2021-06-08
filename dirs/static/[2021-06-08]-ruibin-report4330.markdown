---
layout: page
title: [2021-06-08]-ruibin-report
permalink: /static/ruibin/progress/[2021-06-08]-ruibin-report/
---

[**<-back**](/static/ruibin/progress)  

## What did I do

1. Natural language understanding of patient's input
    * the essential of this part is to extract the symptom entities from the input sentence.

    * I try to extract entity of the input by myself, failed. It is difficult to label the data.  linking the oral description to the normalizational description. 

    * So I decided to use exist system, for example: Biobert and IBM Annotator for clinical data. 

    * examples of labeled sentence.

        label: cd /home/newdisk/personal_code/JointBERT/data/atis


i want to fly from    baltimore        to     dallas           round          trip

O   O   O  O   O  B-fromloc.city_name  O  B-toloc.city_name  B-round_trip   I-round_trip


2. usage of the Biobert

    * API is avaliable([Links](https://bern.korea.ac.kr/))

    * model is trainable([github](https://github.com/dmis-lab/biobert-pytorch)) 

    * The training part of text classification have been finished. 

    * The shortage of this method is too rough, only have three label, BIO. 

    * It is free to use




3. usage of the IBM Annotator for clinical data

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


4. Deep research on the word embedding algrithoms, for example one-hot encoding, word2vec, Elmo, Bert, GPT. Understanding details of each model from the view of mathematics.

5. Research on the essentials of the Attention and Transformer.

6. Individual meeting with Prof Yang every week   

## what I will do next

continue go as we planned

