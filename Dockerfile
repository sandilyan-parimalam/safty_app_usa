FROM python:3.11-slim

# Copy the application code and the virtual environment
COPY crime_report /opt/web/crime_report

# Set the working directory
WORKDIR /opt/web/crime_report

# Activate the virtual environment and install dependencies
RUN pip install -r requirements.txt

# Expose the necessary port
EXPOSE 8000

# Optional: Use RUN to list files for debugging (can be removed in the final version)
RUN find /opt

# Run the Django development server using the Python interpreter from the virtual environment
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
