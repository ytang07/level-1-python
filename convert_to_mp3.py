from pydub import AudioSegment

def convert(filename: str, from_format: str, to_format: str):
    '''Converts audio file from one format to another and exports it
    
    Params:
        filename: name of original file
        from_format: format of og audio file
        to_format: desired format'''
    raw_audio = AudioSegment.from_file(filename+from_format, format=from_format)
    raw_audio.export(filename+to_format, format=to_format)
