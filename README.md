<h1>TeleBot Call API Project</h1>

This project contains a Python script to make API calls to a server that initiates phone calls with specified scripts.

<h2>Features</h2>

   - Accepts input for welcome, cancel, and wait scripts along with a phone number.
   - Constructs an API call to https://telebotserver.onrender.com/make_call with the provided parameters.
   - Sends a GET request to the server.
   - Provides feedback on the success or failure of the API call.

<h2>Prerequisites</h2>

   - Python 3.x
   - requests library

<h2>Installation</h2>
1.) Clone the repository:

    git clone https://github.com/your-username/telebot-call-api.git

2.) Navigate to the project directory:

    cd telebot-call-api

3.) Install the requests library if you haven't already:

    pip install requests

<h2>Usage</h2>

1.)  Run the script:

    python telebot_call.py
2.)  Follow the prompts to input the welcome script, cancel script, wait script, and phone number.

3.)  The script will construct and send an API call to the server and print the result of the call.

<h2>Example</h2>

When you run the script, you will be prompted to provide the necessary inputs:

    Please provide the following inputs:
    Welcome Script: Hello, welcome to our service.
    Cancel Script: Your call has been canceled.
    Wait Script: Please hold on for a moment.
    Phone Number: 1234567890

The script will then make an API call to the server and print whether the call was successful or not:


    API call successful.

or


    API call failed with status code: <status_code>

<h2>Contributing</h2>

*Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for improvements or new features.*
