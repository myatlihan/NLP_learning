from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch
model_name = 'bert-base-uncased'

tokenizer = BertTokenizer.from_pretrained(model_name)

model = BertModel.from_pretrained(model_name)

documents = [
    'machine learning is a field of artificial intelligence',
    'natural language processing involves understating human language',
    'Artificial intelligence encopmasses machine learning and natural language',
    'Deep learning is a subset of machine learning ',
    'Data science combines statistics, data analysis and machine learning',
    'I like shopping'
]

query = 'Get information about natural language processing'


def get_embeddings(text):
    inputs = tokenizer(
        text,
        return_tensors='pt',
        truncation=True, 
        padding=True
    )
    with torch.no_grad():
        outputs = model(**inputs)

    last_hidden_state = outputs.last_hidden_state
    attention_mask = inputs['attention_mask']

    mask = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
    
    summed = torch.sum(last_hidden_state * mask, dim=1) 
    counts = torch.clamp(mask.sum(dim=1), min=1e-9)

    print(last_hidden_state.size())
    return (summed / counts).squeeze().cpu().numpy()

doc_embeddings = np.vstack([get_embeddings(doc) for doc in documents])
query_embedding = get_embeddings(query).reshape(1, -1)

similarities = cosine_similarity(doc_embeddings, query_embedding)

for i, score in enumerate(similarities[:, 0]):
    print(f"Document: {documents[i]}")
    print(f"Score: {score:.4f}\n")

best_index = similarities.argmax()

print("\nMost similar document:")
print(documents[best_index])
print("Score:", similarities.max())





