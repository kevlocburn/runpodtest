FROM nvidia/cuda:11.8.0-base

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy project files
COPY app/ .

# Install Python requirements
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python3", "api.py"]
