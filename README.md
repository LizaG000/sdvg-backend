# <img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="50"/> SDVG server instructions

## Requirements
 Firstly you should install python and dependencies for this project

 ```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Start up
1. Copy `.env.sample` file and rename it for `.env`
  ```bash
  cp .env.sample .env
  ```
2. Run the server
```bash
python main.py
```
![](https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif)

## Fallbacks
If you have some troubles please contact me
Ernest Litvinenko
<a href="mailto:ernest@elitvinenko.tech">ernest@elitvinenko.tech</a>
TG: @ernestlitvinenko

## Generation of a private key.
```bash
openssl genrsa -out private.pem 2048
```

## Generation of a public key.
```bash
openssl rsa -in private.pem -pubout -out public.pem
```
