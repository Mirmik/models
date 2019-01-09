module case(w,h,l,t,r,z,s) {
	w = w*s;
	h = h*0.95;
	union() {
		difference() {
			cube([w,l,h]);
			translate([t,t,t]) cube([w-2*t, l-2*t,h-t+0.001]);
			translate([w/2,t+0.5,h]) rotate([90,0,0]) cylinder(r=r,h=t+1);
		}
		difference() {
			translate([t,-z*2,0]) cube([w-2*t, z*2, h-r]);
			translate([t+z,-z,z]) cube([w-2*t-2*z, z, h-r-z+0.1]);
			translate([t+z*3,-2*z-0.005,2*z]) cube([w-2*t-6*z, z+0.01, h-r-2*z+0.1]);
		}
	}
}

case(w=27,h=20,l=64,t=1.5,r=27/2-4,z=1,s=0.965);