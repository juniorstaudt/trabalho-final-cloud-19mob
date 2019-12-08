import json


def handler(event, context):
    bodyString = event.get('body')
    body = json.loads(bodyString)

    dicionarioRetorno = insereNoDynamo(body['id'],body['nome'],body['email'])


    return send_success_message(dicionarioRetorno)
