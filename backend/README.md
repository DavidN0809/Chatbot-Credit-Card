## Needed Commands to finetune and preprocess
### Using tmux and papermill to process new dataset
### Using tmux and papermill to process dataset
```bash
conda activate CC-Chatbot
tmux new -s papermill_session-pre
conda activate CC-Chatbot
papermill /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/Pre-processing-Dataset1.ipynb /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/outputs/Pre-processing-Dataset1.ipynb
```

### Using tmux and papermill to finetune llama
```bash
conda activate CC-Chatbot
tmux new -s papermill_session-llama
conda activate CC-Chatbot
papermill /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/llama-Copy3.ipynb /opt/notebooks/Chatbot-Credit-Card/backend/notebooks/outputs/llama-output.ipynb
```

## Activate Backend
```bash
conda activate CC-Chatbot
uvicorn backend.main:app --reload
```
### Attach back later
```bash
tmux attach -t papermill_session-llama
```

### force kill
```bash
tmux kill-session -t papermill_session-pre
```

## force kill all
```bash
tmux kill-server
```
