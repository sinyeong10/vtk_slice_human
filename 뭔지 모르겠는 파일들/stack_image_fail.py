import vtk
import os

# CT 이미지 디렉토리 경로
ct_image_dir = r"C:\sin\스타2 ai\히페리온_80"

# 이미지 크기
image_width = 2048#2560#2048
image_height = 1152#1440#1216

# VTK 렌더링 환경 설정
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("CT 3D Visualization")

renderer = vtk.vtkRenderer()
render_window.AddRenderer(renderer)

render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# CT 스캔 이미지 파일을 읽어와 3D로 쌓음
ct_images = []

for i in range(4):  # 이미지 개수에 맞게 조정
    ct_image_path = os.path.join(ct_image_dir, f"히페리온_80 - 복사본.jpg")

    # Raw 파일을 VTK 이미지로 읽기
    reader = vtk.vtkImageReader2()
    reader.SetFileDimensionality(3)
    reader.SetDataExtent(0, image_width - 1, 0, image_height - 1, i, i)  # 이미지 크기와 개수에 맞게 조정
    reader.SetDataScalarTypeToUnsignedShort()
    reader.SetDataByteOrderToLittleEndian()
    reader.SetFilePrefix(ct_image_path)
    reader.SetFilePattern("%s")
    reader.Update()
    print("done",i)

    ct_images.append(reader.GetOutput())

# 이미지 스택을 3D로 표시
# 이미지 스택 생성
stack = vtk.vtkImageAppend()
stack.SetAppendAxis(2)  # Z 축으로 적층

# CT 스캔 이미지 파일을 읽어와 스택에 추가
for i in range(4):  # 이미지 개수에 맞게 조정
    ct_image_path = os.path.join(ct_image_dir, f"히페리온_80 - 복사본.jpg") #2264부터 350이었음

    # Raw 파일을 VTK 이미지로 읽기
    reader = vtk.vtkImageReader2()
    reader.SetFileDimensionality(3)
    reader.SetDataExtent(0, image_width - 1, 0, image_height - 1, i, i)  # 이미지 크기와 개수에 맞게 조정
    reader.SetDataScalarTypeToUnsignedShort()
    reader.SetDataByteOrderToLittleEndian()
    reader.SetFilePrefix(ct_image_path)
    reader.SetFilePattern("%s")
    reader.Update()

    stack.AddInputData(reader.GetOutput())
    print("done",i)

# 스택 업데이트
stack.Update()

color_map = vtk.vtkColorTransferFunction()
color_map.AddRGBPoint(-1000, 0.0, 0.0, 0.0)  # 낮은 밀도에 대한 검은색
color_map.AddRGBPoint(0, 1.0, 1.0, 1.0)     # 중간 밀도에 대한 흰색
color_map.AddRGBPoint(1000, 1.0, 0.0, 0.0)   # 높은 밀도에 대한 빨간색

# 3D 볼륨 렌더링
volume_mapper = vtk.vtkGPUVolumeRayCastMapper()
volume_mapper.SetInputData(stack.GetOutput())  # 스택의 출력을 사용

volume_property = vtk.vtkVolumeProperty()
volume_property.ShadeOff()
volume_property.SetInterpolationTypeToLinear()

volume = vtk.vtkVolume()
volume.SetMapper(volume_mapper)
volume.SetProperty(volume_property)

renderer.AddVolume(volume)

# 렌더링 시작
render_window.Render()
render_window_interactor.Start()

