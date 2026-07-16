# Installation

## Clone the Repository

```bash
git clone https://github.com/galibhub/AI-Powered-Predictive-Maintenance-System.git
cd AI-Powered-Predictive-Maintenance-System
```

## Install uv

**macOS**

```bash
brew install uv
```

**Windows**

```powershell
winget install --id=astral-sh.uv -e
```

**Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup Environment

```bash
uv python install 3.12

uv venv predictive --python 3.12
```

### Activate

**macOS / Linux**

```bash
source predictive/bin/activate
```

**Windows**

```powershell
predictive\Scripts\Activate.ps1
```

## Install Dependencies

```bash
python -m pip install -r backend/requirements.txt
```

## Run the Application

```bash
uvicorn backend.main:app --reload
```

Open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
