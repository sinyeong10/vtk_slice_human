import sys

# 새로운 디렉토리 경로
new_path = r"C:\sin\vtk\slice_human\2_3D객체작업\예시"

# sys.path에 디렉토리 추가
sys.path.append(new_path)

from 부채꼴자르기 import sector_cutting1
from Vector3D import Vector3D
#Vector3D.py파일에서 Vector3D 클래스를 사용
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

sector_cutting1()

class Probe:
    def __init__(self, P1:Vector3D, V1:Vector3D, V2:Vector3D):
        self.Point = P1
        self.front = V1
        self.above = V2

    def rotate(self, theta, radius):
        pass

    def translate(self, moveVector : Vector3D);
        pass
    
    def getObserve():
        pass
    