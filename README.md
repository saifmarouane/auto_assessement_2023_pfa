# Python template app for conversational bot
 
This uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. It is inspired from [quickstart tutorial](https://beta.openai.com/docs/quickstart).

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys and GOOGLE API Key (for STT and TTS) to the newly created `.env` file

8. Run the app

   ```bash
   $ ./run_local.sh
   ```

You should now be able to access the app at [http://127.0.0.1:5001](http://127.0.0.1:5001)!