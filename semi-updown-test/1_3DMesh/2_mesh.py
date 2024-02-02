import vtk

# 볼륨 데이터 로드 (예: .vti 파일)
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(r'C:\sin\vtk\slice_human\updown.vti')
reader.Update()

# spacing = (0.1, 0.1, 30)  # X, Y, Z 방향의 간격을 설정합니다.
# reader.GetOutput().SetSpacing(spacing)
loaded_vtk_image_data = reader.GetOutput()
print('read')

# 단일 구성 요소 추출
extract_components = vtk.vtkImageExtractComponents()
# extract_components.SetInputConnection(loaded_vtk_image_data) #아래로 처리하니 됨
extract_components.SetInputData(loaded_vtk_image_data)
extract_components.SetComponents(0)  # 0번째 구성 요소를 추출
extract_components.Update()


# Marching Cubes 알고리즘 적용
print('marchingcube')
marching_cubes = vtk.vtkMarchingCubes()

marching_cubes.SetInputConnection(extract_components.GetOutputPort())
marching_cubes.SetValue(-100,100)  # your_iso_value는 표면을 추출할 데이터 값입니다
marching_cubes.Update()



# 결과 메시 저장 (예: .vtp 파일)
print('vtp')
writer = vtk.vtkXMLPolyDataWriter()
writer.SetInputConnection(marching_cubes.GetOutputPort())
writer.SetFileName("mesh_updown.vtp")
writer.Write()



# 결과 메시 시각화 (선택 사항)
print('mapper')
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(marching_cubes.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.SetBackground(1.0, 1.0, 1.0)
renderer.AddActor(actor)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)
render_window_interactor.Start()


#=========== 마칭큐브 후 볼륨매핑

# import vtk
#
# # 볼륨 데이터 로드 (예: .vti 파일)
# reader = vtk.vtkXMLImageDataReader()
# reader.SetFileName(r'C:\Users\이제영\PycharmProjects\slice_human\stacker\humanslice.vti')
# reader.Update()
#
# print('read')
#
# # 단일 구성 요소 추출
# extract_components = vtk.vtkImageExtractComponents()
# extract_components.SetInputConnection(reader.GetOutputPort())
# extract_components.SetComponents(0)  # 0번째 구성 요소를 추출
# extract_components.Update()
#
# # Marching Cubes 알고리즘 적용
# print('marchingcube')
# marching_cubes = vtk.vtkMarchingCubes()
# marching_cubes.SetInputConnection(extract_components.GetOutputPort())
# marching_cubes.SetValue(0, 50)  # your_iso_value는 표면을 추출할 데이터 값입니다
# marching_cubes.Update()
#
# # 결과 메시 저장 (예: .vtp 파일)
# print('vtp')
# writer = vtk.vtkXMLPolyDataWriter()
# writer.SetInputConnection(marching_cubes.GetOutputPort())
# writer.SetFileName("zimrmslice_mesh.vtp")
# writer.Write()
#
# # 볼륨 매퍼 생성
# print('volume mapper')
# volume_mapper = vtk.vtkSmartVolumeMapper()
# volume_mapper.SetInputConnection(extract_components.GetOutputPort())
#
# # 볼륨 프로퍼티 생성
# volume_property = vtk.vtkVolumeProperty()
#
# # 볼륨 액터 생성
# volume = vtk.vtkVolume()
# volume.SetMapper(volume_mapper)
# volume.SetProperty(volume_property)
#
# # 결과 메시 시각화 (선택 사항)
# print('mapper')
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(marching_cubes.GetOutputPort())
#
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
#
# renderer = vtk.vtkRenderer()
# renderer.AddActor(actor)
# renderer.AddVolume(volume)  # 볼륨 액터 추가
#
# render_window = vtk.vtkRenderWindow()
# render_window.AddRenderer(renderer)
#
# render_window_interactor = vtk.vtkRenderWindowInteractor()
# render_window_interactor.SetRenderWindow(render_window)
# render_window_interactor.Start()



