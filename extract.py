import os
import zipfile

# 원본 압축 파일이 들어 있는 디렉터리 경로
source_directory = r'C:\Users\이제영\Downloads'

# 압축 파일을 풀 디렉터리 경로
destination_directory = r'C:\Users\이제영_노트북용\sw연구_전병환교수님'

# 압축 파일의 확장자 목록 (여기서는 .zip 파일로 가정)
zip_extensions = ['.zip']

# 디렉터리 내의 모든 압축 파일을 풀기
for root, _, files in os.walk(source_directory):
    for filename in files:
        if any(filename.endswith(ext) for ext in zip_extensions):
            file_path = os.path.join(root, filename)

            # 압축 파일을 다른 디렉터리로 풀기
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_directory)

            print(f'압축 해제 완료: {filename}')

print('모든 압축 파일을 다른 디렉터리로 풀었습니다.')
