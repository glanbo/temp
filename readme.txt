		ƒл€ звуков ƒеник подсказал библ "winsound"
		у нее походу есть асинхронное исполнение
		но она играет только с файлами ".wav"

"https://docs.python.org/2/library/winsound.html"
работает
winsound.Beep(frequency, duration)
	Beep the PCТs speaker. 
	The frequency parameter specifies frequency, in hertz, of the sound, 
	and must be in the range 37 through 32,767. 
	The duration parameter specifies the number of milliseconds the sound should last.
	If the system is not able to beep the speaker, RuntimeError is raised.
winsound.PlaySound(sound, flags)
>>> winsound.PlaySound('notes/fa.wav',winsound.SND_FILENAME )
>>> winsound.PlaySound('storm.wav',winsound.SND_FILENAME|winsound.SND_ASYNC )
winsound.SND_PURGE
	Stop playing all instances of the specified sound.

дл€ преобразовани€ в WAV можно использовать онлайн конвертер
	"https://audio.online-convert.com/ru/convert-to-wav"
или "https://convertio.co/ru/mp3-wav/"

9999999999
