# more at https://developers.deepgram.com/blog/2022/06/best-python-audio-manipulation-tools/#clipping-audio-data-with-python
from pydub import AudioSegment

def clip_audio(sound, start, end):
    extracted = sound[start:end]
    return extracted

def clip_and_save_audio(sound, start, end, filename):
    extracted = clip_audio(sound, start, end)
    extracted.export(f"{filename}.wav", format="wav")

