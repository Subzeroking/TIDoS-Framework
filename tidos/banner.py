# coding: utf-8
#!/usr/bin/env python
from random import *
####################################
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
####################################
def banner():
    infected = color.RED + color.BOLD+"""

                                ▄▀▀▀█▀▀▄  ▄▀▀█▀▄    ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄ 
            _____              █    █  ▐ █   █  █  █ ▄▀   █ █      █  ██   ▐   \033[1;37m【!】 Infection\033[0m      
        \033[1;31m0)—)_____))———.        ▐   █     ▐   █  ▐  ▐ █    █ █      █    ▀▄              \033[1;93mOVERLOADED !!!\033[0m   
                      @           \033[1;31m█          █       █    █ ▀▄    ▄▀ ▀▄   ██  
                                ▄▀        ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀▀   
                               █         █       █ █     ▐            ▐      
                               ▐         ▐       ▐ ▐                         

"""


    oblique = color.CYAN + color.BOLD+"""


                              ███      ▄█  ████████▄   ▄██████▄     ▄████████ 
                          ▀█████████▄ ███  ███   ▀███ ███    ███   ███    ███    \033[1;91mSo YOU think you are SMART ?\033[0m
       \033[1;33mPING-OF-DEATH         \033[1;36m▀███▀▀██ ███▌ ███    ███ ███    ███   ███    █▀          \033[1;91m( ⊙ _ ⊙ ) 
            \033[1;33mis a              \033[1;36m███   ▀ ███▌ ███    ███ ███    ███   ███               \033[1;37mYes! YOU are ;) !!!
           \033[1;31mD D o S            \033[1;36m███     ███▌ ███    ███ ███    ███ ▀███████████ 
                    \033[1;32m◕_◕       \033[1;36m███     ███  ███    ███ ███    ███          ███ 
                              ███     ███  ███   ▄███ ███    ███    ▄█    ███ 
                             ▄████▀   █▀   ████████▀   ▀██████▀   ▄████████▀  

"""


    straight = color.GREEN + color.BOLD+"""

                \033[1;93m| |  \033[1;37m*tock*       \033[1;92m████████╗██╗██████╗  ██████╗ ███████╗        
                \033[1;93m| |     \033[1;37m*tock*    \033[1;92m╚══██╔══╝██║██╔══██╗██╔═══██╗██╔════╝         
                \033[1;93m| \033[1;93m<-*)               \033[1;32m██║   ██║██║  ██║██║   ██║███████╗    \033[1;31mThere the \033[1;93mF B I
                \033[1;93m| |\033[1;93m(()               \033[1;32m██║   ██║██║  ██║██║   ██║╚════██║        \033[1;31mknocks at the DOOR !!!
                \033[1;93m| |\033[1;93m"/                \033[1;32m██║   ██║██████╔╝╚██████╔╝███████║
                \033[1;93m| |\033[1;93m'                 \033[1;32m╚═╝   ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                     
"""



    shadow = color.CYAN + color.BOLD+"""

                          ÛÛÛÛÛÛÛÛÛÛÛ ÛÛÛÛÛ ÛÛÛÛÛÛÛÛÛÛ             ÛÛÛÛÛÛÛÛÛ         \033[1;37m01011001011011110111010100100000011
         \033[1;94mD O N'T         \033[1;96m°Û°°°ÛÛÛ°°°Û°°ÛÛÛ °°ÛÛÛ°°°°ÛÛÛ           ÛÛÛ°°°°°ÛÛÛ       \033[1;37m0011101101111011101000010000001101100
     \033[1;94mH E S I T A T E     \033[1;96m°   °ÛÛÛ  °  °ÛÛÛ  °ÛÛÛ   °°ÛÛÛ  ÛÛÛÛÛÛ °ÛÛÛ    °°°         \033[1;37m00110110101100101001000000110010001
                             \033[1;36m°ÛÛÛ     °ÛÛÛ  °ÛÛÛ    °ÛÛÛ ÛÛÛ°°ÛÛÛ°°ÛÛÛÛÛÛÛÛÛ        \033[1;37m1001010110001101101111011001000110010
            \033[1;37mD O              \033[1;36m°ÛÛÛ     °ÛÛÛ  °ÛÛÛ    °ÛÛÛ°ÛÛÛ °ÛÛÛ °°°°°°°°ÛÛÛ         \033[1;37m101100100001000000010000100100001
             \033[1;37mI T             \033[1;36m°ÛÛÛ     °ÛÛÛ  °ÛÛÛ    ÛÛÛ °ÛÛÛ °ÛÛÛ ÛÛÛ    °ÛÛÛ        
                             \033[1;36mÛÛÛÛÛ    ÛÛÛÛÛ ÛÛÛÛÛÛÛÛÛÛ  °°ÛÛÛÛÛÛ °°ÛÛÛÛÛÛÛÛÛ                 \033[1;93m- There!! Decode this
                             \033[1;36m°°°°°    °°°°° °°°°°°°°°°    °°°°°°   °°°°°°°°°                         \033[1;93mONLY IF YOU CAN !!!
"""
    birdie = color.CYAN + color.BOLD+"""

                               ********** **  *******             ********
                   \033[1;31m>\_/<       \033[1;96m/////**/// /** /**////**           **//////     \033[1;93mI am Watching
                  \033[1;31m_\*v*/_          \033[1;96m/**    /** /**    /**  ****** /**                    \033[1;93m●_●
                  \033[1;31m\.   ./          \033[1;36m/**    /** /**    /** **////**/*********             
                 \033[1;31m===="====         \033[1;36m/**    /** /**    /**/**   /**////////**       \033[1;93mD O N'T   B R E A K
                    \033[1;31m/^\            \033[1;96m/**    /** /**    ** /**   /**       /**                \033[1;93mB A D
                                   \033[1;96m/**    /** /*******  //******  ******** 
                                   //     //  ///////    //////  ////////  

"""
    merlin = color.WARNING + color.BOLD+"""
                           ___________  __     ________      ______    ________            \033[1;96m.---.        .-----------
                          \033[1;93m("     _   ")|" \   |"      "\    /    " \  /"       )          \033[1;96m/     \  __  /    ------
       \033[1;36mT H E   B L U E     \033[1;93m)__//  \__/ ||  |  (.  ___  :)  // ____  \(:   \___/          \033[1;96m/ /     \(  )/    -----
         \033[1;36mF A L C O N          \033[1;93m\ _ /    |:  |  |: \   ) || /  /    ) :)\___  \           \033[1;96m//////   ' \/ `   ---
                              \033[1;33m|.  |    |.  |  (| (___\ ||(: (____/ //  __//  \         \033[1;96m//// / // :    : ---
                              \033[1;33m\:  |    /\  |\ |:       :) \        /  /" \   :)       \033[1;96m// /   /  /`    '--
                               \033[1;33m\__|   (__\_|_)(________/   \______/  (_______/       \033[1;96m//           /||\
                                                                                                                    \033[1;93m=============\033[1;96mUU\033[1;93m====\033[1;96mUU\033[1;93m====
                                                                                                \033[1;96m'%/||\%`
                                                                                                  \033[1;96m''``
"""
    headers = [infected, oblique, straight, shadow, birdie, merlin]
    print headers[randint(0,5)]
