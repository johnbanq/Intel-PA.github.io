---
layout: page
title: kavi_31_03_2021_progress_report
permalink: /static/kavi/progress/kavi_31_03_2021_progress_report/
---

[**<-back**](/static/kavi/progress)  

# Progress report - 31/03/2021 - Kavi

--Got set up with access to a University Linux account in order to try training the Glow-TTS model - installed Anaconda + created the necessary environment and built the project. Unfortunately ran into a problem with pytorch - it is not able to find any CUDA devices on the machine. I checked to be sure and it definitely has an NVIDIA card (8GB VRAM), so I don't know where the problem lies.  

--Investigating the efficacy of audio data augmentation as applied to Text To Speech applications - I think this will be useful in the future when trying to train using audio datasets pertaining to medical speech, which are usually much smaller (Kaggle Medical Speech Dataset ~6k utterances) than more widely used "general" speech datasets (LJSpeech ~13k utterances).

-- Implemented two audio augmentation policies from the paper "Mel-spectrogram augmentation for sequence-to-sequence voice conversion", and applied them to the training, validation, and testing datasets of the Glow-TTS project, doubling them in size.

## What I'll do next:

--Figure out why the pytorch install on my Uni desktop can't seem to communicate with the graphics card. I've encountered this problem once on my personal machine, and a reboot fixed the problem. Though I'm not sure how feasible this is to do on an enterprise server that needs to stay up constantly. 

--Modify the Glow-TTS training/validation script to use the augmented datasets and compare some stats between this and the unaugmented training - does the error converge to an acceptable value faster or slower? No difference?

--Think of a different kind of augmentation policy altogether, and implement it. Current publications transform mel-spectrograms in simple linear ways (e.g. masking frequencies, stretching timescales, adding noise etc). Might be worth trying something more complicated (though I don't know at this stage what that might be) and checking error metrics similar to above.