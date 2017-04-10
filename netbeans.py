#!/usr/bin/env python
import os
import os.path

def read_conf():
    with open("/home/lukas/confs/ntb_conf","r") as conf_file:
        array = []
        for line in conf_file:
            array.append(line)
        return array[0]
def run():
    loc = str(read_conf())
    print(loc)
    os.system("/home/lukas/netbeans-8.2/bin/netbeans --jdkhome "+loc)

class Main:
    @staticmethod
    def checkIfExists():
        if os.path.exists("/home/lukas/netbeans-8.2/bin/netbeans"):
            run()
        else:
            print("Error. File couldn't be find.")

Main.checkIfExists()
