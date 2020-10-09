def hello(event, context):
    body = {
        "message": "Go Serverless Prod env v1.0! Your function executed successfully for prod env!",
        "input":event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
