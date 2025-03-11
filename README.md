# Customer Database Management System

The **Customer Database Management System** is a web-based application designed to efficiently manage customer records, including personal details, purchase history, and interactions. It provides a structured way to organize and retrieve customer information securely.

## Features

- **User Authentication** – Secure login and registration system.
- **Customer Management** – Add, edit, delete, and view customer details.
- **Search & Filter** – Quickly find customers using advanced filters.
- **Data Security** – Protects sensitive customer information.
- **REST API Support** – Structured API endpoints for customer data.
- **Responsive Design** – Works seamlessly on desktop and mobile devices.

## Technologies Used

- **Backend:** Node.js, Express.js
- **Database:** MongoDB with Mongoose ORM
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** JWT (JSON Web Token) Authentication
- **Deployment:** Docker (optional), Heroku/AWS/GCP support

## Project Structure

```
Customer-Database-Management/
├── models/             # Database models
├── routes/             # API routes for CRUD operations
├── views/              # Frontend templates
├── public/             # Static assets (CSS, JS, images)
├── app.js              # Main server file
├── config/             # Configuration files (DB, authentication)
├── package.json        # Project dependencies
├── README.md           # Project documentation
```

## Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/HSk2703/Customer-Database-Management.git
cd Customer-Database-Management
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and configure the necessary environment variables:

```
PORT=5000
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
```

### 4. Start the Server

```bash
npm start
```

### 5. Access the Application

Open your browser and navigate to:

👉 [http://localhost:5000/](http://localhost:5000/)

## API Endpoints

| Method | Endpoint              | Description                     |
|--------|----------------------|---------------------------------|
| GET    | `/customers`         | Get all customers              |
| POST   | `/customers`         | Add a new customer             |
| GET    | `/customers/:id`     | Get details of a customer      |
| PUT    | `/customers/:id`     | Update customer details        |
| DELETE | `/customers/:id`     | Remove a customer from records |

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Commit your changes** with a clear message.
4. **Push your changes** to your forked repository.
5. **Submit a pull request** with details of your changes.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

