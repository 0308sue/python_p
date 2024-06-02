#replace 사용해서 공백제거
instr = '한글 Python 프로그래밍'
outstr = ''

for i in range(len(instr)):
    if instr[i] != ' ':
        outstr += instr[i]
print(outstr)
print(instr.replace(' ',''))