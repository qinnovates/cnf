// ============================================================
// EMG Subvocalization Chin Strap — Parametric Design
// ============================================================
// 4-channel electrode holder for jaw/chin/throat EMG
// Designed for standard 10mm Ag/AgCl snap electrodes
//
// Print guide:
//   Chin cradle + throat arm + ear hooks: TPU 95A (flexible)
//   Jaw arms + electronics box: PLA (rigid)
//   Layer height: 0.2mm, 3 walls, 15-20% infill
//
// Adjust the parameters below to fit your face.
// Measure with a flexible tape measure or string.
// ============================================================

// === USER PARAMETERS (adjust these) ========================

// Measure chin width at the widest point of your jawline
chin_width = 55;           // mm, typical range: 45-65

// Measure from chin tip to ear tragus (front of ear hole)
chin_to_ear = 130;         // mm, typical range: 110-150

// Measure from chin underside to Adam's apple
chin_to_throat = 90;       // mm, typical range: 70-110

// Measure from ear tragus over top of head to other ear
ear_to_ear_over_head = 340; // mm, typical range: 300-380

// Strap width (wider = more stable, narrower = more comfortable)
strap_width = 16;          // mm

// Strap thickness
strap_thickness = 2.5;     // mm (TPU parts)
rigid_thickness = 3.0;     // mm (PLA parts)

// === ELECTRODE PARAMETERS ==================================

// Standard Ag/AgCl snap electrode dimensions
electrode_well_diameter = 12;   // mm, outer well
electrode_snap_hole = 4.2;      // mm, center snap-through hole
electrode_well_depth = 3;       // mm

// Cable channel
cable_channel_width = 4;        // mm
cable_channel_depth = 2.5;      // mm

// === RESOLUTION ============================================
$fn = 60;  // curve smoothness (increase for final print)

// === COLORS (for preview only) =============================
color_tpu = [0.3, 0.7, 0.9, 0.85];   // blue (flexible parts)
color_pla = [0.9, 0.9, 0.9, 0.9];    // white (rigid parts)
color_electrode = [0.8, 0.2, 0.2, 1]; // red (electrode wells)

// === MODULES ===============================================

// Electrode well — recessed pocket for snap electrode
module electrode_well() {
    difference() {
        // Raised pad around well
        cylinder(h = electrode_well_depth + 1.5,
                 d = electrode_well_diameter + 4);

        // Well cavity
        translate([0, 0, 1.5])
            cylinder(h = electrode_well_depth + 0.1,
                     d = electrode_well_diameter);

        // Snap-through hole (all the way through)
        translate([0, 0, -0.1])
            cylinder(h = electrode_well_depth + 2,
                     d = electrode_snap_hole);

        // Wire exit slot
        translate([electrode_well_diameter/2 - 1,
                   -cable_channel_width/2, 1.5])
            cube([6, cable_channel_width, electrode_well_depth + 0.1]);
    }
}

// Cable channel — groove for routing electrode wires
module cable_channel(length) {
    translate([0, -cable_channel_width/2,
               strap_thickness - cable_channel_depth])
        cube([length, cable_channel_width, cable_channel_depth + 0.1]);
}

// Rounded strap segment
module strap_segment(length, width = strap_width,
                     thickness = strap_thickness) {
    hull() {
        translate([0, 0, 0])
            cylinder(h = thickness, d = width);
        translate([length, 0, 0])
            cylinder(h = thickness, d = width);
    }
}

// Curved strap that follows an arc
module curved_strap(radius, angle, width = strap_width,
                    thickness = strap_thickness) {
    steps = max(12, abs(angle) / 3);
    step_angle = angle / steps;

    for (i = [0 : steps - 1]) {
        a1 = i * step_angle;
        a2 = (i + 1) * step_angle;
        hull() {
            rotate([0, 0, a1])
                translate([radius, 0, 0])
                    cylinder(h = thickness, d = width);
            rotate([0, 0, a2])
                translate([radius, 0, 0])
                    cylinder(h = thickness, d = width);
        }
    }
}


