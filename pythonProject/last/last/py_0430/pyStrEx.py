#시험 나올듯?
#문자열 입력 받아서 거꾸로 출력
instr , outstr = '',''
count, i = 0,0

instr = input('문자열 입력 : ')
count = len(instr)

for i in range(0,count):
    outstr = outstr+instr[count-(i+1)]

print(outstr)