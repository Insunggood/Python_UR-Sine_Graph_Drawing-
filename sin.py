import math

x = -0.250      # 초기 x값 설정
y = -0.250      # 초기 y값 설정
z = 0           # z값 초기화

with open('commands01.txt','a') as f:   # .txt 파일 열기
    for i in range(0, 200):             # 좌표 200개 생성
        x += 0.003                      # x 이동거리
        z += math.pi/20                 # sin 값
        lmt_z = math.sin(z)/10       # sin 값 이동거리 제한
        result = "movej(p[%f,%f,0.25 + %f,0.0,2.2,-2.2],a=20,v=20,t=0,r=0)\n"%(x,y,lmt_z)
        f.write(result)