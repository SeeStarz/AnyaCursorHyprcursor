#!/bin/python
from subprocess import call
from os import listdir

call("rm cursors/*", shell=True)

files = listdir("config")
for file in files:
    if file[-3:] == ".in":
        call(f"xcursorgen 'config/{file}' 'cursors/{file[:-3]}'", shell=True)

translate = {
    "help_select": ["question_arrow", "help", "left_ptr_help", "whats_this", "dnd-ask", "5c6cd98b3f3ebcb1f9c7f1c204630408", "d9ce0ab605698f320427677b458ad60b"],
    "horizontal": ["sb_h_double_arrow", "e-resize", "ew-resize", "w-resize", "h_double_arrow", "size-hor", "size_hor", "col-resize", "left_side", "right_side", "left_tee", "right_tee", "028006030e0e7ebffc7f7070c0600140", "14fef782d02440884392942c11205230"],
    "link_select": ["hand2", "link", "dnd-link", "3085a0e285430894940527032f8b26df", "640fb0e74195791501fd1ed57b41487f", "e29285e634086352946a0e7090d73106"],
    "move": ["hand1", "hand", "grab", "openhand", "fleur", "grabbing", "dnd-move", "dnd-copy",
             "1081e37283d90000800003c07f3ef6bf", "4498f0e0c1937ffe01fd06f973665830", "6407b0e94181790501fd1e167b474872", "9081237383d90e509aa00f00170e968f", "9d800788f1b08800ae810202380a0822"],
    "nesw_resize": ["fd_double_arrow", "ne-resize", "sw-resize", "size_bdiag", "bottom_left_corner", "top_right_corner", "ur_angle", "ll_angle", "fcf1c3c7cd4491d801f1e1c78f100000"],
    "normal": ["arrow", "default", "left_ptr", "left_ptr_watch", "watch", "draft_large", "draft_small", "right_ptr", "pencil", "08e8e1c95fe2fc01f976f1e063a24ccd", "3ecb610c1bf2410f44200f48c40d3599"],
    "nwse_resize": ["bd_double_arrow", "nw-resize", "se-resize", "size_fdiag", "bottom_right_corner", "top_left_corner", "ul_angle", "lr_angle", "c7088f0f3e6c8088236ef8e1e3e70000"],
    "precision_select": ["pointer", "pointing_hand", "dotbox", "dot_box_mask", "draped_box", "icon", "plus", "crosshair"],
    "text_select": ["xterm", "ibeam", "text"],
    "unavailable": ["crossed_circle", "cross", "tcross", "forbidden", "not-allowed", "dnd-none", "corss_reverse", "diamond_corss", "X_cursor", "pirate", "03b6e0fcb3499374a867c041f52298f0"],
    "vertical": ["sb_v_double_arrrow", "n_resize", "ns_resize", "s_resize", "size_ver", "size-ver", "v_double_arrow", "row-resize", "sb_up_arrow", "sb_down_arrow", "top_side", "bottom_side", "top_tee", "bottom_tee", "00008160000006810000408080010102", "2870a09082c103050810ffdffffe0204"]
}

for key in translate:
    values = translate[key]
    for value in values:
        call(f"ln -s ../cursors/{key} cursors/{value}", shell=True)
