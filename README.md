# XYZ Chatbot Project Report

## Table of Content
1. [Technical Report](#technical-report)

* [Introduction](#introduction)


2. [Setting Up The Project](#setting-up-the-project)

3. [Project Deliverable and Walkthrough](#project-deliverable-and-walkthrough)

4. [Future Work](#future-work)

## Technical Report

#### Introduction
This report presents the development of an NLP-powered chatbot for XYZ, a fictional company. The objective of this project is to create a chatbot that can effectively handle customer queries and provide appropriate responses in real time on the XYZ website (www.xyz.com). The chatbot aims to enhance customer support and engagement by providing prompt and accurate assistance to users. This report provides an overview of the project, its functionalities, sample queries and responses, data storage considerations, implementation details, and a disclaimer about the fictional nature of XYZ.

### Project Overview
The XYZ chatbot project involves building an NLP model that understands and responds to customer requests in text format. The chatbot is designed to provide various services, including addressing technical issues, guiding customers through the return process, handling complaints, providing company information, and facilitating contact with customer service agents. Additionally, the chatbot prompts users to create an account or sign up for the XYZ mailing list, further enhancing customer engagement.

### Functionalities
The chatbot has been developed with the following key functionalities:

1. Understanding and Responding: The chatbot is capable of comprehending user queries and generating appropriate responses in real time. It employs natural language processing techniques to understand the context and intent of the queries.

2. Service Triggering: Based on user queries, the chatbot triggers specific services such as the agent service, description service, or other services as specified. For example, keywords like "speak," "chat," "talk," "staff," "customer service," or "agent" activate the agent service, providing users with two phone numbers to contact for assistance.

3. Providing Information: When users request information about XYZ, the chatbot responds with general details about the company.

4. Handling Complaints: If users express dissatisfaction or report an issue, the chatbot prompts them to provide further details about their complaint. Subsequently, the agent service is triggered, and users are provided with two phone numbers to contact for customer support.

5. Account Creation and Mailing List: At the end of the conversation, the chatbot prompts users to create an account or sign up for the XYZ mailing list. It provides a URL for registration if users express interest in creating an account, and it collects and stores user email addresses for future communication when users opt to join the mailing list.

### Sample Queries and Responses
The chatbot demonstrates its capabilities through the following sample queries and corresponding responses:

1. Query: "I recently updated my operating system, and ever since then, XYZ mobile application on my phone keeps crashing and quitting."
   - Response: The chatbot suggests restarting the phone as a potential solution. If the issue persists, it triggers the agent service for further assistance.

2. Query: "Today, I received a damaged product, how do I go about returning it?"
   - Response: The chatbot apologizes for the damaged item and provides a URL containing the return policy (www.xyz.com/return_policy).

3. Query: "My item is taking too long to be delivered."
   - Response: The chatbot apologizes for the delay and requests the user's order number. It stores the order number and complaint in JSON format for further processing.

4. Query: "Tell me about XYZ" or "What is XYZ?"
   - Response: The chatbot provides general information about XYZ company (lorem ipsum).

5. Query: "I want to speak/chat/talk to a staff/customer service/agent."
   - Response: The chatbot recognizes keywords related to speaking, chatting, talking, staff, customer service, or agent, and triggers the agent service. It provides two phone numbers that users can call for assistance.

6. Query: "I have a complaint/issue."
   - Response: The chatbot asks about the nature of the complaint and prompts users to provide more details. It then triggers the agent service, offering two phone numbers for contacting customer support.

### Data Storage
All data collected from users, including order numbers, complaints, and email addresses, is stored in a structured format, preferably JSON. This ensures accessibility and enables further analysis and processing of the collected information.

### Implementation
The chatbot can be implemented as either a simple Python application for local testing or as a web application hosted on the cloud. The implementation choice depends on the preferred environment and requirements.

### Disclaimer
It is essential to note that XYZ is a fictional company created solely for the purpose of this project evaluation. The information provided about XYZ is entirely fictitious and does not represent any real company.

### Training Data Source
As typical to every machine learning project, the volume and quality of the data availble will directly impact the performance of the project. Hence, in generating the training data, [OpenAI's ChatGPT](https://chat.openai.com/share/45e13531-10f7-49e6-b39b-0cf16504cdf3) was used to generate (over 1k) simulated question patterns and responses.

### Development Environment
This project was developed in an Ubuntu environment, using Python programming language.

### Challenges Faced

During the execution of the project, several challenges were encountered. These challenges include:

1. **Natural Language Understanding**: Developing a chatbot that can accurately understand and interpret user queries in natural language proved to be a complex task. Ensuring the chatbot comprehends various sentence structures, synonyms, and contextual nuances required extensive language modeling and fine-tuning.

2. **Service Triggering**: Identifying and triggering the appropriate services based on user queries presented a challenge. Keywords and phrases related to specific services needed to be accurately recognized to provide relevant responses.

3. **Data Storage and Accessibility**: Storing user data, such as order numbers, complaints, and email addresses, in a structured format and ensuring its accessibility for future analysis and processing posed a challenge.

4. **Testing and Validation**: Ensuring the chatbot's accuracy, responsiveness, and appropriate behavior across a wide range of user queries and scenarios posed a significant challenge. Rigorous testing and validation processes were necessary to identify and address any inconsistencies, errors, or limitations in the chatbot's performance.

6. **Integration and Deployment**: Integrating the chatbot and deploying it in a production environment required careful coordination.

Addressing these challenges required a combination of domain knowledge, expertise in natural language processing, and rigorous testing.

### Project's Limitation

- Since this is just a simulated project, the actual services and agents that it need to trigger were not setup, but provision was made for adapting them into the app if they were available.

- Also, some dummy details were used, such as contact numbers, addresses, emails etc.

### Conclusion
The development of the XYZ chatbot project aims to provide an effective solution for customer support and engagement on the XYZ website. The chatbot's NLP capabilities enable it to understand and respond to user queries, trigger relevant services, provide information, and collect and store user data. By implementing the functionalities described in this report, the chatbot enhances the overall customer experience and satisfaction on the XYZ website.

## Setting Up the Project

### For unix os (such as Linux, Ubuntu, Mac etc)

```bash
# Clone the project from GitHub
git clone https://github.com/josholam/xyz-chatbot.git

# Change into the project's directory
cd xyz-chatbot

# Create a virtual environment for the project (assuming you have venv installed)
python3 -m venv xyz_env

# Activate the virtual environment
source xyz_env/bin/activate

# Install the project's dependencies using the requirements.txt file
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

# A new window will pop open in your default browser, where you can interact with the chatbot.
```

## Project Deliverable and Walkthrough

![Project Walk Through](https://raw.githubusercontent.com/JoshOlam/xyz-chatbot/85ef5eddb0f2359944a8c01483bf7681079b837c/assets/video/XYZ%20chatbot%20Project%20Walkthrough.mp4)


The deployed web app for the chatbot can be accessed [here](https://josholam-xyz-chatbot-app-7fzmdd.streamlit.app/)


## Future Work

- Implement a spell checker: Before feeding user input to the model, apply a spell checker to correct commonly misspelled words. This helps improve the accuracy of the chatbot's understanding and response generation.

- Cache chat session state: Since Streamlit web app was used in developing the User Interface (UI) of this project, implementing a caching mechanism for the chat session state will be necessary. This avoids unnecessary reruns of the chatbot after each interaction, unless triggered by a specific button or action.

- Clear the textbox: After a user enters text and clicks the send button, clear the textbox to provide a clean interface for the next interaction. This ensures that previous user input is not retained, and users can easily input new queries.

- Move the location of the chat entry point to the bottom of the page, and ensure the app auto scrolls as responses ar generated. This will greatly improve the users' experience (UX) of the app.

- Instead of having to store all the assets and outputs for the project on the local storage of the app, a cloud storage platform could be introduced to house these resources.

