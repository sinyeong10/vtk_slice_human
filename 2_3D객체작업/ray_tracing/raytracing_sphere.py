import vtk

# Create a sphere
sphere = vtk.vtkSphereSource()
sphere.SetCenter(0, 0, 0)
sphere.SetRadius(1)

# Create a mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

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

# Add actor to the scene
renderer.AddActor(actor)

# Set up camera
camera = vtk.vtkCamera()
camera.SetPosition(0, 0, 5)
renderer.SetActiveCamera(camera)

# Render the scene
render_window.Render()

# Start the interaction
interactor.Start()
# Add a light source
light = vtk.vtkLight()
light.SetFocalPoint(1.0, 0.0, 1.0)
light.SetPosition(2.0, 2.0, 2.0)
renderer.AddLight(light)

# Enable ray tracing
render_window.SetNumberOfSamples(100)  # Increase sample count for better quality
renderer.SetUseRayTracing(True)

# Render the scene with ray tracing
render_window.Render()
