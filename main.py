import streamlit as st
import openai
from textblob import TextBlob

def correct_spelling(input_text):
    blob = TextBlob(input_text)
    return str(blob.correct())

def chat_with_gpt(input_topic):
    # Correct the input sentence for spelling and grammar
    corrected_topic = correct_spelling(input_topic)

    # Make API call to ChatGPT
    api_key =   # Replace this with your actual API key
    openai.api_key = api_key

    system_message = "You are an expert in this field. Please provide a concise and accurate answer."
    prompt = f"{system_message}\n\n{corrected_topic}"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.2,
        )

        if response and 'choices' in response and len(response['choices']) > 0:
            answer = response['choices'][0]['text'].strip()
            return answer
    except Exception as e:
        st.error(f"Error in API call: {e}")

    return "Error in API call. Please try again later."

def main():
    st.title("Chatbot with GPT-3.5 API and Spell Check")

    # Get the input topic from the user
    input_topic = st.text_input("Enter your topic:")

    if st.button("Get Answer"):
        if input_topic:
            # Chat with GPT and get the answer
            answer = chat_with_gpt(input_topic)
            st.subheader("Answer (less than 100 words):")
            st.write(answer)
        else:
            st.warning("Please enter a topic to get an answer.")

if __name__ == "__main__":
    main()
