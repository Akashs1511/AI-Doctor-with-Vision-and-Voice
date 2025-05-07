client=Groq()  
messages=[
    {
        "role": "user",
        "content": [
            {
                "type": "text", 
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}",
                },
            },
        ],
    }]
chat_completion=client.chat.completions.create(
    messages=messages,
    model=model
)