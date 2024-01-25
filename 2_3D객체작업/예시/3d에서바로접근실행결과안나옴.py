import vtk
from vtkmodules.util import numpy_support
import numpy as np

reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(r"C:\sin\vtk\slice_human\sc2_3d_object.vti")  # Specify the path to the saved VTI file
# Read the data
reader.Update()
# Get the loaded vtkImageData

# 원뿔 생성
cone = vtk.vtkConeSource()
cone.SetResolution(20)
cone.Update()

# 폴리데이터로 변환
cone_mapper = vtk.vtkPolyDataMapper()
cone_mapper.SetInputConnection(cone.GetOutputPort())

# 폴리데이터 액터 생성
cone_actor = vtk.vtkActor()
cone_actor.SetMapper(cone_mapper)

# Create an implicit function using the cone as input
implicitPolyDataDistance = vtk.vtkImplicitPolyDataDistance()
implicitPolyDataDistance.SetInput(cone.GetOutput())

# Use the implicit function in the clipper
clipper = vtk.vtkClipDataSet()
clipper.SetInputData(reader.GetOutput())
clipper.SetClipFunction(implicitPolyDataDistance)  # Use the implicit function
clipper.InsideOutOn()
clipper.SetValue(0.0)
clipper.Update()

# 클리핑된 결과의 폴리데이터 매퍼 생성
clipper_mapper = vtk.vtkPolyDataMapper()
clipper_mapper.SetInputConnection(clipper.GetOutputPort())

# 클리핑된 결과의 폴리데이터 액터 생성
clipper_actor = vtk.vtkActor()
clipper_actor.SetMapper(clipper_mapper)

# 렌더러 및 윈도우 생성
renderer = vtk.vtkRenderer()
renderer.SetBackground(1.0, 1.0, 1.0)

render_window = vtk.vtkRenderWindow()
render_window.SetWindowName('Clipping with Cone')
render_window.SetSize(800, 600)
render_window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# 렌더러에 액터 추가
renderer.AddActor(cone_actor)
renderer.AddActor(clipper_actor)

# 렌더링 및 인터랙션 시작
render_window.Render()
interactor.Start()




# #!/usr/bin/env python

# import numpy as np
# # noinspection PyUnresolvedReferences
# import vtkmodules.vtkInteractionStyle
# # noinspection PyUnresolvedReferences
# import vtkmodules.vtkRenderingOpenGL2
# from vtkmodules.vtkCommonColor import vtkNamedColors
# from vtkmodules.vtkCommonCore import vtkFloatArray
# from vtkmodules.vtkCommonDataModel import vtkRectilinearGrid
# from vtkmodules.vtkFiltersCore import vtkImplicitPolyDataDistance
# from vtkmodules.vtkFiltersGeneral import vtkClipDataSet
# from vtkmodules.vtkFiltersGeometry import vtkRectilinearGridGeometryFilter
# from vtkmodules.vtkFiltersSources import vtkConeSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkDataSetMapper,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )


# def main():
#     colors = vtkNamedColors()

#     # Create polydata to slice the grid with. In this case, use a cone. This could
#     # be any polydata including a stl file.
#     cone = vtkConeSource()
#     cone.SetResolution(20)
#     cone.Update()

#     # implicit function that will be used to slice the mesh
#     implicitPolyDataDistance = vtkImplicitPolyDataDistance()
#     implicitPolyDataDistance.SetInput(cone.GetOutput())

#     # create a grid
#     xCoords = vtkFloatArray()
#     for x, i in enumerate(np.linspace(-1.0, 1.0, 15)):
#         xCoords.InsertNextValue(i)

#     yCoords = vtkFloatArray()
#     for y, i in enumerate(np.linspace(-1.0, 1.0, 15)):
#         yCoords.InsertNextValue(i)

#     zCoords = vtkFloatArray()
#     for z, i in enumerate(np.linspace(-1.0, 1.0, 15)):
#         zCoords.InsertNextValue(i)

