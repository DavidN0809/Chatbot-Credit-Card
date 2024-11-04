## Needed Commands to finetune and preprocess
### Using tmux and papermill to process new dataset
### Using tmux and papermill to process dataset
```bash
conda activate CC-Chatbot
tmux new -s papermill_session-pre
conda activate CC-Chatbot
papermill /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/Pre-processing-Dataset1.ipynb /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/outputs/Pre-processing-Dataset1.ipynb
Ctrl + b, then d
```

### Using tmux and papermill to finetune llama
```bash
conda activate CC-Chatbot
tmux new -s papermill_session-llama
conda activate CC-Chatbot
papermill /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/llama.ipynb /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/outputs/llama-output.ipynb
```

### Attach back later
```bash
tmux attach -t papermill_session-pre
exit
```

### force kill
```bash
tmux kill-session -t papermill_session-pre
```

## force kill all
```bash
tmux kill-server
```