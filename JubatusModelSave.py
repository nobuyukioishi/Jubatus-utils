from jubatus.classifier.client import Classifier

if __name__ == '__main__':
    client = Classifier("192.168.11.173", 9199, '')
    client.save("default9_20180427")
