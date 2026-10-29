import streamlit as st 

st.sidebar.title("College Portal")
menu = st.sidebar.radio("Navigation", ["Home", "Addmission form", "About"])

st.title("🎓 College Addmission System")

if menu == "Home":
    st.header("Welcome")
    st.write("Welcome to the College Addmission Portal")

elif menu == "Addmission form":
    
    st.header("Addmission form")
    
    tab1, tab2, tab3 = st.tabs(["Personal Details", "Academic Details", "Submit"])
    
    with tab1:
        st.subheader("Personal Details")
        
        name = st.text_input("Enter Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        import datetime
         
        dob = st.date_input(
            "Date of Birth",
            min_value=datetime.date(1990, 1, 1),
            max_value=datetime.date(2026, 12, 31)
        )
        
    with tab2:
        st.header("Academic Details")
        
        course = st.selectbox("select course", ["BCA", "BA", "B.Tech", "BBA"])
        
    with tab3:
        st.subheader("Submit Form")
        
        if st.button("Submit Application"):
            st.success("Application Submitted Successfully")
            st.write("### Entered Details:")
            st.write("Name:", name)
            st.write("Email:", email)
            st.write("Phone:", phone)
            st.write("Gender:", gender)  
            st.write("DOB:", dob)
            st.write("Course:", course)
            
            
elif menu == "About":
    st.header("About")
    st.write("This is simple College Addmission Form using streamlit.")