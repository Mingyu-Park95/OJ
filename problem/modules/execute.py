import os
import subprocess

#gcc ../../code/%s.c -o ../../code/%s

def execute(lang, code, userName, problem_id):
    if lang == 'C':
        file = open("code/%s.c" % userName, 'w')
        file.write(code)
        file.close()

        # 입력 있는 경우
        subprocess.call("gcc code/%s.c -o code/%s" % (userName, userName), shell=True)

        # 명령줄 하나로 실행결과 파일, 수행시간 파일 생성
        subprocess.call("(time code/%s < inputFile/%s.txt) > code/%s.txt 2> code/%stime.txt" % (userName, problem_id, userName, userName), shell=True)

        # 파일에 저장하고 값 받아오기
        f = open("code/%s.txt" %userName, 'r')
        output = f.read()
        f.close()

        # 수행 시간 받아오기
        f = open("code/%stime.txt" %userName,'r')
        runtime = f.readline()
        runtime=runtime[0:4]

        # 소스코드 삭제 - 중복 방지
        subprocess.call("rm code/%s.c"% userName, shell=True)
        return output, runtime

    elif lang == 'C++':
        file = open("code/%s.cpp" % userName, 'w')
        file.write(code)
        file.close()

        subprocess.call("g++ code/%s.cpp -o code/%s" % (userName, userName), shell=True)

        subprocess.call("(time code/%s < inputFile/%s.txt) > code/%s.txt 2> code/%stime.txt" % (
        userName, problem_id, userName, userName), shell=True)

        f = open("code/%s.txt" % userName, 'r')
        output = f.read()
        f.close()

        f = open("code/%stime.txt" % userName, 'r')
        runtime = f.readline()
        runtime = runtime[0:4]

        # 소스코드 삭제 - 중복 방지
        subprocess.call("rm code/%s.c" % userName, shell=True)
        return output, runtime

    elif lang == 'JAVA':
        subprocess.call("mkdir %s" % (userName), shell=True)
        file = open("%s/Main.java" % userName, 'w')
        file.write(code)
        file.close()

        subprocess.call("javac ./%s/Main.java" % (userName), shell=True)
        subprocess.call("(time java -cp %s Main < inputFile/%s.txt) > %s/Main.txt 2> %s/Maintime.txt" % (userName, problem_id, userName, userName), shell=True)
        f = open("%s/Main.txt" %userName, 'r')
        output = f.read()
        f.close()

        # 수행 시간 받아오기
        f = open("%s/Maintime.txt" %userName,'r')
        runtime = f.readline()
        runtime=runtime[0:4]

        subprocess.call("rm %s/Main.java" % userName, shell=True)
        return output, runtime
# def decode(output):
#     output = output.stdout.read().decode('utf8')
#     return output


# subprocess에서 %s 사용가능
# a = 'code.c'
# subprocess.call("gcc %s -o execute" % a, shell=True)
# output = subprocess.Popen('./execute', stdout=subprocess.PIPE, shell=True)
# output = output.stdout.read()
# output = output.decode('ascii')
# print(output)