// ============================================================
// PART 1: CHIN CRADLE
// Sits under the chin, holds CH1 (mentalis) + CH3 (submental)
// Print in TPU
// ============================================================
module chin_cradle() {
    color(color_tpu)
    difference() {
        union() {
            // Main chin cup — curved shell
            // Approximate chin curve as a partial torus/sphere section
            chin_radius = chin_width / 2;

            // Base plate (curved to follow chin contour)
            hull() {
                // Front (under lip)
                translate([0, chin_radius * 0.6, 0])
                    cylinder(h = strap_thickness, d = strap_width);
                // Left
                translate([-chin_radius, 0, 0])
                    cylinder(h = strap_thickness, d = strap_width);
                // Right
                translate([chin_radius, 0, 0])
                    cylinder(h = strap_thickness, d = strap_width);
                // Back (under chin center)
                translate([0, -chin_radius * 0.3, 0])
                    cylinder(h = strap_thickness, d = strap_width);
            }

            // CH1 electrode mount (mentalis - front of chin)
            translate([0, chin_radius * 0.4, 0])
                electrode_well();

            // CH3 electrode mount (submental - under chin center)
            translate([0, -chin_radius * 0.15, 0])
                electrode_well();

            // Left jaw arm connector tab
            translate([-chin_radius - 5, 0, 0])
                cylinder(h = strap_thickness, d = strap_width + 4);

            // Right jaw arm connector tab
            translate([chin_radius + 5, 0, 0])
                cylinder(h = strap_thickness, d = strap_width + 4);

            // Throat arm connector tab (goes down)
            translate([0, -chin_radius * 0.3 - 8, 0])
                cylinder(h = strap_thickness, d = strap_width + 4);
        }

        // Connector holes (for zip ties, elastic, or snap-fit)
        // Left
        translate([-chin_width/2 - 5, 0, -0.1])
            cylinder(h = strap_thickness + 1, d = 3);
        // Right
        translate([chin_width/2 + 5, 0, -0.1])
            cylinder(h = strap_thickness + 1, d = 3);
        // Bottom
        translate([0, -chin_width/2 * 0.3 - 8, -0.1])
            cylinder(h = strap_thickness + 1, d = 3);

        // Cable channels from electrodes to edges
        // CH1 to right edge
        translate([0, chin_width/2 * 0.4, 0])
            rotate([0, 0, -30])
                cable_channel(chin_width/2 + 10);
        // CH3 to bottom edge
        translate([0, -chin_width/2 * 0.15, 0])
            rotate([0, 0, -90])
                cable_channel(20);
    }
}


// ============================================================
// PART 2: JAW ARM (make 2 — left and right, mirrored)
// Runs from chin cradle along jawline to ear
// Holds CH2 (masseter) electrode
// Print in PLA
// ============================================================
module jaw_arm(side = "right") {
    mirror_x = (side == "left") ? 1 : 0;

    color(color_pla)
    mirror([mirror_x, 0, 0])
    difference() {
        union() {
            // Straight section from chin to jaw angle
            // Angle upward at ~30 degrees to follow jawline
            jaw_length = chin_to_ear * 0.6;  // to masseter
            ear_length = chin_to_ear * 0.4;  // masseter to ear

            // Lower section (chin to masseter)
            rotate([0, 0, 35])
                strap_segment(jaw_length, strap_width, rigid_thickness);

            // CH2 electrode mount (masseter)
            rotate([0, 0, 35])
                translate([jaw_length, 0, 0])
                    electrode_well();

            // Upper section (masseter to ear hook attachment)
            rotate([0, 0, 35])
                translate([jaw_length, 0, 0])
                    rotate([0, 0, 25])
                        strap_segment(ear_length, strap_width,
                                      rigid_thickness);

            // Ear hook attachment point
            rotate([0, 0, 35])
                translate([jaw_length, 0, 0])
                    rotate([0, 0, 25])
                        translate([ear_length, 0, 0])
                            cylinder(h = rigid_thickness,
                                     d = strap_width + 6);

            // Chin connector tab
            cylinder(h = rigid_thickness, d = strap_width + 4);
        }

        // Chin connector hole (matches chin cradle)
        translate([0, 0, -0.1])
            cylinder(h = rigid_thickness + 1, d = 3);

        // Ear hook connector hole
        rotate([0, 0, 35]) {
            jaw_length = chin_to_ear * 0.6;
            ear_length = chin_to_ear * 0.4;
            translate([jaw_length, 0, 0])
                rotate([0, 0, 25])
                    translate([ear_length, 0, -0.1])
                        cylinder(h = rigid_thickness + 1, d = 3);
        }

        // Cable channel along the arm
        rotate([0, 0, 35])
            cable_channel(chin_to_ear * 0.6 + 10);
    }
}


