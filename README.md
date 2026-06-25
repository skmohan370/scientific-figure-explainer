# scientific-figure-explainer
AI-powered application that analyzes scientific figures and generates structured English explanations using local vision-language models.
## Features
- Scientific Figure Detection
- Structured Figure Analysis/Output
- Local vision-language model inference using Ollama Qwen2.5-VL
- Streamlit web interface

## Example Worflow
1. Determine if uploaded image is a scientific figure
2. If a figure, analyze it (If not, send a warning instead of result)
3. Generate structured explanation

## Tech Stack
- Python
- Streamlit
- Ollama
- Qwen2.5-VL

## Future Goals
- Figure type classification
- Figure-specific analysis pipelines
- Improvement of microscopy interpretation
- PDF/different input type extraction

## Known Limitations
- Very dense heatmaps with extensive annotations or high-resolution labels may produce incomplete analyses.
- Performance depends on the quality and complexity of the uploaded figure.
- Blurry or low-resolution figures may reduce classification accuracy.

## Installation

### Clone the repository

```bash
git clone https://github.com/skmohan370/scientific-figure-explainer.git
cd scientific-figure-explainer
```

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Download the vision model

```bash
ollama pull qwen2.5vl:3b
```

### Run the application

```bash
streamlit run ftoe.py
```
