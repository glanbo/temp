		��� ������ ����� ��������� ���� "winsound"
		� ��� ������ ���� ����������� ����������
		�� ��� ������ ������ � ������� ".wav"

"https://docs.python.org/2/library/winsound.html"
��������
winsound.Beep(frequency, duration)
	Beep the PC�s speaker. 
	The frequency parameter specifies frequency, in hertz, of the sound, 
	and must be in the range 37 through 32,767. 
	The duration parameter specifies the number of milliseconds the sound should last.
	If the system is not able to beep the speaker, RuntimeError is raised.
winsound.PlaySound(sound, flags)
>>> winsound.PlaySound('notes/fa.wav',winsound.SND_FILENAME )
>>> winsound.PlaySound('storm.wav',winsound.SND_FILENAME|winsound.SND_ASYNC )
winsound.SND_PURGE
	Stop playing all instances of the specified sound.

��� �������������� � WAV ����� ������������ ������ ���������
	"https://audio.online-convert.com/ru/convert-to-wav"
��� "https://convertio.co/ru/mp3-wav/"