// ============================================================
// PART 3: THROAT ARM
// Descends from chin cradle to laryngeal position
// Holds CH4 (laryngeal/thyrohyoid) electrode
// Print in TPU
// ============================================================
module throat_arm() {
    throat_length = chin_to_throat * 0.7;  // don't go all the way

    color(color_tpu)
    difference() {
        union() {
            // Main arm going downward
            rotate([0, 0, -90])
                strap_segment(throat_length, strap_width,
                              strap_thickness);

            // CH4 electrode mount (laryngeal)
            rotate([0, 0, -90])
                translate([throat_length, 0, 0])
                    electrode_well();

            // Chin connector tab (top)
            cylinder(h = strap_thickness, d = strap_width + 4);

            // Adjustable sizing: multiple holes along length
            for (i = [0 : 3]) {
                pos = throat_length * 0.5 + i * 10;
                rotate([0, 0, -90])
                    translate([pos, 0, 0])
                        cylinder(h = strap_thickness, d = 8);
            }
        }

        // Chin connector hole
        translate([0, 0, -0.1])
            cylinder(h = strap_thickness + 1, d = 3);

        // Adjustment holes (slide to adjust throat electrode position)
        for (i = [0 : 3]) {
            pos = throat_length * 0.5 + i * 10;
            rotate([0, 0, -90])
                translate([pos, 0, -0.1])
                    cylinder(h = strap_thickness + 1, d = 3);
        }

        // Cable channel
        rotate([0, 0, -90])
            cable_channel(throat_length + 5);
    }
}


// ============================================================
// PART 4: EAR HOOKS (make 2 — left and right)
// Loop over each ear, connected by over-head strap
// Print in TPU
// ============================================================
module ear_hook(side = "right") {
    mirror_x = (side == "left") ? 1 : 0;

    ear_hook_radius = 22;  // mm, fits around ear

    color(color_tpu)
    mirror([mirror_x, 0, 0])
    difference() {
        union() {
            // Hook curve (wraps behind ear)
            curved_strap(ear_hook_radius, 200, strap_width - 2,
                         strap_thickness);

            // Jaw arm connector tab
            cylinder(h = strap_thickness, d = strap_width + 4);

            // Top: over-head strap connector
            rotate([0, 0, 200])
                translate([ear_hook_radius, 0, 0])
                    cylinder(h = strap_thickness, d = strap_width + 4);
        }

        // Jaw arm connector hole
        translate([0, 0, -0.1])
            cylinder(h = strap_thickness + 1, d = 3);

        // Head strap connector hole
        rotate([0, 0, 200])
            translate([ear_hook_radius, 0, -0.1])
                cylinder(h = strap_thickness + 1, d = 3);
    }
}


// ============================================================
// PART 5: OVER-HEAD STRAP
// Connects left and right ear hooks over the top of the head
// Print in TPU, or use elastic webbing
// ============================================================
module head_strap() {
    // Arc from ear to ear over the head
    head_radius = ear_to_ear_over_head / 3.14159;  // approximate
    arc_angle = 160;  // degrees of arc

