# Use a base image that supports ARM64 architecture
FROM arm64v8/python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy everything in the current directory into the container
COPY . .

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Run create_index.py to create the index
RUN python create_index.py

# Expose the Streamlit port
EXPOSE 8501

# Copy the Streamlit app script into the container
COPY app.py .

# Specify the command to run Streamlit app
CMD ["streamlit", "run", "app.py"]