FROM python:3.9-alpine

COPY . /app
WORKDIR /app

# Update pip
RUN pip install --upgrade pip

# Install dependencies

RUN pip3 install -r requirement.txt

CMD ["python", "app.py"]
