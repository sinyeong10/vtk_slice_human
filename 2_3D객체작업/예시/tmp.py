import vtk
import vtk
import numpy as np

from vtkmodules.util import numpy_support

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
plane_reader.SetFileName("direct_test_cut.vtp")  # Specify the path to the saved .vtp file
plane_reader.Update()


import vtk

# 구 생성
sphere = vtk.vtkSphereSource()
sphere.SetCenter(0, 0, 0)
sphere.SetRadius(5.0)

# 법선 벡터 계산
normals = vtk.vtkPolyDataNormals()
normals.SetInputConnection(sphere.GetOutputPort())
normals.ComputeCellNormalsOn()
normals.AutoOrientNormalsOn()
normals.Update()

# 법선 벡터 시각화를 위한 Glyph 생성
arrow = vtk.vtkArrowSource()

glyph = vtk.vtkGlyph3D()
glyph.SetInputConnection(normals.GetOutputPort())
glyph.SetSourceConnection(arrow.GetOutputPort())
glyph.SetVectorModeToUseNormal()
glyph.SetScaleModeToScaleByVector()
glyph.SetScaleFactor(1.0)

# Mapper 및 Actor 생성
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(glyph.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Renderer, RenderWindow, Interactor 설정
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Add Actor to Renderer
renderer.AddActor(actor)
renderer.SetBackground(1.0, 1.0, 1.0)  # White background

# Set Camera position
renderer.GetActiveCamera().Azimuth(30)
renderer.GetActiveCamera().Elevation(30)
renderer.ResetCamera()

# Render the scene
render_window.Render()
render_window_interactor.Start()

