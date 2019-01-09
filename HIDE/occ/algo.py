import occ.topo as topo
import occ.wire as wire
import occ.geom as geom
from occ.gui import *
from OCC.GProp import GProp_GProps
from OCC.BRepGProp import brepgprop_VolumeProperties, brepgprop_SurfaceProperties
from OCC.BRepOffsetAPI import BRepOffsetAPI_ThruSections, BRepOffsetAPI_MakePipe, BRepOffsetAPI_MakePipeShell
from OCC.TopAbs import TopAbs_FACE, TopAbs_SHELL

def skinning(wires, solid = False, ruled=False, pres3d=1.0e-06, smooth = False, maxdegree=5):
	builder = BRepOffsetAPI_ThruSections(solid, ruled, pres3d)
	builder.SetSmoothing(smooth);
	builder.SetMaxDegree(maxdegree);
	for w in wires:
		if isinstance(w, wire.wire):
			builder.AddWire(w.native())
		elif isinstance(w, topo.vertex):
			builder.AddVertex(w.native())	
		else:
			raise Exception("WrongType")
	return topo.shape(builder.Shape())


def pipe(spine, profile):	
	builder = BRepOffsetAPI_MakePipe (spine.native(), profile.native())
	return topo.shape(builder.Shape())

def pipe_shell(spine, profile):	
	builder = BRepOffsetAPI_MakePipeShell (spine.native())
	builder.Add(profile.native())
	builder.SetMode(True)
	#builder.SetMode(geom.planeOXZ().native())
	#builder.MakeSolid()

	display(profile)
	builder.Build()
	builder.MakeSolid()
	display_raw(builder.LastShape())

	#builder.Faces()

	return topo.shape(builder.Shape())



def center_of_mass(obj):
	nat = obj.native()
	prop = GProp_GProps();

	if nat.ShapeType() == TopAbs_FACE or nat.ShapeType() == TopAbs_SHELL:
		brepgprop_SurfaceProperties(nat, prop);
	else:
		brepgprop_VolumeProperties(nat, prop);
#	}
	#brepgprop_VolumeProperties(obj.native(), prop);
	pnt = prop.CentreOfMass()
	return geom.point(pnt.X(), pnt.Y(), pnt.Z())

	#if (_Shape.IsNull())
	#    return false;
#
	#// Computing of CentreOfMass
	#gp_Pnt pnt;
#
	#if (_Shape.ShapeType() == TopAbs_VERTEX) {
	#    pnt = BRep_Tool::Pnt(TopoDS::Vertex(_Shape));
	#}
	#else {
	#    GProp_GProps prop;
	#    if (_Shape.ShapeType() == TopAbs_EDGE || _Shape.ShapeType() == TopAbs_WIRE) {
	#        BRepGProp::LinearProperties(_Shape, prop);
	#    }
	#    else if (_Shape.ShapeType() == TopAbs_FACE || _Shape.ShapeType() == TopAbs_SHELL) {
	#        BRepGProp::SurfaceProperties(_Shape, prop);
	#    }
	#    else {
	#        BRepGProp::VolumeProperties(_Shape, prop);
	#    }
#
	#    pnt = prop.CentreOfMass();
	#}
#
	#center.Set(pnt.X(), pnt.Y(), pnt.Z());
	#return true;

def move_to_center(obj):
	cent = center_of_mass(obj)
	print(cent)
	return obj.translate(-geom.vector(cent))