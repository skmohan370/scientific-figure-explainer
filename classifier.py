from utils import ask_model
from prompts import FIGURE_CHECK_PROMPT, CLASSIFIER_PROMPT


def is_scientific_figure(image):
    answer = ask_model(image, FIGURE_CHECK_PROMPT)
    return "YES" in answer.upper()

def classify_figure_type(image):
    return ask_model(image, CLASSIFIER_PROMPT)