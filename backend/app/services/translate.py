import os
from openai import OpenAI

# Initialize the client (it automatically looks for OPENAI_API_KEY in env vars)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_to_english(raw_transcript: str, detected_language: str) -> str:
    """
    Translate any language transcript into English using modern OpenAI syntax.
    """

    if detected_language == "en":
        return raw_transcript

    prompt = f"Translate the following sales call transcript into English. Preserve meaning and intent.\n\nTranscript:\n{raw_transcript}"

    # Updated API call syntax
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional translation assistant specialized in sales context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    # Updated response access
    return response.choices[0].message.content.strip()