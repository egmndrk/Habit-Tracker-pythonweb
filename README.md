# Habit Tracker

A minimalist web application built with Flask and MongoDB that helps users track their daily habits. The application features a clean, responsive design with a 7-day view and simple habit completion tracking.

## Features

- Add new daily habits
- Mark habits as completed
- 7-day rolling calendar view
- Responsive design that adapts to different screen sizes
- Clean and modern UI with smooth interactions
- Persistent storage using MongoDB
- Mobile-friendly interface

## Technologies Used

- **Backend:**
  - Flask
  - MongoDB
  - Python
  - PyMongo

- **Frontend:**
  - HTML5
  - CSS3
  - Jinja2 Templates
  - Inter Font (Google Fonts)
  - SVG icons for completion status

## Prerequisites

Before running this project, make sure you have:
- Python 3.x
- MongoDB
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/egmndrk/Habit-Tracker-pythonweb.git
cd habit-tracker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your MongoDB URI:
```
MONGODB_URI=your_mongodb_connection_string
```

## Running the Application

1. Ensure MongoDB is running on your system

2. Start the Flask application:
```bash
flask run
```

3. Open your web browser and navigate to `http://localhost:5000`

## Project Structure

```
habit-tracker/
│
├── static/
│   └── css/
│       └── main.css
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── add_habit.html
│
├── app.py
├── routes.py
├── requirements.txt
└── .env
```

## Usage

1. Click the "+ Add new" button to create a new habit
2. Enter your habit in the text area and click "Add"
3. View your habits for different days using the date navigation
4. Click on a habit to mark it as complete
5. Completed habits are marked with a checkmark icon

## Author

Egemen Doruk

## Acknowledgments

- Flask documentation
- MongoDB documentation
- Python community
