from sys import stderr
from black import out
from django.shortcuts import render,redirect
from django.http import HttpResponse
import subprocess

from matplotlib.style import use
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
            file= os.path.join('C:\OJ_proj\online_judge\media',str(input))
            try:
                if language == "C++":  #managing C++ files
                    f = open("demo.cpp", "w")
                    f.write(str(code))
                    f.close()
                    subprocess.run(['docker','cp','C:\OJ_proj\online_judge\demo.cpp','79ae93e3b6f0:/demo.cpp'])
                    subprocess.run(['docker','cp',file,'79ae93e3b6f0:/input.txt'])
                    subprocess.run(['docker','exec','-it','79ae93e3b6f0','g++','demo.cpp','-o','ans.exe'])
                    subprocess.run(['docker','exec','-it','79ae93e3b6f0','//bin//sh','./best.sh'],timeout=5)
                    subprocess.run(['docker','cp','79ae93e3b6f0:/output.txt','C:\OJ_proj\online_judge\output.txt'])
                    subprocess.run(['docker','exec','-it','79ae93e3b6f0','rm','output.txt'])
                    subprocess.run(['docker','exec','-it','79ae93e3b6f0','rm','ans.exe'])
                    with open('output.txt','r') as f:
                        text = f.read().rstrip()
                    ans=text
                if language=='Python': #managing python files
                    f = open("demo.py", "w")
                    f.write(str(code))
                    f.close()
                    output = subprocess.run(['python',"C:\OJ_proj\online_judge\demo.py"],stdin=open(file,'r'),stdout=open('python_output.txt','w'),timeout=5)
                    with open('python_output.txt','r') as f:
                        text = f.read().rstrip()
                    ans=text                    
            except:
                submission=Submission(username=User.objects.get(username=username),question_name=Problem.objects.get(question_name=question_name),code=code,language=language,status='Compilation Error')
                submission.save()
                return redirect("http://localhost:8000/"+str(username)+"/submissions")

            
            
            outputs.append(str(ans))
            f = open("output.txt", "w")
            f.write("-------")
            f.close()

        if(real_outputs == outputs):
            submission=Submission(username=User.objects.get(username=username),question_name=Problem.objects.get(question_name=question_name),code=code,language=language,status='Accepted')
            submission.save()
            return redirect("http://localhost:8000/"+str(username)+"/submissions")
        else:
            submission=Submission(username=User.objects.get(username=username),question_name=Problem.objects.get(question_name=question_name),code=code,language=language,status='Wrong Answer')
            submission.save()
            return redirect("http://localhost:8000/"+str(username)+"/submissions")
    else:
        return HttpResponse("galat hai bhai")


from .models import Submission

def view_submissions(request,username):
    all_submissions=Submission.objects.all()
    submissions=[]
    
    for submission in all_submissions:
        if(str(submission.username)==str(username)):
            submissions.append(submission)
    # print(submissions)
    submissions.reverse()
    # print(submissions)
    return render(request,'submissions.html',{'submissions':submissions})

def view_code(request,code_id,username):
    code=Submission.objects.get(pk=code_id)
    if(str(username) != str(code.username)):
        return HttpResponse("Invalid User")
    code=code.code
    return render(request,'code.html',{'code':code})
