import argparse
from jubatus.classifier.client import Classifier

parser = argparse.ArgumentParser()
parser.add_argument("-m","--mode", help="set the execution mode save(s)/load(l)")
parser.add_argument("-f","--file", help="load the model file at the specified path")
parser.add_argument("-n","--name", help="set the name of the file to be saved")
parser.add_argument("--host", help="set the host address")
parser.add_argument("--port", help="set the port number")

host_ip = args.host if args.host else socket.gethostbyname(socket.gethostname())
port = args.port if args.port else 9199
args = parser.parse_args()
print(args)

path_to_be_saved = args.save if args.save else nil

if args.mode == "save" or args.mode == "s":
    client = Classifier(host_ip, port, '')
    if args.save:
        client.save(args.name)
    print("file saved at /tmp unless you specified output path with -d/--datadir when executing server process.")
elif args.mode == "load" or args.mode == "l":
    print("load")
else:
    print("save or load!")
