# Model Router

## Getting-Started

### Step-1

Create a virtual environment

```bash
python -m venv venv
# Activate venv
source venv/Scripts/activate # For Linux
# For Windows
.\venv\Scripts\activate
```

### Step-2

Install the dependencies

```bash
pip install -r requirements.txt
```

### Setp-3

Edit the config path
<!-- Create a `.env` file and copy the contents from `.env.example` and replace with your keys -->
```bash
export OPENAI_API_KEY=xxx
export ROUTER_CONFIG_PATH=$(pwd)/config/config.yaml
```

### Step-4

Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

### Step-5

Test the server from the terminal

```sh
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Say hello like a pirate",
    "model": "gpt-4o"
  }'
```


```bash
sudo docker tag model-router:latest infraraja18/main-proj-acc:v0.1
sudo docker push infraraja18/main-proj-acc:v0.1
```
