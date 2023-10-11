from cmds import begin_sim_commands, restart_sim_commands
from directkeys import PressKey, GRAVE, ENTER
import time
import keyboard


class Bot:
    
    def __init__(self, n_sims):
        self.n_sims = n_sims
    
    def run_start_commands(self):
        time.sleep(3)
        # Opening player console
        PressKey(GRAVE)
        
        time.sleep(1)
        for cmd in begin_sim_commands:
            keyboard.write(cmd) 
            time.sleep(1)
            PressKey(ENTER)
        
        
bot = Bot(1)
bot.run_start_commands()


        
        
        
        
        

