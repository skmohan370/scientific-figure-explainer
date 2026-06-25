import streamlit as st
from PIL import Image

from classifier import (
    is_scientific_figure,
    classify_figure_type
)

from analyzers import (
    analyze_graph,
    analyze_bar_chart,
    analyze_scatter,
    analyze_heatmap,
    analyze_microscopy
)

st.set_page_config(page_title="Figure Understanding System")

st.title("Scientific Figure → Explanation System")
st.write("Upload a scientific figure and get a structured explanation.")

uploaded_file = st.file_uploader(
    "Upload a figure image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Figure")
    
    if st.button("Analyze Figure"):
        try:
            with st.spinner("Checking image..."):
                is_figure = is_scientific_figure(image)

            if not is_figure:
                st.warning(
                    "This image does not appear to be a scientific figure."
                )

            else:
                with st.spinner("Classifying figure..."):
                    figure_type = classify_figure_type(image).upper()
                st.success(f"Detected Figure Type: {figure_type}")

                with st.spinner("Analyzing figure..."):

                    if "MICROSCOPY" in figure_type:
                        analysis = analyze_microscopy(image)

                    elif "SCATTER" in figure_type:
                        analysis = analyze_scatter(image)

                    elif "BAR" in figure_type:
                        analysis = analyze_bar_chart(image)

                    elif "HEATMAP" in figure_type:
                        analysis = analyze_heatmap(image)

                    else:
                        analysis = analyze_graph(image)

                st.write("### Analysis")
                st.write(analysis)

        except Exception as e:

            st.error("Analysis failed. Please try again.")
            st.expander("Error Details").write(str(e))