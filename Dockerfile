# Use Python as the base image
FROM python:3.9

# Copy your calculator program into the container
COPY cal2.py .

# Run your calculator when container starts
CMD ["python", "cal2.py"]
