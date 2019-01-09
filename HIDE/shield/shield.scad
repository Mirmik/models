
size = 100;
ext = 6;
wall = 4;
height = 1;

module img() {
	translate([-size/2,-size/2]) 
		linear_extrude(height + 1, convexity= 4)
			resize([size,size]) 
				offset(r = 0.1) import("image.dxf");
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
		translate([-2,-0.6,0])img();
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

//img();
positive();