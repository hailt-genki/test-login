#!/bin/bash
uvicorn --host=0.0.0.0 --port=3000 app.main:app
