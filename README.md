# Chatbot-Credit-Card
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
