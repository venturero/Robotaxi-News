import pandas as pd
from datetime import datetime, timedelta
from fetch_data import main
from PIL import Image
import base64
import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Optional
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI(title="Latest AI News API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create necessary directories
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Setup templates
templates = Jinja2Templates(directory="templates")

# Create a simple CSS file in static directory
with open("static/style.css", "w") as f:
    f.write("""
    .news-card {
        transition: transform 0.2s;
    }
    .news-card:hover {
        transform: translateY(-5px);
    }
    """)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Placeholder image path
PLACEHOLDER_IMAGE_PATH = "placeholder.jpeg"

# Convert image to base64 if file exists
if os.path.exists(PLACEHOLDER_IMAGE_PATH):
    img_base64 = get_base64_encoded_image(PLACEHOLDER_IMAGE_PATH)
    PLACEHOLDER_IMAGE = f"data:image/jpeg;base64,{img_base64}"
else:
    PLACEHOLDER_IMAGE = "https://img.freepik.com/free-vector/artificial-intelligence-ai-robot-server-room-digital-technology-banner_39422-794.jpg"

def get_data():
    """Fetch and return the latest news data"""
    return main()

def filter_news(df, start_date=None, end_date=None, selected_sources=None):
    """Filter news data based on date range and sources"""
    if start_date:
        start_date = pd.to_datetime(start_date)
        df = df[df['date'] >= start_date]
    
    if end_date:
        end_date = pd.to_datetime(end_date)
        df = df[df['date'] <= end_date]
    
    if selected_sources:
        # Convert selected_sources to list if it's a single string
        if isinstance(selected_sources, str):
            selected_sources = [selected_sources]
        # Filter by exact source match
        df = df[df['Source'].isin(selected_sources)]
    
    return df

def process_news_item(row):
    """Process a single news item and return formatted data"""
    image_url = PLACEHOLDER_IMAGE
    if pd.notna(row.get('Image')) and row.get('Image') is not None and row['Source'] != "deeplearning.ai":
        image_url = row['Image']
    
    return {
        'Title': row['Title'],
        'Description': row['Description'][:150] + "..." if len(row['Description']) > 150 else row['Description'],
        'Link': row['Link'],
        'Source': row['Source'],
        'date': row['date'].strftime('%Y-%m-%d'),
        'Image': image_url
    }

def get_news_data(start_date=None, end_date=None, selected_sources=None):
    """Main function to get filtered news data"""
    try:
        df = get_data()
        
        if df.empty:
            return []
        
        # Print debug information
        print(f"Filtering with sources: {selected_sources}")
        print(f"Available sources in data: {df['Source'].unique()}")
        
        df_filtered = filter_news(df, start_date, end_date, selected_sources)
        
        # Print debug information
        print(f"Number of articles after filtering: {len(df_filtered)}")
        
        if len(df_filtered) == 0:
            return []
        
        return [process_news_item(row) for _, row in df_filtered.iterrows()]
    
    except Exception as e:
        print(f"Error fetching news data: {str(e)}")
        return []

# API Models
class NewsItem(BaseModel):
    Title: str
    Description: str
    Link: str
    Source: str
    date: str
    Image: Optional[str] = None

# API Endpoints
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/news")
async def get_news(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    sources: Optional[str] = None
):
    """Get news articles with optional filters"""
    try:
        print(f"Received request with sources: {sources}")  # Debug print
        news_items = get_news_data(start_date, end_date, sources)
        return news_items
    except Exception as e:
        print(f"Error in get_news: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/sources")
async def get_sources():
    """Get list of available news sources"""
    try:
        df = get_data()
        sources = sorted(df['Source'].unique().tolist())
        return sources
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("\n🚀 Starting Latest AI News API server...")
    print("📝 API Documentation available at: http://localhost:8000/docs")
    print("🌐 Frontend available at: http://localhost:8000")
    print("🌐 API Endpoints:")
    print("   - http://localhost:8000/api/news")
    print("   - http://localhost:8000/api/sources")
    print("\nPress Ctrl+C to stop the server\n")
    uvicorn.run(app, host="0.0.0.0", port=8000) 


