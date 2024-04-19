import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.environ.get("GOOGLE_API_KEY")

# Configure Gemini Pro API with the API key
genai.configure(api_key=API_KEY)

#st.image("../pics/capgemini.png", width=200)

def main():
    # st.title("COBOL to PySpark Code Converter")
    
    # File uploader for COBOL file
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload COBOL File", type=["cob", "txt","cbl","db2","sqb"])
    
    Cobol_Input_Code,Create_PySpark_Code, Unit_Test_Case_Doc, Unit_Test_Case_Scripts = st.tabs(["CobolInputCode","PySparkCode", "Unit Test Case Documentation", "Unit Test Case Scripts"])

    if uploaded_file is not None:
        # Read the file content
        cobol_content = uploaded_file.getvalue().decode("utf-8")
        
        
        with Cobol_Input_Code:
            # Display the COBOL file content
            st.subheader("COBOL File Content")
            st.code(cobol_content)

        with Create_PySpark_Code:
            # Convert COBOL to PySpark code
            pyspark_code = convert_to_pyspark(cobol_content)
            st.subheader("Generated PySpark Code")
            st.code(pyspark_code)

        with Unit_Test_Case_Doc:
            # Create a prompt for the AI model
            prompt = f"Generate unit test case documentation for the following PySpark code:\n\n{pyspark_code}"
            
            # Choose the model (gemini-1.5-pro-latest) for content generation
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            
            # Call the model to generate content
            response = model.generate_content(prompt)
            
            # Extract the generated test cases from the response
            generated_test_cases = response.text
            
            # Split the generated test cases into documentation and actual test cases
            doc_section = generated_test_cases.split("\n\n### Unit Test Cases Section:\n\n")
            
            # Display the generated unit test case documentation
            st.markdown("\n\n".join(doc_section), unsafe_allow_html=True)

        with Unit_Test_Case_Scripts:
            # Create a prompt for the AI model
            prompt = f"Generate unit test cases for the following PySpark code:\n\n{pyspark_code}"
            
            # Choose the model (gemini-1.5-pro-latest) for content generation
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            
            # Call the model to generate content
            response = model.generate_content(prompt)
            
            # Extract the generated test cases from the response
            generated_test_cases = response.text
            
            # Display the generated unit test cases
            st.subheader("Generated Unit Test Cases")
            st.code(generated_test_cases)


def convert_to_pyspark(cobol_content):
    # Call the Gemini Pro API to generate PySpark code from COBOL
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"Generate PySpark code:\n\n{cobol_content}"
    # Call the model to generate content
    response = model.generate_content(prompt)
    pyspark_code = response.text
    return pyspark_code



if __name__ == "__main__":
    main()
