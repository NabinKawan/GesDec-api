# GesDec-api
This repo provides the basic APIs for fetching and feedback for GesDec-web. 

The server is primarily deployed at:
```
http://gesdec-api.herokuapp.com
```

## Running it locally
```shell
# Install the dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:api --reload
```
The server can be access at:
```
http://localhost:8000/docs
```
