from motherofissues import motherofissues
import sys

def get_settings():
    settings = {}
    with open('settings.txt', 'r') as settings_file:
        for line in settings_file:
            kv = line.partition("=")
            settings[kv[0]] = kv[2].replace("\n", "")
    return settings

if __name__ == '__main__':
    help_options = ["--help", "--h"]
    if any(sys.argv[1] in s for s in help_options):
        print "usage: python main.py [category]\n"
        print "[category]: either `all` or your own custom category"
    elif sys.argv[1] is not None:
        motherofissues.run(sys.argv[1], get_settings())
    else:
        motherofissues.run(None, get_settings())
