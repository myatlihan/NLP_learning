from collections import defaultdict, Counter

data = [
    # Articles + noun + verb structure
    [("the", "DET"), ("dog", "N"), ("eats", "V"), ("food", "N")],
    [("a", "DET"), ("cat", "N"), ("chases", "V"), ("mouse", "N")],
    [("the", "DET"), ("boy", "N"), ("likes", "V"), ("football", "N")],
    [("a", "DET"), ("girl", "N"), ("reads", "V"), ("book", "N")],

    # Adjectives included
    [("the", "DET"), ("big", "ADJ"), ("dog", "N"), ("runs", "V")],
    [("a", "DET"), ("small", "ADJ"), ("cat", "N"), ("eats", "V"), ("fish", "N")],
    [("the", "DET"), ("fast", "ADJ"), ("car", "N"), ("moves", "V")],

    # Prepositions (more realistic language)
    [("the", "DET"), ("dog", "N"), ("runs", "V"), ("in", "PREP"), ("park", "N")],
    [("a", "DET"), ("cat", "N"), ("sleeps", "V"), ("on", "PREP"), ("sofa", "N")],
    [("the", "DET"), ("bird", "N"), ("flies", "V"), ("in", "PREP"), ("sky", "N")],

    # More verb variety
    [("students", "N"), ("study", "V"), ("hard", "ADV")],
    [("teachers", "N"), ("teach", "V"), ("students", "N")],
    [("engineers", "N"), ("build", "V"), ("systems", "N")],

    # More complex sentences
    [("the", "DET"), ("smart", "ADJ"), ("student", "N"), ("solves", "V"), ("problem", "N")],
    [("a", "DET"), ("young", "ADJ"), ("engineer", "N"), ("designs", "V"), ("robot", "N")],
    [("the", "DET"), ("robot", "N"), ("works", "V"), ("autonomously", "ADV")],

    # Tech / ML context (senin alanına uygun)
    [("machine", "N"), ("learning", "N"), ("models", "N"), ("learn", "V"), ("data", "N")],
    [("deep", "ADJ"), ("learning", "N"), ("improves", "V"), ("accuracy", "N")],
    [("neural", "ADJ"), ("networks", "N"), ("extract", "V"), ("features", "N")],
    [("yolo", "N"), ("detects", "V"), ("objects", "N"), ("in", "PREP"), ("images", "N")],

    # More natural language flow
    [("the", "DET"), ("model", "N"), ("achieves", "V"), ("high", "ADJ"), ("accuracy", "N")],
    [("a", "DET"), ("dataset", "N"), ("contains", "V"), ("many", "ADJ"), ("samples", "N")],
]

import nltk
from nltk.tag import hmm
from nltk.corpus import brown
import tkinter as tk
from tkinter import ttk



trainer = hmm.HiddenMarkovModelTrainer()

#Kendi mini datasetimiz, bu datasetle modeli train edip kullanabiliriz fakat çok küçük bir dataset olduğundan ötürü iyi sonuç vermeyecektir. 
model1 = trainer.train(data)

#text olarak bahsi geçen hazır daatsetleri kullanmak için  downaload ediyoruz cihazımıza
nltk.download('brown')
nltk.download('universal_tagset')
sentences = brown.tagged_sents(tagset="universal")


#Datasetimiz %80 train, %20 test olacak şekilde split ediyoruz.
split_index = int(len(sentences) * 0.8)

train_data = sentences[:split_index]
test_data = sentences[split_index:]

#modeli tarin ediyoruz
model2 = trainer.train(train_data)


# FUNCTION
def tag_sentence():
    #GUI dan aldığımız text
    sentence = sentence_entry.get().strip()

    if not sentence:
        return

    tokens = sentence.lower().split()
    #predict tag
    tagged_sentence = model2.tag(tokens)

    result_box.delete("1.0", tk.END)

    result_box.insert(tk.END, "WORD\t\tTAG\n")
    result_box.insert(tk.END, "-" * 30 + "\n")

    for word, tag in tagged_sentence:
        result_box.insert(tk.END, f"{word:<15} {tag}\n")




# GUI
root = tk.Tk()
root.title("Hidden Markov Model POS Tagger")
root.geometry("700x500")

title_label = tk.Label(
    root,
    text="Hidden Markov Model POS Tagger",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

instruction_label = tk.Label(
    root,
    text="Bir cümle giriniz:"
)
instruction_label.pack()

sentence_entry = tk.Entry(
    root,
    width=60,
    font=("Arial", 12)
)
sentence_entry.pack(pady=10)

predict_button = tk.Button(
    root,
    text="Tag Sentence",
    command=tag_sentence,
    width=20
)
predict_button.pack(pady=10)

result_box = tk.Text(
    root,
    width=70,
    height=18,
    font=("Courier New", 11)
)
result_box.pack(pady=10)

root.mainloop()

#finalde accuracy hesabı yapıyor modelimiz için, 2-3 dakika sürebilir.
accuracy = model2.accuracy(test_data)
print("Accuracy:", accuracy)