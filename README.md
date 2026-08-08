---# 📚 AI Exam Question Predictor

An AI-powered application that analyzes multiple exam question papers and predicts the most frequently asked questions using **Sentence Transformers** and **Cosine Similarity**.

Unlike traditional keyword matching, this project identifies **semantically similar questions**, allowing different wordings of the same question to be grouped together and ranked based on their frequency.

---

# 🚀 Features

* 📄 Reads multiple PDF question papers
* 🔍 Extracts questions using Regular Expressions (Regex)
* 🔢 Supports multiple question formats:

  * `1.`
  * `1)`
  * `Q1.`
  * `Q1)`
* ✂️ Removes question numbers from extracted questions
* 🧹 Normalizes questions before semantic comparison
* 🧠 Generates sentence embeddings using `all-MiniLM-L6-v2`
* 📊 Calculates semantic similarity using Cosine Similarity
* 🗂️ Groups semantically similar questions
* 🔢 Counts occurrences of similar questions
* 📈 Ranks questions based on frequency
* 📋 Displays the most frequently asked questions

---

# 🛠️ Technologies Used

| Technology            | Purpose                                 |
| --------------------- | --------------------------------------- |
| Python                | Core programming language               |
| Sentence Transformers | Generate sentence embeddings            |
| `all-MiniLM-L6-v2`    | Pre-trained embedding model             |
| PyTorch               | Deep learning backend                   |
| PyPDF                 | Extract text from PDF files             |
| NumPy                 | Numerical operations                    |
| Regex                 | Question extraction and text processing |

---

# 📂 Project Structure

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

# ⚙️ How It Works

The application follows a simple NLP-based pipeline:

```text
PDF Question Papers
        ↓
Text Extraction
        ↓
Question Extraction using Regex
        ↓
Remove Question Numbers
        ↓
Question Normalization
        ↓
Sentence Embeddings
        ↓
Cosine Similarity
        ↓
Semantic Question Grouping
        ↓
Frequency Counting
        ↓
Question Ranking
        ↓
Most Frequently Asked Questions
```

### 1. Load Question Papers

The application reads all PDF files placed inside the `papers/` directory.

### 2. Extract Text

Text is extracted from every page using **PyPDF**.

### 3. Extract Questions

Regular Expressions are used to identify questions with different numbering formats such as:

```text
1. What is a process?
2) Explain CPU scheduling.
Q3. What is deadlock?
Q4) Explain virtual memory.
```

### 4. Remove Question Numbers

Question numbers are removed before further processing.

For example:

```text
Q1. What is a Process?
```

becomes:

```text
What is a Process?
```

### 5. Normalize Questions

The extracted questions are normalized to make comparison more consistent.

The current normalization process includes:

* Converting text to lowercase
* Removing leading and trailing whitespace
* Removing unnecessary punctuation
* Removing extra spaces

Example:

```text
"What is a Process?"
```

becomes:

```text
"what is a process"
```

### 6. Generate Sentence Embeddings

Each normalized question is converted into a numerical vector using the **Sentence Transformer** model:

```text
all-MiniLM-L6-v2
```

This allows the application to understand the semantic meaning of questions rather than simply comparing individual words.

### 7. Calculate Semantic Similarity

The generated embeddings are compared using **Cosine Similarity**.

For example:

```text
"What is a process?"

"Define process in operating system."
```

Although the wording is different, the questions have a similar meaning and can therefore be grouped together.

### 8. Group Similar Questions

Questions with similarity above the selected threshold are placed into the same semantic group.

### 9. Count and Rank Questions

The number of occurrences of each semantic group is calculated.

The groups are then sorted from **most frequently asked to least frequently asked**.

---

# 🧹 Question Normalization

Normalization is performed before generating embeddings so that unnecessary differences in formatting do not affect the comparison.

### Example

**Original question:**

```text
Q1. What is a Process?
```

**After removing question number:**

```text
What is a Process?
```

**After normalization:**

```text
what is a process
```

---

# 📊 Semantic Question Grouping

Traditional keyword matching may fail when two questions use different wording.

For example:

```text
What is a deadlock?
```

and

```text
Explain the concept of deadlock in an operating system.
```

Keyword-based comparison may consider them different questions.

Using sentence embeddings and Cosine Similarity, the application can identify that they are **semantically related** and group them together.

---

# 📌 Sample Output

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

The number on the right represents how many times that question, or a semantically similar version of it, appeared across the provided question papers.

---

# ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/ar-j-un-404/EXAM_QUESTION_PREDICTOR.git
```

### Navigate to the Project

```bash
cd EXAM_QUESTION_PREDICTOR
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Question Papers

Place your PDF question papers inside:

```text
papers/
```

Example:

```text
papers/
├── 2017.pdf
├── 2018.pdf
├── 2019.pdf
└── 2020.pdf
```

### Run the Application

```bash
python app.py
```

---

# 🔮 Future Improvements

### Semantic Analysis

* Improve semantic grouping using clustering algorithms such as **DBSCAN** or **Agglomerative Clustering**
* Fine-tune similarity thresholds
* Improve handling of differently worded questions

### Exam Prediction

* Add topic and syllabus module detection
* Add recency-based prediction scoring
* Add prediction confidence levels
* Identify important and repeated topics
* Provide explanations for why a question was predicted

### Model Evaluation

* Add **Precision**
* Add **Recall**
* Add **F1-score**
* Add **Top-K Accuracy**
* Evaluate prediction performance on historical question papers

### RAG Integration

* Add **RAG (Retrieval-Augmented Generation)**
* Use syllabus documents as additional context
* Use lecture notes and study materials
* Retrieve relevant study material for predicted questions

### LLM Integration

* Integrate an LLM for question explanations
* Generate study recommendations
* Generate topic summaries
* Provide personalized preparation suggestions

### User Interface

* Add a **Streamlit web interface**
* Allow users to upload question papers directly
* Display predicted questions interactively
* Show similarity groups and frequency statistics

### Export and Document Support

* Export predictions to **CSV**
* Export results to **Excel**
* Support additional document formats:

  * DOCX
  * TXT
* Add OCR support for scanned PDF question papers

---

# 👨‍💻 Author

**Arjun**

This project was built to explore **Natural Language Processing (NLP)**, **semantic search**, **sentence embeddings**, and **AI-powered document analysis** using modern embedding models.

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
