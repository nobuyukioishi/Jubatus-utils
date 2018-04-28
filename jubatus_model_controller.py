import argparse
import socket
from jubatus.classifier.client import Classifier

parser = argparse.ArgumentParser()
parser.add_argument("-m","--mode", help="set the execution mode save(s)/load(l)")
parser.add_argument("-n","--name", help="set the name of the file to be saved/loaded")
parser.add_argument("--host", help="set the host address")
parser.add_argument("--port", help="set the port number")

args = parser.parse_args()
print(args)
host_ip = args.host if args.host else socket.gethostbyname(socket.gethostname())
port = args.port if args.port else 9199

if args.mode == "save" or args.mode == "s":
    client = Classifier(host_ip, port, '')
    if args.name:
        client.save(args.name)
        print("file saved at /tmp of the "+host_ip+" unless you specified output path with -d/--datadir when you started server process.")
    else:
        print("[Error] specify the model's name to be saved!")
elif args.mode == "load" or args.mode == "l":
    client = Classifier(host_ip, port, "")
    if args.name:
        print(args.name)
        client.load(args.name)
        print("model "+args.name+" was loaded")
    else:
        print("[Error] specify the model's name to be loaded!")
else:
    print("specify mode [-s/--save] or [-l/--load]")
