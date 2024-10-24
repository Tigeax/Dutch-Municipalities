# Dutch Municipalities

This project provides a CRUD REST API for managing data on Dutch municipalities. It includes a web server built with Django and a data loader script for populating the database with data from a .geojson file.

## Project Structure

The project consists of two main components:

- **Web Server**: A Django application that serves the CRUD REST API.
- **Data Loader**: A script to post the geo json data to the API.

## Prerequisites

Make sure you have the following installed on your machine:

- Docker
- Docker Compose
- Curl

## Installation

### 1. Clone the Repository

Clone the repository to your local machine and navigate into the project directory:

```bash
git clone https://github.com/Tigeax/Dutch-Municipalities
cd /Dutch-Municipalities/
```

### 2. Run the Webserver

Navigate to the `/webserver/` directory and launch the web server using Docker Compose:

```bash
cd /webserver/
docker compose up --build
```

### 3. Populate the Database

Open another terminal window, navigate to the `/data_loader/` directory, and run the data loader script:

```bash
cd /data_loader/
docker compose up --build
```

## Accessing the API

You can access the API by navigating to http://localhost/api/municipality/ in your web browser.

Below are examples of how to perform each CRUD operation using Curl.

### CREATE

```bash
curl -X POST http://localhost/api/municipality/ -H "Content-Type: application/json" -d "{\"name\": \"New Municipality\", \"geometry\": \"MULTIPOLYGON (((30 10, 40 40, 20 40, 10 20, 30 10)))\"}"
```

### READ

Replace <municipality_id> with the actual ID.

```bash
curl -X GET http://localhost/api/municipality/<municipality_id>/
```

### UPDATE

Replace <municipality_id> with the actual ID.

```bash
curl -X PATCH http://localhost/api/municipality/<municipality_id>/ -H "Content-Type: application/json" -d "{\"name\": \"Renamed Municipality\"}"
```

### DELETE

Replace <municipality_id> with the actual ID.

```bash
curl -X DELETE http://localhost/api/municipality/<municipality_id>/
```

## Filtering by Bounding Box

You can filter municipalities by specifying a bounding box. For example, to retrieve municipalities located within Friesland, navigate to:

http://localhost/api/municipality/?in_bbox=6.34,52.76,6.28,53.53

Or use the following Curl command:

```bash
curl -X GET http://localhost/api/municipality/?in_bbox=5.34,52.76,6.28,53.53
```
