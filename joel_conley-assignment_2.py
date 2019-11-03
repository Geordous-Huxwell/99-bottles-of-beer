

def song():
	
		
	for num_bott in range(100,-1,-1):		#set bottle countdown
		
		str_bott = str(num_bott)		#stringify the bottle counter for string concatenation purposes
		
		lyrics = (str_bott + " bottles of beer on the wall. " + 		#set standard lyrics including bottle subtraction within the string
		str_bott + " bottles of beer. Take one down and pass it around. " +
		str(num_bott-1) + " bottles of beer on the wall.")


		if num_bott > 2:		#check that pluralization still makes sense in the string. If so, print as is.
			print(lyrics)

		elif num_bott == 2:		#when 2 bottles are left, account for singularization in last section of lyric only
			new_lyric = lyrics.replace((str(num_bott-1) + " bottles"), (str(num_bott-1) + " bottle")) 	
			print(new_lyric)
		
		elif num_bott == 1:		#when one bottle is left, alter string to singular bottle for first 2 occurences
			new_lyric = lyrics.replace("bottles", "bottle", 2)
			new_lyric = new_lyric.replace((str(num_bott-1)), "No more")
			print(new_lyric)
		
		elif num_bott == 0:		#when no bottles are left, make multiple changes to the string to create the final lyric
			new_lyric = lyrics.replace(str_bott, "No more")
			new_lyric = new_lyric.replace("Take one down and pass it around.", "Go to the store and buy some more.")
			new_lyric = new_lyric.replace((str(num_bott-1)), "99")
			print(new_lyric)
	

song()