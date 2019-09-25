def colorize(table_rows):
    # Complete the function here:
	html_string = ''
	for html_string in range(1, table_rows, 2):
		html_string.append("<tr class=\"white\"></tr>\n")
		return html_string
	for html_string in range(0, table_rows, 2):
			html_string.append(" <tr class=\"light-grey\"></tr>\n")
			return html_string
# Sample function call
print(colorize(10))