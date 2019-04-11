import sys
from functools import partial
import struct

def parseFile(f):
    state = None
    datasize = 0
    scenecount = 0
    scenes = []
    textsize = 0
    data = []
    #while (not EOF):
    #    pass
    for chunk in iter(partial(f.read, 4), b''):
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
                yield("---SCENE---\n")
            continue
        if (state == "TEXT"):
            try:
                data.append(chunk)
            except:
                pass
            datasize -= 4
            if (datasize < -1):
                for byte in data:
                    chars = list(byte)
                    for char in range(len(chars)):
                    #     if (chars[char] == 0x0d):    # CR
                    #         chars[char] = 0x00
                    #     elif (chars[char] == 0x05):  # EOT
                    #         chars[char] = 0x00
                    #     elif (chars[char] == 0x0c):  # FF
                    #         chars[char] = 0x00
                    #     elif (chars[char] == 0x0a):  # LF
                        if (chars[char] in [0x00, 0x05, 0x0c, 0x0d]):
                            chars[char] = 0x00
                        elif (chars[char] == 0x0a):
                            pass
                        elif (chars[char] > 0x7e or chars[char] < 0x20):
                            chars[char] = 0x7e
                    try:
                        yield(bytes([x for x in chars if x != 0x00]).decode())
                    except:
                        yield("~")
                yield("\n")
                data = []
                state = None
                scenes = []

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("Program needs a rom to read from! Call it as:")
        print("yanktext.py [filename]")
        sys.exit()
    if (len(sys.argv) == 2):
        with open(sys.argv[1], "rb") as infile:
            for data in parseFile(infile):
                print(data, end='')
                