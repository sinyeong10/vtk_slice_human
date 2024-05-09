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

#카메라 0,0,0세팅
# Create a camera and set its position and focal point
camera = vtk.vtkCamera()
camera.SetPosition(1000, 1000, 1000)  # Set camera position
camera.SetFocalPoint(0, 0, 0)  # Set focal point

# Set the camera to the renderer
ren.SetActiveCamera(camera)


# Load the saved plane (VTK PolyData) from the .vtp file
plane_reader = vtk.vtkXMLPolyDataReader()
plane_reader.SetFileName("test_cut.vtp")  # Specify the path to the saved .vtp file
plane_reader.Update()




#normal_vector값 설정이 어려움..
# # Define the normal vector of the plane (given)
# normal_vector = [2,4,6] #[0.4082482904638631, 0.4082482904638631, 0.8164965809277261]

# # Create a transform to perform the projection
# transform = vtk.vtkTransform()

# # Calculate the projection matrix
# projection_matrix = vtk.vtkMatrix4x4()
# projection_matrix.Identity()
# for i in range(3):
#     for j in range(3):
#         projection_matrix.SetElement(i, j, (1 - normal_vector[i] * normal_vector[j]))
# for i in range(3):
#     projection_matrix.SetElement(i, 3, -normal_vector[i])
# print("변환 행렬 :", projection_matrix)

# # Set the projection matrix to the transform
# transform.SetMatrix(projection_matrix)

# # Apply the transform to the plane
# plane_reader.Update()
# transform_filter = vtk.vtkTransformFilter()
# transform_filter.SetTransform(transform)
# transform_filter.SetInputData(plane_reader.GetOutput())
# transform_filter.Update()


import numpy as np
# 두 법선 벡터 간의 회전 각도와 축을 계산하여 처리
# Define the normal vectors
normal_vector1 = np.array([1,2,3])  # Given normal vector #[1,2,3]
# normal_vector1 = normal_vector1 / np.linalg.norm(normal_vector1)
normal_vector2 = np.array([0, 0, 1])  # Target normal vector

# Calculate the rotation axis and angle between the two normal vectors
rotation_axis = np.cross(normal_vector1, normal_vector2) #외적으로 회전축 계산
rotation_angle = np.arccos(np.dot(normal_vector1, normal_vector2) / (np.linalg.norm(normal_vector1) * np.linalg.norm(normal_vector2))) #벡터의 각도 계산

# Convert rotation axis to VTK vector
rotation_axis_vtk = vtk.vtkVector3d(rotation_axis[0], rotation_axis[1], rotation_axis[2])

# Create a transform to perform the rotation
transform = vtk.vtkTransform() #회전축과 각도로 회전 변환 생성
transform.RotateWXYZ(np.degrees(rotation_angle), rotation_axis_vtk)

# Apply the transform to the plane
plane_reader.Update()
transform_filter = vtk.vtkTransformFilter()
transform_filter.SetTransform(transform)
transform_filter.SetInputData(plane_reader.GetOutput())
transform_filter.Update()

# Your further code for extracting color information and setting up actors can be added here




# Extract color information from the original data
original_colors = vtk.vtkUnsignedCharArray()
original_colors.DeepCopy(plane_reader.GetOutput().GetPointData().GetScalars())

# Create a new array for grayscale colors in the transformed data
transformed_colors = vtk.vtkUnsignedCharArray()
transformed_colors.SetNumberOfComponents(1)  # Grayscale color
transformed_colors.SetName("Grayscale")

# Apply the original grayscale values to the transformed data
for i in range(transform_filter.GetOutput().GetNumberOfPoints()):
    gray_value = original_colors.GetValue(i)  # Assuming grayscale value is already extracted
    transformed_colors.InsertNextValue(gray_value)

# Set the colors to the transformed data
transform_filter.GetOutput().GetPointData().SetScalars(transformed_colors)

# Create a mapper for the transformed plane
transformed_mapper = vtk.vtkPolyDataMapper()
transformed_mapper.SetInputData(transform_filter.GetOutput())

