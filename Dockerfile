FROM python:3.11
RUN mkdir /usr/src/app/
COPY ./api/ /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]