    color(color_tpu)
    difference() {
        union() {
            // Main arc
            translate([0, 0, head_radius])
                rotate([90, 0, 0])
                    curved_strap(head_radius, arc_angle,
                                 strap_width - 4, strap_thickness);

            // End tabs with velcro/adjustment slots
            rotate([90, 0, 0])
                translate([0, 0, 0]) {
                    translate([head_radius, 0, 0])
                        cylinder(h = strap_thickness,
                                 d = strap_width + 4);
                    rotate([0, 0, arc_angle])
                        translate([head_radius, 0, 0])
                            cylinder(h = strap_thickness,
                                     d = strap_width + 4);
                }
        }

        // Adjustment slots along the strap
        for (i = [30 : 20 : arc_angle - 30]) {
            rotate([90, 0, 0])
                rotate([0, 0, i])
                    translate([head_radius, 0, -0.1])
                        hull() {
                            cylinder(h = strap_thickness + 1, d = 3);
                            translate([5, 0, 0])
                                cylinder(h = strap_thickness + 1,
                                         d = 3);
                        }
        }
    }
}


// ============================================================
// PART 6: ELECTRONICS ENCLOSURE
// Houses ESP32 + ADS1115 + battery
// Clips to head strap or sits behind ear
// Print in PLA
// ============================================================
module electronics_box() {
    // ESP32 DevKit: ~55 x 28 x 13 mm
    // ADS1115 breakout: ~20 x 15 x 3 mm
    // LiPo battery: ~50 x 30 x 8 mm

    inner_length = 62;
    inner_width = 35;
    inner_height = 28;
    wall = 1.6;

    color(color_pla)
    difference() {
        union() {
            // Outer shell
            translate([-inner_length/2 - wall,
                       -inner_width/2 - wall, 0])
                cube([inner_length + wall*2,
                      inner_width + wall*2,
                      inner_height + wall]);

            // Clip tabs for head strap attachment
            translate([-15, -inner_width/2 - wall - 3,
                       inner_height/2])
                cube([30, 3, 10]);
            translate([-15, inner_width/2 + wall,
                       inner_height/2])
                cube([30, 3, 10]);
        }

        // Inner cavity
        translate([-inner_length/2, -inner_width/2, wall])
            cube([inner_length, inner_width, inner_height + 1]);

        // USB port opening (ESP32 micro-USB)
        translate([-inner_length/2 - wall - 1, -5, wall + 2])
            cube([wall + 2, 10, 8]);

        // Wire entry holes (4 channels + ground)
        for (i = [-2 : 2]) {
            translate([inner_length/2 + wall - 0.5,
                       i * 6, wall + inner_height/2])
                rotate([0, 90, 0])
                    cylinder(h = wall + 2, d = 3.5);
        }

        // Ventilation slots (top)
        for (i = [-2 : 2]) {
            translate([i * 10, -inner_width/4,
                       inner_height + wall - 0.5])
                cube([6, inner_width/2, wall + 1]);
        }

        // Clip slot for head strap
        translate([-12, -inner_width/2 - wall - 4,
                   inner_height/2 + 2])
            cube([24, 10 + inner_width + wall*2, 3]);
    }

    // Internal dividers
    color(color_pla)
    union() {
        // Battery shelf (lower level)
        translate([-inner_length/2 + 1, -inner_width/2 + 1,
                   wall + 10])
            cube([inner_length - 2, inner_width - 2, 1]);

        // ADS1115 standoffs
        for (pos = [[-10, -8], [-10, 8], [10, -8], [10, 8]]) {
            translate([pos[0], pos[1], wall])
                cylinder(h = 12, d = 3);
        }
    }
}


// ============================================================
// PART 7: ELECTRONICS BOX LID
// Snap-fit or screw-on lid
// Print in PLA
// ============================================================
module electronics_lid() {
    inner_length = 62;
    inner_width = 35;
    wall = 1.6;
    lid_thickness = 1.6;

    color(color_pla)
    union() {
        // Lid plate
        translate([-inner_length/2 - wall,
                   -inner_width/2 - wall, 0])
            cube([inner_length + wall*2,
                  inner_width + wall*2, lid_thickness]);

