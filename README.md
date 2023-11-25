# Zoommarizer

## Description
Zoommarizer is a python application that allows to summarize Zoom meetings (or anything else). It is built using OpenAI technology such as GPT-3.5 and Whisper.

## Installation
1. Clone the repository
2. (Optional) Create a virtual environment using `python -m venv venv` (If that doesn't work, try `python3 -m venv venv` or install virtualenv using `pip install virtualenv`)
3. Install the requirements using `pip install -r requirements.txt`
4. Create a `.env` file in the root directory and add the following variables:
```
OPENAI_API_KEY=<your openai api key>
// Example: OPENAI_API_KEY=sk-1234567890
```

## Usage
1. Run the application using `py main.py --video VIDEO-NAME` (If that doesn't work, try `python3 main.py --video VIDEO-NAME`)
2. The summary will be saved in the `transcript.txt` folder

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/) Feel free to use this code for whatever you want.

## Authors
- [Enrique Madrid]('https://github.com/nervesscat')


