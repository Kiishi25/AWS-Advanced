import json
import boto3

dynamodb = boto3.resource('dynamodb')
films= dynamodb.Table('Films')

def lambda_handler(event, context):
    title = event['queryStringParameters'].get("title")
    year = int(event['queryStringParameters'].get("year"))
    film = films.get_item(Key=dict(FilmTitle=title, ReleaseYear=year))
    film['Item']['ReleaseYear'] = str(film['Item']['ReleaseYear'])
    return {
        'statusCode': 200,
        'body': json.dumps(film['Item'])
    }