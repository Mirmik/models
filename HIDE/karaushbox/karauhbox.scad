$fn=60;

t = 1;
x = 50;
y = 44;
z = 11;

do = 6;
di = 2;
lo = 5;
li = 4;
p = 2.5;

module mainform() {
	translate([-(x+t*2)/2, -(y+t*2)/2, 0]) cube([x+2*t,y+2*t,z+2*t]);	
}

module cbox() {
	translate([-(x+t*2)/2, -(y+t*2)/2, 0]) difference() {
		cube([x+t*2,y+t*2,z+t]);
		translate([t,t,t]) cube([x,y,z+0.001]);
	}
}

module cyl() {
		difference() {
			translate([t/3,t/3,0]) cylinder(h=lo, r=(do)/2);
			translate([0,0,t]) cylinder(h=li+0.001, r=di/2);
		}
}

difference() {
	intersection() {
		union() {
			cbox(); 
			translate([x/2-p,y/2-p,t]) cyl();
			translate([-x/2+p,y/2-p,t]) rotate(90) cyl();
			translate([-x/2+p,-y/2+p,t]) rotate(180) cyl();
			translate([x/2-p,-y/2+p,t]) rotate(270) cyl();
		}
		mainform();
	}
	translate([0,0,z+t+0.001-4]) cube([x,6.5,4]);
	translate([-x,-10/2,z+t+0.001-4]) cube([x,10,4]);
}