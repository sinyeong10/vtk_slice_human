from PIL import Image

# .raw 파일 경로 및 이미지 너비와 높이 설정
file_path = "C:/sin/vtk/a_vm2560.raw"  # .raw 파일 경로
width = 2048                     # 이미지 너비
height = 2048                     # 이미지 높이
mode = "L"                       # 이미지 모드 (예: "L"는 흑백 이미지, CT용, RGB로 색 가능)

# .raw 파일 열기
with open(file_path, "rb") as file:
    raw_data = file.read()

# 이미지 생성
image = Image.frombytes(mode, (width, height), raw_data)

# 이미지 표시
image.show()