import config
from umqtt.robust import MQTTClient
import ujson as json

class MQTT(object):

    client = object

    def __init__(self):
        print("## MQTT object created")
        self.__connect()
        self.__subscribe()
        self.client.check_msg()
        # self.__poll()

    def ping():
        return self.client.ping()

    # Topic is only relevant if #topic# is used within the publish configuration
    def publish(self, message, topic="info"):
        print("### Sending a message")
        try:
            message = json.dumps({
                "client": config.config['mqtt']['client'],
                "topic": topic,
                "message": message
            })
            self.client.publish(
                # bytes(str(config.config['mqtt']['topics']['pub'].format(config.config['mqtt']['client'])), 'utf-8'), 
                bytes(str(self.__makeTopic(config.config['mqtt']['topics']['pub'], topic)), 'utf-8'),
                bytes(str(message), 'utf-8')
            )
        except Exception as inst:
            self.__error(inst, " - **Abort Abort** _Failed sending a message_")

    def disconnect(self):
        self.client.disconnect()

    def __makeTopic(self, template, topic="info"):
        return template \
            .replace('#topic#', topic) \
            .replace('#hostname#', config.config['hostname']) \
            .replace('#client#', config.config['mqtt']['client']) \
            .replace('#server#', config.config['mqtt']['server']) \
            .replace('#username#', config.config['mqtt']['username'])

    def __poll(self):
        print("### Checking for a new config")
        try:
            self.client.check_msg()
        except Exception as inst:
            self.__error(inst, " - **Abort Abort** _Failed polling the server_")

    def __incoming(self, topic, msg):
        print("### Handling incoming request")
        try:
            print((topic,msg))
        except Exception as inst:
            self.__error(inst, " - **Abort Abort** _Failed handling incoming message_")

    def __subscribe(self):
        print("### Subscribing to topic")
        try:
            self.client.subscribe(
                # bytes(str(config.config['mqtt']['topics']['sub'].format(config.config['mqtt']['client'])), 'utf-8')
                bytes(str(self.__makeTopic(config.config['mqtt']['topics']['sub'])), 'utf-8'),
            )
        except Exception as inst:
            self.__error(inst, " - **Abort Abort** _Failed during subscription_")

    def __connect(self):
        try:
            print("### Attempting to create client!")
            self.client = MQTTClient(
                client_id=bytes(str(config.config['mqtt']['client']), 'utf-8'), server=config.config['mqtt']['server'], 
                user=config.config['mqtt']['username'], password=config.config['mqtt']['password']
            )
            self.client.DEBUG = True
            self.client.set_callback(self.__incoming)
            self.client.connect(clean_session=False)
        except Exception as inst:
            self.__error(inst, " - **Abort Abort** _MQTT exception in client definition?_")

    def __error(self, exception, msg=" - **Abort Abort** _Something went wrong_"):
        print(" - **Exception raised!!!!**")
        print(msg)
        print(type(exception))
        print(exception.args)
        print(exception)
        print(config.config['mqtt'])
        pass
