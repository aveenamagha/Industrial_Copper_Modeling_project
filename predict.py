import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pickle

# ------------------------------- Configuration -------------------------------
st.set_page_config(
    page_title="Industrial Copper Modeling",
    page_icon="🏨",
    layout="wide",
)

# ------------------------------- Sidebar -------------------------------
with st.sidebar:
    selected = option_menu(
        "Home Page",  
        ["About Project", "Selling Price Prediction", "Status (Win/Lost)"],
        icons=["house", "gear", "gear"],
        styles={
            "nav-link": {
                "font-size": "18px",
                "text-align": "center",
                "background-color": "transparent",  
                "color": "#1c1c1c", 
            },
            "nav-link-selected": {
                "background-color": "#d4edda", 
                "color": "black", 
            },
        },
    )

# ------------------------------- About Project -------------------------------
if selected == "About Project":
    st.markdown("<h1 style='color: blue;'>Industrial Copper Modeling</h1>", unsafe_allow_html=True)
    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)



 
# Display image 
    st.image("C:/Users/ELCOT/Downloads/WhatsApp Image 2024-12-09 at 11.16.00 AM (1).jpeg", use_container_width=True)

    st.markdown(
    """
    ### About the Copper Industry:
    The **copper industry** is an essential sector focused on the extraction, production, and recycling of copper. Copper is known for its excellent electrical conductivity and is widely used in industries like **electronics**, **construction**, **transportation**, and **renewable energy**.

    Copper is primarily obtained from mining and recycling, and it is refined through various processes such as **smelting** and **electrolytic refining**. The copper produced is used in applications like **wiring**, **plumbing**, **electric vehicles**, and **solar panels**.

    **Chile**, **Peru**, and **China** are key players in copper production, with China being the largest consumer. Recycling plays a crucial role in reducing the environmental impact by minimizing the need for mining.

    ### Technologies:
    Python, Pandas, Numpy, Scikit-Learn, Streamlit, Python scripting, 
    Machine Learning, Data Preprocessing, Visualization, EDA, Model Building, 
    Data Wrangling, Model Deployment.

    ### Overview:
    This project builds machine learning models and implements them as a user-friendly 
    online application to predict Selling Price and Status (Win/Lost) of industrial copper 
    models based on past transaction data.
    """
)




# ------------------------------- Mapping Dictionaries ------------------------
item_type_mapping = {
    "W": 5.0,
    "WI": 6.0,
    "S": 3.0,
    "Others": 1.0,
    "PL": 2.0,
    "IPL": 0.0,
    "SLAWR": 4.0,
}

status_mapping = {
    "Won": 7.0,
    "Draft": 0.0,
    "To be approved": 6.0,
    "Lost": 1.0,
    "Not lost for AM": 2.0,
    "Wonderful": 8.0,
    "Revised": 5.0,
    "Offered": 4.0,
    "Offerable": 3.0,
}

# ------------------------------- Selling Price Prediction --------------------
if selected == "Selling Price Prediction":
    st.markdown("# :blue[Predict Selling Price]")
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    # Columns for Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        a1 = st.text_input("Quantity")
        b1 = st.selectbox("Status", options=list(status_mapping.keys()))
        c1 = st.selectbox("Item Type", options=list(item_type_mapping.keys()))

    with col2:
        d1 = st.text_input("Application")
        e1 = st.text_input("Thickness")
        f1 = st.text_input("Width")

    with col3:
        g1 = st.text_input("Country")
        h1 = st.text_input("Customer")
        i1 = st.text_input("Product Reference")

    with open(r"selling_price_model.pkl", "rb") as file_1:
        regression_model = pickle.load(file_1)

    # Predict Button
    predict_button_1 = st.button("Predict Selling Price")
    if predict_button_1:
        try:
            # Convert inputs
            a1 = float(a1)
            d1 = float(d1)
            e1 = float(e1)
            f1 = float(f1)
            g1 = float(g1)
            h1 = float(h1)
            i1 = float(i1)

            # Map status and item type
            b1_numeric = status_mapping[b1]
            c1_numeric = item_type_mapping[c1]

            # Prediction
            new_sample_1 = np.array(
                [[np.log(a1), b1_numeric, c1_numeric, d1, np.log(e1), f1, g1, h1, i1]]
            )
            new_pred_1 = regression_model.predict(new_sample_1)[0]
            st.success(f"Predicted Selling Price: ₹{np.exp(new_pred_1):,.2f}")
        except Exception as e:
            st.error(f"Error: {e}")

# ------------------------------- Status Prediction ---------------------------
if selected == "Status (Win/Lost)":
    st.markdown("# :blue[Predict Status (Win/Lost)]")
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    # Columns for Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        a2 = st.text_input("Quantity")
        b2 = st.text_input("Selling Price")
        c2 = st.selectbox("Item Type", options=list(item_type_mapping.keys()))

    with col2:
        d2 = st.text_input("Application")
        e2 = st.text_input("Thickness")
        f2 = st.text_input("Width")

    with col3:
        g2 = st.text_input("Country")
        h2 = st.text_input("Customer")
        i2 = st.text_input("Product Reference")

    with open(r"status_model.pkl", "rb") as file_2:
        classification_model = pickle.load(file_2)

    # Predict Button
    predict_button_2 = st.button("Predict Status")
    if predict_button_2:
        try:
            # Convert inputs
            a2 = float(a2)
            b2 = float(b2)
            d2 = float(d2)
            e2 = float(e2)
            f2 = float(f2)
            g2 = float(g2)
            h2 = float(h2)
            i2 = float(i2)

            # Map item type
            c2_numeric = item_type_mapping[c2]

            # Prediction
            new_sample_2 = np.array(
                [[np.log(a2), np.log(b2), c2_numeric, d2, np.log(e2), f2, g2, h2, i2]]
            )
            new_pred_2 = classification_model.predict(new_sample_2)

            if new_pred_2 == 1:
                st.success("The Status is: Won")
            else:
                st.error("The Status is: Lost")
        except Exception as e:
            st.error(f"Error: {e}")
