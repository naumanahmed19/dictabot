from pydub import AudioSegment
from core.config import openai


def split_audio_to_chunks_by_size(audio_file_path, max_chunk_size_mb=24):
    """
    Split a large audio file into smaller chunks based on size.

    :param audio_file_path: Path to the large audio file
    :param max_chunk_size_mb: Maximum size of each chunk in megabytes (default is 24MB)
    :return: List of audio chunks (each chunk is an instance of AudioSegment)
    """
    audio = AudioSegment.from_file(audio_file_path)
    max_chunk_size_bytes = max_chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    avg_bitrate = audio.frame_rate * audio.frame_width * 8  # Calculate average bitrate in bits per second
    chunk_length_ms = (max_chunk_size_bytes * 8) / avg_bitrate * 1000  # Calculate chunk length in milliseconds
    
    chunks = []
    for i in range(0, len(audio), int(chunk_length_ms)):
        chunk = audio[i:i + int(chunk_length_ms)]
        chunks.append(chunk)
    
    return chunks

def transcribe_audio_chunks(audio_chunks):
    """
    Transcribe a list of audio chunks using OpenAI's audio transcription API.

    :param audio_chunks: List of audio chunks (each chunk is an instance of AudioSegment)
    :return: The combined transcript of all audio chunks
    """
    transcript = ""
    
    for chunk in audio_chunks:
        # Export the chunk to a temporary file
        chunk.export("temp_chunk.wav", format="wav")
        
        # Use OpenAI's API to transcribe the audio chunk
        with open("temp_chunk.wav", "rb") as audio_file:
            response = openai.audio.transcriptions.create(
                file=audio_file,
                model="whisper-1",
                response_format="verbose_json",
                timestamp_granularities=["word"]
            )
            transcript += response['text'] + " "
    
    return transcript.strip()

# Example usage
audio_file_path = "path_to_large_audio_file.wav"
chunks = split_audio_to_chunks_by_size(audio_file_path)
transcript = transcribe_audio_chunks(chunks)
print(transcript)