# Daily Workflow

## Open Project

```bash
cd ~/Desktop/AI-Powered-Predictive-Maintenance-System
```

## Activate Virtual Environment

```bash
source predictive/bin/activate
```

## Verify Python

```bash
python --version
```

## Run Backend

```bash
uvicorn backend.main:app --reload
```

## If You Updated Dependencies

```bash
python -m pip install -r backend/requirements.txt
```

## Stop Working

```bash
deactivate
```