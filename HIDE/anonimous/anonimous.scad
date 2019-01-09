
size = 100;
ext = 5;
wall = 4;
height = 1;

module img() {
	translate([-size/2,-size/2]) 
		linear_extrude(height, convexity= 4)
			resize([size,size]) 
				offset(r = 0.5) import("anonimous.dxf");
}

module base(height = height) {
	union() {
		img();
		circle(r = 16, h = 1);
	}
}

module sqbase(height = height, ext = ext) {
	cube([size + ext, size + ext, 1], center = true);
}

module positive() {
	union() {
		img();
		translate([0,0,-height / 2]) sqbase();
		translate([0,0,height / 2]) difference() {
			cube([size + ext, size + ext, height] , center = true);
			cube([size + ext - wall, size + ext- wall, height*1.001], center = true);
		}
	}
}

module negative() {
	difference() {
		cube([size + ext, size + ext, height * 2], center = true);
		translate([0, 0, -height * 0]) img();
	}
}

positive();