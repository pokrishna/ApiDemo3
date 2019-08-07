from django.shortcuts import render
from django.views.generic import View
from myapp.utils import is_json
from myapp.mixins import HttpResponseMixin,SerializeMixin
import json
from myapp.models import Student
from myapp.forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class StudentCBV(View,SerializeMixin,HttpResponseMixin):
    def get_object_by_id(id):
        try:
            obj=Student.object.get(id=id)
        except Student.DoesNotExist:
            s=None
        return obj

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send me json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(request.body)
        id=pdata.get('id',None)
        if id is not None:
            std=self.get_object_by_id(id)
            if std is None:
                json_data=json.dumps({'msg':'object does not exist'})
                return self.render_to_http_response(json_data,status=400)
            json_data=self.serialize([std,])
            return self.render_to_http_response(json_data,status=200)
        qs=Student.objects.all()
        print("Query Set---: ",qs)
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data,status=200)

    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(request.body)
        if not valid_json:
            return render_to_http_response(json.dumps({'msg':'Pls send me valid data'}),status=400)
        pdata=json.loads(request.body)
        stuForm=StudentForm(pdata)
        if stuForm.is_valid():
            stuForm.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'Resource created successfully'}),status=201)
        if stuForm.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        json_valid=is_json(request.body)
        if not json_valid:
            return render_to_http_response(json.dumps({'msg':'Pls send me valid data'}),status=400)
        pdata=json.loads(request.body)
        id=pdata.get('id',None)
        print(id)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'Pls send me valid id'}),status=400)
        obj=Student.objects.get(id=id)
        if obj is None:
            return render_to_http_response(json.dumps({'msg':'Obj does not exist'}),status=400)
        old_obj={
            "name":obj.name,
            "rollno":obj.rollno,
            "marks":obj.marks,
            "gf":obj.gf,
            "bf":obj.bf,
        }
        old_obj.update(pdata)
        form=StudentForm(old_obj,instance=obj)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'Resource Updated successfully'}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return selr.render_to_http_response(json_data,status=400)
    def delete(self,request,*args,**kwargs):
        valid_json=is_json(request.body)
        if not valid_json:
            return render_to_http_response(json.dumps({'msg':'Pls send me valid data'}),status=400)
        data=json.loads(request.body)
        id=data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'Require id'}),status=400)
        obj=Student.objects.get(id=id)
        if obj is None:
            return self.render_to_http_response(json.dumps({'msg':'Obj Doesnot Exist'}),status=400)
        status,deleted_item=obj.delete()
        if status==1:
            json_data=json.dumps({'msg':'Resource deleted Successfully'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'unable to delete'})
        return self.render_to_http_response(json_data,status=500)