#     # The coordinates are assigned to the rectilinear grid. Make sure that
#     # the number of values in each of the XCoordinates, YCoordinates,
#     # and ZCoordinates is equal to what is defined in SetDimensions().
#     rgrid = vtkRectilinearGrid()
#     rgrid.SetDimensions(x + 1, y + 1, z + 1)
#     rgrid.SetXCoordinates(xCoords)
#     rgrid.SetYCoordinates(yCoords)
#     rgrid.SetZCoordinates(zCoords)

#     # Create an array to hold distance information
#     signedDistances = vtkFloatArray()
#     signedDistances.SetNumberOfComponents(1)
#     signedDistances.SetName('SignedDistances')

#     # Evaluate the signed distance function at all of the grid points
#     for pointId in range(rgrid.GetNumberOfPoints()):
#         p = rgrid.GetPoint(pointId)
#         signedDistance = implicitPolyDataDistance.EvaluateFunction(p)
#         signedDistances.InsertNextValue(signedDistance)

#     # add the SignedDistances to the grid
#     rgrid.GetPointData().SetScalars(signedDistances)

#     # use vtkClipDataSet to slice the grid with the polydata
#     clipper = vtkClipDataSet()
#     clipper.SetInputData(rgrid)
#     clipper.InsideOutOn()
#     clipper.SetValue(0.0)
#     clipper.Update()

#     # --- mappers, actors, render, etc. ---
#     # mapper and actor to view the cone
#     coneMapper = vtkPolyDataMapper()
#     coneMapper.SetInputConnection(cone.GetOutputPort())
#     coneActor = vtkActor()
#     coneActor.SetMapper(coneMapper)

#     # geometry filter to view the background grid
#     geometryFilter = vtkRectilinearGridGeometryFilter()
#     geometryFilter.SetInputData(rgrid)
#     geometryFilter.SetExtent(0, x + 1, 0, y + 1, (z + 1) // 2, (z + 1) // 2)
#     geometryFilter.Update()

#     rgridMapper = vtkPolyDataMapper()
#     rgridMapper.SetInputConnection(geometryFilter.GetOutputPort())

#     wireActor = vtkActor()
#     wireActor.SetMapper(rgridMapper)
#     wireActor.GetProperty().SetRepresentationToWireframe()
#     wireActor.GetProperty().SetColor(colors.GetColor3d('Black'))

#     # mapper and actor to view the clipped mesh
#     clipperMapper = vtkDataSetMapper()
#     clipperMapper.SetInputConnection(clipper.GetOutputPort())

#     clipperActor = vtkActor()
#     clipperActor.SetMapper(clipperMapper)
#     clipperActor.GetProperty().SetRepresentationToWireframe()
#     clipperActor.GetProperty().SetColor(colors.GetColor3d('Black'))

#     # A renderer and render window
#     renderer = vtkRenderer()
#     renderer.SetBackground(colors.GetColor3d('Snow'))

#     # add the actors
#     # renderer.AddActor(coneActor) #객체
#     # renderer.AddActor(wireActor) #기준
#     renderer.AddActor(clipperActor) #객체를 함수로 변환

#     renwin = vtkRenderWindow()
#     renwin.AddRenderer(renderer)
#     renwin.SetWindowName('ClipDataSetWithPolyData')

#     # An interactor
#     interactor = vtkRenderWindowInteractor()
#     interactor.SetRenderWindow(renwin)

#     # Start
#     interactor.Initialize()
#     renwin.Render()
#     renderer.GetActiveCamera().SetPosition(0, -1, 0)
#     renderer.GetActiveCamera().SetFocalPoint(0, 0, 0)
#     renderer.GetActiveCamera().SetViewUp(0, 0, 1)
#     renderer.GetActiveCamera().Azimuth(30)
#     renderer.GetActiveCamera().Elevation(30)
#     renderer.ResetCamera()
#     renwin.Render()
#     interactor.Start()


# if __name__ == '__main__':
#     main()