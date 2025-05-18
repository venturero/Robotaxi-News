<<<<<<< HEAD
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
=======
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from fetch_data import main
from PIL import Image
import base64
import os

# Yerel placeholder görüntüyü yüklemek için fonksiyon
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Placeholder görüntü yolu - kendi dosya yolunuzu buraya yazın
PLACEHOLDER_IMAGE_PATH = "placeholder.jpeg"  # Bu dosyanın Python kodunuzla aynı dizinde olduğunu varsayıyorum

# Görüntüyü base64 formatına dönüştür (eğer dosya mevcutsa)
if os.path.exists(PLACEHOLDER_IMAGE_PATH):
    img_base64 = get_base64_encoded_image(PLACEHOLDER_IMAGE_PATH)
    PLACEHOLDER_IMAGE = f"data:image/jpeg;base64,{img_base64}"
else:
    # Dosya bulunamazsa yedek olarak online bir görsel kullan
    PLACEHOLDER_IMAGE = "https://img.freepik.com/free-vector/artificial-intelligence-ai-robot-server-room-digital-technology-banner_39422-794.jpg"
    st.warning(f"Placeholder image not found at {PLACEHOLDER_IMAGE_PATH}. Using fallback image.")

all_sources = ["The Last Driver License Holder","Tech Crunch Waymo","Wired: Waymo","Cars Arstechnica"]


# Use Streamlit's built-in caching
@st.cache_data(ttl=60)  # Cache for 1 minute
def get_data():
    with st.spinner('Fetching latest Robotaxi news...'):
        return main()

def run_dashboard():
    st.title("Latest Robotaxi News")
    
    # Add sidebar for all filters
    with st.sidebar:
        st.header("Filter Options")
        
        # Add a refresh button at the top of sidebar
        if st.button("Refresh News"):
            # Clear the cache and get fresh data
            st.cache_data.clear()
            st.rerun()
    
    # Load data with caching
    try:
        df = get_data()
        
        # Check if df is empty
        if df.empty:
            st.error("No news data available. Please try refreshing later.")
            return
            
        # Get min and max dates
        min_date = df['date'].min()
        max_date = df['date'].max()
        
        # Calculate default date range (last 7 days)
        default_end_date = max_date
        default_start_date = default_end_date - timedelta(days=7)
        if default_start_date < min_date:
            default_start_date = min_date
        
        # Continue with sidebar for filters
        with st.sidebar:
            # Date filter
            selected_dates = st.date_input(
                "Choose dates",
                value=(default_start_date, default_end_date),
                min_value=min_date,
                max_value=max_date
            )
            
            # Handle single date selection
            if len(selected_dates) == 1:
                start_date = selected_dates[0]
                end_date = selected_dates[0]
            else:
                start_date, end_date = selected_dates
            
            
            # Get unique sources from predefined list
            sources = sorted(all_sources)
            
            # Use multiselect without "All" option
            selected_sources = st.multiselect(
                "Choose sources",
                options=sources
            )
            
        
        # Main content area for displaying news
        # Convert dates to datetime
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        # Filter by date range
        df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
        
        # Handle source filtering
        if selected_sources:  # If sources are selected
            # Filter by selected sources
            df_filtered = df_filtered[df_filtered['Source'].isin(selected_sources)]
            print(df_filtered)
            print(selected_sources)
        # If no sources selected, show all (no additional filtering needed)
        
        # Display results
        if len(df_filtered) > 0:
            
            # Apply CSS styling for cards
            st.markdown("""
            <style>
            .news-card {
                border-radius: 20px;
                padding: 0;
                margin-bottom: 20px;
                background-color: #E8E8E8;
                height: 480px;
                overflow: hidden;
                position: relative;
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            }
            .news-image-container {
                width: 100%;
                height: 220px;
                overflow: hidden;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 10px 10px 0 10px;
            }
            .news-image {
                width: 100%;
                height: 100%;
                object-fit: cover;
                border-radius: 12px;
            }
            .news-content {
                padding: 12px 15px;
            }
            .news-title {
                font-weight: bold;
                font-size: 16px;
                margin-bottom: 10px;
                color: #000;
                line-height: 1.3;
                max-height: 105px;
                display: -webkit-box;
                -webkit-line-clamp: 4;
                -webkit-box-orient: vertical;
                overflow: hidden;
            }
            .news-meta {
                display: flex;
                justify-content: space-between;
                margin-bottom: 12px;
                align-items: center;
                border-bottom: 1px solid #ddd;
                padding-bottom: 8px;
            }
            .news-source {
                color: #555;
                font-size: 12px;
                font-style: italic;
            }
            .news-date {
                color: #555;
                font-size: 12px;
                text-align: right;
                font-style: italic;
            }
            .news-description {
                color: #333;
                font-size: 13px;
                padding-bottom: 10px;
                line-height: 1.4;
                display: -webkit-box;
                -webkit-line-clamp: 5;
                -webkit-box-orient: vertical;
                overflow: hidden;
                height: 90px;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Create 3-column layout
            num_cols = 3
            
            # Process news items in groups of 3 for the grid
            for i in range(0, len(df_filtered), num_cols):
                cols = st.columns(num_cols)
                
                # Get the current batch of news items
                current_batch = df_filtered.iloc[i:i+num_cols]
                
                # Display each news item in its column
                for j, (_, row) in enumerate(current_batch.iterrows()):
                    if j < len(cols):  # Ensure we have a column for this item
                        with cols[j]:
                            # Eğer kaynak deeplearning.ai ise veya geçerli bir görüntü yoksa, placeholder kullan
                            if row['Source'] == "deeplearning.ai" or not pd.notna(row.get('Image')) or row.get('Image') is None:
                                image_url = PLACEHOLDER_IMAGE
                            else:
                                image_url = row['Image']
                            
                            # Format the date
                            date_str = row['date'].strftime('%d %b %Y')
                            
                            # Truncate description if it's too long
                            description = row['Description'][:150] + "..." if len(row['Description']) > 150 else row['Description']
                            
                            # Display card with HTML
                            html_content = f"""
                            <a href="{row['Link']}" target="_blank" style="text-decoration: none; color: inherit;">
                                <div class="news-card">
                                    <div class="news-image-container">
                                        <img src="{image_url}" class="news-image" onerror="this.onerror=null;this.src='{PLACEHOLDER_IMAGE}';">
                                    </div>
                                    <div class="news-content">
                                        <div class="news-title">{row['Title']}</div>
                                        <div class="news-meta">
                                            <div class="news-source">{row['Source']}</div>
                                            <div class="news-date">{date_str}</div>
                                        </div>
                                        <div class="news-description">{description}</div>
                                    </div>
                                </div>
                            </a>
                            """
                            st.markdown(html_content, unsafe_allow_html=True)
        else:
            st.warning("No news found with the selected filters. Please adjust your date range or source selection.")
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Try refreshing the data using the button above.")

if __name__ == '__main__':
    run_dashboard()
>>>>>>> 8e640c3bc8bc9b57b2b196b1224cc7ee4069d4b2
