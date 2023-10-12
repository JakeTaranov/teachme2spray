from cmds import begin_sim_commands, shooting_sequence_commands, restart_round
from directkeys import PressKey, ReleaseKey, GRAVE, ENTER, ESC
import time
import keyboard
import pywinauto


class Bot:
    
    def __init__(self, n_sims):
        self.n_sims = n_sims
    
    def run_start_commands(self):
        # countdown for program to begin
        for i in range(4)[::-1]:
            print("Running start commands in %i" % (i))
            time.sleep(1)
            
        # opening player console
        PressKey(GRAVE)
        time.sleep(1)
        
        # running all commands to begin match
        for cmd in begin_sim_commands:
            keyboard.write(cmd) 
            time.sleep(1)
            PressKey(ENTER)
        
        ReleaseKey(GRAVE)
        ReleaseKey(ENTER)
        
        # closing console
        PressKey(ESC)
        ReleaseKey(ESC)

            
    def run_shooting_sequence(self):

        time.sleep(1)
        # opening player console
        PressKey(GRAVE)
        time.sleep(1)
        
        for cmd in shooting_sequence_commands:
            keyboard.write(cmd) 
            time.sleep(1)
            PressKey(ENTER)
            
        # closing console again
        ReleaseKey(GRAVE)
        ReleaseKey(ENTER)
        PressKey(ESC)
        ReleaseKey(ESC)
        
        
        # shoot
        pywinauto.mouse.press(button='left', coords=(0,0))
        time.sleep(4)
        pywinauto.mouse.release(button='left', coords=(0, 0))
        
        time.sleep(1)
        PressKey(GRAVE)
        time.sleep(1)

        # restart round
        for cmd in restart_round:
            keyboard.write(cmd)
            time.sleep(1)
            PressKey(ENTER)
        
        # closing console 
        ReleaseKey(GRAVE)
        ReleaseKey(ENTER)
        PressKey(ESC)
        ReleaseKey(ESC)
         
            
        
            
    def wait_for_round_restart(self):
        time.sleep(5)
            
    
        

bot = Bot(1)

bot.run_start_commands()
bot.wait_for_round_restart()

while 1:
    bot.run_shooting_sequence()
    time.sleep(2)






        
        
        
        
        

