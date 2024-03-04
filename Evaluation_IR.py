import numpy as np
from collections import OrderedDict

class Evaluation_IR:
    def __init__(self):
        self.ks = ks
        self.max_k = max(self.ks)

    def evaluate(self, model, dataset, mode = 'valid'):
        if mode == 'valid':
            eval_mat = 
            eval_id = 
            qid2pid = 
            doc_id = 
        elif mode == 'test':
            eval_mat = 
            eval_id = 
            qid2pid = 
            doc_id = 

        score_dict = OrderDict()
        topns = self.ks
        # make predictions and compute scores

        close_docs_topk = 


def closest_docs(query, model, method, mode):
    doc_length = 8841823
    query_length = query_vectors.shape[0]
    topk = 1000 
    topk_docs = np.zeros((query_length, topk), dtype=np.int32)

    if method == 'dot':
        document_output = model.get_sparse_output(mode)
    
    return topk_docs

def precision_at_k(actual, predicted, k):
    return precision
    
def recall_at_k(actual, predicted, k):
    return recall

def ap_at_k(actual, predicted, k):
    ap = sum(precision_at_i) / min(len(actual), k)
    return ap

def mrr(actual, predicted):
    return mrr
        
        

  
