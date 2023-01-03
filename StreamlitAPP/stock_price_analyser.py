import pandas as pd
import streamlit as st
import yfinance as yf
import datetime
import pickle

st.write(
        """"
        # Stock Price Indicator

        Shown are the price of Apple.
        """
)

ticker_symbol=st.text_input("Enter Stock Symbol",
                            "AAPL",
                            key="placeholder")

col1,col2=st.columns(2)

#start date of analysis
with col1:
    start_date=st.date_input("Input Start date",
                datetime.date(2019,1,1)

    )
#end date of analysis
with col2:
    end_date=st.date_input("Input End date",
                datetime.date(2022,12,31)

    )
ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",
                                start=start_date,
                                end=end_date)

st.dataframe(ticker_df)

st.write("""

Daily Closing Price

""")
st.line_chart(ticker_df.Volume)

st.write("""

Daily Trading Volume

""")
st.line_chart(ticker_df.Close)