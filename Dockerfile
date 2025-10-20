FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files first (for better caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --no-dev --locked

ENV PATH="/app/.venv/bin:$PATH"

COPY src/ ./src/

ENTRYPOINT ["python", "-u", "-m", "src.backend"]
CMD ["--host", "0.0.0.0", "--port", "5001", "--workers", "2"]
