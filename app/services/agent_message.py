from datetime import datetime


class AgentMessage:

    def create(

        self,

        sender,

        receiver,

        message_type,

        payload
    ):

        return {

            "timestamp":
                datetime.now().isoformat(),

            "sender":
                sender,

            "receiver":
                receiver,

            "message_type":
                message_type,

            "payload":
                payload
        }