FROM python:3.10
WORKDIR task2/
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENTRYPOINT ["python", "main.py"]