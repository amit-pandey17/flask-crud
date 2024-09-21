# Second-Round Interview – Systems Analyst

### ports
Flask: 5000

### project structure:
    ├──cmc-assignment/
        ├── backend/
            ├── app.py
            ├── Dockerfile
            ├── requirements.txt
        ├── View/
            ├── index.html
            ├── style.css
        ├── compose.yaml
        ├── .gitignore
        ├── README.md

## Hands-On Demonstration Overview

**Objective:**  
Build a small but meaningful feature or application component within a limited time frame.

**Duration:**  
60–90 minutes

**Technologies:**  
Use languages and tools relevant to the role (e.g., .NET C#, Java, SQL, REST APIs, HTML/CSS, etc.).

**Focus Areas:**  
- Code quality
- Problem-solving
- Data handling
- API usage

---

## Exercise: Build a Simple CRUD API with Data Validation

### Scenario

You are tasked with building a simple REST API for managing an entity (e.g., users, students, employees) using technologies of your choice such as .NET C#, .NET MVC, Java, Java Spring Boot, SQL, REST APIs, Node.js, HTML/CSS, etc.

### Key Components

#### 1. Create a Simple Application (UI)

- **Purpose:** Display, add, modify, and delete entities.
- **Requirements:**
  - A user-friendly interface to interact with the data.
  - Forms for creating and editing entities.
  - Tables or lists to display existing entities with options to edit or delete.

#### 2. Set Up a Simple REST API

- **Implement Basic CRUD Operations:**
  - **Create:** Add new entities.
  - **Read:** Retrieve existing entities.
  - **Update:** Modify existing entities.
  - **Delete:** Remove entities.

- **Entity Attributes:**
  - **ID:** Unique identifier.
  - **Name:** Non-empty string.
  - **Email:** Valid email address.
  - **Role:** Must be from a predefined set (e.g., Admin, Student, Employee, Guest).

#### 3. Data Validation

- **Email Validation:**
  - Ensure that only valid email addresses are accepted.
  
- **Name Validation:**
  - The name field must not be empty.
  
- **Role Validation:**
  - The role must be one of the predefined options (e.g., Admin, Student, Employee, Guest).

#### 4. Database or In-Memory Storage

- **Options:**
  - **In-Memory Data Store:** Use an in-memory list to simulate data persistence.
  - **Lightweight Database:** Utilize SQLite, MySQL, SQLExpress, etc., to persist data.

#### 5. Error Handling

- **Implement Meaningful Error Messages:**
  - Handle invalid inputs gracefully.
  - Provide clear messages for missing resources or failed operations.

---

### Additional Features (If Time Allows)

1. **Pagination**
   - Implement pagination for the GET endpoint to handle large datasets efficiently.

2. **Search Functionality**
   - Add the ability to filter users by name or role within the application.

3. **API Authentication**
   - Incorporate token-based authentication (e.g., JSON Web Token – JWT or OAuth) to secure the API endpoints​