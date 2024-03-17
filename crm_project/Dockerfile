FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./crm_project

WORKDIR /crm_project
CMD ["uvicorn", "crm_project.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
