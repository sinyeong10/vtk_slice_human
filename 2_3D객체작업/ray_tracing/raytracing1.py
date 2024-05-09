# import vtk

# # Create a tilted plane in 3D
# plane = vtk.vtkPlane()
# plane.SetOrigin(0, 0, 0)
# plane.SetNormal(0.5, 0.5, 1)  # Adjust the normal to tilt the plane

# # Create a renderer
# renderer = vtk.vtkRenderer()
# renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color

# # Create a render window
# render_window = vtk.vtkRenderWindow()
# render_window.SetSize(800, 600)
# render_window.AddRenderer(renderer)

# # Create an interactor
# interactor = vtk.vtkRenderWindowInteractor()
# interactor.SetRenderWindow(render_window)

# # Create a camera
# camera = vtk.vtkCamera()
# camera.SetPosition(0, 0, 5)  # Adjust camera position
# camera.SetFocalPoint(0, 0, 0)
# renderer.SetActiveCamera(camera)

# # Project the 3D scene onto a 2D plane
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(plane.GetOutputPort())
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)

# # Add actor to the scene
# renderer.AddActor(actor)

# # Render the scene
# render_window.Render()

# # Start the interaction
# interactor.Start()


# import vtk

# # Create a tilted plane in 3D
# plane_source = vtk.vtkPlaneSource()
# plane_source.SetOrigin(0, 0, 0)
# plane_source.SetPoint1(1, 0, 0)  # Adjust the size of the plane
# plane_source.SetPoint2(0, 1, 0)
# plane_source.SetCenter(0, 0, 0)
# plane_source.SetResolution(10, 10)  # Adjust the resolution of the plane

# # Create a mapper
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(plane_source.GetOutputPort())

# # Create an actor
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)

# # Create a renderer
# renderer = vtk.vtkRenderer()
# renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color

# # Create a render window
# render_window = vtk.vtkRenderWindow()
# render_window.SetSize(800, 600)
# render_window.AddRenderer(renderer)

# # Create an interactor
# interactor = vtk.vtkRenderWindowInteractor()
# interactor.SetRenderWindow(render_window)

# # Create a camera
# camera = vtk.vtkCamera()
# camera.SetPosition(0, 0, 5)  # Adjust camera position
# camera.SetFocalPoint(0, 0, 0)
# renderer.SetActiveCamera(camera)

# # Add actor to the scene
# renderer.AddActor(actor)

# # Render the scene
# render_window.Render()

# # Start the interaction
# interactor.Start()

import vtk
import numpy as np

# Create a tilted plane in 3D
plane_source = vtk.vtkPlaneSource()
plane_source.SetOrigin(0, 0, 0)
plane_source.SetPoint1(1, 0, 0)  # Adjust the size of the plane
plane_source.SetPoint2(0, 1, 0)
plane_source.SetCenter(0, 0, 0)
plane_source.SetResolution(10, 10)  # Adjust the resolution of the plane

# Create a mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(plane_source.GetOutputPort())

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.SetSize(800, 600)
render_window.AddRenderer(renderer)

# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Create a camera
camera = vtk.vtkCamera()
camera.SetPosition(0, 0, 5)  # Adjust camera position
camera.SetFocalPoint(0, 0, 0)
renderer.SetActiveCamera(camera)

# Add actor to the scene
renderer.AddActor(actor)

# Render the scene
render_window.Render()

# Start the interaction
interactor.Start()

# Convert VTK data to numpy array
polydata = plane_source.GetOutput()
points = polydata.GetPoints()
num_points = points.GetNumberOfPoints()
numpy_array = np.zeros((num_points, 3))
for i in range(num_points):
    numpy_array[i] = points.GetPoint(i)

# Save numpy array to file
np.savetxt('plane_data.txt', numpy_array)
