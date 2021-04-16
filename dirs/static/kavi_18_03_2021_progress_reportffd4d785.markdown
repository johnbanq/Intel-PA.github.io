---
layout: page
title: kavi_18_03_2021_progress_report
permalink: /static/kavi/progress/kavi_18_03_2021_progress_report/
---

[**<-back**](/static/kavi/progress)  

# Progress report - Kavi

- Got a working demo of a Glow-TTS implementation running on the BU machine. Initially tried to train the model myself, but was unable to due to memory constraints. However, I used a pretrained model provided by the researchers to run the inference and confirm that the model generates sensible speech. 

- Found a medical speech dataset on Kaggle that could be helpful in our chatbot's domain. Consists of about 8 hours of audio of patients describing various ailments. Some clips are of poor quality and the dataset would need to be cleaned before use 

- Found a similar dataset which consists of doctors reading out clinical reports. Much shorter than previous (1h of audio), but cleaner and contains utterences that include medical jargon that would be sensible for our bot to learn


- MELD dataset - audio clips of spoken dialogue annotated with its text and also with the emotional state of the speaker. Emotions labelled are Anger, Disgust, Fear, Joy, Neutral, Sadness and Surprise. While most of these would not be desireable for a medical diagnostic application (with the exception of perhaps neutral or sadness), it might be more applicable later down the line when the Intel-PA becomes more general purpose. 

- Literature review in progress, exploring work done in current implementations of Text to Spectrogram models (Tacotron2, GlowTTS), vocoders(WaveGlow, melGAN) and End-to-End solutions(Wave-Tacotron)