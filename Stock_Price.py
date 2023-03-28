# Commit test1

import yfinance as yf
import pandas as pd

company1 = input("Enter the ticker symbol of the first company: ")
company2 = input("Enter the ticker symbol of the second company: ")
start_date = input("Enter the start date (yyyy-mm-dd): ")
end_date = input("Enter the end date (yyyy-mm-dd): ")

df1 = yf.download(company1.upper(), start=start_date, end=end_date)
df2 = yf.download(company2.upper(), start=start_date, end=end_date)

returns1 = df1["Adj Close"].pct_change().groupby(pd.Grouper(freq='Y')).sum().dropna()
returns2 = df2["Adj Close"].pct_change().groupby(pd.Grouper(freq='Y')).sum().dropna()

returns = pd.DataFrame({"Year": returns1.index.year, f"{company1}": returns1.values, f"{company2}": returns2.values})
returns.to_excel("returns.xlsx", index=False)
