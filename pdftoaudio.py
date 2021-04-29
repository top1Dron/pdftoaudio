from gtts import gTTS, tts   
import pdftotext
import sys, os, time


def open_pdf(pdf_folder, pdf_file, audio_file_path):
    pdf_file = os.path.join(pdf_folder, pdf_file)
    with open(pdf_file, 'rb') as file:
        pdf = pdftotext.PDF(file)
    text = '\n\n'.join(pdf)
    for i in range(20):
        for removed_elem in '_.(:':
            removed_line = removed_elem * 5
            text = text.replace(removed_line, '')
    return text
    


def write_mp3(text, audio_file):
    final_file = gTTS(text=text, lang='ru')
    final_file.save(audio_file)
    
    
if __name__ == '__main__':
    current_directory = os.path.abspath(os.getcwd())
    audio_path = os.path.join(current_directory, 'audios')
    if not os.path.exists(audio_path):
        os.system('mkdir audios')

    for filename in os.listdir(sys.argv[1]):
        if filename.endswith('.pdf'):
            audio_file = filename.replace('.pdf', '.mp3')
            pdf_text = open_pdf(sys.argv[1], filename, audio_path)
            try:
                write_mp3(pdf_text, os.path.join(audio_path, audio_file))
                time.sleep(120)
            except tts.gTTSError:
                print('429 Error. Too many requests.')
                break
