# FINTRACK - A multi product finance tracking API
## Overview
A Flask python api that retrives image(only 1 for now) of receipt from firebase storage, and performs OCR text extraction on it to  extract item(product) name which is then categorised to find which macro category it belongs to.

## How to use
1. Keep the files -  main.py, fireabase_config.py, SVC_model.pkl in the same folder. 
2. Upload a scanned image of your receipt with a dark(not necessarily black, any dark color works good) backgroud on all 4 sides. Also, make sure the text in receipt is readable.
3. Download the seviceAccount.json file from your firebase console.
4. Fill the configuration details in firebase_config.py. 
5. Run main.py using 
```
python3 main.py
# or
python main.py
```
## Contribute to data

## API

### A third-level heading
