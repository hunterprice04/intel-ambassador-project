import sys
import os
from vtkmodules.vtkRenderingVolume import vtkOSPRayVolumeInterface
# import vtkmodules
import vtk
# print(dir(vtkmodules))
t = vtkOSPRayVolumeInterface()
print(t)
#
# # noinspection PyUnresolvedReferences
# import vtkmodules.vtkInteractionStyle
# # noinspection PyUnresolvedReferences
# import vtkmodules.vtkRenderingOpenGL2
# from vtkmodules.vtkCommonColor import vtkNamedColors
# from vtkmodules.vtkFiltersSources import vtkCylinderSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# ) https://gitlab.kitware.com/vtk/vtk/-/blob/master/Documentation/dev/build.md#obtaining-the-source