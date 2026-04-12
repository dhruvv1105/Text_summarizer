import tkinter as tk
from tkinter import scrolledtext
import heapq
import spacy

nlp = spacy.load('en_core_web_sm')

def summarize_text():
    text = input_text.get("1.0", tk.END)
    
    doc = nlp(text)
    sentences = list(doc.sents)

    word_freq = {}
    for word in doc:
        if word.text.lower() not in nlp.Defaults.stop_words and word.text.isalnum():
            word_freq[word.text] = word_freq.get(word.text, 0) + 1

    sentence_scores = {}
    for sent in sentences:
        for word in sent:
            if word.text in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word.text]

    summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)
    summary = " ".join([sent.text for sent in summary_sentences])

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)


# UI
root = tk.Tk()
root.title("Text Summarizer")
root.geometry("700x500")

tk.Label(root, text="Enter Text:", font=("Arial", 14)).pack()

input_text = scrolledtext.ScrolledText(root, height=10)
input_text.pack()

tk.Button(root, text="Summarize", command=summarize_text).pack(pady=10)

tk.Label(root, text="Summary:", font=("Arial", 14)).pack()

output_text = scrolledtext.ScrolledText(root, height=10)
output_text.pack()

root.mainloop()