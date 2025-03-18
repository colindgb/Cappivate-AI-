import openai

API_KEY = "your_openai_api_key_here"

def generate_content(prompt, style="engaging"):
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Write a {style} social media post."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]
