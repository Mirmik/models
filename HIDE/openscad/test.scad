$fn = 32;

module thread(od, id, l, step, m) {
	or = od / 2; ir = id / 2;
	c=(or-ir)/2;
	r=(or+ir)/2;

    cs = cos((l-step)/step*360);
    ss = -sin((l-step)/step*360);

	//union() {
        /*linear_extrude(step, twist = 360, scale = m)
            translate([c/m,0]) 
                circle(r/m);*/
        
        //translate([0,0,step])
        linear_extrude(l, twist = l / step*360, slices = 20 * l / step)
            translate([c,0]) 
                circle(r);
        
        /*translate([0,0,l-step])
        linear_extrude(step, twist = 360, scale = 1/m)
            translate([c*cs,c*ss]) 
                circle(r);*/
    //} 
}

difference() {
   cylinder(h=6, r = 6);
   thread(od=8, id=6.466, l=6, step=1.25, m = 1.05);
}
//#translate([0,0,-3]) cylinder(r=4,h=10,$fn = 32);

//rotate_extrude() {
//        square([3,7]);
//};