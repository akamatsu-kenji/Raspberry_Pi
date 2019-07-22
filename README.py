# Raspberry_Pi
import wave     #wavファイルを扱うためのライブラリ
import pyaudio
# import webapi

WAVE_OUTPUT_FILENAME = "sample.wav" #音声を保存するファイル名
iDeviceIndex = 0 #録音デバイスのインデックス番号

def MakeWavFile(FileName = "sample.wav", Record_Seconds = 60):

	#生音声取得時の設定
	CHUNK = 1024  #1024個のデータをfsというサンプル周波数で取ってきた。
	FORMAT = pyaudio.paInt16
	CHANNELS = 1 #モノラル
	RATE = 44100 #サンプルレート（録音の音質）

	p = pyaudio.PyAudio()
	print(p)
	stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, input_device_index = iDeviceIndex, frames_per_buffer = CHUNK)

	#レコード開始
	print('Now Recording...')
	all = []
	for i in range(0, int(RATE / CHUNK * Record_Seconds)):
	    data = stream.read(CHUNK) #音声を読み取って、
	    all.append(data) #データを追加

	#レコード終了
	print('Now Recording...')

	stream.close()
	p.terminate()

	#保存
	wavFile = wave.open(FileName, 'wb')
	wavFile.setnchannels(CHANNELS)
	wavFile.setsampwidth(p.get_sample_size(FORMAT))
	wavFile.setframerate(RATE)
	wavFile.writeframes(b"".join(all)) #Python3用
	wavFile.close()

if __name__ == "__main__":
#WAVファイル作成, 引数は（ファイル名, 録音する秒数）
	MakeWavFile("sample.wav", Record_Seconds = 60)
#webapi.changedata(wavFile)
