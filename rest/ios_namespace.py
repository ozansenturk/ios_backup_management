from flask_restx import Namespace, Resource, fields
import http.client
from backend import services

api_ns = Namespace('api', description='IOS Backup')


backup_input = api_ns.model('input', {
    'udid': fields.String(description='The UDID of the device to read from'),
    'password': fields.String(description='The plain text password for the encrypted backup'),
    'media': fields.Boolean(description='0 or 1, if 1 parse media/photos/videos, if 0 do not'),
    'output': fields.String(description='place where to save the files (overwrite existing files)')
})

backup_output = api_ns.model('output', {
    'udid': fields.String(description='The UDID of the device to read from'),
    'name': fields.String(description='name'),
    'ios': fields.String(description='ios version'),
    'serial': fields.String(description='serial'),
    'type': fields.String(description='type of device'),
    'encrypted': fields.Boolean(description='boolean')
})

backup_outputs = api_ns.model('outputs', {
    'data':fields.List(fields.Nested(backup_output))
})

@api_ns.route('/getDeviceList/')
class Reservations(Resource):

    @api_ns.doc('Devices')
    @api_ns.marshal_with(backup_outputs, code=http.client.OK)
    def get(self):
        '''Get all reservations'''
        data = api_ns.payload
        api_ns.logger.debug("data {}".format(data))

        # data_json = services.serialization(data)

        raw_response = services.get_devices()
        print("raw response {}".format(raw_response))
        return raw_response