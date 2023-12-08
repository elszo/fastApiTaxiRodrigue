# fastApiTaxiRodrigue

## Files
- `main.py`: script for predictions and execute FastAPI server with uvicorn main:app --reload.
- `requirements.txt`: package requirements file

## Run Demo Locally 

### Shell

To test app locally, run `main.py` file on your IDE and execute the following command on cmd:

```shell
$ http post http://127.0.0.1:8000/predict pickup_longitude:=40.751237 pickup_latitude:=-73.985965 dropoff_longitude:=40.754828 dropoff_latitude:=-73.984092 hour:=15 weekday:='1' month:='5'
```
Don't forget to install httpie with `pip install httpie` to use http.
You can change the values of features.