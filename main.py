from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome 브라우저를 사용하여 웹 드라이버 초기화
driver = webdriver.Chrome()

# 웹 페이지 열기
url = 'https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Male-Images/Fullcolor/fullbody/index.html'
driver.get(url)

# 다운로드할 파일의 범위 지정 (1001부터 2878까지)
start_index = 526
end_index = 1878

# XPath 패턴 설정
xpath_pattern = '//*[@id="list"]/tbody/tr[{}]/td[1]/a'

# 파일 다운로드 루프
for index in range(start_index, end_index + 1):
    link_xpath = xpath_pattern.format(index)

    try:
        # 링크를 찾고 클릭
        link_element = driver.find_element(By.XPATH, link_xpath)
        link_element.click()

        # 파일 다운로드가 완료될 때까지 잠시 대기 (파일 크기, 네트워크 속도 등에 따라 시간이 다를 수 있음)
        # 이 부분을 필요에 따라 조정하세요.
        driver.implicitly_wait(10)  # 예: 10초 대기
    except Exception as e:
        print(f"다운로드 실패: {index}, 에러: {str(e)}")

# 작업 완료 후 셀레니움 드라이버 종료
driver.quit()
