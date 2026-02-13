# My Awesome FastAPI Project

A simple and blazing fast API built with [FastAPI](https://fastapi.tiangolo.com/) that says "Hello World".

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   [Python 3.9+](https://www.python.org)
*   [`pip`](https://pypi.org) (Python package manager)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/msoumik78/testcicdpipeline
    cd testcicdpipeline
    ```

2.  **Create and activate a virtual environment** (optional, but recommended):
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the API locally

Run the application using [`uvicorn`](https://uvicorn.dev/):
```bash
uvicorn app.main:app
```
