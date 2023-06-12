import os
import nltk
import ssl
import streamlit as st
from streamlit_chat import message
import random
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import json
from sklearn.metrics.pairwise import cosine_similarity

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
# nltk.download('punkt')


# ---- PAGE CONFIGURATION ---- #
PAGE_ICON = "assets/imgs/xyz_ecommerce2.png"
PAGE_TITLE = "XYZ chatbot"
PAGE_LAYOUT = "centered"
HELP = "https://www.xyz.com/help"
REPORT_BUG = "mailto:bug@xyz.com"
ABOUT = """
This is a Chatbot that is built on NLP model for **XYZ**,
an e-commerce website. It can understand and
appropriately respond to customers' requests in text format.


Feel free to interact with the chatbot and report
any bug using the `Report a bug` button, or use the
`Get Help` button to get assistance from our technical team.
"""

st.set_page_config(
    page_icon = PAGE_ICON,
    page_title = PAGE_TITLE,
    layout = PAGE_LAYOUT,
    menu_items={
        'Get Help': HELP,
        'Report a bug': REPORT_BUG,
        'About': ABOUT
    }
)

# # Load the JSON data
# with open('Ecommerce_FAQ_Chatbot_dataset.json') as file:
#     data = json.load(file)

DATA_PATH = "assets/data/data.json"
with open(DATA_PATH, "r") as  data:
    intents = json.load(data)

def convert_session_state_to_dict(session_state):
    state_dict = {}
    for key, value in session_state.items():
        state_dict[key] = value
    return state_dict

CHAT_HISTORY_PATH = "outputs/chat_histories"
EMAIL_PATH = "outputs/emails/"

# Hide streamlit header and footer
def hide_streamlit_header_footer():
    hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

# # Extract questions and answers from the JSON data
# questions = [item['question'] for item in data['questions']]
# answers = [item['answer'] for item in data['questions']]

# # Create a TF-IDF vectorizer
# vectorizer = TfidfVectorizer()

# # Transform the questions into a TF-IDF matrix
# tfidf_matrix = vectorizer.fit_transform(questions)

# # Define a function to find the best matching response
# def get_best_response(user_input):
#     # Transform the user input into a TF-IDF vector
#     user_input_tfidf = vectorizer.transform([user_input])

#     # Calculate the cosine similarity between the user input and the questions
#     similarities = cosine_similarity(user_input_tfidf, tfidf_matrix)

#     # Get the index of the most similar question
#     best_question_index = similarities.argmax()

#     # Return the corresponding answer
#     return answers[best_question_index]



# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)
# clf = RandomForestClassifier(random_state=2023, max_depth=3)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)
# col1, col2 = st.columns(2)

# with col1:
#     st.write(tags)
#     # st.header("A cat")
#     # st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.write(patterns)
#     # st.header("A dog")
#     # st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            if intent["tag"] == "goodbye":
                return [response, tag, "goodbye"]
            return [response, tag]

# ------------------------------------------------------------------
# Save history

# This is used to save chat history and display on the screen
if 'tag' not in st.session_state:
    st.session_state["tag"] = []

if "answer" not in st.session_state:
    st.session_state["answer"] = []

if "question" not in st.session_state:
    st.session_state["question"] = []

counter = 0

def main():
    # hide_streamlit_header_footer()
    global counter
    st.title("Chatbot")
    st.write("Welcome to the chatbot. Please type a message and click the `Send` button to start the conversation.")
    # st.write(intents)
    counter += 1
    
    # Generate a timestamp for the current file
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    user_input = st.text_input("You:", key=f"user_input_{counter}")

    if st.button("`Send`", help="Click here to send") or user_input:
            
        if user_input:
            # Get the predicted response for the user
            response = chatbot(user_input)

            # Get the predicted tag of the question
            tag = response[1]

            # ------------------------------------------------------------------
            # Display the current response. Chat history is displayed below
            
            # Add the predicted tag, question and answer to display chat history in a list
            # Latest answer appears at the top
            st.session_state.tag.insert(0, tag)
            st.session_state.question.insert(0, user_input)
            st.session_state.answer.insert(0, response[0])
            # message
            
            # st.write(response[0])
            if "goodbye" in response:
                st.write(response[0])
                # st.session_state.answer.insert(0, response[0])
                # st.write(st.session_state)
                # Retrieve the data from streamlit.session_state
                chat_history = convert_session_state_to_dict(st.session_state)
                
                if st.checkbox(":green[Click here to either create an account or sign-up to our mailing list]"):

                    end_of_discussion_question = st.radio("Select an option", ("Create Account", "Mailing list"))
                    if end_of_discussion_question == "Create Account":
                        st.write("Kindly visit `www.xyz.com/reg` to create an account.")
                        st.write("Thank you for chatting with me. Have a great day!")
                    elif end_of_discussion_question == "Mailing list":
                        user_email = st.text_input("Kindly enter your email address here")
                        if st.button("Enter") or user_email:
                            path = f"{EMAIL_PATH}mail-{timestamp}.txt"
                            # Create the target directory if it doesn't exist
                            if not os.path.isdir(EMAIL_PATH):
                                os.makedirs(EMAIL_PATH)
                            with open(path, "w") as mail:
                                mail.write(user_email)
                            st.success(f"Thank you for your response! I have saved your email (`{user_email}`) and will forward to the mailing team", icon="✅")
                            st.write("Thank you for chatting with me. Have a great day!")
                    else:
                        pass
                
                # clear the chat and save it as a json file before stopping
                    
                # Clear the conversation's history
                st.session_state.clear()

                # Create the target directory if it doesn't exist
                if not os.path.isdir(CHAT_HISTORY_PATH):
                    os.makedirs(CHAT_HISTORY_PATH)
                
                # Save the conversation history to file
                path = os.path.join(CHAT_HISTORY_PATH, f"chat_history-{timestamp}.json")
                with open(path, "w") as chat_file:
                    # chat_file.write(json.dump(chat_history, indent=4))
                    json.dump(chat_history, chat_file, indent=4)

                st.stop()
                

            if st.button(":red[Clear chat]"):
                clear_chat = st.selectbox("Are you sure you want to clear your chat history?", ("No", "Yes"))
                if clear_chat == "Yes":
                    st.write("Yes")
                    st.session_state.clear()
                    
                    st.success("Chat history cleared!", icon="🚨")
                    # st.stop()
                    # st.experimental_rerun()
                else:
                    pass
                    # st.stop()
            
            # Display the chat history, answer stays above
            for i in range(len(st.session_state.question)):
                message(st.session_state["answer"][i], is_user=False, key=f"answer_{i}")
                message(st.session_state["question"][i], is_user=True, key=f"question_{i}")
            # st.text_ area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")
            

        else:
            st.warning("Kindly enter your message", icon="⚠️")

if __name__ == '__main__':
    main()