#================ 볼륨매핑 후 마칭큐브

# import vtk
#
# # 볼륨 데이터 로드 (예: .vti 파일)
# reader = vtk.vtkXMLImageDataReader()
# reader.SetFileName(r'C:\Users\이제영\PycharmProjects\slice_human\stacker\humanslice.vti')
# reader.Update()
#
# print('read')
#
# # 볼륨 매퍼 생성
# print('volume mapper')
# volume_mapper = vtk.vtkSmartVolumeMapper()
# volume_mapper.SetInputConnection(reader.GetOutputPort())
#
# # 볼륨 프로퍼티 생성
# volume_property = vtk.vtkVolumeProperty()
#
# # 볼륨 액터 생성
# volume = vtk.vtkVolume()
# volume.SetMapper(volume_mapper)
# volume.SetProperty(volume_property)
#
# # 렌더러 및 렌더 윈도우 생성
# renderer = vtk.vtkRenderer()
# renderer.AddVolume(volume)  # 볼륨 액터 추가
#
# render_window = vtk.vtkRenderWindow()
# render_window.AddRenderer(renderer)
#
# # 렌더 윈도우 상호 작용자 생성
# render_window_interactor = vtk.vtkRenderWindowInteractor()
# render_window_interactor.SetRenderWindow(render_window)
#
# # 렌더링 시작 (볼륨 렌더링)
# print('volume rendering')
# render_window.Render()
#
# # 단일 구성 요소 추출 (Marching Cubes 알고리즘을 위해)
# print('extract components')
# extract_components = vtk.vtkImageExtractComponents()
# extract_components.SetInputConnection(reader.GetOutputPort())
# extract_components.SetComponents(0)  # 0번째 구성 요소를 추출
# extract_components.Update()
#
# # Marching Cubes 알고리즘 적용
# print('marching cube')
# marching_cubes = vtk.vtkMarchingCubes()
# marching_cubes.SetInputConnection(extract_components.GetOutputPort())
# marching_cubes.SetValue(0, 50)  # your_iso_value는 표면을 추출할 데이터 값입니다
# marching_cubes.Update()
#
# # 결과 메시 시각화
# print('mapper')
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(marching_cubes.GetOutputPort())
#
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
#
# renderer.AddActor(actor)  # 메시 액터 추가
#
# # 렌더링 업데이트 (볼륨 렌더링 + Marching Cubes 메시)
# print('update rendering')
# render_window.Render()
#
# # 상호 작용 시작
# render_window_interactor.Start()

# ================ 볼륨렌더링만 진행
# import vtk
#
# # 볼륨 데이터 로드 (예: .vti 파일)
# print('reader')
# reader = vtk.vtkXMLImageDataReader()
# reader.SetFileName(r'C:\Users\이제영\PycharmProjects\slice_human\stacker\humanslice.vti')
# reader.Update()
#
# # 볼륨 매퍼 생성
# print('volume_mapper')
# volume_mapper = vtk.vtkSmartVolumeMapper()
# volume_mapper.SetInputConnection(reader.GetOutputPort())
#
# # 볼륨 프로퍼티 생성
# print('volume_property')
# volume_property = vtk.vtkVolumeProperty()
#
# # 볼륨 액터 생성
# print('volume')
# volume = vtk.vtkVolume()
# volume.SetMapper(volume_mapper)
# volume.SetProperty(volume_property)
#
# # 렌더러 및 렌더 윈도우 생성
# renderer = vtk.vtkRenderer()
# renderer.AddVolume(volume)  # 볼륨 액터 추가
#
# render_window = vtk.vtkRenderWindow()
# render_window.AddRenderer(renderer)
#
# # 렌더 윈도우 상호 작용자 생성
# render_window_interactor = vtk.vtkRenderWindowInteractor()
# render_window_interactor.SetRenderWindow(render_window)
#
# # 렌더링 시작 (볼륨 렌더링)
# render_window.Render()
# render_window_interactor.Start()