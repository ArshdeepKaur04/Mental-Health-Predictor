import streamlit as st
from generating_explanations import predict_condition, generate_explanation
from fpdf import FPDF
import io
import os 

# Function to generate PDF
def generate_pdf(explanation):
    # Create FPDF instance
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Mental Health Condition Explanation", ln=True, align="C")

    # Set body text
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, explanation)

    # Save the pdf to a temporary file
    pdf_output_path = "temp_mental_health_explanation.pdf"
    pdf.output(pdf_output_path)

    # Read the PDF back into a BytesIO object
    with open(pdf_output_path, "rb") as f:
        pdf_file = io.BytesIO(f.read())

    # Clean up the temporary file
    os.remove(pdf_output_path)

    # Return the PDF file as a BytesIO object
    return pdf_file

st.title("Mental Health Condition Predictor")

# User Input
symptoms = st.text_area("Enter your symptoms:")

if st.button("Predict"):
    if symptoms:
        # Predict Condition
        predicted_condition = predict_condition(symptoms)
        st.write(f"### Predicted Condition: {predicted_condition}")

        # Display "Generating explanation..." message
        with st.spinner("Generating explanation... Please wait."):
            explanation = generate_explanation(predicted_condition)

        # Ensure explanation appears
        if explanation:
            st.write(f"### Explanation & Coping Mechanisms:")
            st.write(explanation)

            # Generate PDF
            pdf_file = generate_pdf(explanation)

            # Allow the user to download the PDF
            st.download_button(
                label="Download Explanation as PDF",
                data=pdf_file,
                file_name="mental_health_explanation.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Could not generate an explanation. Try again.")

    else:
        st.warning("Please enter symptoms.")