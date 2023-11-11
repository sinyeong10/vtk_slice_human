import vtkmodules.all as vtk
from vtkmodules.vtkCommonColor import vtkNamedColors
import numpy as np

colors = vtkNamedColors()

# # Create a render window, renderer, and interactor
# renWin = vtk.vtkRenderWindow()
# ren = vtk.vtkRenderer()
# iren = vtk.vtkRenderWindowInteractor()


import vtk
#이전에 만든 3D 객체 읽어옴
# Create a reader for the saved VTK XML file
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(r"C:\sin\vtk\slice_human\sc2_3d_object.vti")  # Specify the path to the saved VTI file
# Read the data
reader.Update()
# Get the loaded vtkImageData
loaded_vtk_image_data = reader.GetOutput()
# Now, you can work with the loaded 3D object as you need.


# 3d 객체의 차원 값을 읽어옴
# Get the dimensions of the loaded vtkImageData
dimensions = loaded_vtk_image_data.GetDimensions()

# Get the origin (minimum coordinates) of the data
origin = loaded_vtk_image_data.GetOrigin()

# Calculate the maximum coordinates based on dimensions and spacing
spacing = loaded_vtk_image_data.GetSpacing()
max_coords = [origin[i] + (dimensions[i] - 1) * spacing[i] for i in range(3)]

# The 'max_coords' list now contains the maximum coordinates for X, Y, and Z axes.
# 'origin' contains the minimum coordinates for X, Y, and Z axes.
print(max_coords)
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


base = [2048//2-1,1152//2-1,100//2-1]
top = [base[0]+300,base[1]+300,base[2]+0]
front = [base[0]+0,base[1]+2000,base[2]+0]

renWin.AddRenderer(ren)
iren.SetRenderWindow(renWin)

# Create a cube
cube = vtk.vtkCubeSource()
cube.SetXLength(40)
cube.SetYLength(30)
cube.SetZLength(20)
cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())

# create a plane to cut, here it cuts in the XZ direction (xz normal=(1,0,0); XY =(0,0,1), YZ =(0,1,0)
plane = vtk.vtkPlane()
plane.SetOrigin(base[0],base[1],base[2])


#2직선의 외적을 통해 평면의 법선벡터를 계산
# 첫 번째 선의 방향 벡터
direction_vector1 = np.array(top) - np.array(base)
# 두 번째 선의 방향 벡터
direction_vector2 = np.array(front) - np.array(base)
# 두 방향 벡터의 외적을 계산하여 평면의 법선 벡터를 얻음
normal_vector = np.cross(direction_vector1, direction_vector2)

plane.SetNormal(normal_vector[0],normal_vector[1],normal_vector[2])

# create cutter
cutter = vtk.vtkCutter()
cutter.SetCutFunction(plane)
cutter.SetInputConnection(reader.GetOutputPort())
cutter.Update()
cutterMapper = vtk.vtkPolyDataMapper()
cutterMapper.SetInputConnection(cutter.GetOutputPort())

# create plane actor
planeActor = vtk.vtkActor()
planeActor.GetProperty().SetColor(colors.GetColor3d('Yellow'))
planeActor.GetProperty().SetLineWidth(2)
planeActor.GetProperty().SetAmbient(1.0)
planeActor.GetProperty().SetDiffuse(0.0)
planeActor.SetMapper(cutterMapper)

# create cube actor
cubeActor = vtk.vtkActor()
cubeActor.GetProperty().SetColor(colors.GetColor3d('Aquamarine'))
cubeActor.GetProperty().SetOpacity(0.5)
cubeActor.SetMapper(cubeMapper)

# Create a point at (0, 0, 0)
point = vtk.vtkPoints()
point.InsertNextPoint(0, 0, 0)

# Create a polydata to represent the point
pointPolyData = vtk.vtkPolyData()
pointPolyData.SetPoints(point)

pointMapper = vtk.vtkPolyDataMapper()
pointMapper.SetInputData(pointPolyData)

