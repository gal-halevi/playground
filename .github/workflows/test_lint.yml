name: CI(test)
on:
  workflow_dispatch:
jobs:
  Lint:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/astral-sh/ruff:0.5.7
      volumes:
        - .:/io
    steps:
      - uses: actions/checkout@v4

      - name: Run Ruff
        continue-on-error: true
        run: ruff check --output-format=github .
