from sys import stderr
from django.shortcuts import render,redirect
from django.http import HttpResponse
import subprocess
from submissions.models import Submission
from testcases.models import Testcase
from django.contrib.auth.models import User
from problems.models import Problem
import os
# Create your views here.



def submit(request,question_name,username):
    if request.method == 'POST':
        code=request.POST['code']
        language=request.POST['language']
        testcases=Testcase.objects.all()
        inputs=[]
        real_outputs=[]
        
        
        for testcase in testcases:
            if(str(testcase.question_name) == str(question_name)):
                inputs.append(testcase.input_tc)
                txt_file=open(os.path.join('C:\OJ_proj\online_judge\media',str(testcase.output_tc)),'r')
                data=txt_file.read()
                txt_file.close()
                real_outputs.append(str(data))        
        
        outputs=[]
        for input in inputs:
            f = open("demo.cpp", "w")
            f.write(str(code))
            f.close()

            file= os.path.join('C:\OJ_proj\online_judge\media',str(input))
            try:
                output = subprocess.run(['g++','C:\OJ_proj\online_judge\demo.cpp','-o','outputfile.exe'], capture_output=True, shell =True,text=True, input="C:\OJ_proj\online_judge\media\input\input.txt", check=True, timeout=5)
                output = subprocess.run(['outputfile.exe','<',file], capture_output=True, shell =True,text=True, input="C:\OJ_proj\online_judge\media\input\input.txt", check=True, timeout=5)
            except:
                submission=Submission(username=User.objects.get(username=username),question_name=Problem.objects.get(question_name=question_name),code=code,language=language,status='Compilation Error')
                submission.save()
                return redirect("http://localhost:8000/ramesh/submissions")

            ans=output.stdout
            
            outputs.append(str(ans))

        if(real_outputs == outputs):
            submission=Submission(username=User.objects.get(username=username),question_name=Problem.objects.get(question_name=question_name),code=code,language=language,status='Accepted')
            submission.save()
            return redirect("http://localhost:8000/ramesh/submissions")
        else:
            submission=Submission(username=User.objects.get(username=username),question_name=Problem.objects.get(question_name=question_name),code=code,language=language,status='Wrong Answer')
            submission.save()
            return redirect("http://localhost:8000/ramesh/submissions")
    else:
        return HttpResponse("galat hai bhai")


from .models import Submission

def view_submissions(request,username):
    all_submissions=Submission.objects.all()
    submissions=[]
    for submission in all_submissions:
        if(str(submission.username)==str(username)):
            submissions.append(submission)
    return render(request,'submissions.html',{'submissions':all_submissions})