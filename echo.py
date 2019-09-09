import json

def handler(event, _):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": event["headers"]["content-type"],
        },
        "body": event["body"],
        "isBase64Encoded": event["isBase64Encoded"],
    }
