# Tuckr Backend 🍔

The Tuckr backend is built with FastAPI, providing a robust and efficient API for the Tuckr food ordering app. It handles order creation, food item management, and user input validation. With support for asynchronous operations, the backend ensures high performance and quick response times. It securely stores order data and integrates seamlessly with the React frontend, delivering a smooth experience from browsing food items to completing orders. This backend is optimized for scalability and reliability, making it a powerful foundation for the Tuckr app.

<img alt="Project Frontend Preview" src="./preview.jpg"/>

Frontend for Tuckr has been developed in React 19. [Tucker Frontend](https://github.com/ummamali/tuckr)

## API Routes 📡

The Tuckr backend provides the following RESTful API endpoints:

### 📋 Food Items

- `GET /fooditems`  
  Retrieve the list of available food items.

### 🛒 Orders (Full CRUD)

- `GET /orders`  
  Retrieve all orders.

- `GET /orders/{id}`  
  Retrieve a specific order by ID.

- `POST /orders`  
  Create a new order.

- `PUT /orders/{id}`  
  Update an existing order by ID.

- `DELETE /orders/{id}`  
  Delete an order by ID.

### 👥 Users

- `GET /users`  
  Retrieve a list of users (for reference or admin use).


## Features ⚙️

- **Order Management**  
  Create, retrieve, and manage food orders through RESTful API endpoints.

- **Data Validation with Pydantic**  
  Utilize Pydantic models for robust data validation and serialization, ensuring data integrity and type safety.

- **Static File Handling**  
  Serve static files, such as food item images, efficiently using FastAPI's `StaticFiles` integration.

- **Asynchronous Support**  
  Leverage FastAPI's asynchronous capabilities for high-performance, non-blocking operations.

- **Interactive API Documentation**  
  Access auto-generated, interactive API documentation via Swagger UI and ReDoc for seamless integration and testing.

## Technologies 🛠️

- **Python 3.11+**  
  The backend is built with Python, leveraging its modern features and libraries for efficient development.

- **FastAPI**  
  A fast, modern Python web framework for building APIs with automatic validation, interactive documentation, and high performance.

- **Pydantic**  
  Used for data validation and settings management, ensuring type safety and accurate data handling.

- **JSON**  
  FastAPI uses JSON for request and response payloads, facilitating smooth communication between the frontend and backend.

- **CORS (Cross-Origin Resource Sharing)**  
  Configured to handle requests from different domains securely, enabling frontend-backend communication.

- **Typing**  
  Python's typing library is used for type hints, improving code clarity, and ensuring better development practices.

### Data Storage 💾

The Tuckr backend stores order data in a flat-file JSON database. A dedicated class handles the CRUD operations, providing methods for creating, reading, updating, and deleting orders. This simple, yet effective, approach ensures easy data persistence without the need for a full-fledged relational database, while maintaining fast read/write performance for small-scale applications.

### Route Builder 🛣️

The Tuckr backend includes a dynamic route builder that simplifies API development. By providing a database manager (in this case, a flat-file JSON database), the route builder automatically generates four major RESTful routes: `GET`, `POST`, `PUT`, and `DELETE`. This eliminates the need to manually define common CRUD operations, speeding up development and reducing boilerplate code. The generated routes enable seamless interaction with the database for managing orders and food items with minimal configuration.

### Server-Level Validation Using Pydantic ✅

Tuckr leverages Pydantic to perform server-level validation on incoming request objects for `POST` and `PUT` requests. This ensures that all incoming data adheres to the expected schema and type constraints before being processed. With Pydantic, invalid data is automatically rejected, reducing the likelihood of errors and ensuring the integrity of the application's data. This built-in validation provides a robust and secure way to manage user input, improving the overall reliability and safety of the backend.

## Installation 🚀

Follow these steps to set up and run the Tuckr backend locally:


### 1. Clone the repository

```bash
git clone https://github.com/ummamali/tuckrbck.git
cd tuckrbck
```
### 2. Create and activate a virtual environment

Linux/MacOS
```bash
python -m venv venv
source venv/bin/activate 
```

Windows
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the development server

```bash
fastapi dev main.py
```

## License 📄

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).



