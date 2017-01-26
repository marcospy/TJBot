from mongoengine import *


class Questao(Document):
    prova = StringField(required=True)
    enunciado = StringField(required=True)
    alternativas = DictField(required=True)
    resposta = StringField(required=True, max_lenght=1)


class User(Document):
    telegram_id = LongField(required=True)
    respondidas = ListField(ReferenceField(Questao))
    acertos = ListField(ReferenceField(Questao))
    erros = ListField(ReferenceField(Questao))

    meta = {
        'indexes': [
            'telegram_id',
        ],
    }
