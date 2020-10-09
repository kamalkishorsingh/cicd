def hello(event, context):
    body = {
        "message": "Go Serverless dev env v1.0! Your function executed successfully for dev env!",
        "input":event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
