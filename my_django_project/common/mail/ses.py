import boto3
from botocore.exceptions import ClientError
from django.conf import settings

client = boto3.client(
    "ses",
    region_name=settings.AWS_SES_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)

def send_mail(subject, body, recipient):

    try:
        response = client.send_email(
            Source=settings.AWS_SES_FROM,
            ReturnPath=settings.AWS_SES_FROM,
            Destination={
                "ToAddresses": [recipient],
            },
            Message={
                "Subject": {
                    "Data": subject,
                    "Charset": "UTF-8",
                },
                "Body": {
                    "Text": {
                        "Data": body,
                        "Charset": "UTF-8",
                    }
                },
            },
        )

        return {
            "success": True,
            "message_id": response["MessageId"],
        }

    except ClientError as e:
        return {
            "success": False,
            "error": e.response["Error"]["Message"],
        }