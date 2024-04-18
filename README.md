## Setup Instructions
Clone repository
```
git clone https://github.com/Patrick-Bonini/SuperChargedChatBot
```

## Backend

1. Create an env file `.env` in the root directory with the contents:

```
AWS_SECRET_ACCESS_KEY=key
AWS_ACCESS_KEY_ID=id
```
Fill in the key and id with valid keys and ids

2. Create a virtual environment and install the requirements

```
pip install -r requirements.txt
```

3. Change directories and run chat

```
cd backend
```

```
python server.py
```

## Frontend

1. cd to frontend and install dependencies

```
cd frontend
```

```
npm install
```

2. Run frontend

```
npm start
```


