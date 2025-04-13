import streamlit as st

# Conversion dictionaries
length_units = {
    'Meters': 1,
    'Kilometers': 0.001,
    'Centimeters': 100,
    'Miles': 0.000621371,
    'Feet': 3.28084,
    'Inches': 39.3701
}

weight_units = {
    'Kilograms': 1,
    'Grams': 1000,
    'Pounds': 2.20462,
    'Ounces': 35.274
}

temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']

# Temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Convert to Celsius first
    if from_unit == 'Fahrenheit':
        value = (value - 32) * 5 / 9
    elif from_unit == 'Kelvin':
        value = value - 273.15
    # Convert from Celsius to target
    if to_unit == 'Fahrenheit':
        return (value * 9 / 5) + 32
    elif to_unit == 'Kelvin':
        return value + 273.15
    else:
        return value

# App UI
st.title("Google-style Unit Converter")

unit_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

if unit_type == "Length":
    units = length_units
elif unit_type == "Weight":
    units = weight_units
elif unit_type == "Temperature":
    units = temperature_units

from_unit = st.selectbox("From", list(units.keys()) if isinstance(units, dict) else units)
to_unit = st.selectbox("To", list(units.keys()) if isinstance(units, dict) else units)

value = st.number_input("Enter value to convert", format="%.4f")

# Perform conversion
if st.button("Convert"):
    if unit_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        base_value = value / units[from_unit]
        result = base_value * units[to_unit]
    
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
