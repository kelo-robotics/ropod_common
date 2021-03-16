from ropod.utils.timestamp import TimeStamp
from ropod.utils.uuid import generate_uuid

meta_model_template = 'ropod-%s-schema.json'


class MessageFactoryBase(object):
    def __init__(self):
        self.factories = {}
        self.messages = {}

    def register_factory(self, factory_name, factory):
        self.factories[factory_name] = factory

    def register_msg(self, message_name, factory):
        self.messages[message_name] = factory

    def get_factory(self, message_name):
        for factory_name, factory in self.factories.items():
            if message_name in factory.messages:
                return factory

    def create_message(self, contents, recipients=[]):
        pass

    @staticmethod
    def get_header(message_type, meta_model='msg', recipients=[]):
        if recipients is not None and not isinstance(recipients, list):
            raise Exception("Recipients must be a list of strings")

        return {"header": {'type': message_type,
                           'metamodel': 'ropod-%s-schema.json' % meta_model,
                           'msgId': generate_uuid(),
                           'timestamp': TimeStamp().to_str(),
                           'receiverIds': recipients}}

    @staticmethod
    def get_payload(contents, model):
        payload = contents.to_dict()
        metamodel = meta_model_template % model
        payload.update(metamodel=metamodel)
        return {"payload": payload}

    @staticmethod
    def update_timestamp(message):
        header = message.get('header')
        if header:
            header.update(timeStamp=TimeStamp().to_str())
        else:
            header = MessageFactoryBase.get_header(None)
            message.update(header)

    @staticmethod
    def update_msg_id(message, id=None):
        header = message.get('header')

        if header:
            if id:
                header.update(msgId=id)
            else:
                header.update(msgId=generate_uuid())
        else:
            header = MessageFactoryBase.get_header(None)
            message.update(header)

    @staticmethod
    def get_acknowledge_msg(message):
        msg = MessageFactoryBase.get_header('ACKNOWLEDGEMENT')
        message_id = message.get('header').get('msgId')
        payload = {'payload': {'receivedMsg': message_id}}
        msg.update(payload)
        return msg
