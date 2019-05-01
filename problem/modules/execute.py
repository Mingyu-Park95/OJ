import subprocess

#gcc ../../code/%s.c -o ../../code/%s

def execute(lang, code, userName):
    if lang == 'C':
        file = open("code/%s.c" % userName, 'w')
        file.write(code)
        file.close()

        subprocess.call("gcc code/%s.c -o code/%s" % (userName, userName), shell=True)
        output = subprocess.Popen('code/%s' % userName, stdout=subprocess.PIPE, shell=True)
        print(output)
        return decode(output)

    elif lang == 'C++':
        file = open("code/%s.cpp" % userName, 'w')
        file.write(code)
        file.close()

        subprocess.call("g++ code/%s.cpp -o code/%s" % (userName, userName), shell=True)
        output = subprocess.Popen('code/%s' % userName, stdout=subprocess.PIPE, shell=True)
        print(output)
        return decode(output)

def decode(output):
    output = output.stdout.read().decode('utf8')
    return output


# subprocess에서 %s 사용가능
# a = 'code.c'
# subprocess.call("gcc %s -o execute" % a, shell=True)
# output = subprocess.Popen('./execute', stdout=subprocess.PIPE, shell=True)
# output = output.stdout.read()
# output = output.decode('ascii')
# print(output)