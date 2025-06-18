# 🏠 House Listing API
A simple yet effective RESTful API built with Django and Django REST Framework (DRF) for managing house listings. This project includes user authentication and full CRUD operations for houses — ideal for real estate platforms, property management systems, or learning API development with Django.

## 🚀 Features
- User Authentication
- Register a new user
- Login and logout functionality
- House Listings
- Create a new house listing
- View all house listings
- View details of a single house
- Edit/update existing house data
- Delete a house listing

## 🧱 Built With
| Purpose   | Technology                    |
| --------- | ----------------------------- |
| Language  | Python                        |
| Framework | Django                        |
| API Layer | Django REST Framework         |
| Database  | SQLite (default, replaceable) |

## 🔧 API Endpoints Overview
| Method | Endpoint            | Description                     |
| ------ | ------------------- | ------------------------------- |
| POST   | `/api/register/`    | Register a new user             |
| POST   | `/api/login/`       | Login and receive token/session |
| POST   | `/api/logout/`      | Logout current user             |
| GET    | `/api/houses/`      | View all houses                 |
| POST   | `/api/houses/`      | Create a new house listing      |
| GET    | `/api/houses/<id>/` | View details of a house         |
| PUT    | `/api/houses/<id>/` | Update an existing listing      |
| DELETE | `/api/houses/<id>/` | Delete a house                  |

- You can test these endpoints using tools like Postman, curl, or httpie.

## 🧠 To-Do / Future Enhancements
- Add JWT or token-based authentication
- Add image upload support for house listings
- Implement pagination and filtering
- Role-based permissions (admin, agent, user)
- Integrate with frontend or mobile apps
