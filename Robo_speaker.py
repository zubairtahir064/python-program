import pyttsx3

if __name__ == "__main__":

    engine = pyttsx3.init()
    print("Welcom to robo Speaker 1.1 Created by Zubair")
    x = input("What you want me to speak and press e to exit: ")
    engine.say(x)
    engine.runAndWait()
    engine.stop()