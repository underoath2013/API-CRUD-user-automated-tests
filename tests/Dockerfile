FROM python:3.11-alpine

WORKDIR /api-tests

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY /tests ./tests
COPY /schemas ./schemas
COPY basic_assertions.py .
COPY conftest.py .
COPY db.py .
COPY environment.py .
COPY fake_data.py .
COPY logger.py .
COPY my_requests.py .
COPY query.py .
COPY pytest.ini .

CMD ["pytest"]
