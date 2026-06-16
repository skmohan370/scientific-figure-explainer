import streamlit as st
from PIL import Image
from ollama import chat
import tempfile

def is_scientific_figure(image):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    ) as temp_file:

        image.save(temp_file.name)

        response = chat(
            model='qwen2.5vl:3b',
            messages=[
                {
                    'role': 'user',
                    'content': '''
Is this a scientific figure, graph, chart,
microscopy image, scientific illustration,
or scientific visualization?

Answer with only:

YES

or

NO
''',
                    'images': [temp_file.name]
                }
            ]
        )

    answer = response['message']['content'].strip()

    return "YES" in answer.upper()

def analyze_figure(image):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    ) as temp_file:

        image.save(temp_file.name)

        response = chat(
            model='qwen2.5vl:3b',
            messages=[
                {
                    'role': 'user',
                    'content': '''
                        Analyze this scientific figure.

                        Provide:
                        1. Figure Type
                        2. Axes
                        3. Main Trend
                        4. Groups or Conditions
                        5. Key Insight

                        Be concise and structured.
                        ''',
                    'images': [temp_file.name]}])

    return response['message']['content']

st.set_page_config(page_title="Figure Understanding System")

st.title("Scientific Figure → Explanation System")
st.write("Upload a scientific figure and get a structured explanation.")

uploaded_file = st.file_uploader("Upload a figure image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Figure")
    if st.button("Analyze Figure"):
        try:
            with st.spinner("Checking image..."):
                is_figure = is_scientific_figure(image)

            if not is_figure:

                st.warning("This image does not appear to be a scientific figure.")

            else:
                with st.spinner("Analyzing figure..."):
                    analysis = analyze_figure(image)

                st.write("### Analysis")
                st.write(analysis)
        except Exception as e:
            st.error("Analysis failed. Please try again.")
            st.expander("Error Details").write(str(e))