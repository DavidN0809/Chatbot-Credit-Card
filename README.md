# Chatbot-Credit-Card
The goal of this project augment a credit card approval dataset from [kaggle](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction) with reasoning for the approval or decline. The next goal take that new dataset and finetune llama3 on it to provide the approval/decline and the reason. The final goal is to build an front end webui/cli to prompt this model with an API.

## Needed Commands
## Using tmux and papermill to process new dataset
```bash
conda activate CC-Chatbot
tmux new -s papermill_session-pre
conda activate CC-Chatbot
papermill Pre-processing-Copy2.ipynb two-pre-output.ipynb
Ctrl + b, then d
```
## Process original dataset
```bash
papermill Pre-processing.ipynb pre-output.ipynb
```

## Using tmux and papermill to finetune llama
```bash
conda activate CC-Chatbot
tmux new -s papermill_session-llama
conda activate CC-Chatbot
papermill llama.ipynb llama-output.ipynb
```

## Attach back later
```bash
tmux attach -t papermill_session-pre
exit
```

## force kill
```bash
tmux kill-session -t papermill_session-pre
```

## force kill all
```bash
tmux kill-server
```
