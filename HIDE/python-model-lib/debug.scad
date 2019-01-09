$fn = 40;

union() {
	union() {
		translate(v = [2, 2, 0]) {
			offset(r = 2) {
				square(size = [6, 16]);
			}
		}
		translate(v = [0.0000000000, 0.0000000000, 0]) {
			square(size = [5.0000000000, 10.0000000000]);
		}
	}
	translate(v = [5.0000000000, 0.0000000000, 0]) {
		square(size = [5.0000000000, 10.0000000000]);
	}
}