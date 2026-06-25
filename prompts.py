GRAPH_PROMPT = """
Analyze this scientific graph.

Provide:

1. Graph Type
2. X-Axis
3. Y-Axis
4. Main Trend
5. Groups or Conditions
6. Important Observations
7. Main Conclusion
8. General Audience Explanation (3 sentences max)

Be concise and structured.
"""

BAR_PROMPT = """
Analyze this bar chart.

Provide:

1. Chart Type
2. X-Axis
3. Y-Axis
4. Highest Category
5. Lowest Category
6. Important Comparisons
7. Main Conclusion
8. General Audience Explanation (3 sentences max)

Be concise and structured.
"""

SCATTER_PROMPT = """
Analyze this scatter plot.

Provide:

1. Plot Type
2. X-Axis
3. Y-Axis
4. Relationship Between Variables
5. Clusters or Groups
6. Outliers
7. Main Conclusion
8. General Audience Explanation (3 sentences max)

Be concise and structured.
"""

HEATMAP_PROMPT = """
Analyze this heatmap.

Provide:

1. Heatmap Type
2. Axes
3. Color Scale Meaning
4. Key Patterns (include high and low regions)
5. Main Conclusion
6. General Audience Explanation

Be concise and structured.
"""

MICROSCOPY_PROMPT = """
Analyze this microscopy image.

Provide:

1. Image Type
2. Visible Structures
3. Cell Morphology
4. Cell Density
5. Notable Features
6. Biological Interpretation
7. General Audience Explanation (3 sentences max)

Be concise and structured.
"""

FIGURE_CHECK_PROMPT = """
Is this a scientific figure, graph, chart,
microscopy image, scientific illustration,
or scientific visualization?

Answer with only:

YES

or

NO
"""

CLASSIFIER_PROMPT = """
Classify the type of this scientific figure.

Respond with ONLY one of:

LINE_GRAPH
BAR_CHART
SCATTER_PLOT
MICROSCOPY
HEATMAP
OTHER
"""