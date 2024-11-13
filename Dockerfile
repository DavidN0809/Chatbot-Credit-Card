# Backend
FROM python:3.9-slim as backend
WORKDIR /app
COPY ./backend/models ./models
COPY ./backend/main.py ./main.py
RUN pip install fastapi uvicorn transformers
RUN pip install fastapi uvicorn transformers torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Frontend
FROM nginx:alpine as frontend
COPY ./frontend/index.html /usr/share/nginx/html/index.html
EXPOSE 80

# Combine both in a multi-stage build
FROM backend
COPY --from=frontend /usr/share/nginx/html /usr/share/nginx/html
