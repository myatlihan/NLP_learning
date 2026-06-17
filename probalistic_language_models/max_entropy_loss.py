from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression


data = [
    # POSITIVE
    ("i love this movie", "positive"),
    ("this is amazing", "positive"),
    ("great product very useful", "positive"),
    ("i am happy with this", "positive"),
    ("excellent experience", "positive"),
    ("really good quality", "positive"),

    # NEGATIVE
    ("i hate this", "negative"),
    ("this is terrible", "negative"),
    ("worst product ever", "negative"),
    ("i am very sad", "negative"),
    ("bad experience", "negative"),
    ("not good at all", "negative"),
]


def features(text):

    words = text.lower().split()

    return {
        "contains_love": "love" in words,
        "contains_like": "like" in words,
        "contains_great": "great" in words,
        "contains_good": "good" in words,
        "contains_amazing": "amazing" in words,
        "contains_happy": "happy" in words,
        "contains_excellent": "excellent" in words,

        "contains_bad": "bad" in words,
        "contains_hate": "hate" in words,
        "contains_terrible": "terrible" in words,
        "contains_worst": "worst" in words,
        "contains_sad": "sad" in words,
        "contains_not": "not" in words,
    }




X = []
y = []

for text, label in data:
    X.append(features(text))
    y.append(label)


vec = DictVectorizer(sparse=True)
X_vec = vec.fit_transform(X)




model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)


def predict(text):

    x = vec.transform([features(text)])

    pred = model.predict(x)[0]
    prob = model.predict_proba(x)[0]

    return {
        "prediction": pred,
        "confidence": max(prob)
    }

print(predict("this movie is amazing"))
print(predict("this is the worst experience"))