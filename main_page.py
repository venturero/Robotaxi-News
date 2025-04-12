import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from fetch_data import main

# Veriyi bir defa alıyoruz ve önbelleğe alıyoruz
@st.cache_data(ttl=600) 
def get_data():
    return main()

df = get_data()

# df'deki min ve max tarihleri alıyoruz
min_date = df['date'].min()
max_date = df['date'].max()

def show_filtered_news(start_date, end_date):
    # Tarihleri datetime formatına dönüştürme
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Yükleme göstergesi
    with st.spinner('Loading news...'):
        # Seçilen tarih aralığına göre verileri filtreleme
        df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
        
        # Kartlar şeklinde haberi gösterme
        for index, row in df_filtered.iterrows():
            st.markdown(f"### [{row['Title']}]({row['Link']})")
            st.write(f"**Source**: {row['Source']}")
            st.write(f"**Description**: {row['Description']}")
            st.write(f"**Date**: {row['date'].strftime('%Y-%m-%d')}")
            st.markdown("---")  # Kartlar arasına ayrım eklemek

# Streamlit UI kısmı
def main():
    st.title("AI News Dashboard")
    
    # Stil eklemek
    st.markdown(
        """
        <style>
        .css-1d391kg {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            color: #1a1a1a;
            text-align: center;
        }
        .css-1ofsbqf {
            background-color: #FF6347;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 20px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Tarih aralığı seçme (Start ve End aynı takvimde)
    st.subheader("Select Date Range")
    selected_dates = st.date_input(
        "Choose Date Range",
        value=(min_date, max_date),  # min ve max tarihleri df'den alıyoruz
        min_value=min_date, 
        max_value=max_date
    )

    # Eğer yalnızca bir tarih seçilmişse, start_date ve end_date'i aynı yap
    if len(selected_dates) == 1:
        start_date = selected_dates[0]
        end_date = selected_dates[0]
    else:
        start_date, end_date = selected_dates

    # Buton eklemek
    if st.button("Show News", key="show"):
        show_filtered_news(start_date, end_date)

if __name__ == '__main__':
    main()
