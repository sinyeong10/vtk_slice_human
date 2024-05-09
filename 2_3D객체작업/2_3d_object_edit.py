import vtk
#이전에 만든 3D 객체 읽어옴
# Create a reader for the saved VTK XML file
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(r"C:\sin\vtk\slice_human\updown.vti")  # Specify the path to the saved VTI file
# Read the data
reader.Update()
# Get the loaded vtkImageData
loaded_vtk_image_data = reader.GetOutput()
# Now, you can work with the loaded 3D object as you need.


# 3d 객체의 차원 값을 읽어옴
# Get the dimensions of the loaded vtkImageData
dimensions = loaded_vtk_image_data.GetDimensions()
print("차원값 :",dimensions)

# Get the origin (minimum coordinates) of the data
origin = loaded_vtk_image_data.GetOrigin()

# Calculate the maximum coordinates based on dimensions and spacing
spacing = loaded_vtk_image_data.GetSpacing()
max_coords = [origin[i] + (dimensions[i] - 1) * spacing[i] for i in range(3)]

# The 'max_coords' list now contains the maximum coordinates for X, Y, and Z axes.
# 'origin' contains the minimum coordinates for X, Y, and Z axes.
print("여기에 1더한게 차원", max_coords)
#[2047.0, 1151.0, 99.0]은 0부터 시작하므로 2048 x 1152 x 100를 의미




#loaded_vtk_image_data를 시각화 함
# Create a renderer
ren = vtk.vtkRenderer()

#흰색으로 배경 지정
ren.SetBackground(1.0, 1.0, 1.0)

# Create a render window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# Create a render window interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


#카메라 0,0,0세팅
# Create a camera and set its position and focal point
camera = vtk.vtkCamera()
camera.SetPosition(1000, 1000, 1000)  # Set camera position
camera.SetFocalPoint(0, 0, 0)  # Set focal point

# Set the camera to the renderer
ren.SetActiveCamera(camera)


# Define coordinates for the lines
line_coords = [
    [(0, 0, 0), (0, 0, 600)],
    [(0, 0, 0), (0, 600, 0)],
    [(0, 0, 0), (600, 0, 0)]
]

# Define colors for the lines
line_colors = [
    [1, 0, 0],  # Red
    [0, 1, 0],  # Green
    [0, 0, 1]   # Blue
]

# Create and add lines to the renderer
for i in range(3):
    # Create a line source
    line_source = vtk.vtkLineSource()
    line_source.SetPoint1(line_coords[i][0])
    line_source.SetPoint2(line_coords[i][1])

    # Create polydata for the line
    line_mapper = vtk.vtkPolyDataMapper()
    line_mapper.SetInputConnection(line_source.GetOutputPort())

    # Create an actor for the line
    line_actor = vtk.vtkActor()
    line_actor.SetMapper(line_mapper)
    line_actor.GetProperty().SetColor(line_colors[i])  # Set color
    line_actor.GetProperty().SetLineWidth(2.0)  # Set line width

    # Add the line actor to the renderer
    ren.AddActor(line_actor)


# Create a volume property
volume_property = vtk.vtkVolumeProperty()

#투명도 설정
# Set the opacity (transparency) of the volume
opacity = vtk.vtkPiecewiseFunction()
opacity.AddPoint(0, 0.0)  # Fully transparent at intensity 0
opacity.AddPoint(100, 1)  # Fully opaque at intensity 100
volume_property.SetScalarOpacity(opacity)


# Create a volume mapper
volume_mapper = vtk.vtkSmartVolumeMapper()
volume_mapper.SetInputData(loaded_vtk_image_data)

# Create a volume
volume = vtk.vtkVolume()
volume.SetMapper(volume_mapper)
volume.SetProperty(volume_property)

# Add the volume to the renderer
ren.AddViewProp(volume)




point_1 = (250,250,0)#(500,500,10) #구의 중심!
direct = (2,4,6)
point_2 = (250+direct[0]*100,250+direct[1]*100,10+direct[2]*100)



#지정 좌표에 점을 넣음
# Define the coordinates for the red point (replace with your desired coordinates)
x_coord, y_coord, z_coord = point_1

#구로 시각화
# Create a red sphere source (a point)
sphere_source = vtk.vtkSphereSource()
sphere_source.SetCenter(x_coord, y_coord, z_coord)
sphere_source.SetRadius(10)  # Adjust the size as needed

# Create polydata
point_mapper = vtk.vtkPolyDataMapper()
point_mapper.SetInputConnection(sphere_source.GetOutputPort())

# Create an actor for the point
point_actor = vtk.vtkActor()
point_actor.SetMapper(point_mapper)
point_actor.GetProperty().SetColor(1, 0, 0)  # Set color to red (RGB values)
point_actor.GetProperty().SetOpacity(1.0) #투명도 조절

# Add the point actor to the renderer
ren.AddActor(point_actor)



#선 시각화
# Create a line from the starting point to the ending point
end_point = point_2

import numpy as np

# 벡터의 크기 계산
vector_length = np.sqrt((point_2[0] - x_coord)**2 + (point_2[1] - y_coord)**2 + (point_2[2] - z_coord)**2)
print(point_1, point_2, vector_length)
print(f"({(point_2[0] - x_coord)}, {(point_2[1] - y_coord)}, {(point_2[2] - z_coord)})")
#법선벡터로 쓸 방향벡터
print(f"({(point_2[0] - x_coord)/vector_length}, {(point_2[1] - y_coord)/vector_length}, {(point_2[2] - z_coord)/vector_length})")
#point_1에서 point_2까지의 선분
line_source = vtk.vtkLineSource()
line_source.SetPoint1([x_coord, y_coord, z_coord])
line_source.SetPoint2(end_point)

# Create polydata for the line
line_mapper = vtk.vtkPolyDataMapper()
line_mapper.SetInputConnection(line_source.GetOutputPort())

# Create an actor for the line
line_actor = vtk.vtkActor()
line_actor.SetMapper(line_mapper)
line_actor.GetProperty().SetColor(0, 0, 1)  # Set color to blue (RGB values)
line_actor.GetProperty().SetLineWidth(2.0)  # Set line width

# Add the line actor to the renderer
ren.AddActor(line_actor)



# Create a plane using the blue line as the normal vector
plane = vtk.vtkPlane()
plane.SetOrigin(x_coord, y_coord, z_coord)
plane.SetNormal(point_2[0] - x_coord, point_2[1] - y_coord, point_2[2] - z_coord) #방향벡터를 법선 벡터로

# Create a cutter and set the plane
cutter = vtk.vtkCutter()
cutter.SetInputData(loaded_vtk_image_data)  # Use your loaded vtkImageData here
cutter.SetCutFunction(plane)
#여기서 cutter.Update()는 렌더링 루프에서 내부적으로 처리됨

# Create mapper for the cut object
cutter_mapper = vtk.vtkPolyDataMapper()
cutter_mapper.SetInputConnection(cutter.GetOutputPort())

# Create actor for the cut object
cutter_actor = vtk.vtkActor()
cutter_actor.SetMapper(cutter_mapper)

# Add the cut object to the renderer
ren.AddActor(cutter_actor)

# Set up the rendering environment
renWin.Render()

# Start the interaction
iren.Start()



#짜른 평면 저장
# Now, save the cut object (plane) as a VTK file
plane_writer = vtk.vtkXMLPolyDataWriter()
plane_writer.SetInputData(cutter.GetOutput())
plane_writer.SetFileName(f"test_cut.vtp")  # Specify the path and filename for the saved file
plane_writer.Write()
print(f"end")