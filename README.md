# Wish List Project

## Overview

The Wish List Project is a simple, user-friendly application designed to help users manage their grocery shopping more efficiently. It allows for the creation of multiple shopping lists, enabling users to organize their shopping needs by store, type of product, or any other categorization they prefer. Users can add, remove, and update items in these lists at any time, making grocery shopping planning flexible and convenient.

## Features

- **Multiple Shopping Lists:** Create as many lists as you need for different purposes - groceries, hardware supplies, party planning, etc.
- **Manage Items:** Easily add new items to your lists, remove unnecessary ones, or update existing items as your needs change.
- **User-Friendly Interface:** A simple and intuitive interface ensures that managing your shopping lists is straightforward and hassle-free.
- **Real-Time Updates:** Changes to your lists are saved in real-time, so you never have to worry about losing track of your updates.

## Getting Started

To get started with the Wish List Project, follow these steps to set up both the backend and frontend environments.

### Setting Up the Backend

The backend of this project is built with Django. Follow these steps to set up the backend environment:

1. **Create a Python Virtual Environment:**
   - Navigate to the project directory in your terminal.
   - Create a virtual environment by running `python3 -m venv venv`.
2. **Activate the Virtual Environment:**
   - On Windows, use `venv\Scripts\activate`.
   - On Unix or MacOS, use `source venv/bin/activate`.
3. **Install Dependencies:**
   - Ensure you have the virtual environment activated.
   - Install the required dependencies by running `pip install -r requirements.txt`.
4. **Start the Django App:**
   - Initialize the Django app with `django-admin startproject myproject` (if you're setting up the project structure) or navigate to your project directory where `manage.py` is located if already set up.
   - Run the server using `python manage.py runserver`.

### Setting Up the Frontend

The frontend of this project uses React. Follow these steps to get the frontend running:

1. **Install Dependencies:**
   - Navigate to the frontend directory within the project.
   - Install the required npm packages by running `npm install`.
2. **Start the Frontend Application:**
   - Start the React app by running `npm start`.
   - Your default web browser should open automatically to the app running on `localhost:3000`.

## Running the Application

After setting up both the backend and frontend, you can use the application by navigating to `localhost:3000` in your web browser (for the frontend) and ensuring the backend server is running simultaneously to handle requests.
