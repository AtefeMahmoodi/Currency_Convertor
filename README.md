# Currency Convertor

## Project Overview
The Currency Convertor project is going to create a tool that allows users to convert amounts between different currencies. This project utilizes the ExchangeRate-API for fetching real-time exchange rate data and provides an interface for users to specify the amount in one currency and get the equivalent amount in another currency. Additionally, the project features a user-friendly UI using Streamlit, making it accessible for non-technical users to perform currency conversions with ease.

## Project Structure
The project has the following structure:

- `currency_convertor.py`: A python script containing currency and amount converting functions; `get_exchange_rate`, `convert_amount`.
- `app.py`: A Python script using Streamlit to create a web app interface for the currency convertor.
- `constants.py`: A Python script containing a list of available currencies in the ExchangeRate-API.
- `requirements.txt`: Contains all the required modules and libraries needed to run the project.
- `README.md`: Documentation for the project solution. You are currently reading this!

## Getting Started

Follow the instructions below to set up this project on your local machine.

### Prerequisites

- Python 3.6 or later
- Streamlit
- Cachetools

To install Cachetools, use pip:

```bash
pip install chachetools
```
Then install Streamlit using pip:

```bash
pip install streamlit
```
You can install all the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

After following the installation steps, you can run the Streamlit web app as follows:

```sh
streamlit run app.py
```

This will open a web page in your default browser running on your localhost.
