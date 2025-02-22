import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

st.title("Temperature Converter")
st.write("Convert temperatures between Celsius and Fahrenheit.")

option = st.radio("Select conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

temp_input = st.number_input("Enter temperature:", format="%.2f")

if st.button("Convert"):
    if option == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(temp_input)
        st.success(f"{temp_input}°C is equal to {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(temp_input)
        st.success(f"{temp_input}°F is equal to {result:.2f}°C")