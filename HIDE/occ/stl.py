from OCC.StlAPI import StlAPI_Writer
import os

from OCC.BRepMesh import BRepMesh_IncrementalMesh

def make_stl(inmodel, file, prec = 0.9):
	model = inmodel.native()

	mesh = BRepMesh_IncrementalMesh(model, prec)
	mesh.Perform()
	assert mesh.IsDone()

	stl_output_file = os.path.abspath(file)
	stl_writer = StlAPI_Writer()
	stl_writer.SetASCIIMode(True)
	stl_writer.Write(model, stl_output_file)
	assert os.path.isfile(stl_output_file)