module section(w, h, l, t, d, d2) {
	difference() {
		cube([2*t+w, t+l, 2*t+h]);
		translate([t,0,t]) cube([w, l, h]);//.
		translate([t+d,0,0]) cube([w-2*d,l,h+2*t]);
		translate([t,0,d2+t]) cube([w,l+t,h-d2]);
	}
}

//n, m - параметры матрицы.
//w,h,l - параметры нишы.
//t - толщина стенок.
//d - выступ поддержки.
//d2 - высота заднего бампера.
module storage(m, n, w, h, l, t, d, d2) {
	//sect = section(w,h,l,t,d, d2)
	//transes = []
	//for i in range(0,n):
	//	for j in range(0,m):
	//		transes.append(trans.translate(j*(w+t), 0, i*(h+t)))
	//plate = solid.box(w*m + t*(n+1),l+t,t)
	//return util.multiple_transform(sect, transes) + plate + plate.up(h*n+t*n)
	union() {
		for (i = [0 : 1 : n-1])
			for (j = [0 : 1 : m-1])
				translate([j*(w+t),0,i*(h+t)]) section(w,h,l,t,d,d2); 
		cube([w*m+t*(m+1), l+t, t]);
		translate([0,0,h*n+t*n]) cube([w*m + t*(m+1),l+t,t]);
	}
}

rotate([-90,0,0]) storage(4,6,27,20,64,1.5,5,5);