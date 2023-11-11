# import vtkmodules.all as vtk
# import numpy as np

# # Create a cone to represent the fan shape
# cone = vtk.vtkConeSource()
# cone.SetHeight(1.0)
# cone.SetRadius(0.5)
# cone.SetResolution(100)
# coneMapper = vtk.vtkPolyDataMapper()
# coneMapper.SetInputConnection(cone.GetOutputPort())
# coneActor = vtk.vtkActor()
# coneActor.SetMapper(coneMapper)

# # Create a fan-shaped polygon representing the circular blade
# # The polygon has a fan shape with the center at (0, 0, 0) and points on the circle
# fanPolyData = vtk.vtkPolyData()
# fanPoints = vtk.vtkPoints()
# fanCells = vtk.vtkCellArray()

# center = [0, 0, 0]
# radius = 0.5
# numPoints = 100
# angle = 360.0 / numPoints

# fanPoints.InsertNextPoint(center)

# for i in range(numPoints + 1):
#     x = center[0] + radius * np.cos(np.radians(i * angle))
#     y = center[1] + radius * np.sin(np.radians(i * angle))
#     z = center[2]
#     fanPoints.InsertNextPoint(x, y, z)
#     if i > 0:
#         triangle = vtk.vtkTriangle()
#         triangle.GetPointIds().SetId(0, 0)
#         triangle.GetPointIds().SetId(1, i)
#         triangle.GetPointIds().SetId(2, i - 1)
#         fanCells.InsertNextCell(triangle)

# fanPolyData.SetPoints(fanPoints)
# fanPolyData.SetPolys(fanCells)

# fanMapper = vtk.vtkPolyDataMapper()
# fanMapper.SetInputData(fanPolyData)
# fanActor = vtk.vtkActor()
# fanActor.SetMapper(fanMapper)

# # Create a plane to intersect the fan-shaped polygon
# plane = vtk.vtkPlane()
# plane.SetOrigin(0, 0, 0)
# plane.SetNormal(0, 0, 1)

# # Create cutter to perform intersection
# cutter = vtk.vtkCutter()
# cutter.SetCutFunction(plane)
# cutter.SetInputData(fanPolyData)
# cutter.Update()

# cutterMapper = vtk.vtkPolyDataMapper()
# cutterMapper.SetInputData(cutter.GetOutput())

# cutterActor = vtk.vtkActor()
# cutterActor.SetMapper(cutterMapper)

# # Create a renderer, render window, and render window interactor
# renderer = vtk.vtkRenderer()
# renderWindow = vtk.vtkRenderWindow()
# renderWindow.AddRenderer(renderer)
# renderWindowInteractor = vtk.vtkRenderWindowInteractor()
# renderWindowInteractor.SetRenderWindow(renderWindow)

# # Add the actors to the renderer
# renderer.AddActor(coneActor)
# renderer.AddActor(fanActor)
# renderer.AddActor(cutterActor)

# # Set up camera
# renderer.GetActiveCamera().Azimuth(30)
# renderer.GetActiveCamera().Elevation(30)

# # Set the background color
# renderer.SetBackground(1.0, 1.0, 1.0)

# # Start the rendering loop
# renderWindow.Render()
# renderWindowInteractor.Start()

import vtkmodules.all as vtk
def visualize_and_cut():
    # Create a render window, renderer, and interactor
    renWin = vtk.vtkRenderWindow()
    ren = vtk.vtkRenderer()
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

    # Create a cone to use as a cutting tool (부채꼴)
    cone = vtk.vtkConeSource()
    cone.SetResolution(100)  # Adjust the resolution as needed
    cone.SetHeight(300)  # Adjust the height as needed
    cone.SetRadius(100)  # Adjust the radius as needed

    # Create a transform filter to position and orient the cone
    transform = vtk.vtkTransform()
    transform.PostMultiply()
    transform.Translate(2048//2-1, 1152//2-1, 0)  # Set the position based on your requirements
    transform.RotateX(90.0)  # Rotate the cone as needed
    transformFilter = vtk.vtkTransformPolyDataFilter()
    transformFilter.SetTransform(transform)
    transformFilter.SetInputConnection(cone.GetOutputPort())

    # Create a boolean operation filter to cut the cone with the plane
    booleanOperation = vtk.vtkBooleanOperationPolyDataFilter()
    booleanOperation.SetOperationToIntersection()
    booleanOperation.SetInputData(0, plane_reader.GetOutput())
    booleanOperation.SetInputData(1, transformFilter.GetOutput())

    # Create a mapper for the boolean operation result
    boolean_mapper = vtk.vtkPolyDataMapper()
    boolean_mapper.SetInputConnection(booleanOperation.GetOutputPort())

    # Create an actor for the boolean operation result
    boolean_actor = vtk.vtkActor()
    boolean_actor.SetMapper(boolean_mapper)

    # Add the loaded plane and boolean operation actor to the renderer
    ren.AddActor(plane_actor)
    ren.AddActor(boolean_actor)

    # Set up the rendering environment
    renWin.AddRenderer(ren)
    renWin.SetSize(800, 600)
    ren.SetBackground(1.0, 1.0, 1.0)  # Set background color to white

    # Start the interaction
    iren.Start()



# #짜른 평면 저장
# # Now, save the cut object (plane) as a VTK file
# plane_writer = vtk.vtkXMLPolyDataWriter()
# plane_writer.SetInputData(cutter.GetOutput())
# plane_writer.SetFileName("circle.vtp")  # Specify the path and filename for the saved file
# plane_writer.Write()



# # Create a renderer
# ren = vtk.vtkRenderer()

# # Set the background color to white
# ren.SetBackground(0, 0, 0)  # White background

# # Create a render window
# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(ren)

# # Create a render window interactor
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)

