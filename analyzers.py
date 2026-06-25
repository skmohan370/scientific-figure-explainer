from utils import ask_model

from prompts import (
    GRAPH_PROMPT,
    BAR_PROMPT,
    SCATTER_PROMPT,
    HEATMAP_PROMPT,
    MICROSCOPY_PROMPT
)

def analyze_graph(image):
    return ask_model(image, GRAPH_PROMPT)

def analyze_bar_chart(image):
    return ask_model(image, BAR_PROMPT)

def analyze_scatter(image):
    return ask_model(image, SCATTER_PROMPT)

def analyze_heatmap(image):
    return ask_model(image, HEATMAP_PROMPT)

def analyze_microscopy(image):
    return ask_model(image, MICROSCOPY_PROMPT)