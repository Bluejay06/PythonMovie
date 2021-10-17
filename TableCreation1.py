from __future__ import print_function # Python 2/3 compatibility
from datetime import date
import boto3



table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'MovieName',
            'KeyType': 'HASH'  #Partition key
        },
	{
            'AttributeName': 'Date',
            'KeyType': 'RANGE'  #Sort key
        }
    
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'MovieName',
            'AttributeType': 'S'
        },
	{
            'AttributeName': 'Date',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)