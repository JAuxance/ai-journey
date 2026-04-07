FROM python:3.11-slim

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive
# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1
# Expose project root to Python imports
ENV PYTHONPATH=/workspace

WORKDIR /workspace

# Build tools needed by some Python packages (e.g. numpy wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt jupyterlab

# Copy the full project
COPY . .

EXPOSE 8888

# Default: start JupyterLab (no token/password for local dev)
CMD ["jupyter", "lab", \
     "--ip=0.0.0.0", \
     "--port=8888", \
     "--no-browser", \
     "--allow-root", \
     "--NotebookApp.token=", \
     "--NotebookApp.password="]
