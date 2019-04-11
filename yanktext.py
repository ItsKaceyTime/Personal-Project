import sys
from functools import partial
import struct

if __name__ == "__main__":
    with open("dirty.gba", "rb") as infile:
        state = None
        datasize = 0
        scenecount = 0
        scenes = []
        textsize = 0
        data = []
        read = 5
        #while (not EOF):
        #    pass
        for chunk in iter(partial(infile.read, 4), b''):
            if (state == None and chunk == b'STR '):
                state = "SIZE"
                continue
            if (state == "SIZE"):
                datasize = struct.unpack('<I', chunk)[0]
                state = "OFFSET"
                continue
            if (state == "OFFSET"):
                scenecount = struct.unpack('<I', chunk)[0]
                state = "VERIFY"
                continue
            if (state == "VERIFY"):
                if (chunk == b'\x00\x00\x00\x00'):
                    state = "SCENES"
                    scenes.append(0)
                else:
                    state = None
                datasize -= 4
            if (state == "SCENES" and scenecount > 0):
                scenecount -= 1
                scenes.append(struct.unpack('<I', chunk)[0])
                datasize -= 4
                if (scenecount == 0):
                    state = "TEXT"
                    print("---SCENE---")
            if (state == "TEXT"):
                try:
                    data.append(chunk)
                except:
                    pass
                datasize -= 4
                if (datasize < -1):
                    for byte in data:
                    #     for char in byte:
                    #         if (bytes(char) == b'\x0d'):    # CR
                    #             char = 0
                    #         elif (bytes(char) == b'\x05'):  # EOT
                    #             char = 0
                    #         elif (bytes(char) == b'\x0c'):  # FF
                    #             char = 0
                        try:
                            print(bytes(byte).decode(),end='')
                        except:
                            print("_", end='')
                    print("")
                    data = []
                    state = None
                    scenes = []
                    read -=1
                    if (read == 0):
                        sys.exit()