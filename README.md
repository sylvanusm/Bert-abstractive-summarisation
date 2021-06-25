## Master Project

This repository is inspired from https://github.com/nayeon7lee/bert-summarization implementation of the Paper: https://arxiv.org/pdf/1902.09243.pdf

### Preparing package/dataset
0. Run: `pip install -r requirements.txt` to install required packages
1. In the root folder run `python download_data.py` to download a preprocessed verssion of CNN//DailyMail
2. Run python `utils/data.py` to prepare the data for the model

### model training
To train the model you can run for example:. 
`CUDA_VISIBLE_DEVICES=3 python main.py --cuda --batch_size=2 --hop 4 --hidden_dim 100`
or `python main.py --batch_size=2 --hop 4 --hidden_dim 100` if you want to run on cpu
batch_size, hop and hidden_dim can be change as well as all the hyper-parameters located in `utils/config.py`

to fine-tune `bert-large-uncased` based model, one can run for example
`python main.py --batch_size=1 --hop 4 --hidden_dim 100 --model_name bert-large-uncased --emb_dim 1024 --heads 16`