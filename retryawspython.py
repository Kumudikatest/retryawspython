import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://paper-api.alpaca.markets/v2/calendar",
            params={"start":"1587534033","end":"1587620433"},
            headers={"Accept":"application/json"}
        )
        # your code goes here
        print(res)
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