pointActor = vtk.vtkActor()
pointActor.SetMapper(pointMapper)
pointActor.GetProperty().SetColor(1, 0, 0)  # Red color

# Create a line from (0, 0, 0) to (0, 0, 1100)
line = vtk.vtkLineSource()
line.SetPoint1(base[0],base[1],base[2])
line.SetPoint2(top[0],top[1],top[2])

lineMapper = vtk.vtkPolyDataMapper()
lineMapper.SetInputConnection(line.GetOutputPort())

lineActor = vtk.vtkActor()
lineActor.SetMapper(lineMapper)
lineActor.GetProperty().SetColor(0, 1, 0)  # Green color


line2 = vtk.vtkLineSource()
line2.SetPoint1(base[0],base[1],base[2]) #동일한 점
line2.SetPoint2(front[0],front[1],front[2])

lineMapper2 = vtk.vtkPolyDataMapper()
lineMapper2.SetInputConnection(line2.GetOutputPort())

lineActor2 = vtk.vtkActor()
lineActor2.SetMapper(lineMapper2)
lineActor2.GetProperty().SetColor(0, 0, 1)


# Add the actors to the renderer
ren.AddActor(planeActor)
ren.AddActor(cubeActor)
ren.AddActor(pointActor)
ren.AddActor(lineActor)
ren.AddActor(lineActor2)

# Set up the rendering environment
ren.SetBackground(0.1, 0.1, 0.1)  # Set background color
renWin.SetSize(800, 600)


#카메라 설정
# Create a camera
camera = ren.GetActiveCamera()

# Set the camera position and focal point to focus on 'base'
# camera.SetPosition(base[0], base[1], base[2] + 3000)  # Adjust the last value (Z position) as needed
camera.SetFocalPoint(base[0], base[1], base[2])
# camera.SetViewUp(0, 0, 1)  # Ensure the up direction is appropriate for your scene


iren.Start()



#짜른 평면 저장
# Now, save the cut object (plane) as a VTK file
plane_writer = vtk.vtkXMLPolyDataWriter()
plane_writer.SetInputData(cutter.GetOutput())
plane_writer.SetFileName("test_cut.vtp")  # Specify the path and filename for the saved file
plane_writer.Write()



# Create a renderer
ren = vtk.vtkRenderer()

# Set the background color to white
ren.SetBackground(1.0, 1.0, 1.0)  # White background

# Create a render window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# Create a render window interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Load the saved plane (VTK PolyData) from the .vtp file
plane_reader = vtk.vtkXMLPolyDataReader()
plane_reader.SetFileName("test_cut.vtp")  # Specify the path to the saved .vtp file
plane_reader.Update()

# Create a mapper for the loaded plane
plane_mapper = vtk.vtkPolyDataMapper()
plane_mapper.SetInputData(plane_reader.GetOutput())

# Create an actor for the loaded plane
plane_actor = vtk.vtkActor()
plane_actor.SetMapper(plane_mapper)

# Add the loaded plane actor to the renderer
ren.AddActor(plane_actor)
ren.AddActor(lineActor)
ren.AddActor(lineActor2)

# Set up the rendering environment
renWin.Render()

# Capture a screenshot and save it as a jpg file
w2if = vtk.vtkWindowToImageFilter()
w2if.SetInput(renWin)
w2if.Update()

jpg_writer = vtk.vtkJPEGWriter()
jpg_writer.SetFileName("test_cut.jpg")  # Specify the path and filename for the saved jpg file
jpg_writer.SetInputConnection(w2if.GetOutputPort())
jpg_writer.Write()


#카메라 설정
# Create a camera
camera = ren.GetActiveCamera()

# Set the camera position and focal point to focus on 'base'
# camera.SetPosition(base[0], base[1], base[2] + 3000)  # Adjust the last value (Z position) as needed
camera.SetFocalPoint(base[0], base[1], base[2])
# camera.SetViewUp(0, 0, 1)  # Ensure the up direction is appropriate for your scene


# Start the interaction
iren.Start()
