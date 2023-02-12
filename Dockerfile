FROM python:3.10-slim



# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update
# # RUN apt-get install -y libssl1.0.2 libasound2
# RUN apt-get install libssl1.0.2 libasound2

# Set work directory
WORKDIR /app

# Copy project
COPY app .
COPY requirements.txt .


# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run server
CMD ["streamlit", "run" , "app.py","--server.port","80"]