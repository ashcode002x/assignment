import os 
import asyncio


log_file_path="./log/sample.log"


async def sendLog():
    # print("working")
    with open(log_file_path,'r') as f:
        lines=read10LineReverse()
        f.seek(0,os.SEEK_END)
        # lines=lines[::-1]
        for line in lines:
            yield line
        while True:
            line=f.readline()
            if not line or line=="\n":
                await asyncio.sleep(2)
                continue
            # print(line)
            yield line

# def send_last_10_line():

def read10LineReverse():
    lines=[]
    with open(log_file_path) as f:
        f.seek(0,os.SEEK_END)
        position=f.tell()
        line=""
        curr=10
        while position>=0 and curr>0:
            f.seek(position)
            next_char=f.read(1)
            # print(next_char,end=" ")
            if next_char=='\n':
                if line:
                    line=line[::-1]
                    lines.append(line)
                    curr-=1
                line=''
            else:
                line+=next_char
            position-=1
        if line:
            lines.append(line)
            curr-=1
        # print(lines)
    return lines[::-1]
     
