# DPR Assessment System (FastAPI + ML + NLP)

A modular, production-ready backend for analyzing Detailed Project Reports (DPRs) using NLP + Machine Learning. Built with **FastAPI**, **scikit-learn**, and **transformers**, designed to integrate cleanly with a **React** frontend.

---

## 🚀 Features

* PDF upload and text extraction
* NLP-driven DPR section analysis
* ML-based risk prediction
* Report generation (JSON + PDF)
* Database logging of submissions
* Modular architecture for easy scaling
* Fully typed API using Pydantic

---

## 📁 Project Structure

```
app/
  ml/
    train_model.py
    load_model.py
    feature_extractor.py
    risk_predictor.py
    model.pkl

  nlp/
    pdf_processor.py
    dpr_analyzer.py
    text_cleaner.py
    keyword_extractor.py

  routes/
    upload.py
    analyze.py
    predict.py
    history.py
    report.py

  services/
    pdf_service.py
    analysis_service.py
    prediction_service.py
    database_service.py
    report_service.py

  utils/
    file_utils.py
    logging_utils.py
    config.py

  main.py

tests/
```

---

## 🛠️ Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000/
```

Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔗 Core API Endpoints

### **Upload DPR PDF**

```
POST /upload/
```

Body: Multipart PDF file.

### **Analyze Content (NLP)**

```
POST /analyze/
```

Body: Extracted text.

### **Predict Project Risk (ML)**

```
POST /predict/
```

### **Get Past Reports**

```
GET /history/
```

### **Download Report**

```
GET /report/{id}
```

---

## 🔧 ML Pipeline

* Extract features using TF-IDF / embeddings
* Train model (Random Forest / Gradient Boosting)
* Normalize features and serialize model
* Store model in `app/ml/model.pkl`
* Load model in FastAPI for inference

---

## 📊 NLP Pipeline

* PDF → raw text
* Cleaning (regex, whitespace, noise)
* Keyword extraction
* Sentence embeddings (optional)
* Section scoring and tagging

---

## 📦 Database

SQLite (default) at:

```
dpr_analysis.db
```

Holds:

* Uploaded file metadata
* Summary
* ML predictions
* Generated reports

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

Tests live in:

```
tests/
```

---


---


---

## 📄 License

MIT

---

If you need more templates (CI/CD, Docker Compose, API examples, or full architecture diagrams), just ask.
