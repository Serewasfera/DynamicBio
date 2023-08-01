import scratchattach as scratch3
import configparser, time, os, ctypes

config = configparser.ConfigParser()

if os.path.exists('config.ini'):
	config.read('config.ini')
else:
	print('INFO: config.ini not found. Generating config.ini...')

	config.add_section('BIOs')
	config.set('BIOs', 'bio1', 'first bio')
	config.set('BIOs', 'bio2', 'second bio')

	config.add_section('User')
	config.set('User', 'name', 'your_scratch_account_name_here')
	config.set('User', 'password', 'your_scratch_account_pwd_here')

	config.add_section('Options')
	config.set('Options', 'cooldown', '10')
	config.set('Options', 'mode', 'bio')

	with open('config.ini', 'w') as configfile:
	    config.write(configfile)

try:
	username = config.get('User', 'name', raw = True)
	password = config.get('User', 'password', raw = True)
	print(f'INFO: Login as a {username}...')

	session = scratch3.login(username, password)
	user = session.connect_user(username)

except BaseException:
	print('ERROR: Failed to connect to the Scratch server. Check the entered user data.')
	ctypes.windll.user32.MessageBoxW(0, u"Failed to connect to the Scratch server. Check the entered user data.", u"DynamicBio by Serewasfera", 0)

else:
	print('INFO: Login successful!')

	mode = config.get('Options', 'mode', raw = True)
	if mode == 'bio' or mode == 'wiwo':
		print(f'INFO: Selected mode: {mode}')
	else:
		print('ERROR: Invalid mode specified. Mode must be "bio" or "wiwo"')
		ctypes.windll.user32.MessageBoxW(0, u'Invalid mode specified. Mode must be "bio" or "wiwo"', u"DynamicBio by Serewasfera", 0)
		exit()

	bio = [config.get('BIOs', key, raw=True) for key in config.options('BIOs')]

	try:
		cd = int(config.get('Options', 'cooldown'))
	except ValueError:
		print('ERROR: Wrong cooldown added. Enter an integer.')
		ctypes.windll.user32.MessageBoxW(0, u"Wrong cooldown added. Enter an integer.", u"DynamicBio by Serewasfera", 0)
	else:
		while True:
			for x in bio:
				if mode == 'bio':
					user.set_bio(x)
				elif mode == 'wiwo':
					user.set_wiwo(x)
				print('INFO: Switched to ' + str(bio.index(x)))
				time.sleep(cd)