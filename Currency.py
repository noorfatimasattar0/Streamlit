import streamlit as st
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(target_currency, None)
    return None

def main():
    st.title("Currency Converter")
    
    currencies = ["USD", "EUR", "GBP", "PKR", "INR", "CAD", "AUD", "JPY"]
    
    base_currency = st.selectbox("From Currency", currencies)
    target_currency = st.selectbox("To Currency", currencies)
    amount = st.number_input("Amount", min_value=0.01, value=1.0, step=0.01)
    
    if st.button("Convert"):
        rate = get_exchange_rate(base_currency, target_currency)
        if rate:
            converted_amount = amount * rate
            st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            st.error("Error fetching exchange rate. Please try again.")

if __name__ == "__main__":
    main()
