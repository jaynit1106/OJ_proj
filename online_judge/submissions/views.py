from distutils.log import error
from http.client import NOT_FOUND
from pydoc import doc
from time import sleep
from django.shortcuts import render,redirect
from django.http import HttpResponse
import subprocess
import docker
from docker.models.containers import Container
from matplotlib.style import use
from submissions.models import Submission
from testcases.models import Testcase
from django.contrib.auth.models import User
from problems.models import Problem
import os
# Create your views here.

client=docker.from_env()
docker_img_python = 'python'
docker_img_gcc = 'gcc'

def submit(request,question_name,username):
    if request.method == 'POST':
        code=request.POST['code']
        language=request.POST['language']
        testcases=Testcase.objects.all()
        inputs=[]
        real_outputs=[]
        
        #getting the testcases
        for testcase in testcases:
            if(str(testcase.question_name) == str(question_name)):
                inputs.append(testcase.input_tc)
                txt_file=open(os.path.join('C:\OJ_proj\online_judge\media',str(testcase.output_tc)),'r')
                data=txt_file.read()
                txt_file.close()
                real_outputs.append(str(data))        
        
        outputs=[]
        
        #creating a docker container
        try:
            container:Container=client.containers.get(username)
            if(container.status != 'running'):
                container.start()
        except docker.errors.NotFound:
            if(language=='C++'):
                container = client.containers.run(docker_img_gcc,detach=True,tty=True,name=username)
            if(language=='Python'):
                container = client.containers.run(docker_img_python,detach=True,tty=True,name=username)

        #finding output for each input testcase
        for input in inputs:
            file= os.path.join('C:\OJ_proj\online_judge\media',str(input))
            best_file=os.path.join('C:\OJ_proj\online_judge','best.sh')
            container_string=container.id
            try:
                if language == "C++":  #managing C++ files
                    f = open("demo.cpp", "w")
                    f.write(str(code))
                    f.close()
                    #send files
                    subprocess.run(['docker','cp','C:\OJ_proj\online_judge\demo.cpp',str(container_string)+':/demo.cpp'])
                    subprocess.run(['docker','cp',file,str(container_string)+':/input.txt'])

                    #run files
                    subprocess.run(['docker' ,'exec' ,str(container_string),'bash','-c',"g++ demo.cpp"],timeout=5)
                    subprocess.run(['docker' ,'exec' ,str(container_string),'bash','-c',"./a.out<input.txt>output.txt"],timeout=5)
                    
                    #bring back the files
                    temp=str(container_string)+':/output.txt'
                    output_file_add='C:\OJ_proj\online_judge\output'+ str(container_string) + '.txt'

                    subprocess.run(['docker','cp',temp,output_file_add])
                    with open(output_file_add,'r') as f:
                        text = f.read().rstrip()
                    ans=text
                    os.remove(output_file_add)
                
                if language=='Python': #managing python files
                    f = open("demo.py", "w")
                    f.write(str(code))
                    f.close()

                    #send files
                    subprocess.run(['docker','cp','C:\OJ_proj\online_judge\demo.py',str(container_string)+':/demo.py'])
                    subprocess.run(['docker','cp',file,str(container_string)+':/input.txt'])

                    #run files
                    subprocess.run(['docker' ,'exec' , container.id,'bash','-c',"python demo.py<input.txt>output.txt"],timeout=5)

                    #bring back the files
                    temp=str(container_string)+':/output.txt'
                    output_file_add='C:\OJ_proj\online_judge\output'+ str(container_string) + '.txt'

                    subprocess.run(['docker','cp',temp,output_file_add])
                    subprocess.run(['docker','exec','-it',str(container_string),'rm','demo.py'])
                    
                    
                    with open(output_file_add,'r') as f:
                        text = f.read().rstrip()
                    ans=text
                    os.remove(output_file_add)                    
            except:
                submission=Submission(username=User.objects.get(username=username),question_name=Problem.objects.get(question_name=question_name),code=code,language=language,status='Compilation Error')
                submission.save()
                return redirect("http://localhost:8000/"+str(username)+"/submissions")

            
            
            outputs.append(str(ans))
            
        #removing the docker container
        subprocess.run(['docker','stop',container.id ])
        subprocess.run(['docker','rm',container.id ])

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
    submissions.reverse()
    return render(request,'submissions.html',{'submissions':submissions})

def view_code(request,code_id,username):
    code=Submission.objects.get(pk=code_id)
    if(str(username) != str(code.username)):
        return HttpResponse("Invalid User")
    code=code.code
    return render(request,'code.html',{'code':code})
