## Needed Commands to finetune and preprocess
### Using tmux and papermill to process new dataset

### Using tmux and papermill to finetune llama
```bash
conda activate CC-Chatbot
tmux new -s papermill_session-llama
conda activate CC-Chatbot
papermill ./notebooks/llama.ipynb ./notebooks/llama-output.ipynb
```

```bash
conda activate CC-Chatbot
tmux new -s papermill_session-pre
conda activate CC-Chatbot
papermill ./notebooks/Pre-processing-Copy2.ipynb ./notebooks/two-pre-output.ipynb
Ctrl + b, then d
```
### Process original dataset
```bash
papermill ./notebooks/Pre-processing.ipynb ./notebooks/pre-output.ipynb
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
