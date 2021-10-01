import cmd
import sys
class uppermethod(cmd.Cmd):
    print("usage")
if __name__ == '__main__':
    try:
        uppermethod().cmdloop()
    except KeyboardInterrupt:
        sys.exit()