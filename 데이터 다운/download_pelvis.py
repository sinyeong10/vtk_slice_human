import urllib.request

# 다운받을 이미지의 범위를 지정합니다.
start_index = 1732
end_index = 2028

# 이미지 다운로드를 위한 기본 URL
base_url = "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Male-Images/PNG_format/pelvis/a_vm"

# 이미지를 다운로드할 디렉토리 경로
download_dir = r"E:\sw연구_전교수님\pmg_male\pelvis"

# 반복문을 사용하여 이미지 다운로드
for i in range(start_index, end_index + 1):
    # 현재 이미지의 URL 생성
    current_url = f"{base_url}{i}.png"

    # 이미지를 다운로드할 파일 경로 생성
    file_path = f"{download_dir}\\a_vm{i}.png"

    try:
        # 이미지 다운로드
        urllib.request.urlretrieve(current_url, file_path)
        print(f"Downloaded: a_vm{i}.png")
    except Exception as e:
        print(f"Error downloading a_vm{i}.png: {str(e)}")

print('다운로드가 완료되었습니다.')
