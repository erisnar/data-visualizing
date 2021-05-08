FROM python:3.9.2

# Copy files to image
WORKDIR /usr/src/app
COPY . .

# Install modules
RUN pip3 install -r requirements.txt

CMD ["main.py"]
ENTRYPOINT ["python3"]