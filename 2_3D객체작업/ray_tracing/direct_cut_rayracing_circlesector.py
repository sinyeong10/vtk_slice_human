import numpy as np

# Define parameters
center = np.array([0, 0])  # 부채꼴의 중심 좌표
radius = 10  # 부채꼴의 반지름
start_angle = 0  # 부채꼴의 시작 각도 (라디안 단위)
end_angle = np.pi / 2  # 부채꼴의 끝 각도 (라디안 단위)
num_points = 50  # 생성할 점의 개수

# 각도 범위에 따른 각도 배열 생성
angles = np.linspace(start_angle, end_angle, num_points)

# 부채꼴의 각 점 좌표 생성
fan_polygon_vertices = np.column_stack([center[0] + radius * np.cos(angles),
                                        center[1] + radius * np.sin(angles), np.zeros_like(angles)])

print(fan_polygon_vertices)

import vtk
# Create points for the fan shape
fan_points = vtk.vtkPoints()
for point in fan_polygon_vertices:
    fan_points.InsertNextPoint(point)

# Create a polydata to hold the fan shape
fan_polydata = vtk.vtkPolyData()
fan_polydata.SetPoints(fan_points)

# Create a polydata mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(fan_polydata)

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 1.0, 1.0)  # 흰색으로 설정

# Create a renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start the interaction
interactor.Initialize()
render_window.Render()
interactor.Start()