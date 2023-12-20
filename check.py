import os
import timeit
final=[]
res=[]
time=[]
time_libc=[]
def get_ls():
    r=os.popen("ls testcases")
    info=r.readlines()
    info1=[] # 第一级目录
    for line in info:
        line=line.strip("\n")
        info1.append("testcases/"+line)
    for i in info1:
        r=os.popen("ls "+i)
        info=r.readlines()
        for line in info:
            line=line.strip("\n")
            final.append(i+"/"+line)
    # print(final)
get_ls()

def run(str):
    os.system("cd ..")
    os.system("cargo run -- "+str+" > input.s")
    start=timeit.default_timer()
    os.system("qemu-riscv32 a.out")
    end=timeit.default_timer()
    time.append(end-start)
    os.system("riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -O2 "+str)
    start2=timeit.default_timer()
    os.system("qemu-riscv32 a.out")
    end2=timeit.default_timer()
    time_libc.append(end2-start2)
    print(str+" runtime : ")
    print("sysyc: ",end="")
    print(end-start)
    print("gcc: ",end="")
    print(end2-start2)
    #os.system("cd sysyc-tests")
#run(final[0])

def __main__():
    for i in final:        
        run(i)
            
__main__()