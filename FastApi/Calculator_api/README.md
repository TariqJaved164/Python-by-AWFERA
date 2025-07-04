# Simple Calculator API

## Overview
A lightweight API using FastAPI to perform basic arithmetic operations with input as query parameters.

## Endpoints
- `/calculator/add?x=10&y=20`
- `/calculator/subtract?x=10&y=5`
- `/calculator/multiply?x=10&y=2`
- `/calculator/divide?x=10&y=0` (error if `y=0`)

## Installation
```bash
pip install -r requirements.txt
