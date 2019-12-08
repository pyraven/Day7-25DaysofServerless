FROM python:3.5

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod 444 app.py
RUN chmod 444 requirements.txt

ENV PORT 8080

CMD [ "python", "app.py" ]