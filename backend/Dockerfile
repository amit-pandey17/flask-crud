# Use the official Python image as the base
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install necessary system dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Copy the rest of the application code
COPY . .

# Define the default command to run the application
CMD ["flask", "run", "--debug"]