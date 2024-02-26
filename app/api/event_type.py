from flask import request
from flask_restful import Resource

from core.factory import factoryApp
from core.response import error_response, generate_response

from schema.event_type import EventTypeParams,EventType

from controllers.event_type import ListEventType
factory_app = factoryApp()


class EventTypeAPI(Resource):
    @error_response
    def get(self):
        query_params = {k:v for k, v in request.args.items() if v is not None}
        event_type_params = EventTypeParams(**query_params)

        data = ListEventType(factory_app,event_type_params)
        print(data)

        return generate_response(data=[EventType.from_orm(it).dict() for it in data],message="Successfully !")