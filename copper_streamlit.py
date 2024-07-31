import copper_industry_project
import streamlit as st

st.title(":green[INDUSTRIAL COPPER MODELLING]")
with st.sidebar:
    prediction=st.radio("Select any ML prediction",("Home","Regression Model","Classification Model"))
if prediction=="Home":
    st.image("copper_industry_project\copperimg.jpeg",width=800)
    st.header("About this project")
    st.markdown("This project is about dealing with copper industry production dataset.")
    st.markdown("These data suffer from skewness and noisy data. This may affect the manual prediction of pricing")
    st.markdown("We use machine learning algorithms to correct the skewness and predict the pricing and status of the product")
elif prediction=="Regression Model":
    with st.form(key='my_form'):
        type=st.selectbox("Choose any Item Type",['W','WI','S','Others','PL','IPL','SLAWR'])
        customer=st.number_input("Enter a customer_ID",min_value=12000,max_value=30410000)
        quantity=st.number_input("Enter the quantity in tons")
        application=st.number_input("Enter the application of the product",min_value=2,max_value=99)
        thickness=st.number_input("Enter the thickness of the product",min_value=0,max_value=2500)
        width=st.number_input("enter the width of product",min_value=1,max_value=3000)
        # price=st.number_input("Enter the price of product")
        status=st.selectbox("Choose the status of purchase",['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM',
                                                            'Wonderful', 'Revised', 'Offered', 'Offerable'])
        submit=st.form_submit_button(label='Predict Result')

    if submit:
        st.subheader("Given Data")
        st.write(f"Item Type: {type}")
        st.write(f"Customer_ID: {customer}")
        st.write(f"Quantity: {quantity}")
        st.write(f"Application: {application}")
        st.write(f"Thickness: {thickness}")
        st.write(f"Width: {width}")
        st.write(f"Product Status: {status}")
        predicted_value=copper_industry_project.regression_model(quantity,customer,status,type,application,thickness,width)
        st.write(f"Predicted selling price is: {predicted_value}")
    
elif prediction=="Classification Model":
    with st.form(key='my_form'):
        type=st.selectbox("Choose any Item Type",['W','WI','S','Others','PL','IPL','SLAWR'])
        customer=st.number_input("Enter a customer_ID",min_value=12000,max_value=30410000)
        quantity=st.number_input("Enter the quantity in tons")
        application=st.number_input("Enter the application of the product",min_value=2,max_value=99)
        thickness=st.number_input("Enter the thickness of the product",min_value=0,max_value=2500)
        width=st.number_input("enter the width of product",min_value=1,max_value=3000)
        price=st.number_input("Enter the price of product")
        # status=st.selectbox("Choose the status of purchase",['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM','Wonderful', 'Revised', 'Offered', 'Offerable'])
        submit=st.form_submit_button(label='Predict Result')

    if submit:
        st.subheader("Given Data")
        st.write(f"Item Type: {type}")
        st.write(f"Customer_ID: {customer}")
        st.write(f"Quantity: {quantity}")
        st.write(f"Application: {application}")
        st.write(f"Thickness: {thickness}")
        st.write(f"Width: {width}")
        st.write(f"Product Price: {price}")
        predicted_value=copper_industry_project.classification_model(quantity,customer,type,application,thickness,width,price)
        st.write(f"Predicted staus of transaction is: {predicted_value}")

    
