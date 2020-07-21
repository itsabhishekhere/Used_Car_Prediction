import pickle
import streamlit as st
from PIL import Image

rf_model = pickle.load(open('rf_reg_model.pkl', 'rb'))

def convert_var(location, owner, fuel, transmission):
    Location_Ahmedabad = 0
    Location_Bangalore = 0
    Location_Chennai = 0
    Location_Coimbatore = 0
    Location_Delhi = 0
    Location_Hyderabad = 0
    Location_Jaipur = 0
    Location_Kochi = 0
    Location_Kolkata = 0
    Location_Mumbai = 0
    Location_Pune = 0
    Fuel_Type_CNG = 0
    Fuel_Type_Diesel = 0
    Fuel_Type_LPG = 0
    Fuel_Type_Petrol = 0
    Transmission_Automatic = 0
    Transmission_Manual = 0

    loc = ('Location_'+location)
    vars()[loc] = 1
    fu = ('Fuel_Type_'+fuel)
    vars()[fu] = 1
    tran = ('Transmission_' + transmission)
    vars()[fu] = 1

    if owner == 'First':
        owner = 1
    elif owner == 'Second':
        owner = 2
    elif owner == 'Third':
        owner = 3
    else:
        owner = 4

    return (Location_Ahmedabad, Location_Bangalore, Location_Chennai, Location_Coimbatore, Location_Delhi,
            Location_Hyderabad, Location_Jaipur, Location_Kochi, Location_Kolkata, Location_Mumbai,
            Location_Pune, Fuel_Type_CNG, Fuel_Type_Diesel, Fuel_Type_LPG, Fuel_Type_Petrol, Transmission_Automatic,
            Transmission_Manual, owner)



def main():
    html_temp = """
    <div style = "background color:#5F4B8BFF; padding:10px">
    <h1 style="color:#E69A8DFF; text-align:center;">Used Car Price Prediction</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    image = Image.open('car.jpg')
    st.image(image, use_column_width=True, format='JPEG')

    activities = ['Calcuate Price', 'About', 'Contact']
    option = st.sidebar.selectbox('Menu ', activities)
    st.subheader('Calcuate Price')

    if option == 'About':
        html_temp_about = """
            <div style = "background color:#FDD20EFF; padding:10px">
            <h3 style="color:#F93822FF; text-align:center;">About</h3></div>
            <div style = "background color:#D7C49EFF; padding:10px">
            <p>Kaggle Notebook: <a href="https://www.kaggle.com/iabhishekmaurya/used-car-price-prediction">Link</a></p>
            <p>So called Second hand's car have a huge market base. Many consider to buy a Used Car intsead of buying of new one, as it's is feasible and a better investment. </p>
            <p>The main reason for this huge market is that when you buy a New Car and sale it just another day without any default on it, the price of car reduces by 30%.</p>
            <p>There are also many frauds in the market who not only sale wrong but also they could mislead to wrong price.</p>
            <p>So, here I used this following dataset to Predict the price of any used car.</p>
            </div>
            """
        st.sidebar.markdown(html_temp_about, unsafe_allow_html=True)
    elif option == 'Contact':
        html_temp_contact = """
                    <div style = "background color:#FDD20EFF; padding:10px">
                    <h3 style="color:#F93822FF; text-align:center;">Contact</h3></div>
                    <div style = "background color:#D7C49EFF; padding:10px">
                    <p>This Model is Developed by <b>Abhishek (solos_silence)</b></p>
                    <p>LinkedIn: <a href="https://www.linkedin.com/in/abhishek-5b642580/">Link</a></p>
                    <p>Kaggle: <a href="https://www.kaggle.com/iabhishekmaurya/">Link</a></p>
                    <p>JAI HIND</p>
                    </div>"""
        st.sidebar.markdown(html_temp_contact, unsafe_allow_html=True)

    name = st.text_input("Name of Model Name", "Type Here")
    kg_dr = st.text_input("Kilometer Driven", "Type Here")
    mileage = st.text_input("Mileage in Km/l", "Type Here")
    engine = st.text_input("Engine in CC", "Type Here")
    power = st.text_input("Power in bhp", "Type Here")
    city = ['Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad']
    location = st.selectbox('Select your city', city)
    owner = st.radio("Choose Owner Type", ('First', 'Second', 'Third', 'Fourth & Above'))
    fuel = st.radio("Choose Fuel Type", ('CNG', 'Diesel', 'Petrol', 'LPG'))
    transmission = st.radio("Choose Transmission", ('Manual', 'Automatic'))
    seats = st.slider("Select Number Seats", 0.0, 12.0, step=1.0)
    year = st.slider("Select Purchase year", 1980, 2020)

    Location_Ahmedabad, Location_Bangalore, Location_Chennai, Location_Coimbatore, Location_Delhi,\
    Location_Hyderabad, Location_Jaipur, Location_Kochi, Location_Kolkata, Location_Mumbai, Location_Pune,\
    Fuel_Type_CNG, Fuel_Type_Diesel, Fuel_Type_LPG, Fuel_Type_Petrol, Transmission_Automatic, \
    Transmission_Manual, owner = convert_var(location, owner, fuel, transmission)

    inputs = [[year, kg_dr, owner, seats, mileage, engine, power, Location_Ahmedabad,
               Location_Bangalore, Location_Chennai, Location_Coimbatore,
               Location_Delhi, Location_Hyderabad, Location_Jaipur,
               Location_Kochi, Location_Kolkata, Location_Mumbai, Location_Pune, Fuel_Type_CNG,
               Fuel_Type_Diesel, Fuel_Type_LPG, Fuel_Type_Petrol, Transmission_Automatic, Transmission_Manual]]

    st.subheader("Price")

    if st.button('Calculate'):
        st.write('**Hey Buyer/Seller! **')
        st.write('**You Model: **:')
        st.success(name)
        st.write("**Has a Predicted Price (in Rs.)**")
        st.success("{:.2f}".format(rf_model.predict(inputs)[0] * 100000))
    else:
        pass

    html_temp_end = """
        <div style="background-color:#603F83FF">
        <h3 style="color:#C7D3D4FF;text-align:center;" >Happily Developed By: <b>solo_silence</b> </h3>
        </div>
        """
    st.markdown(html_temp_end, unsafe_allow_html=True)



if __name__=='__main__':
    main()