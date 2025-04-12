import feedparser
import pandas as pd
from datetime import datetime, timedelta
import ssl
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def fetch_feed(links):
    entries = {"Title": [], "Link": [], "Published": [], "Description": [], "Source": []}
    
    try:
        # Linklerin üzerinden geçilir
        for link, source in links.items():
            feed = feedparser.parse(link)
            
            # Feeddeki her bir girişi işler
            for entry in feed.entries:
                entries["Title"].append(entry.get("title", "No Title"))
                entries["Link"].append(entry.get("link", "No Link"))
                entries["Published"].append(entry.get("published", "No Date"))
                entries["Description"].append(entry.get("description", "No Description"))
                entries["Source"].append(source)
                
    except Exception as e:
        # Hata durumunda hata mesajını yazdır
        print(f"An error occurred: {e}")

    # DataFrame oluşturuluyor
    df = pd.DataFrame(entries)
    return df


def extract_and_clean_data(df):
    try:
        # Regex pattern for date extraction
        pattern = r'(\d{2} \w{3} \d{4})'

        # Apply regex to the 'Published' column and extract the date
        df['date'] = df['Published'].str.extract(pattern)

        # Convert the extracted date to datetime
        df['date'] = pd.to_datetime(df['date'], format='%d %b %Y')

        # Drop the original 'Published' column
        df.drop(columns=['Published'], inplace=True)

        # Get today's date and calculate the date 7 days ago
        today = datetime.now()
        seven_days_ago = today - timedelta(days=7)

        # Filter the rows within the last 7 days
        df_last_seven_days = df[(df['date'] >= seven_days_ago) & (df['date'] <= today)]

        # Sort by date in descending order
        df_last_seven_days.sort_values(by='date', ascending=False, inplace=True)

        # Function to clean HTML tags
        def clean_html(text):
            try:
                soup = BeautifulSoup(text, "html.parser")
                return soup.get_text()
            except Exception as e:
                print(f"Error cleaning HTML: {e}")
                return text

        # Apply the HTML cleaning function and shorten descriptions to 500 characters
        df_last_seven_days['Description'] = df_last_seven_days['Description'].apply(lambda x: clean_html(x)[:500])

        # Remove newline characters from the 'Description' column
        df_last_seven_days["Description"] = df_last_seven_days["Description"].str.replace("\n", "")

        return df_last_seven_days

    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
    

def main():
    # rss links
    links = {"https://bair.berkeley.edu/blog/feed.xml": "The Berkeley Artificial Intelligence Research Blog",
        "https://feeds.feedburner.com/nvidiablog": "NVDIA Blog",
        "https://www.microsoft.com/en-us/research/feed/": "Microsoft Research",
        "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml": "Science Daily",
        "https://research.facebook.com/feed/" : "META Research",
        "https://openai.com/news/rss.xml": "OpenAI News",
        "https://deepmind.google/blog/feed/basic/" : "Google DeepMind Blog",
    }

    df = fetch_feed(links)
    final_df = extract_and_clean_data(df)

    return final_df

if __name__ == "__main__":
    df = main()
    print(df.columns)
