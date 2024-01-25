#500 700 1800 x,y,z의 값
import numpy as np
import matplotlib.pyplot as plt

def draw_color_circle(size, color_value):
    # 원의 중심 좌표
    center_x, center_y = size // 2, size // 2

    # 원의 반지름
    radius = size // 4

    # 배열 생성 (흰색으로 초기화)
    image = np.ones((size, size, 3), dtype=np.uint8) * 255

    # 원 그리기
    for i in range(size):
        for j in range(size):
            distance = np.sqrt((i - center_x)**2 + (j - center_y)**2)
            if distance < radius:
                # 원 안의 영역에 색상 값 적용 (color_value에 따라 RGB 값 설정)
                intensity = color_value
                image[i, j] = [intensity, intensity, intensity]

    return image


# 이미지를 JPG 파일로 저장
for i in range(256):
    # 이미지 크기와 색상 값 설정
    image_size = 500
    color_value = i #[color_value, 0, 0]로 처리  # 0부터 255까지의 값을 사용하여 색상 설정

    # 원 그리기
    result_image = draw_color_circle(image_size, color_value)

    # # 이미지 시각화
    # plt.imshow(result_image)
    # plt.title('Color Circle')
    # plt.show()

    output_file_path = f'semi-updown-test/0_image_create/data/color_image_{i}.jpg'
    plt.imsave(output_file_path, result_image)
    if i % 20 == 0:
        print(f'이미지가 {output_file_path}에 저장되었습니다.')
