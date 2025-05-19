# Com-Scrum

## requirements
 - pip  22.0.2 
 - python  3.10.11 


## Install Dependencies
- Linux
```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip3 install -r requirements.txt
```

- Windows
```bash
  python -m venv .venv
  .\.venv\Scripts\activate
  pip install -r requirements.txt
```

## Run code

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```
