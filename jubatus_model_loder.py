import argparse
import socket
from jubatus.classifier.client import Classifier

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="set the name of the file to load")
parser.add_argument("--host", help="set the host address")
parser.add_argument("--port", help="set the port number")

args = parser.parse_args()
print(args)
host_ip = args.host if args.host else socket.gethostbyname(socket.gethostname())
port = args.port if args.port else 9199

client = Classifier(host_ip, port, "")

if args.name:
    print(args.name)
    client.load(args.name)
    print("model " + args.name + " has been loaded")
else:
    print("[Error] specify the model's name to be loaded!")
