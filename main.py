from waveGenerator import WaveGen
import os

def choose(option):
    if option not in ['1','2','3']:
        return
    
    if option == '3':
        exit()
    
    if option == '1':       #  To Encode
        secretMessage = input("Write a message: ")
        filename = input("Name audio wave file: ")
        wg.encode(secretMessage, filename)
        input("Press Enter...")

    if option == '2':       # To Decode
        audioFileName = input("Name the audio wave file (same folder as selected before): ")
        wg.decode(audioFileName)
        input("\n[Press Enter]")


def main():
    while True:
        os.system('cls')
        operation = input("\n\nPress:\n1) Generate an audio wave file with a secret message\n2) Decode Secret Message from audio .wav file\n3) Quit\n\n>> ")
        choose(operation)

wg = WaveGen()
main()

