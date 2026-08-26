# import io
# from rest_framework.parsers import JSONParser
# from django.shortcuts import render
# from .models import Data
# from .serializers import DataSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse


# # Create your views here.
# def data_list(req):
#     if req.method=="POST":
#         json=req.body
#         print(json)
#         print(type(json))
#         stream = io.BytesIO(json)
#         print(stream)
#         print(type(stream))
#         p_data=JSONParser().parse(stream)
#         print(p_data)
#         print(type(p_data))
#         serializer=DataSerializer(data=p_data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             data={
#                 'msg':"Object Created..."
#             }
#             json=JSONRenderer().render(data)
#             return HttpResponse(json,content_type='application/json')
#         else:
#             json = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json,content_type='application/json')
#     x=Data.objects.all()
#     serializer=DataSerializer(x,many=True)
#     print(serializer)
#     print(serializer.data)
#     json=JSONRenderer().render(serializer.data)
#     print(json)
#     return HttpResponse(json,content_type='application/json')

        

# def data_detail(req,pk):
#     x = Data.objects.get(id=pk)
#     serializer = DataSerializer(x)
#     print(serializer)
#     print(serializer.data)
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#     return HttpResponse(json,content_type='application/json')











# _____________________________________________________________________________________
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
@api_view(['GET', 'POST'])
def stu_list(req):
    if req.method=='POST':
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return Response(serializer.data)


	
@api_view(['GET','PUT','PATCH','DELETE'])
def stu_details(req,pk):
	u_id = Student.objects.filter(id=pk)
	if u_id:
		if req.method=='PUT':
			snippet = Student.objects.get(id=pk)
			serializer = StudentSerializer(snippet, data=req.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		elif req.method=='PATCH':
			snippet = Student.objects.get(id=pk)
			serializer = StudentSerializer(snippet, data=req.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		elif req.method=='DELETE':
			snippet = Student.objects.get(id=pk)
			snippet.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		
		snippet = Student.objects.get(id=pk)
		serializer = StudentSerializer(snippet)
		return Response(serializer.data)
	else:
		return Response({}, status=status.HTTP_400_BAD_REQUEST)