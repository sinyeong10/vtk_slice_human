import vtk
#이전에 만든 3D 객체 읽어옴
# Create a reader for the saved VTK XML file
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(r"C:\sin\vtk\slice_human\updown.vti")  # Specify the path to the saved VTI file
# Read the data
reader.Update()
# Get the loaded vtkImageData
loaded_vtk_image_data = reader.GetOutput()
# Now, you can work with the loaded 3D object as you need.


# 3d 객체의 차원 값을 읽어옴
# Get the dimensions of the loaded vtkImageData
dimensions = loaded_vtk_image_data.GetDimensions()
print(dimensions)

# Get the origin (minimum coordinates) of the data
origin = loaded_vtk_image_data.GetOrigin()

# Calculate the maximum coordinates based on dimensions and spacing
spacing = loaded_vtk_image_data.GetSpacing()
max_coords = [origin[i] + (dimensions[i] - 1) * spacing[i] for i in range(3)]

# The 'max_coords' list now contains the maximum coordinates for X, Y, and Z axes.
# 'origin' contains the minimum coordinates for X, Y, and Z axes.
print(max_coords)
#[2047.0, 1151.0, 99.0]은 0부터 시작하므로 2048 x 1152 x 100를 의미


def slice_cutting(point_1, point_2, i):
    #지정 좌표에 점을 넣음
    # Define the coordinates for the red point (replace with your desired coordinates)
    x_coord, y_coord, z_coord = point_1

    # Create a plane using the blue line as the normal vector
    plane = vtk.vtkPlane()
    plane.SetOrigin(x_coord, y_coord, z_coord)
    plane.SetNormal(point_2[0] - x_coord, point_2[1] - y_coord, point_2[2] - z_coord)

    # Create a cutter and set the plane
    cutter = vtk.vtkCutter()
    cutter.SetInputData(loaded_vtk_image_data)  # Use your loaded vtkImageData here
    cutter.SetCutFunction(plane)
    cutter.Update() #이거 해야지 반영됨 안하면 iren.Start()를 호출하여 렌더링 루프를 돌때 내부적으로 처리됨

    #짜른 평면 저장
    # Now, save the cut object (plane) as a VTK file
    plane_writer = vtk.vtkXMLPolyDataWriter()
    plane_writer.SetInputData(cutter.GetOutput())
    plane_writer.SetFileName(f"test_cut{i}.vtp")  # Specify the path and filename for the saved file
    plane_writer.Write()
    print(f"end {i}")

point_1 = (500,500,10)
point_2 = (500,500,500)
point_3 = (500,500,20)
from sys import stdin
count = 1
while True:
    try:
        x,y,z = list(map(int, stdin.readline().split()))
        slice_cutting((x,y,z), point_2, count)
        count += 1
    except:
        print("end")
        break
