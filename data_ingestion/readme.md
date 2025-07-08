# Crude Oil Imports CSV Uploader

This is a Python script that reads a CSV file containing crude oil import records, normalizes the data, and uploads each record to a FastAPI backend using POST requests.

## Features

- Accepts a CSV file as input via command-line argument
- Cleans the `origin_name` field (strips whitespace, converts to lowercase)
- Sends data to the FastAPI `/imports` endpoint
- Handles duplicates and displays relevant messages

---

## Requirements

- Python 3.8+
- Required Python packages:

```bash
pip install pandas requests
```

## Run Script
```bash
python .\ingest_data.py --csv_file data1.csv
```
