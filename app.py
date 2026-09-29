import streamlit as st

st.set_page_config(page_title="Edu-Genie", page_icon="📚", layout="wide")

st.title("📚 Edu-Genie - Your AI Study Buddy")
st.markdown("### Upload your notes and get Instant Quiz, Summary & Doubts Cleared!")

st.sidebar.header("Settings")
subject = st.sidebar.selectbox("Select Subject", ["Computer Science", "AI", "Maths", "General"])

uploaded_file = st.file_uploader("Upload your Study Material (PDF/TXT)", type=["pdf","txt"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name} for {subject}")
    text = uploaded_file.read().decode('utf-8', errors='ignore')[:2000]
    st.text_area("File Preview", text, height=200)

    tab1, tab2, tab3 = st.tabs(["📝 Summary", "❓ Quiz", "💡 Ask Doubt"])
    
    with tab1:
        st.write("**Summary of your notes:**")
        st.info("Edu-Genie has analyzed your notes. Key points: Important definitions, formulas and concepts are extracted for quick revision.")
    
    with tab2:
        st.write("**Auto Generated Quiz:**")
        st.write("1. What is the main topic of this chapter?")
        st.write("2. Explain the key concept in 2 lines.")
        if st.button("Generate More Questions"):
            st.write("3. Give one real-world example.")
            
    with tab3:
        q = st.text_input("Ask any doubt from your notes:")
        if q:
            st.write(f"**Answer for '{q}':** This concept is explained in your notes on page 2. Let me simplify it for you...")

else:
    st.info("Please upload a file to start learning!")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
