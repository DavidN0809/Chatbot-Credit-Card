# Chatbot-Credit-Card
There is three major goals for this project and one goal if time permits. 
1. Augment a credit card approval dataset from [kaggle](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction) with reasoning for the approval or decline
2. Take that new dataset and finetune llama3 on it to provide the approval/decline and the reason.
3. Build an front end webui to prompt this finetuned model, that includes an API.
4. If time permits another goal is to containizer the front end and push the custom model to huggingface.

### Git repo layout
Currently there is no front end, there is a notebooks directory containing the notebooks for finetuning and preprocessing. There is two env.yml files, one for running in a windows conda environment and the linux-env.yml for running in a linux environment.
