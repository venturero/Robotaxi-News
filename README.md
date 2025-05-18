# Latest AI News Dashboard

A modern web application that displays the latest news about robotaxis and autonomous vehicles from various sources.

## Features

- Modern, responsive UI built with React and Material-UI
- Real-time news updates from multiple sources
- Filter news by date range and sources
- Beautiful card layout with images and descriptions
- Fast and efficient backend API built with FastAPI

## Project Structure

```
latest-ai-news/
├── frontend/           # React frontend application
│   ├── src/
│   │   ├── components/ # React components
│   │   ├── api.js      # API service
│   │   └── App.js      # Main application component
│   └── package.json    # Frontend dependencies
├── backend/           # FastAPI backend application
│   ├── app/
│   │   └── main.py    # Backend API implementation
│   └── requirements.txt # Backend dependencies
└── README.md          # This file
```

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```

The backend server will run on http://localhost:8000

### Frontend Setup

1. Install Node.js dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

The frontend application will run on http://localhost:3000

## Usage

1. Open your browser and navigate to http://localhost:3000
2. Use the filter panel on the left to:
   - Select date ranges
   - Filter by news sources
   - Reset filters
3. Click on news cards to read the full articles
4. The news feed will automatically update when filters are changed

## API Endpoints

- `GET /api/news` - Get news articles with optional filters
  - Query parameters:
    - `start_date`: Filter by start date (YYYY-MM-DD)
    - `end_date`: Filter by end date (YYYY-MM-DD)
    - `sources`: Filter by news sources (can be multiple)
- `GET /api/sources` - Get list of available news sources

## Contributing

Feel free to submit issues and enhancement requests!
