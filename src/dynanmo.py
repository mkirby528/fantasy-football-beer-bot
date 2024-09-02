import boto3
from boto3.dynamodb.conditions import Key, Attr

TABLE_NAME = "beer-bot-sor"
table = boto3.resource('dynamodb').Table(TABLE_NAME)


def write_to_dynamo(item: dict):
    print(f"Writing str{item} to dynamo...")
    table.put_item(Item=item)


def update_with_fulfilled(week_number, user_id):
    table.update_item(
        Key={
            'week_number': week_number,
            'user_id': user_id
        },
        UpdateExpression="set fulfilled = :value",
        ExpressionAttributeValues={
            ':value': True,
        },
    )


def get_unfulfilled_users_for_week(week_number):
    items = table.query(KeyConditionExpression=Key('week_number').eq(
        week_number), FilterExpression=Attr('fulfilled').eq(False)).get("Items",[])
    print([item for item in items])
    return [f"{item.get('user_id')}" for item in items]