<<<<<<< HEAD
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
=======

# Latest Robotaxi News

This repository serves as a curated collection of the most recent and significant developments in artificial intelligence. The goal is to provide AI enthusiasts, researchers, students, and professionals with a centralized resource to stay updated on breakthroughs, research papers, product launches, and industry trends.

## 📚 Contents

This repository includes:
- News about major AI product releases
- Updates on AI industry trends
- Insights from AI conferences and events
- Resources for learning about new AI technologies
  

## 🎬 Demo

Watch our video demonstration to see the app in action:


https://github.com/user-attachments/assets/1db2065e-766a-47f5-b23a-56aad8938841


## ✨ Features

- **Modern Card-Based Interface**: News displayed in an elegant three-column grid layout
- **Responsive Design**: Works well on different screen sizes
- **RSS Feed Integration**: Automatically pulls content from top AI news sources
- **Smart Filtering**: Filter news by date range and source
- **Customizable View**: Select specific news sources or view all content
- **Real-time Updates**: Refresh data with a single click
- **Image Support**: Displays source images when available

## 🔄 Updates

This repository is updated regularly to ensure the content remains current and relevant. Check back frequently or watch the repository to be notified of new updates.

## 💻 Technical Details

- **Framework**: Built with Streamlit for rapid development and easy deployment
- **Data Sources**: Aggregates news from 12+ leading AI publications including:
  - Google DeepMind Blog
  - OpenAI News
  - MIT Technology Review
  - NVIDIA Blog
  - Microsoft Research
  - The Berkeley AI Research Blog
  - And more...
- **Automatic Content Processing**: Handles different date formats and content structures
- **Parallel Processing**: Uses concurrent fetching for faster data retrieval

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this repository:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Ensure all information is accurate and from reliable sources
- Include references or links to original sources
- Follow the existing formatting structure

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

If you have any questions or suggestions, feel free to:
- Open an issue in this repository
- Contact the repository owner (Buse Koseoglu) through GitHub

## ⭐ Star This Repository

If you find this repository useful, please consider giving it a star to help others discover it!

---

Created and maintained by [Buse Koseoglu](https://github.com/busekoseoglu)
>>>>>>> 8e640c3bc8bc9b57b2b196b1224cc7ee4069d4b2
