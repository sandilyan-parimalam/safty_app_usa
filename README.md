
# Safty App USA

**Safty App USA** is a Django-based web application designed to track and report crime data across various U.S. cities and states. The application fetches real-time data from different APIs and presents it in a user-friendly, filterable, and sortable table. It also includes features like time-based queries, location-specific reports, and plans for future integration with maps and notifications.

## Features

- **Dynamic Crime Reports**: Generate crime reports by selecting specific date and time ranges.
- **Multiple Locations**: Support for multiple U.S. locations (starting with New York).
- **Sortable and Filterable Data**: Users can sort and filter data by different columns.
- **Time Picker**: Date and time selection for precise crime data retrieval.
- **Responsive Design**: User-friendly design with sticky headers and filter rows.
- **Dockerized Deployment**: Easily deployable using Docker.

## Project Structure

- **`Dockerfile`**: Contains instructions to build a Docker image for the application.
- **`report_view`**: Handles the generation of crime reports based on user input.
- **`newyork.py`**: Module for handling New York-specific crime data.
- **`requirements.txt`**: Lists the Python dependencies needed to run the project.
- **`templates/reports/report.html`**: The main template for rendering the crime report page.
- **`static/`**: Contains CSS and JS files for the front-end.

## Installation

### Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sandilyan-parimalam/safty_app_usa.git
   cd safty_app_usa
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t safty_app_usa .
   ```

3. **Run the Docker Container**:
   ```bash
   docker run -d -p 8000:8000 safty_app_usa
   ```

### Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sandilyan-parimalam/safty_app_usa.git
   cd safty_app_usa
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Usage

1. **Navigate to** `http://localhost:8000/reports/`.
2. **Select Date and Time**: Use the date and time pickers to specify the range.
3. **Generate Report**: Click on the "Generate" button to retrieve the crime data.
4. **Filter and Sort**: Utilize the filter boxes and column headers to refine the displayed data.

## Planned Features

- **Location-Based Notifications: Receive real-time risk alerts tailored to your current location and time, providing timely warnings for various crime types in selected areas.
- **Interactive Maps**: Visual representation of crime data on maps.
- **Mobile App Integration**: Expanding accessibility through a mobile application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any changes you'd like to make.

## License

This project is licensed under the MIT License.

---

Developed by Sandilyan Parimalam
