from gtts import gTTS
import os
import platform
import subprocess

def get_download_folder():
    return os.path.join(os.path.expanduser("~"), "Downloads")

def open_file(file_path):
    system_platform = platform.system()
    if system_platform == 'Darwin':  # macOS
        subprocess.run(['open', file_path])
    elif system_platform == 'Windows':
        os.startfile(file_path)
    elif system_platform == 'Linux':
        subprocess.run(['xdg-open', file_path])

def text_to_speech(text, voice_option):
    download_folder = get_download_folder()
    file_path = os.path.join(download_folder, f"output_{voice_option}.mp3")

    if voice_option == 1:
        tts = gTTS(text=text, lang='en', slow=False)
    elif voice_option == 2:
        tts = gTTS(text=text, lang='en', slow=False, tld='com.au')
    elif voice_option == 3:
        tts = gTTS(text=text, lang='en', slow=False, tld='co.uk')
    elif voice_option == 4:
        tts = gTTS(text=text, lang='en', slow=False, tld='ca')
    else:
        print("Invalid voice option. Please choose 1, 2, 3, or 4.")
        return

    tts.save(file_path)
    print(f"Speech saved to: {file_path}")

    # Opening the file
    open_file(file_path)

if __name__ == "__main__":
    print("\033[1;36m--- Text-to-Speech Converter ---\033[0m")
    print("""                                                                                               
 ,-----.                             ,--.                       ,------.                         
'  .-.  '  ,--.,--. ,--,--.,--,--, ,-'  '-. ,---. ,--,--,--.    |  .-.  \  ,---.,--.  ,--.,---.  
|  | |  |  |  ||  |' ,-.  ||      \'-.  .-'| .-. ||        |    |  |  \  :| .-. :\  `'  /(  .-'  
'  '-'  '-.'  ''  '\ '-'  ||  ||  |  |  |  ' '-' '|  |  |  |    |  '--'  /\   --. \    / .-'  `) 
 `-----'--' `----'  `--`--'`--''--'  `--'   `---' `--`--`--'    `-------'  `----'  `--'  `----'  
""")
    while True:
        text_input = input("Enter the text you want to convert to speech: ")

        voice_option = int(input("Choose a voice (1, 2, 3, or 4): "))
        text_to_speech(text_input, voice_option)

        more_conversion = input("Do you want to convert more text? (yes/no): ").lower()
        if more_conversion != 'yes':
            print("Thank you for using Text-to-Speech Converter. Have a great day!\nConsider subscribing to Quantom: https://youtube.com/@quantomz 😉")
            break
