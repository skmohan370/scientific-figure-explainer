import tempfile
from ollama import chat


def ask_model(image, prompt):
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    ) as temp_file:
        image.save(temp_file.name)
        response = chat(
            model="qwen2.5vl:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [temp_file.name]
                }
            ],
            options={
                "num_predict": 400
            }
        )
    return response["message"]["content"].strip()