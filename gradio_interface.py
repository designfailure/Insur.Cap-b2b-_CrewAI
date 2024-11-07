import gradio as gr
import pandas as pd
import PyPDF2
import io
from crewai import Crew

def create_interface(crew: Crew):
    def process_input(input_text: str, file) -> str:
        file_content = ""
        if file:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file.name)
                file_content = df.to_string()
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file.name)
                file_content = df.to_string()
            elif file.name.endswith('.pdf'):
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
                file_content = "\n".join([page.extract_text() for page in pdf_reader.pages])
            else:
                file_content = file.read().decode('utf-8')

        # Process the input and file using the crew
        result = crew.kickoff(input_text=input_text, file_content=file_content)
        return result

    interface = gr.Interface(
        fn=process_input,
        inputs=[
            gr.Textbox(label="Enter your insurance query"),
            gr.File(label="Upload a file (optional)", file_types=[".csv", ".xlsx", ".pdf", ".txt", ".doc", ".docx"])
        ],
        outputs=gr.Markdown(label="Insurance Analysis Results"),
        title="InsurTech Agentic Workflow System",
        description="Enter your insurance query and optionally upload a file to start the insurance analysis process.",
        examples=[
            ["I need insurance for my small business", None],
            ["What's the best policy for a high-risk construction project?", None],
        ],
        allow_flagging="never"
    )

    return interface