# Create an actor for the transformed plane
transformed_actor = vtk.vtkActor()
transformed_actor.SetMapper(transformed_mapper)

# Add the transformed plane actor to the renderer
ren.AddActor(transformed_actor)

print(transform_filter.GetOutput().GetPoints().GetPoint(0))
print(transform_filter.GetOutput().GetPoints().GetPoint(1))
print(transform_filter.GetOutput().GetPoints().GetPoint(2))
# print(transform_filter.GetOutput().GetPoints().GetPoint(149147))
# print(transform_filter.GetOutput().GetPoints().GetPoint(149148))
# print(transform_filter.GetOutput().GetPoints().GetPoint(149149))
cells_bounds = transform_filter.GetOutput().GetBounds()
x_min, x_max, y_min, y_max, z_min, z_max = cells_bounds
print(f"({x_min}, {x_max}), {x_min-x_max}, ({y_min}, {y_max}), {y_min-y_max}, {z_min}, {z_max}")

#numpy로 저장
import numpy as np

# Extract color information from the transformed data
transformed_colors_vtk = transform_filter.GetOutput().GetPointData().GetScalars()
# print(transformed_colors_vtk)
# Convert VTK array to numpy array
num_points = transformed_colors_vtk.GetNumberOfTuples()
print(num_points) #데이터의 각 점의 수

#.0일 경우 -1안해도 되지만 범위를 1 크게 하고 처리해도 크게 차이 x
x_min = int(x_min-1)
y_min = int(y_min-1)
#2차원 배열 x가 열, y가 행
transformed_colors_np = np.zeros((int(y_max+1)-y_min, int(x_max+1)-x_min), dtype=np.uint8)
transformed_colors_np[:] = 255
# print("범위", int(y_max+1)-y_min, int(x_max+1)-x_min)
for i in range(num_points):
    x, y, _ = transform_filter.GetOutput().GetPoints().GetPoint(i)
    # print(i, x, y, "->", x-x_min, y-y_min)
    color = transformed_colors_vtk.GetTuple(i)
    transformed_colors_np[round(y)-y_min-1][round(x)-x_min-1] = color[0] #값을 인덱스로 바꿔서 -1뺌

# #1차원의 경우!
# transformed_colors_np = np.zeros(num_points, dtype=np.uint8)  # Create a 1D array for grayscale values
# for i in range(num_points):
#     color = transformed_colors_vtk.GetTuple(i)  # Get RGB values
#     grayscale_value = color[0]  # Select one of the components (e.g., red value)
#     # if grayscale_value < 10:
#     #     print(grayscale_value, i, transform_filter.GetOutput().GetPoints().GetPoint(i))
#     #     break
#     transformed_colors_np[i] = grayscale_value  # Set selected component as grayscale value

file_name = "transformed_colors.csv"

np.savetxt(file_name, transformed_colors_np, delimiter=",")



import matplotlib.pyplot as plt
# # 이미지로 표현
plt.imshow(transformed_colors_np, cmap='gray')
# plt.colorbar()  # 컬러바 표시
plt.show()

# import cv2
# image = cv2.cvtColor(transformed_colors_np, cv2.COLOR_GRAY2BGR)
# # 이미지 표시
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 배열의 크기
row, col = transformed_colors_np.shape

# 3x3 윈도우로 max 필터 처리
result = np.zeros((row-3, col-3))

for i in range(row-3):
    for j in range(col-3):
        window = transformed_colors_np[i:i+4, j:j+4]
        result[i, j] = np.min(window)


plt.imshow(result, cmap='gray')
# plt.colorbar()  # 컬러바 표시
plt.show()


# def tmp(trash):
    # pass
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





# ######

# Create a mapper for the loaded plane
base_mapper = vtk.vtkPolyDataMapper()
base_mapper.SetInputData(plane_reader.GetOutput())

# Create an actor for the loaded plane
base_actor = vtk.vtkActor()
base_actor.SetMapper(base_mapper)

# Add the loaded plane actor to the renderer
ren.AddActor(base_actor)

# Set up the rendering environment
renWin.Render()


#jpg로 저장하는 코드
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
