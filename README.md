## Setup Instructions
1. Clone this branch
`git clone -b cli https://github.com/Patrick-Bonini/SuperChargedChatBot`

2. Create an env file `.env` in the root directory with the contents:

```
AWS_SECRET_ACCESS_KEY=key
AWS_ACCESS_KEY_ID=id
```
Fill in the key and id with valid keys and ids

3. Create a virtual environment and install the requirements

```
pip install -r requirements.txt
```
or 
```
pip3 install -r requirements.txt
```

4. Run with 

```
python chat.py
```
or 
```
python3 chat.py
```

## Usage

Upon running `chat.py`, you will be asked to enter a URL. This can be any URL, but if the web scraper fails to get a response from the page, then it will default to SDKPerf's documentation page. You can then ask questions relating to the contents of the webpage that you entered.

To exit from the chat and enter another URL, type in any of the following commands in the chat:
```
'q', 'quit', 'leave', 'url', 'exit', 'esc', 'escape'
```

This same set of commands also allows you to exit the program as well from the `Enter URL:` prompt.