# # Load the saved plane (VTK PolyData) from the .vtp file
# plane_reader = vtk.vtkXMLPolyDataReader()
# plane_reader.SetFileName("circle.vtp")  # Specify the path to the saved .vtp file
# plane_reader.Update()

# # Create a mapper for the loaded plane
# plane_mapper = vtk.vtkPolyDataMapper()
# plane_mapper.SetInputData(plane_reader.GetOutput())

# # Create an actor for the loaded plane
# plane_actor = vtk.vtkActor()
# plane_actor.SetMapper(plane_mapper)

# # Add the loaded plane actor to the renderer
# ren.AddActor(plane_actor)

# # Set up the rendering environment
# renWin.Render()

# # Capture a screenshot and save it as a jpg file
# w2if = vtk.vtkWindowToImageFilter()
# w2if.SetInput(renWin)
# w2if.Update()

# jpg_writer = vtk.vtkJPEGWriter()
# jpg_writer.SetFileName("circle.jpg")  # Specify the path and filename for the saved jpg file
# jpg_writer.SetInputConnection(w2if.GetOutputPort())
# jpg_writer.Write()


# # Start the interaction
# iren.Start()

def sector_cutting1():
    print("cutting1")
    pass



import vtk
import numpy as np

# VTK 파일 읽기
reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName("test_cut.vtp")
reader.Update()

# vtkPolyData에서 NumPy 배열로 변환
polydata = reader.GetOutput()
points = polydata.GetPoints()
numpy_array = np.array([points.GetPoint(i) for i in range(points.GetNumberOfPoints())])

# 결과 확인
# print(numpy_array)



import numpy as np

def sector_mask(shape,centre,radius,angle_range):
    """
    Return a boolean mask for a circular sector. The start/stop angles in  
    `angle_range` should be given in clockwise order.
    """

    x,y = np.ogrid[:shape[0],:shape[1]]
    cx,cy = centre
    tmin,tmax = np.deg2rad(angle_range)

    # ensure stop angle > start angle
    if tmax < tmin:
            tmax += 2*np.pi

    # convert cartesian --> polar coordinates
    r2 = (x-cx)*(x-cx) + (y-cy)*(y-cy)
    theta = np.arctan2(x-cx,y-cy) - tmin

    # wrap angles between 0 and 2*pi
    theta %= (2*np.pi)

    # circular mask
    circmask = r2 <= radius*radius

    # angular mask
    anglemask = theta <= (tmax-tmin)

    return circmask*anglemask

from matplotlib import pyplot as pp

matrix = numpy_array.reshape((2048, 1152, 3))
print(matrix.shape)
mask = sector_mask(matrix.shape,(200,100),300,(0,50))
matrix[~mask] = 0
pp.imshow(matrix)
pp.show()


def circleMask(mat, r=0):
    if mat.shape[0] != mat.shape[1]:
        raise TypeError('Matrix has to be square')
    if not isinstance(r, int):
        raise TypeError('Radius has to be of type int')

    s = mat.shape[0]
    d = np.abs(np.arange(-s/2 + s%2, s/2 + s%2))
    dm = np.sqrt(d[:, np.newaxis]**2 + d[np.newaxis, :]**2)

    return np.logical_and(dm >= r-.5, dm < r+.5)

import numpy as np
from matplotlib import pyplot as plt

matrix = np.zeros((512, 512))
matrix[100:400, 100:400] = 255  # 예시 이미지 생성

# 반지름이 50인 원 모양 마스크 생성
mask = circleMask(matrix, 50)

# 마스크를 이미지에 적용하여 원 부분만 남기기
masked_matrix = np.where(mask, matrix, 0)

# 결과 플로팅
plt.imshow(masked_matrix, cmap='gray')
plt.title('Circle Mask Applied')
plt.show()