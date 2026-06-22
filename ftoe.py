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
                }])
    answer = response['message']['content'].strip()
    return "YES" in answer.upper()


def classify_figure_type(image):
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
                        Classify the type of this scientific figure.
                        Respond with ONLY one of the following:
                        LINE_GRAPH
                        BAR_CHART
                        SCATTER_PLOT
                        MICROSCOPY
                        HEATMAP
                        OTHER
                        ''',
                    'images': [temp_file.name]
                }])
    return response['message']['content'].strip()


def analyze_graph(image):
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
                        1. Graph Type
                        2. X-Axis
                        3. Y-Axis
                        4. Main Trend
                        5. Groups or Conditions
                        6. Notable Observations
                        7. Main Conclusion

                        For each section, provide 1-3 bullet points max.
                        Ensure all seven sections are complete, even if some are "None" or "N/A".
                        ''',
                    'images': [temp_file.name]}])
    return response['message']['content']

def analyze_microscopy(image):
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
                        1. Image Type
                        2. Visible Structures
                        3. Cell Morphology
                        4. Cell Density
                        5. Staining Patterns
                        6. Notable Observations
                        7. Biological Interpretation

                        For each section, provide 1-3 bullet points max.
                        Ensure all seven sections are complete, even if some are "None" or "N/A".
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
                with st.spinner("Classifying figure type..."):
                    figure_type = classify_figure_type(image)
                st.write("### Figure Type")
                st.write(figure_type)
                with st.spinner("Analyzing figure..."):
                    if figure_type == "MICROSCOPY":
                        analysis = analyze_microscopy(image)
                    else:
                        analysis = analyze_graph(image)
                st.write("### Analysis")
                st.write(analysis)
        except Exception as e:
            st.error("Analysis failed. Please try again.")
            st.expander("Error Details").write(str(e))