from PIL import Image

# 이미지 파일 열기
image = Image.open(r"E:\sw연구_전교수님\pmg_male\head\a_vm1001.png")

# 이미지의 너비와 높이 가져오기
width, height = image.size

# 픽셀 데이터 가져오기
pixels = list(image.getdata())

row_pix = []

# 픽셀 데이터 출력 (첫 10개만 출력 예시)
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        print(f"픽셀 ({x}, {y}): {pixel}")

# 이미지 닫기 (필수는 아니지만 권장됨)
image.close()

