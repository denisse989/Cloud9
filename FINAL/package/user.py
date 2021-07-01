
import json
import boto3
import os

from boto3.dynamodb.conditions import Key, Attr

users_table = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)


def getInvalid(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    response = table.scan(
        FilterExpression=Attr('age').lt(27)
    )

    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }

def putInvalid(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(cabina_id)
    item = {
        'pk': cabina_id,
        'invalido': body["invalido"],
        'ciudad': body["ciudad"],
         'escuela': body["escuela"],
        'resultadoImagen': body["resultadoImagen"],
        'resultadoFinal': body["resultadoFinal"],
        'ausentes': body["ausentes"],
        'votosEmitidos': body["votosEmitidos"],
        'votosTotales': body["votosTotales"]

        
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getCity(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    movie_id = path.split("/")[-3] # ["user", "id"]
    body = json.loads(event["body"])
    response = table.get_item(
        Key={
            'pk': cabina_id,
            'sk': city
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }

def getSchool(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': cabina_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def getPerson(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    person_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': person_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putPeople(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(room_id)
    item = {
        'pk': room_id,
        'sk': 'info',
        'room_list': body["room_list"],

    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }