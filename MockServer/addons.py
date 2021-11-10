import os
import joker

addons = [
    joker.Joker()
]

if __name__ == "__main__":
    os.system("mitmweb -s addons.py")