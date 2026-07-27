# 📚 AI Exam Question Predictor

An AI-powered application that analyzes multiple exam question papers and predicts the most frequently asked questions using **Sentence Transformers** and **Cosine Similarity**. Unlike traditional keyword matching, this project groups semantically similar questions to provide more accurate predictions.

---

## 🚀 Features

* 📄 Reads multiple PDF question papers
* 🔍 Extracts questions using Regular Expressions (Regex)
* 🧠 Converts questions into sentence embeddings using Sentence Transformers
* 📊 Compares semantic similarity with Cosine Similarity
* 📈 Groups similar questions and counts their occurrences
* 📋 Displays the most frequently asked questions

---

## 🛠️ Technologies Used

* Python
* Sentence Transformers (`all-MiniLM-L6-v2`)
* PyTorch
* PyPDF
* Regular Expressions (Regex)

---

## 📂 Project Structure

```text
EXAM_QUESTION_PREDICTOR/
│
├── papers/
│   ├── 2017.pdf
│   ├── 2018.pdf
│   └── 2019.pdf
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. Load all PDF question papers.
2. Extract text from every page.
3. Identify exam questions using Regex.
4. Generate sentence embeddings for every question.
5. Compare embeddings using Cosine Similarity.
6. Group semantically similar questions.
7. Count occurrences and rank them by frequency.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/ar-j-un-404/EXAM_QUESTION_PREDICTOR.git
```

Move into the project folder:

```bash
cd EXAM_QUESTION_PREDICTOR
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 📌 Sample Output

```text
What is a Deadlock? Explain necessary conditions. -> 3
Explain CPU Scheduling algorithms. -> 3
What is Virtual Memory? -> 3
Explain Banker’s Algorithm. -> 3
Explain the process management in Operating Systems. -> 2
Explain Paging and Segmentation. -> 2
Explain Process Synchronization. -> 2
What is a Semaphore? -> 2
```

---

## 🔮 Future Improvements

* Improve semantic grouping with a best-match strategy
* Fine-tune similarity thresholds
* Add a Streamlit web interface
* Export results to CSV or Excel
* Support additional document formats

---

## 👨‍💻 Author

**Arjun**

This project was built to explore Natural Language Processing (NLP), semantic search, and AI-powered document analysis using modern embedding models.
