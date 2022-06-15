# Use base Python image from Docker Hub
FROM public.ecr.aws/lambda/python:3.9 AS base

# Set the working directory
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy the requirements file used for dependencies
COPY requirements.txt  .

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

ENTRYPOINT ["python", "main.py"]
