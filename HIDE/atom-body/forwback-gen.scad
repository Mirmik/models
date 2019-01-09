$fn = 40;

difference() {
	translate(v = [0, 0, 18.0710678119]) {
		rotate(a = [0, 90, 0]) {
			linear_extrude(convexity = 4, height = 120) {
				union() {
					hull() {
						translate(v = [0, 0]) {
							circle(r = 1);
						}
						translate(v = [10, 0]) {
							circle(r = 1);
						}
					}
					union() {
						hull() {
							translate(v = [10, 0]) {
								circle(r = 1);
							}
							translate(v = [17.0710678119, 7.0710678119]) {
								circle(r = 1);
							}
						}
						union() {
							hull() {
								translate(v = [17.0710678119, 7.0710678119]) {
									circle(r = 1);
								}
								translate(v = [17.0710678119, 32.0710678119]) {
									circle(r = 1);
								}
							}
							union() {
								hull() {
									translate(v = [17.0710678119, 32.0710678119]) {
										circle(r = 1);
									}
									translate(v = [10.0000000000, 39.1421356237]) {
										circle(r = 1);
									}
								}
								hull() {
									translate(v = [10.0000000000, 39.1421356237]) {
										circle(r = 1);
									}
									translate(v = [0.0000000000, 39.1421356237]) {
										circle(r = 1);
									}
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [20, 19.0710678119, 0]) {
		linear_extrude(height = 2) {
			union() {
				circle(r = 4);
				union() {
					union() {
						union() {
							translate(v = [8, 0, 0]) {
								circle(r = 1.6000000000);
							}
							rotate(a = [0, 0, 90.0000000000]) {
								translate(v = [8, 0, 0]) {
									circle(r = 1.6000000000);
								}
							}
						}
						rotate(a = [0, 0, 180.0000000000]) {
							translate(v = [8, 0, 0]) {
								circle(r = 1.6000000000);
							}
						}
					}
					rotate(a = [0, 0, 270.0000000000]) {
						translate(v = [8, 0, 0]) {
							circle(r = 1.6000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [100, 19.0710678119, 0]) {
		linear_extrude(height = 2) {
			union() {
				circle(r = 4);
				union() {
					union() {
						union() {
							translate(v = [8, 0, 0]) {
								circle(r = 1.6000000000);
							}
							rotate(a = [0, 0, 90.0000000000]) {
								translate(v = [8, 0, 0]) {
									circle(r = 1.6000000000);
								}
							}
						}
						rotate(a = [0, 0, 180.0000000000]) {
							translate(v = [8, 0, 0]) {
								circle(r = 1.6000000000);
							}
						}
					}
					rotate(a = [0, 0, 270.0000000000]) {
						translate(v = [8, 0, 0]) {
							circle(r = 1.6000000000);
						}
					}
				}
			}
		}
	}
}