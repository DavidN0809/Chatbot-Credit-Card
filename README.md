# Chatbot-Credit-Card
There is three major goals for this project and one goal if time permits. 
1. Augment a credit card approval dataset from [kaggle](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction) with reasoning for the approval or decline
2. Take that new dataset and finetune llama3 on it to provide the approval/decline and the reason.
3. Build an front end webui to prompt this finetuned model, that includes an API.
4. If time permits another goal is to containizer the front end and push the custom model to huggingface.

## How to use
1. git clone https://github.com/DavidN0809/Chatbot-Credit-Card.git
2. cd Chatbot-Credit-Card
3. ```conda activate CC-Chatbot && cd backend```
4. ```uvicorn main:app --host 0.0.0.0 --port 8000```
5. test backend ```curl -X POST http://0.0.0.0:8000/generate/ -H "Content-Type: application/json" -d '{"prompt": "Test prompt"}'```
6. ```cd frontend```
7. ```python -m http.server 8080```

frontend
http://192.168.68.63:8080/
fast api
http://192.168.68.63:7888/docs


### Git repo layout
Currently there is no front end, there is a notebooks directory containing the notebooks for finetuning and preprocessing. There is two env.yml files, one for running in a windows conda environment and the linux-env.yml for running in a linux environment.
