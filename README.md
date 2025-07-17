# 🎬 Movie Recommender System

A content-based movie recommender system built using **Scikit-Learn**, **Pandas**, and **NLP techniques**, with an interactive frontend developed using **Streamlit**.

This project recommends movies based on textual similarity using information like genres, cast, director, and keywords. It processes and cleans data from the TMDB 5000 dataset and delivers real-time recommendations via a user-friendly web app.

---

## 📌 Features

- ✅ Content-based filtering using movie metadata (overview, cast, crew, genres, keywords)
- ✅ Vectorization and similarity scoring using CountVectorizer and Cosine Similarity
- ✅ Cleaned and merged TMDB datasets
- ✅ Pickled preprocessed data for performance
- ✅ Streamlit web interface for user interaction
- ✅ Modular, readable, and beginner-friendly codebase

---

## 🗂️ Project Structure
📁 Movie Recommender system/
│
├── movie-recommender-system.ipynb # Jupyter notebook for model building
├── movies.pkl # Pickled DataFrame of processed movies
├── movies_dict.pkl # Pickled dictionary used in recommendation
├── tmdb_5000_movies.csv # Raw dataset containing movie info
├── tmdb_5000_credits.csv # Raw dataset containing cast and crew
├── Movie Recommender system/ # Contains Streamlit app files
│
├── .ipynb_checkpoints/ # Auto-generated notebook backup
├── .virtual_documents/ # Internal files by editor
└── README.md # Project documentation

---

## 🚀 How to Run the Project

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

### 🧪 2. Install Dependencies

Make sure Python is installed (preferably 3.8 or above). Then install the required packages:

```bash
pip install -r requirements.txt
```

### 💻 3. Launch the Web App

```bash
streamlit run "Movie Recommender system/your_streamlit_file.py"
```

## 📊 Dataset
--> Name: TMDB 5000 Movie Dataset

--> Source: Kaggle - TMDB Dataset

## 🛠️ Libraries and Tools Used

--> pandas

--> numpy

--> scikit-learn

--> nltk

--> pickle

--> streamlit
