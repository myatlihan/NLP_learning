from nltk import ngrams, word_tokenize
from collections import Counter
import re

raw_text = """
Machine learning models learn patterns from data.
Convolutional networks extract features from images.
YOLO performs real-time object detection in drones.
N-gram models predict the next word in a sequence.
Overfitting reduces model generalization performance.
Docker ensures reproducible machine learning environments.
Gradient descent minimizes loss during training.
"""



tokens = word_tokenize(raw_text.lower())

bigrams = list(ngrams(tokens, 2))

trigrams = list(ngrams(tokens, 3))

bigram_counts = Counter(bigrams)
trigram_counts = Counter(trigrams)


print("TOP BIGRAMS:")
for item, freq in bigram_counts.most_common(5):
    print(item, "->", freq)

print("\nTOP TRIGRAMS:")
for item, freq in trigram_counts.most_common(5):
    print(item, "->", freq)