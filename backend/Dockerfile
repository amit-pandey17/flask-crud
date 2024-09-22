# Use the official Python image as the base
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Set environment variables for Flask
# Adjusted for the full module path
ENV FLASK_APP=backend.app  
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH=/code

# Install necessary system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5002

# Copy the rest of the application code
COPY . .

# Define the default command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]