        // Inner lip (friction fit)
        translate([-inner_length/2 + 0.3,
                   -inner_width/2 + 0.3, -3])
            difference() {
                cube([inner_length - 0.6, inner_width - 0.6, 3]);
                translate([wall, wall, -0.1])
                    cube([inner_length - 0.6 - wall*2,
                          inner_width - 0.6 - wall*2, 3.2]);
            }
    }
}


// ============================================================
// PART 8: REFERENCE ELECTRODE CLIP
// Small clip for REF/GND electrode behind the ear (mastoid)
// Print in TPU
// ============================================================
module ref_electrode_clip() {
    clip_width = 20;
    clip_radius = 12;  // curves around the ear

    color(color_tpu)
    difference() {
        union() {
            // Curved clip body
            curved_strap(clip_radius, 120, clip_width,
                         strap_thickness);

            // Electrode well on inner surface
            rotate([0, 0, 60])
                translate([clip_radius, 0, 0])
                    electrode_well();
        }

        // Cable exit
        rotate([0, 0, 60])
            translate([clip_radius + 5,
                       -cable_channel_width/2,
                       strap_thickness - cable_channel_depth])
                cube([10, cable_channel_width,
                      cable_channel_depth + 0.1]);
    }
}


// ============================================================
// ASSEMBLY VIEW
// Shows all parts in their approximate wearing positions
// Use this for visualization only — export parts individually
// ============================================================
module assembly() {
    // Chin cradle (center)
    chin_cradle();

    // Jaw arms
    translate([-chin_width/2 - 5, 0, 0])
        jaw_arm("left");
    translate([chin_width/2 + 5, 0, 0])
        jaw_arm("right");

    // Throat arm
    translate([0, -chin_width/2 * 0.3 - 8, 0])
        throat_arm();

    // Ear hooks (positioned approximately)
    translate([-chin_to_ear * 0.55, chin_to_ear * 0.45, 0])
        ear_hook("left");
    translate([chin_to_ear * 0.55, chin_to_ear * 0.45, 0])
        ear_hook("right");

    // Reference electrode clip
    translate([chin_to_ear * 0.6, chin_to_ear * 0.5, 0])
        ref_electrode_clip();

    // Electronics box (behind right ear area)
    translate([chin_to_ear * 0.5, chin_to_ear * 0.6, 10])
        electronics_box();

    // Electronics lid
    translate([chin_to_ear * 0.5, chin_to_ear * 0.6, 38.5])
        electronics_lid();
}


// ============================================================
// PLATING VIEW — Individual parts laid flat for printing
// Uncomment the view you want to render/export
// ============================================================
module print_plate() {
    // Chin cradle
    translate([0, 0, 0])
        chin_cradle();

    // Right jaw arm
    translate([80, 0, 0])
        jaw_arm("right");

    // Left jaw arm
    translate([80, 60, 0])
        jaw_arm("left");

    // Throat arm
    translate([-70, 0, 0])
        throat_arm();

    // Right ear hook
    translate([0, 80, 0])
        ear_hook("right");

    // Left ear hook
    translate([60, 80, 0])
        ear_hook("left");

    // Reference electrode clip
    translate([-70, 80, 0])
        ref_electrode_clip();

    // Electronics box
    translate([0, -80, 0])
        electronics_box();

    // Electronics lid
    translate([80, -80, 0])
        electronics_lid();
}


// ============================================================
// SELECT WHAT TO RENDER
// ============================================================
// Uncomment ONE of these lines:

assembly();           // Full assembly view (default)
// print_plate();     // All parts laid flat for printing
// chin_cradle();     // Export individual part
// jaw_arm("right");  // Export individual part
// jaw_arm("left");   // Export individual part
// throat_arm();      // Export individual part
// ear_hook("right"); // Export individual part
// ear_hook("left");  // Export individual part
// head_strap();      // Export individual part
// electronics_box(); // Export individual part
// electronics_lid(); // Export individual part
// ref_electrode_clip(); // Export individual part
