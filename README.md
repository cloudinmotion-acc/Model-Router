# Model Router

A unified API gateway for routing requests to multiple LLM providers (OpenAI, Claude, Gemini) with a single endpoint.

## Features

- 🔄 **Multi-Provider Support**: OpenAI, Anthropic Claude, Google Gemini
- 🚀 **FastAPI**: Built on modern async Python framework
- 📊 **Token Usage Tracking**: Monitor input/output tokens for each request
- 🔌 **Easy Model Switching**: Route to any configured model via simple parameter
- 💾 **Conversation History**: Support for multi-turn conversations with state management

## Supported Models

### OpenAI
- `gpt-5-nano`

### Anthropic Claude
- `claude-3-5-sonnet-20241022`
- `claude-opus-4-1-20250805`
- `claude-3-haiku-20250307`

### Google Gemini
- `gemini-2.0-flash`
- `gemini-3-flash-preview`

## Quick Start

### 1. Setup Environment

```bash
# Clone/navigate to project
cd Model-Router

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or: .\venv\Scripts\activate  # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Set your API keys as environment variables:

```bash
export API_KEY=your_api_key_here
export ROUTER_CONFIG_PATH=$(pwd)/app/config/config.yaml
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

Access the interactive API docs at `http://localhost:8000/docs`

## API Usage

### Basic Request

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain AI in one sentence",
    "model": "gpt-5-nano",
    "parameters": {"temperature": 0.7}
  }'
```

### Response Format

```json
{
  "text": "AI is technology that enables computers to learn and perform human-like tasks.",
  "model": "gpt-4o",
  "usage": {
    "input_tokens": 8,
    "output_tokens": 15
  }
}
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | The input text/question |
| `model` | string | Yes | Model to use (defaults to config default) |
| `parameters` | object | Optional | Model-specific parameters (temperature, max_tokens, etc.) |
| `state` | object | Optional | Conversation history for multi-turn interactions |

### Examples

**Using Gemini:**
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain quantum computing",
    "model": "gemini-3-flash-preview",
    "parameters": {"temperature": 0.5}
  }'
```

## Configuration

Edit `app/config/config.yaml` to customize available models:

```yaml
default_model: gpt-5-nano
models:
  gpt-5-nano:
    provider: openai
  claude-3-5-sonnet-20241022:
    provider: claude
  gemini-3-flash-preview:
    provider: gemini
```

## Project Structure

```
Model-Router/
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── schemas.py              # Request/response schemas
│   ├── config/
│   │   ├── config.yaml         # Model configuration
│   │   └── loader.py           # Config loader
│   ├── api/
│   │   └── generate.py         # /generate endpoint
│   └── providers/
│       ├── base.py             # Base provider class
│       ├── openai.py           # OpenAI implementation
│       ├── claude.py           # Claude implementation
│       ├── gemini.py           # Gemini implementation
│       └── registry.py         # Provider registry
├── requirements.txt            # Python dependencies
└── README.md
```
