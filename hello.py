# -*- coding: utf-8 -*-
import sys
print("version", sys.version)

import vtk
import gdcm
import vtkgdcm
import wx
import numpy
import scipy


def main():
    print("Hello, world from python sandbox.")
    print(vtk.vtkVersion().GetVTKVersion())


if __name__ == '__main__':
    main()
