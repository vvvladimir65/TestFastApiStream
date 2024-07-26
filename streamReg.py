import streamlit as st
import requests

st.title('FastAPI & Streamlit Integration')

# Endpoint URL
fastapi_url = "http://127.0.0.1:8000"

st.write("BedroomCount: ")
BedroomCount = st.number_input('BedroomCount', min_value=1.0)
st.write("LivingArea: ")
LivingArea = st.number_input('LivingArea', min_value=100.0)
st.write("BathroomCount: ")
BathroomCount = st.number_input('BathroomCount', min_value=1.0)
st.write("StateOfBuilding_Encoded: ")
StateOfBuilding_Encoded = st.number_input('StateOfBuilding_Encoded', min_value=0.0)
st.write("SwimmingPool: ")
SwimmingPool = st.number_input('SwimmingPool', min_value=0.0)
st.write("RoomCount:")
RoomCount = st.number_input('RoomCount', min_value=3.0)

if st.button('Submit'):
    response = requests.post(f"{fastapi_url}/predict/", json={
        "BedroomCount": BedroomCount,
        "LivingArea": LivingArea,
        "BathroomCount": BathroomCount,
        "StateOfBuilding_Encoded": BathroomCount,
        "SwimmingPool": SwimmingPool,
        "RoomCount": RoomCount
    })
    # Ensure you're using POST here to match the FastAPI endpoint
    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction")
        st.write("### Prediction")
        st.write(prediction)
    else:
        st.write("Error:", response.json())

if st.button('Ping'):
    response = requests.get(fastapi_url)
    result = response.json()
    st.write("### Ping Result")
    st.write(result["message"])