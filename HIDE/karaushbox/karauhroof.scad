$fn=60;

t = 1;
x = 50;
y = 44;
z = 11;

do = 6;
di = 3;
lo = 4.5;
p = 2.5;

techn = 0.5;

module mainform() {
	translate([-(x-techn)/2, -(y-techn)/2, 0]) cube([x-techn,y-techn,z-techn]);	
}

module plate() {
	translate([-(x+2*t)/2, -(y+2*t)/2, 0]) cube([x+2*t,y+2*t,t]);	
}

module cyl(b=0) {
	if (b == 0) {
		difference() {
			translate([t/3,t/3,0]) cylinder(h=lo, r=(do)/2);
			translate([0,0,t]) cylinder(h=100+0.001, r=di/2, center = true);
		}
	} else {

			translate([0,0,t]) cylinder(h=100+0.001, r=di/2, center = true);
	}
}

module center_button() {
	difference() {
		cube([20,10,t + 0.001]);
		translate([t,t,-0.0005]) cube([20-t,10-2*t,t+0.001]);
	}
}

difference() {
	union() {
		plate();
		intersection() {
			union() {
				translate([x/2-p,y/2-p,t]) cyl();
				translate([-x/2+p,y/2-p,t]) rotate(90) cyl();
				translate([-x/2+p,-y/2+p,t]) rotate(180) cyl();
				translate([x/2-p,-y/2+p,t]) rotate(270) cyl();
			}
			mainform();
		}
		translate([-(x+2*t)/2,techn,t]) cube([t*1.5,6.5 - techn * 2,3]);
		translate([+(x+2*t)/2-t*1.5,-5,t]) cube([t*1.5,10 - techn * 2,2]);
	}
	translate([-25+12,22-10-18,-0.0005]) center_button();
	
			union() {
				translate([x/2-p,y/2-p,t]) cyl(1);
				translate([-x/2+p,y/2-p,t]) rotate(90) cyl(1);
				translate([-x/2+p,-y/2+p,t]) rotate(180) cyl(1);
				translate([x/2-p,-y/2+p,t]) rotate(270) cyl(1);
			}
}

