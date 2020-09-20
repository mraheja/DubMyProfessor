import os
import json
import base64
import wave

def create_audio(text,speaker,output):
	f1 = open('query.js','r')
	f2 = open('query_with_data.js','w')

	t = f1.read()
	t = t.replace('[TEXT]',text)
	t = t.replace('[SPEAKER]',speaker)
	f2.write(t)

	f1.close()
	f2.close()

	os.system('node query_with_data.js > query.json')

	f = open('query.json','r')

	x = f.readlines()

	idx_start = x[1].find("'")
	idx_end = x[1].find("'",idx_start+1)
	base64_audio = x[1][idx_start:idx_end]

	decode_string = base64.b64decode(base64_audio)
	wav_file = open(output, "wb")
	wav_file.write(decode_string)
	wav_file.close()

	return base64_audio

	

