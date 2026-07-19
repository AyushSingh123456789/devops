import time, sys

try:
    while True: # The main program loop
        # Draw lines with increasing length:
        for i in range(1,9):
            print('-' * (i * i))
            # first i = 1 => i * i = 1 no of '-' printed
            # second i = 2 => i * i = 4 no of '-' printed
            # third i = 3 => i * i = 9 no of '-' printed .... till i = 8
            time.sleep(0.1)
        
        # Draw lines with decreasing length:
        for i in range(7, 1, -1):
            print('-' * (i * i))
            # first i = 7 => i * i = 49 no of '-' printed
            # second i = 6 => i * i = 36 no of '-' printed
            # third i = 5 => i * i = 25 no of '-' printed .... till i = 2
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
        