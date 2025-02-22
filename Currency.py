exchange_rates = {
    "USD": 0.0036,  # 1 PKR = 0.0036 USD
    "GBP": 0.0028,  # 1 PKR = 0.0028 GBP
    "CNY": 0.026,   # 1 PKR = 0.026 CNY
    "RUB": 0.33,    # 1 PKR = 0.33 RUB
    "IDR": 56.7     # 1 PKR = 56.7 IDR
}

# Streamlit UI
st.title("💱 PKR Currency Converter")

# User inputs amount in PKR
amount = st.number_input("Enter amount in PKR", min_value=0.0, format="%.2f")

# Dropdown for currency selection
currency = st.selectbox("Select currency to convert:", list(exchange_rates.keys()))

# Convert button
if st.button("Converted"):
    if amount > 0:
        converted_amount = amount * exchange_rates[currency]
        st.success(f"**{amount} PKR = {converted_amount:.2f} {currency}**")
    else:
        st.warning("Enter a valid amount.")    


