import streamlit as st
from groq import Groq

st.title('Bollywood Music Mood analyzer')
song=st.text_input('Enter a song')
if st.button('Analyze its vibe'):
    if song:
        client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )
        response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
                {"role": "user", "content": f"""Analyze the Bollywood song '{song}' and give me:
1. The Mood or vibe it exhibits (in 1 line)
2. The Emotion it triggers within someone according to its mood (2 sentences)
3. Psychology behind why people connect with it (2-3 sentences)
4. Three similar songs."""}
            ]
        )

        st.write(response.choices[0].message.content)
    else:
        st.warning("No song")
