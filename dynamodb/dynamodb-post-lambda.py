import json
import boto3

dynamodb = boto3.resource('dynamodb')
films = dynamodb.Table('Films')

def lambda_handler(event, context):
    film = eval(event['body'])
    films.put_item(Item=dict(FilmTitle=film.get('title'), ReleaseYear=film.get('year'), Runtime=film.get('runtime')))
    return {
        'statusCode': 200,
        'body': json.dumps(f"Added {film.get('title')}")
    }
