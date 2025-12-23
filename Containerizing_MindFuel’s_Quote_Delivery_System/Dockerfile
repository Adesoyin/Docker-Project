# Base Image
FROM python:3.12.3-slim-bookworm

# Working directory:signifies the main directory where all files are gotten from
WORKDIR /app

# Copying requirements file to working directory
COPY requirements.txt ./
COPY includes ./

# Installing dependencies from requirements file
RUN pip install -r requirements.txt

# ENV DB_HOST="" \
#     DB_PORT="5432" \
#     DB_NAME="" \
#     DB_USER=""

# Copying all files from current directory to working directory in the container
COPY . .

# Load environment variables at runtime
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "main.py"]




# This File conatins a layer of instructions to be followed up for creation of image and running of container in docker.





