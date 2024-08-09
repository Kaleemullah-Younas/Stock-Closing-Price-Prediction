# 📉 Stock Closing Price Prediction

Unlock the potential of financial forecasting with our Stock Closing Price Prediction project! This application leverages advanced machine learning techniques to predict the closing prices of stocks listed on the Pakistan Stock Exchange (PSX). By analyzing historical stock data, the model aids investors in making informed decisions and optimizing their trading strategies.

## Introduction & Objective

Predicting stock market prices is a complex yet vital task due to the volatile nature of financial markets. This project focuses on predicting the closing prices of stocks, an essential indicator reflecting the stock's value at the end of a trading session. Our primary goal is to develop a predictive model using historical stock data to provide accurate forecasts, helping investors and traders optimize their investment strategies.

## Features & Data Preprocessing

The dataset, sourced from Kaggle, includes various attributes of stock data, such as:
- **Date** , **Open** , **High** , **Low** , **Close** , **Volume** , **Company Name** , **Sector**

### Data Preprocessing Techniques:

- **Concatenation:** Grouping data into meaningful categories.
- **Exploratory Data Analysis (EDA):** Conducting univariate, bivariate, and multivariate analyses.
- **Feature Engineering:** Handling outliers, applying power transformations, and creating relevant features.
- **Feature Selection:** Using Principal Component Analysis (PCA) for dimensionality reduction.

## Model Selection & Evaluation

Various regression techniques were implemented:
- **Ridge Regression**
- **Lasso Regression**
- **Polynomial Regression**

## Conclusion:

Polynomial Regression emerged as the most effective model, achieving an R² score of 0.8617, capturing complex, non-linear patterns within the data.

## How to Run the Project

1. Fork the repository to local machine
2. Install Python 3.10 and install all additional dependencies in `requirements.txt` using the command `pip install -r ./requirements.txt`.
3. Run the Jupyter notebook from the terminal using the command `python -m jupyterlab`.
4. Run the Streamlit app from the terminal using the command `streamlit run app.py`.
5. The Streamlit app will be hosted on `localhost:8501`.

#

## Contribute:

We welcome contributions from the developer community! Feel free to fork the repository, submit issues, and create pull requests to enhance this project further.

Embark on your financial forecasting journey with our Stock Closing Price Prediction project! 📊🚀
