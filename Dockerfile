FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["btcvalues.py"]
