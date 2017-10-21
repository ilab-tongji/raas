import pyaudio
import wave
import audioop
from collections import deque
from voicetotext import ToText
import os
import math

class SST:
    # chunk is the size of bytes once read; rate is the .wav file sampling rate(16000 or 8000); threshold is the silence
    # threshold, which belows it will be seen as quiet; silence_limit is the silence time mic wait; prev_audio is the pre_get
    # voice to avoid losing information
    def __init__(self, chunk=1024, rate=16000, threshold=2600, silence_limit=2, prev_audio=1):
        self.lang_code = 'en-US'
        self.chunk = chunk
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = rate
        self.threshold = threshold
        self.silence_limit = silence_limit
        self.prev_audio = prev_audio
        self.api_key = "R3zEZiZsGDIcijugRElifDW5"
        self.api_secret = "e3aa3fb132288c5bbed272ed34d58e1a"
        self.voiceget = ToText("test_baidu", self.api_key, self.api_secret)

    def listen_for_speech(self, num_phrases=-1):
        #num_phrases is the voice get time (-1 is unlimit);
        # Open stream
        p = pyaudio.PyAudio()

        stream = p.open(format = self.format,
                        channels=self.channels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)

        print "* Listening mic. "
        audio2send = []
        cur_data = ''  # current chunk  of audio data

        rel = self.rate / self.chunk
        slid_win = deque(maxlen=self.silence_limit * rel)
        # slid_win = deque(maxlen=SILENCE_LIMIT * rel)
        # Prepend audio from 1 seconds before noise was detected
        prev_audio = deque(maxlen=self.prev_audio * rel)
        started = False
        n = num_phrases
        response = []

        while (num_phrases == -1 or n > 0):
            cur_data = stream.read(self.chunk)
            slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
            if (sum([x > self.threshold for x in slid_win]) > 0):
                if (not started):
                    print "Starting record of phrase"
                    started = True
                audio2send.append(cur_data)
            elif (started is True):
                print "Finished"
                # The limit was reached, finish capture and deliver.
                filename = save_speech(list(prev_audio) + audio2send, p, self.rate)
                # return
                r = self.voiceget.getText("output.wav")
                if num_phrases == -1:
                    print "Response", r[0]
                else:
                    response.append(r)
                # Remove temp file. Comment line to review.
                os.remove(filename)
                # Reset all
                started = False
                slid_win = deque(maxlen=self.silence_limit * rel)
                prev_audio = deque(maxlen=0.5 * rel)
                audio2send = []
                n -= 1
                print "Listening ..."
            else:
                prev_audio.append(cur_data)
        print "* Done recording"
        stream.close()
        p.terminate()
        return response


def save_speech(data, p, rate):
    filename = 'output'
    # writes data to WAV file
    data = ''.join(data)
    wf = wave.open(filename + '.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(data)
    wf.close()
    return filename + '.wav'


if(__name__ == '__main__'):
    SST().listen_for_speech(5)