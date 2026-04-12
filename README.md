# 📝 Text Summarizer using Python

## 👨‍💻 Author

Dhruv Sharma

---

## 📌 Project Description

This project is a Text Summarizer built using Python and Natural Language Processing (NLP). It uses the TF-IDF (Term Frequency - Inverse Document Frequency) algorithm to extract important sentences from a given text and generate a concise summary.

---

## 🚀 Features

* Summarizes large text into shorter meaningful content
* Supports multiple input methods:

  * Manual text input
  * Text file (.txt)
  * PDF file (.pdf)
  * Wikipedia URL
* GUI-based interface using Tkinter
* Uses NLP libraries like SpaCy and NLTK

---

## 🧠 Algorithm Used

* TF-IDF (Term Frequency - Inverse Document Frequency)
* Extractive Summarization (selects important sentences)

---

## 🛠️ Technologies Used

* Python
* NLTK
* SpaCy
* BeautifulSoup
* PyPDF2
* Tkinter (for GUI)

---

## ▶️ How to Run

1. Install dependencies:

```
pip install nltk spacy beautifulsoup4 PyPDF2
python -m spacy download en_core_web_sm
```

2. Run CLI version:

```
python text_summarizer.py
```

3. Run GUI version:

```
python gui_summarizer.py
```

---

## 💡 Improvements Made

* Replaced threshold-based sentence selection with ranking using heapq
* Added dynamic summary length
* Developed GUI interface using Tkinter for better usability

---

## ⚠️ Limitations

* Uses extractive summarization (does not generate new sentences)
* Performance depends on input size

---

## 🎯 Conclusion

This project demonstrates how NLP techniques can be used to efficiently summarize large text data and improve readability.

---
