📚 AI Exam Question Predictor
An AI-powered application that analyzes multiple exam question papers and predicts the most frequently asked questions using Sentence Transformers and Cosine Similarity. Unlike traditional keyword matching, this project groups semantically similar questions to provide more accurate predictions.
---
🚀 Features
📄 Reads multiple PDF question papers
🔍 Extracts questions using Regular Expressions (Regex)
🔢 Supports different question formats such as `1.`, `1)`, `Q1.`, and `Q1)`
✂️ Removes question numbers from extracted questions
🧹 Normalizes extracted questions before semantic comparison
🧠 Converts questions into sentence embeddings using Sentence Transformers (`all-MiniLM-L6-v2`)
📊 Compares semantic similarity using Cosine Similarity
🗂️ Groups semantically similar questions
🔢 Counts the occurrences of similar questions
📈 Sorts questions based on their frequency
📋 Displays the most frequently asked questions
---
🛠️ Technologies Used
Python
Sentence Transformers (`all-MiniLM-L6-v2`)
PyTorch
PyPDF
NumPy
Regular Expressions (Regex)
---
📂 Project Structure
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
4. Remove question numbers from the extracted questions.
5. Normalize the questions by converting them to lowercase and removing unnecessary spaces and punctuation.
6. Generate sentence embeddings for every normalized question.
7. Compare embeddings using Cosine Similarity.
8. Group semantically similar questions.
9. Count occurrences and rank them by frequency.
---
🧹 Question Normalization
Before generating embeddings, extracted questions are normalized to make the text more consistent.
The current normalization process includes:
Converting questions to lowercase
Removing leading and trailing whitespace
Removing unnecessary punctuation
For example:
```text
"What is a Process?"

becomes...

"what is a process"
```
---
▶️ Installation
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
📌 Sample Output
```text
What is a Deadlock? Explain necessary conditions. -> 3
Explain CPU Scheduling algorithms. -> 3
What is Virtual Memory? -> 3
Explain Banker's Algorithm. -> 3
Explain the process management in Operating Systems. -> 2
Explain Paging and Segmentation. -> 2
Explain Process Synchronization. -> 2
What is a Semaphore? -> 2
```
---
## 🔮 Future Improvements

* Improve semantic grouping using clustering algorithms such as DBSCAN or Agglomerative Clustering
* Fine-tune similarity thresholds
* Add topic and syllabus module detection
* Add recency-based prediction scoring
* Add prediction confidence levels
* Add explanations for why a question was predicted
* Add model evaluation using Precision, Recall, F1-score, and Top-K accuracy
* Add RAG using syllabus, lecture notes, and study materials
* Integrate an LLM for explanations and study recommendations
* Add a Streamlit web interface
* Export results to CSV or Excel
* Support additional document formats such as DOCX and TXT
* Add OCR support for scanned PDFs
---
👨‍💻 Author
Arjun
This project was built to explore Natural Language Processing (NLP), semantic search, and AI-powered document analysis using modern embedding models.
