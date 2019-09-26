def colorize(table_rows):
    # Complete the function here:
	html_string = ''
	str1 = '<tr class=\"light-grey\"></tr>'
	str2 = '<tr class=\"white\"></tr>'
	for i in range(table_rows):
		if i%2 == 0:
			html_string = html_string + str1
			print(html_string)
			html_string = ''
		else:
			html_string = html_string + str2
			print(html_string)
			html_string = ''
# Sample function call
colorize(10)