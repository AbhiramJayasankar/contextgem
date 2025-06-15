# ContextGem

A modular pipeline for retrieving, processing, extracting, mapping, and storing lube oil lab report data from PDFs to MongoDB, with support for multiple lab schemas.

---

## Directory Structure & Components

```
contextgem/
│
├── main.py
├── data_retrieval.py
├── pdf_to_img.py
├── extraction_and_jsonification.py
├── final_output_and_push.py
├── fieldmappings.py
├── requirements.txt
├── .env
├── .gitignore
│
├── extract_functions/
│   ├── extract.py
│   ├── json_merge.py
│   └── __init__.py
│
├── jsonobjectconept_schemas/
│   └── ... (lab-specific schema definitions)
│
├── pdfs/
│   └── ... (downloaded and sorted PDFs, lab-wise)
│
├── images/
│   └── ... (images generated from PDFs, lab-wise)
│
├── extracted_jsons/
│   └── ... (raw extracted JSONs from images, lab-wise)
│
├── final_output/
│   └── ... (final mapped JSONs, lab-wise)
│
├── venv/
│   └── ... (your Python virtual environment)
│
└── README.md
```

---

## File & Folder Explanations

### **main.py**
- The entry point for the pipeline.
- Accepts IMO numbers as arguments.
- Runs the full process: data retrieval → PDF-to-image conversion → extraction and JSONification.

### **data_retrieval.py**
- Connects to MongoDB to fetch report links for given IMO numbers.
- Downloads PDFs and sorts them into the `pdfs/` folder by lab.
- Uses `.env` for MongoDB URI.

### **pdf_to_img.py**
- Converts all PDFs in `pdfs/` to images (one per page).
- Saves images in the `images/` folder, preserving lab-wise structure.

### **extraction_and_jsonification.py**
- Processes all images in `images/`.
- Extracts structured data using lab-specific extraction logic.
- Saves raw extracted JSONs in `extracted_jsons/`.

### **final_output_and_push.py**
- Maps each extracted JSON to a unified schema using `fieldmappings.py`.
- Saves mapped JSONs in `final_output/` (lab-wise).
- Pushes mapped outputs to MongoDB.
- Uses `.env` for MongoDB URI.

### **fieldmappings.py**
- Contains mapping dictionaries for each lab, defining how to transform extracted data into the unified schema.

### **extract_functions/**
- **extract.py**: Contains image processing and extraction logic for each lab.
- **json_merge.py**: Utilities for merging JSONs (e.g., multi-page reports).
- **__init__.py**: Package initializer.

### **jsonobjectconept_schemas/**
- Contains schema definitions and concept files for each lab, used during extraction.

### **pdfs/**
- Stores downloaded PDFs, organized by lab.

### **images/**
- Stores images generated from PDFs, organized by lab.

### **extracted_jsons/**
- Stores raw extracted JSONs, organized by lab.

### **final_output/**
- Stores final mapped JSONs, organized by lab.

### **venv/**
- Your Python virtual environment (not tracked by git).

### **requirements.txt**
- Lists all Python dependencies for the project.

### **.env**
- Stores environment variables (e.g., `MONGO_URI`).  
  **Example:**
  ```
  MONGO_URI=mongodb://<username>:<password>@<host>:<port>/<database>
  ```

### **.gitignore**
- Specifies files/folders to be ignored by git (e.g., `venv/`, `.env`, etc).

---

## Setup Instructions

1. **Clone the repository and navigate to the `contextgem` directory.**

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**
   ```
   MONGO_URI=mongodb://<username>:<password>@<host>:<port>/<database>

   GOOGLE_API_KEY=<API_KEY>
   ```

---

## Usage

### **Run the full pipeline:**
```bash
python main.py <IMO_NUMBER_1> <IMO_NUMBER_2> ...
```
- Downloads and sorts PDFs, converts to images, extracts and saves JSONs.

### **Map and push final outputs:**
```bash
python final_output_and_push.py
```
- Maps extracted JSONs to the unified schema, saves to `final_output/`, and pushes to MongoDB.

---

## Notes

- All scripts assume you are running them from the `contextgem` directory.
- Make sure your `.env` file is present and correct.
- The pipeline is modular; you can run each step independently if needed.
