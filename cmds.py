begin_sim_commands = [
"sv_cheats 0;",
"sv_cheats 1; ",
"mp_freezetime 0; ",
"mp_roundtime 1000000; ",
"mp_maxmoney 100000; ",
"mp_startmoney 100000; ",
"mp_afterroundmoney 100000; ",
"sv_infinite_ammo 2; ",
"r_drawviewmodel 0; ",
"r_draw_only_deathnotices = 0; ",
"mp_do_warmup_period 0; ",
"sv_infinite_ammo 2; ",
"mp_round_restart_delay 0; ",
"mp_buytime 0; ",
"mp_maxrounds 100; ",
"crosshair 0",
"give weapon_ak47",
"mp_restartgame 1; "
]

shooting_sequence_commands = [
    "setpos -500 545 130;",
    "setang 3 90 0.00000;", 
    "give weapon_ak47",
]

restart_round = [
    "endround;"
]
