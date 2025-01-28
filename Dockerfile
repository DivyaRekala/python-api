# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY app/ /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Command to run the Gunicorn server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
