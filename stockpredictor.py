import yfinance as yf
import streamlit as st
import pandas as pd

tickerSymbol = 'GOOGL'

st.write(""" 
    # Simple Stock Price App

Shown are the stock closing price and volume of Google
""")


#get data on this ticket
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-10-20')
#Open High      Low Close         Volume    dividends    Stock Splits

st.write(""" 
    ## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write(""" 
    ## Volume Price
""")
st.line_chart(tickerDf.Volume)



"""
 to run the script, write streamlir run stockpredictor.py in terminal
"""