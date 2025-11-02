# BookVault: Your Digital Library

A mini full-stack web application to manage a personal book collection. It allows users to add, view, and delete books with a clean, modern 3D-style UI featuring a background image and smooth interactions.

---

## Features

- Display a list of registered books with ID, Title, Author, and Price
- Add new books using a user-friendly form
- Delete existing books by clicking a trash can icon button
- Responsive and visually appealing glassmorphism-inspired UI
- Backend built with Flask and SQLite for storage
- Frontend built with HTML, CSS, and JavaScript (vanilla)

---

## Prerequisites

- Python 3.x installed
- `pip` package manager available

---

## Setup Instructions

### 1. Clone or Download the Project

Place the project files (`app.py`, `index.html`) in a folder on your computer.

### 2. Install Backend Dependencies

Open a terminal or PowerShell in the project folder and run:


### 3. Run the Backend Server

Start the Flask server by running:


The server will start on `http://localhost:5000`.

### 4. Open the Frontend

Open `index.html` in your web browser by double-clicking it or right-clicking and choosing **Open with** your browser.

---

## Usage

- The homepage shows the list of books stored in the backend.
- Use the **Add a New Book** form to input book details and submit.
- The new book will appear instantly in the list.
- Click the **trash can icon** next to a book to delete it (confirmation required).
- The table and form are responsive and work well on desktop and mobile.

---

## Project Structure

- `app.py`: Flask backend API with endpoints for retrieving, adding, and deleting books.
- `books.db`: SQLite database file generated automatically to store books.
- `index.html`: Frontend UI file with JavaScript logic to interact with backend API.

---


