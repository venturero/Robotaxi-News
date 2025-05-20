# Latest Robotaxi-News Dashboard

A modern web application that displays the latest news about robotaxis and autonomous vehicles from various sources.

![image](https://github.com/user-attachments/assets/84be51f8-5088-4b40-b145-6392102badb0)


## Features

- Modern, responsive UI built with React and Material-UI
- Real-time news updates from multiple sources
- Filter news by date range and sources
- Beautiful card layout with images and descriptions
- Fast and efficient backend API built with FastAPI

## Project Structure

```
latest-ai-news/
├── main_page.py              # Main FastAPI application file
├── fetch_data.py            # Data fetching and processing module
├── requirements.txt         # Python dependencies
├── placeholder.jpeg         # Default image for news articles
├── templates/              # HTML templates directory
│   └── index.html         # Main webpage template
├── static/                # Static files directory
│   └── style.css         # CSS styles
├── notebooks/            # Jupyter notebooks directory
└── README.md            # Project documentation
```

## Setup Instructions
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
- News about major RoboTaxi product releases
- Updates on RoboTaxi industry trends
- Insights from RoboTaxi conferences and events
- Resources for learning about new RoboTaxi technologies

## ✨ Features

- **Modern Card-Based Interface**: News displayed in an elegant three-column grid layout
- **Responsive Design**: Works well on different screen sizes
- **RSS Feed Integration**: Automatically pulls content from top Robotaxi news sources
- **Smart Filtering**: Filter news by date range and source
- **Customizable View**: Select specific news sources or view all content
- **Real-time Updates**: Refresh data with a single click
- **Image Support**: Displays source images when available

## 🔄 Updates

This repository is updated regularly to ensure the content remains current and relevant. Check back frequently or watch the repository to be notified of new updates.

## 💻 Technical Details

- **Framework**: Built with FastAPI and React
- **Data Sources**: Aggregates news from 4 leading Robotaxi publications including:
  - Cars Arstechnica
  - Tech Crunch Waymo
  - deeplearning.ai
  - The Last Driver License Holder
- **Automatic Content Processing**: Handles different date formats and content structures
- **Parallel Processing**: Uses concurrent fetching for faster data retrieval

## 🤝 Contributing

Contributions are welcome! Please feel free to [submit](https://github.com/venturero/Robotaxi-News/pulls) a Pull Request.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

If you have any questions or suggestions, feel free to:
- Open an issue in this repository
- Contact with me on [Linkedin]([url](https://www.linkedin.com/in/semi/)). 

## ⭐ Star This Repository

If you find this repository useful, please consider giving it a star to help others discover it!

---

Created by [Buse Koseoglu](https://github.com/busekoseoglu/) and updated by [Semi Venturero](https://github.com/busekoseoglu/).
