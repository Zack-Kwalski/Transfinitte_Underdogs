# Transfinnite
# Virtual-Voice-Assistant

#### Welcome to Virtual Voice Assisant, a virtual voice assistant that can help you with a variety of tasks. This project utilizes machine learning and natural language processing to create a natural and intuitive experience for users. With Virtual Voice Assistant, you can easily interact with your computer by simply speaking to it.
#### For more details checkout [Project Report](https://github.com/Krish-Depani/Virtual-Voice-Assistant/blob/main/Project%20Report%20GitHub.pdf)

## Features
Our virtual voice assistant comes packed with a wide range of features, including:
- Bringing a smile to your face with its ability to tell you jokes.
- Telling you your IP address, so you can stay connected.
- Testing your internet speed, so you can ensure you're getting the best connection.
- Editing content for you.
- Giving you brief information (3 sentences) on any topic or personality.
- Performing math operations and answering any general queries or GK questions.
- Taking notes, so you can keep track of important information.
- Saving your chat history, so you can refer back to it later.
- Performing internet search, so you can find the information you need.


## API Keys
To run this program you will require the following API,
-OpenAI API

## Installation

Please make sure that Python and pip are installed on your system before proceeding with the installation.

Open a terminal and navigate to your home directory.

Obtain all necessary API keys and open the file Virtual-Voice-Assistant/Data/.env to insert the keys into the designated placeholder fields.

Run the setup script by using the command

python setup.py


Navigate to the `` directory and run the below command to start the virtual voice assistant.

python main.py


You're all set! The virtual voice assistant should be up and running now.

## Code Structure

    ├── Virtual-Voice-Assistant
        ├── Data                              
            ├── .env                          # Stores the API keys, email and password.
            ├── chat_model                    # Directory that stores the trained model used to understand user's intent
            ├── chats.db                      # Database file that stores the chat history
         ├── Plugins
            ├── API_functionalities.py        # Contains functions that interact with different APIs
            ├── browsing_functionalities.py   # Contains functions for web browsing
            ├── database.py                   # Contains functions for interacting with the chat history database
                        ├── main.py                       # It is the entry point of the virtual voice assistant                    ├── requirements.txt                  # Lists the dependencies required for the project
        └── setup.py                          # Contains code for setting up the virtual voice assistant


## Thanks for checking out!!
