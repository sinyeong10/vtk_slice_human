import vtk

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

# Start the interaction
iren.Start()
