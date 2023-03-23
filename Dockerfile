# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# PyDub dependencies
RUN apt-get -y update
RUN apt-get install -y ffmpeg

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade --trusted-host pypi.python.org pip
RUN pip install --upgrade --trusted-host pypi.python.org -r requirements.txt

# Set environment variables
ENV OPENAI_TOKEN=$OPENAI_TOKEN
ENV TELEGRAM_TOKEN=$TELEGRAM_TOKEN


# Run bot.py when the container launches
CMD ["python", "bot.py"]
