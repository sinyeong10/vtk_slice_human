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
plane_reader.SetFileName("test_cut6.vtp")  # Specify the path to the saved .vtp file
plane_reader.Update()

# ####
# import vtkmodules.all as vtk
# from vtkmodules.util import numpy_support
# import numpy as np

# # Get PolyData from the plane
# plane_data = plane_reader.GetOutput()

# # Get points and scalars from PolyData
# points = plane_data.GetPoints().GetData()
# scalars = plane_data.GetPointData().GetScalars()

# # Convert VTK data to NumPy arrays
# points_np = numpy_support.vtk_to_numpy(points)
# scalars_np = numpy_support.vtk_to_numpy(scalars)

# # Define the circle parameters (center and radius)
# circle_center = np.array([0.0, 0.0, 10.0])
# circle_radius = 500.0

# ###
# import vtkmodules.all as vtk

# # Create a plane source
# plane_source = vtk.vtkPlaneSource()
# plane_source.SetOrigin(0, 0, 0)
# plane_source.SetPoint1(1, 0, 0)
# plane_source.SetPoint2(0, 1, 0)
# plane_source.SetResolution(1, 1)

# # Update the plane source
# plane_source.Update()

# # # Get the normal vector of the plane
# # normal_vector = plane_source.GetNormal()
# # print(normal_vector)
# # print(plane_data.GetNormal())
# # sys.exit()
# ###

# # Find points inside the circle
# inside_circle_mask = np.linalg.norm(points_np - circle_center, axis=1) < circle_radius
# #아래는 값을 가져오는 방식
# # points_inside_circle = points_np[inside_circle_mask]
# # scalars_inside_circle = scalars_np[inside_circle_mask]
# scalars_np[inside_circle_mask] = -1
# points_inside_circle = points_np
# scalars_inside_circle = scalars_np
# i=200000-100
# print(points_inside_circle.shape, scalars_inside_circle.shape)
# print(points_inside_circle[i:i+100], scalars_inside_circle[i:i+100])

# #2048 x 1152 x 100
# tmp = [[0]*2048 for _ in range(1152)]
# for i in range(scalars_inside_circle.shape[0]):
#     x,y,z = points_inside_circle[i]
#     tmp[int(y)][int(x)] = scalars_inside_circle[i]
#     # print(x,y,z,scalars_inside_circle[i])

# numpy_array = np.array(tmp, dtype=np.uint8)
# print(numpy_array.shape)
# from PIL import Image
# pil_image = Image.fromarray(numpy_array)
# pil_image.show()


# #######
# #변환중

# # # Get the PolyData from the reader
# # poly_data = plane_reader.GetOutput()

# # #경계선의 정보
# # # Get the bounds of the PolyData
# # bounds = poly_data.GetBounds()
# # # Extract the dimensions (xmin, xmax, ymin, ymax, zmin, zmax)
# # xmin, xmax, ymin, ymax, zmin, zmax = bounds
# # width = xmax - xmin
# # height = ymax - ymin
# # print(bounds, width, height)

# # # Extract the points from the PolyData
# # points = poly_data.GetPoints().GetData()

# # # Convert the VTK PolyData points to a NumPy array
# # numpy_array = numpy_support.vtk_to_numpy(points)
# # # numpy_array=numpy_array.reshape(int(xmax)+1, int(ymax)+1, 3)
# # # Now, numpy_array contains the coordinates of the points in NumPy format
# # # You can use numpy_array for further processing or visualization
# # print(numpy_array.shape, type(numpy_array[0][0]), numpy_array[0][0])

# # import matplotlib.pyplot as plt
# # # 예제로 주어진 넘파이 배열
# # # 넘파이 배열을 이미지로 변환하여 플로팅
# # plt.imshow(numpy_array)
# # plt.show()




# # # Split the numpy array into x, y, z components for 3D plotting
# # x, y, z = numpy_array[:, 0], numpy_array[:, 1], numpy_array[:, 2]

# # # Plot the sphere using matplotlib
# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection="3d")
# # ax.scatter(x, y, z, color="b", alpha=0.6, edgecolors="w", s=20)
# # plt.show()




# # # Convert NumPy array back to VTK PolyData
# # vtk_points = vtk.vtkPoints()
# # vtk_points.SetData(numpy_support.numpy_to_vtk(numpy_array.reshape(-1,3), deep=True))

# # # Create a new PolyData and set the points
# # new_poly_data = vtk.vtkPolyData()
# # new_poly_data.SetPoints(vtk_points)

# # # Optionally, you can add other data arrays or geometry to new_poly_data

# # # Save the PolyData to a new .vtp file
# # writer = vtk.vtkXMLPolyDataWriter()
# # writer.SetFileName("tmp_test.vtp")  # Specify the path for the new .vtp file
# # writer.SetInputData(new_poly_data)
# # writer.Write()



# ######



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
