import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.environ.get("GOOGLE_API_KEY")

# Configure Gemini Pro API with the API key
genai.configure(api_key=API_KEY)

def main():
    st.title("GenAI-PySpark Unit Test Generator")
    
    # File uploader for PySpark code file
    uploaded_file = st.file_uploader("Upload PySpark Code File", type=["py"])
    
    if uploaded_file is not None:
        # Read the file content
        file_content = uploaded_file.getvalue().decode("utf-8")
        
        # Display the code file content
        st.subheader("Code File Content")
        st.code(file_content)
        
        # Button to generate unit tests
        if st.button("Generate Unit Test Cases"):
            # Create a prompt for the AI model
            prompt = f"Generate unit test cases for the following PySpark code:\n\n{file_content}"
            
            # Choose the model (gemini-1.5-pro-latest) for content generation
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            
            # Call the model to generate content
            response = model.generate_content(prompt)
            
            # Extract the generated test cases from the response
            generated_test_cases = response.text
            
            # Display the generated unit test cases
            st.subheader("Generated Unit Test Cases")
            st.code(generated_test_cases)

if __name__ == "__main__":
    main()
