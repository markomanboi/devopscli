FROM python:3.8

ADD main.py .
 
RUN pip3 install --no-cache-dir awscli

RUN chmod +x main.py

ENTRYPOINT ["python", "./main.py"]
