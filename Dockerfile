FROM python:3.10
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python","manage.py","runserver","0.0.0.0:8000"]