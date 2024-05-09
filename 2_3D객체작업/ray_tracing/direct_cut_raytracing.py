#짜르는 과정 시각화
# import vtk

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

# # Create a sphere
# sphere = vtk.vtkSphereSource()
# sphere.SetCenter(0, 0, 0)
# sphere.SetRadius(1)

# # Create a mapper
# sphere_mapper = vtk.vtkPolyDataMapper()
# sphere_mapper.SetInputConnection(sphere.GetOutputPort())

# # Create an actor
# sphere_actor = vtk.vtkActor()
# sphere_actor.SetMapper(sphere_mapper)

# # Add sphere actor to the scene
# renderer.AddActor(sphere_actor)

# # Create a plane
# plane = vtk.vtkPlane()
# plane.SetOrigin(0, 0, 0)
# plane.SetNormal(1, 1, 0)  # Set the normal of the plane

# # Create a cutter
# cutter = vtk.vtkCutter()
# cutter.SetInputConnection(sphere.GetOutputPort())
# cutter.SetCutFunction(plane)
# cutter.Update()

# # Create a mapper for the cutter output
# cutter_mapper = vtk.vtkPolyDataMapper()
# cutter_mapper.SetInputConnection(cutter.GetOutputPort())

# # Create an actor for the cutter
# cutter_actor = vtk.vtkActor()
# cutter_actor.SetMapper(cutter_mapper)
# cutter_actor.GetProperty().SetColor(1, 0, 0)  # Set color to red

# # Add cutter actor to the scene
# renderer.AddActor(cutter_actor)

# # Render the scene
# render_window.Render()

# # Start the interaction
# interactor.Start()

import vtk

# Create a sphere
sphere = vtk.vtkSphereSource()
sphere.SetCenter(0, 0, 0)
sphere.SetRadius(1)

# Create a plane
plane = vtk.vtkPlane()
plane.SetOrigin(0, 0, 0)
plane.SetNormal(1, 1, 0)  # Set the normal of the plane

# Create a cutter
cutter = vtk.vtkCutter()
cutter.SetInputConnection(sphere.GetOutputPort())
cutter.SetCutFunction(plane)
cutter.Update()

# Get the cutter output
cutter_output = cutter.GetOutput()

# # Write cutter output to a PLY file
# writer = vtk.vtkPLYWriter()
# writer.SetFileName("cutter_output.ply")
# writer.SetInputData(cutter_output)
# writer.Write()

# Create a writer for the VTP file
writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName("cutter_output.vtp")
writer.SetInputData(cutter_output)
writer.Write()

print("end")

import vtk

# Create a reader for the VTP file
reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName("cutter_output.vtp")
reader.Update()

# Create a mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

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
interactor.Start()
