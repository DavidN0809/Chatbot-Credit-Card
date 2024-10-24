```bash
conda activate CC-Chatbot
tmux new -s papermill_session-pre
conda activate CC-Chatbot
papermill Pre-processing-Copy2.ipynb two-pre-output.ipynb
Ctrl + b, then d
```
papermill Pre-processing.ipynb pre-output.ipynb

```bash
conda activate CC-Chatbot
tmux new -s papermill_session-llama
conda activate CC-Chatbot
papermill llama.ipynb llama-output.ipynb
```

attach back later

```bash
tmux attach -t papermill_session-pre
exit
```

force kill

```bash
tmux kill-session -t papermill_session-pre
```