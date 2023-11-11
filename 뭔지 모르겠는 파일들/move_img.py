import os
import shutil

# 원본 디렉터리 경로
source_directory = r'C:\Users\이제영_노트북용\sw연구_전병환교수님'

# 대상 디렉터리 경로
destination_directory = r'C:\Users\이제영_노트북용\sw연구_전병환교수님\이미지만'

# .raw 파일을 찾아서 대상 디렉터리로 이동
for root, _, files in os.walk(source_directory):
    for filename in files:
        if filename.endswith('.raw'):
            source_file_path = os.path.join(root, filename)
            destination_file_path = os.path.join(destination_directory, filename)

            # .raw 파일을 대상 디렉터리로 이동
            shutil.move(source_file_path, destination_file_path)

            print(f'.raw 파일 이동 완료: {filename}')

print('모든 .raw 파일을 이동했습니다.')
