#jpg 읽고 출력
# import vtk

# jpeg_file_path = r"C:\sin\스타2 ai\히페리온0.jpg"  # JPEG 파일 경로를 여기에 입력하세요.

# # JPEG 파일을 읽어와 VTK 이미지로 변환
# jpeg_reader = vtk.vtkJPEGReader()
# jpeg_reader.SetFileName(jpeg_file_path)
# jpeg_reader.Update()

# # VTK 이미지 객체 얻기
# vtk_image = jpeg_reader.GetOutput()

# # 이미지 정보 출력
# print("Image dimensions:", vtk_image.GetDimensions())
# print("Scalar type:", vtk_image.GetScalarTypeAsString())
# print("Number of components:", vtk_image.GetNumberOfScalarComponents())

# # VTK 이미지를 화면에 출력
# viewer = vtk.vtkImageViewer2()
# viewer.SetInputData(vtk_image)
# viewer.Render()
# viewer.GetRenderer().ResetCamera()  # 이미지가 화면에 맞게 나타나도록 카메라 조정
# viewer.Render()
# viewer.GetRenderWindow().SetWindowName("JPEG Image")
# viewer.GetRenderWindow().Render()

# # 렌더링 인터랙터 시작
# render_window_interactor = vtk.vtkRenderWindowInteractor()
# render_window_interactor.SetRenderWindow(viewer.GetRenderWindow())
# render_window_interactor.Start()

#Image dimensions: (2560, 1440, 1)


# Raw 이미지 파일읽고 출력
# import vtk

# raw_file_path = r"C:\sin\vtk\a_vm2560.raw"

# # Raw 파일을 VTK 이미지로 읽어오기
# reader = vtk.vtkImageReader2()
# reader.SetFileDimensionality(2)  # 2D 이미지로 가정
# reader.SetDataExtent(0, 2047, 0, 1215, 0, 0)  # 이미지 크기에 맞게 조정
# reader.SetDataScalarTypeToUnsignedChar()
# reader.SetDataByteOrderToLittleEndian()
# reader.SetFileName(raw_file_path)
# reader.Update()

# # VTK 이미지 객체 얻기
# vtk_image = reader.GetOutput()

# # 이미지 정보 출력
# print("Image dimensions:", vtk_image.GetDimensions())
# print("Scalar type:", vtk_image.GetScalarTypeAsString())
# print("Number of components:", vtk_image.GetNumberOfScalarComponents())

# # VTK 이미지를 화면에 출력
# viewer = vtk.vtkImageViewer2()
# viewer.SetInputData(vtk_image)
# viewer.Render()
# viewer.GetRenderer().ResetCamera()  # 이미지가 화면에 맞게 나타나도록 카메라 조정
# viewer.Render()
# viewer.GetRenderWindow().SetWindowName("JPEG Image")
# viewer.GetRenderWindow().Render()

# # 렌더링 인터랙터 시작
# render_window_interactor = vtk.vtkRenderWindowInteractor()
# render_window_interactor.SetRenderWindow(viewer.GetRenderWindow())
# render_window_interactor.Start()



import vtk

# 첫 번째 JPEG 파일 경로 설정 #검은색.jpg
jpeg_file_path1 = r"semi-updown-test\0_image_create\data\color_image_0.jpg"  # JPEG 파일 경로를 입력하세요.

# 첫 번째 JPEG 파일 읽기
jpeg_reader1 = vtk.vtkJPEGReader() #JPEG 읽기 위한 객체 생성
jpeg_reader1.SetFileName(jpeg_file_path1) #객체에 이미지 파일 경로 설정
jpeg_reader1.Update() #이미지를 읽고 VTK 데이터 구조로 변환, 즉, 이 함수로 이미지를 로드

# 첫 번째 이미지의 VTK 데이터 얻기
image1 = jpeg_reader1.GetOutput() #객체에서 VTK데이터를 반환받음

# 이미지 크기 얻기
dims = image1.GetDimensions() #객체의 차원 정보 반환 받음, x,y,z축의 값
# print(dims)



# 두 이미지를 결합하여 Z 축 방향으로 스택
n = 100 #z축 슬라이스 깊이

#chat GPT는 vtkImageData()를 활용하는 방법을 설명해줬는데 잘 안됨
# stacked_image = vtk.vtkImageData()
# stacked_image.SetDimensions(dims[0], dims[1], n)  # Z 축 방향으로 n개의 슬라이스
# print("base Image dimensions1:", stacked_image.GetDimensions())


# 이미지 스택을 만들 vtkImageAppend 객체 생성
stacked_image = vtk.vtkImageAppend() #이미지 스택을 만들때 쓰는 객체 생성
stacked_image.SetAppendAxis(2)  # Z-축 방향으로 이미지를 스택하라고 방향 설정
print(stacked_image.GetPreserveExtents())#현재 설정된 이미지 스택을 만들 때 영역을 유지할 것인지 여부를 확인
#이미지의 크기가 동일하지 않은 경우에도 영역을 자동으로 조정하지 않음을 의미
#기본은 0 False

