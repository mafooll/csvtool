FROM python:3.13-slim

RUN pip install uv

WORKDIR /csvtool

COPY pyproject.toml uv.lock ./

RUN uv sync

ENV PATH="/csvtool/.venv/bin:$PATH"
ENV PYTHONPATH="/csvtool"
