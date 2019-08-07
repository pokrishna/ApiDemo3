from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_http_response(self,data,status=200):
        return HttpResponse(data,content_type="application/json",status=200)

from django.core.serializers import serialize
import json
class SerializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        pdata=json.loads(json_data)
        final_list=[]
        for obj in pdata:
            final_list.append(obj['fields'])
        json_data=json.dumps(final_list)
        return json_data