# 원본 이미지를 읽어오고 복사하여 스택에 추가
for i in range(n):

    jpeg_file_path1 = f"semi-updown-test/0_image_create/data/color_image_{i+1}.jpg"

    jpeg_reader = vtk.vtkJPEGReader()
    jpeg_reader.SetFileName(jpeg_file_path1)  # 다음 이미지 파일 경로 설정
    jpeg_reader.Update()

    # 이미지를 복사하여 스택에 추가
    copied_image = vtk.vtkImageData() #이미지 데이터를 저장하는 객체 생성
    copied_image.DeepCopy(jpeg_reader.GetOutput()) #읽어서 반환받은 vtk 데이터를 깊은 복사함
    
    stacked_image.AddInputData(0, copied_image) #스택용 객체에 vtk파일을 넣음
    #0은 없어도 됨, 이미지 스택에 추가되는 입력의 인덱스를 의미
    #설명 상으로는 한 번에 여러장 되는 거 같기도 함

    # 각 이미지 슬라이스의 차원 정보 출력
    dimensions = copied_image.GetDimensions()
    print(f"Image Slice {i + 1} Dimensions:", dimensions)

# 이미지를 스택하여 결과 이미지 생성
stacked_image.Update() #스택한 거 로드, 데이터 파이프 라인 실행, 최종 결과 생성 느낌?

#3D 흑백 출력
# Create a volume rendering renderer
ren = vtk.vtkRenderer() # 3D 객체와 카메라를 사용하여 3D 장면을 렌더링하는 데 사용하는 렌더러 객체 생성
renWin = vtk.vtkRenderWindow() #렌더링 결과 표시할 창 설정
renWin.AddRenderer(ren) #렌더러가 렌더 윈도우에 렌더링 결과를 표시하게 함
iren = vtk.vtkRenderWindowInteractor() #사용자 입력 (키보드 및 마우스 이벤트 등)[상호작용]을 처리하고 3D 장면을 제어
iren.SetRenderWindow(renWin) #상호 작용 이벤트를 렌더 윈도우와 연결하여 사용자 입력을 처리하게 함

# Create a volume rendering object (vtkVolume)
volume = vtk.vtkVolume() # 3D 볼륨 렌더링을 위한 객체 생성

# Create and configure a volume mapper (vtkVolumeRayCastMapper or vtkSmartVolumeMapper)
volume_mapper = vtk.vtkSmartVolumeMapper() # 3D 볼륨 데이터를 시각적으로 렌더링 가능한 형식으로 변환하는 볼륨 매퍼 객체 생성

# Assuming stacked_image is a 3D volume data
# Convert stacked_image to vtkImageData
vtk_image_data = vtk.vtkImageData()
vtk_image_data.ShallowCopy(stacked_image.GetOutput()) #데이터의 참조만 복사해서 사용, 얕은 복사

# Now, set the vtkImageData as input to the volume mapper
volume_mapper.SetInputData(vtk_image_data)  # Set your 3D volume data here
#볼륨 매퍼에 vtk데이터를 넣음

# Create a volume property (vtkVolumeProperty) to control rendering properties
volume_property = vtk.vtkVolumeProperty() #볼륨 렌더링의 시각적인 특성(예: 색상, 투명도)을 제어하기 위한 객체 설정
volume.SetProperty(volume_property) #볼륨 객체에 앞서 생성한 볼륨 속성을 설정

# Connect the mapper to the volume
volume.SetMapper(volume_mapper) #볼륨 매퍼를 설정하여 볼륨 객체에 어떤 데이터를 렌더링할지를 지정

# Add the volume to the renderer
ren.AddViewProp(volume) #렌더러에 볼륨 객체를 추가하여 볼륨이 실제로 렌더링되고 화면에 표시되게 함

# Set up the rendering environment and start interaction
renWin.Render() #렌더 윈도우를 렌더링하여 3D 볼륨 데이터를 기반으로 렌더링이 수행하고 결과를 렌더 윈도우에 표시
iren.Start() #이벤트 루프를 시작하고 사용자 입력을 처리함, 상호 작용을 적용함



#컬러, 2D로 출력함!!
#2D 이미지 출력 객체로 받아서 출력하고
#volume처리 안해서 그럼!
# # 결과 이미지를 저장 또는 시각화
# # 여기에 결과 이미지를 저장하거나 시각화하는 코드를 추가하세요.

# # VTK 렌더링 환경 설정
# ren = vtk.vtkRenderer()
# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(ren)
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)

# # 이미지 데이터를 텍스처로 변환하여 표시
# image_actor = vtk.vtkImageActor() #2D 이미지 표시용 VTK Actor
# image_actor.SetInputData(stacked_image.GetOutput()) #이미지 데이터 가져옴
# ren.AddActor(image_actor) #렌더러에 이미지 추가되고 렌더링 됨

# # 렌더링 윈도우 표시
# renWin.Render()
# iren.Start()


# VTK XML 파일 작성기 생성
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName("updown.vti")  # 출력 파일 이름과 형식을 지정합니다 (VTI는 VTK 이미지 데이터를 위한 형식)

# 입력 데이터를 스택된 3D 객체로 설정
writer.SetInputData(vtk_image_data)

# 데이터를 파일로 쓰기
writer.Write()

print("end")