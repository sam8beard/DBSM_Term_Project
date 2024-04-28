# Converts a list in python to an html table
def list_to_html_table(data):
    # Generate the table header
    table_html = '<table>\n<thead>\n<tr>'
    for header in data[0]:
        table_html += f'<th>{header}</th>'
    table_html += '</tr>\n</thead>\n'

    # Generate the table rows
    table_html += '<tbody>\n'
    for row in data[1:]:
        table_html += '<tr>'
        for value in row:
            table_html += f'<td>{value}</td>'
        table_html += '</tr>\n'
    table_html += '</tbody>\n'

    # Close the table tag
    table_html += '</table>'

    return table_html


# Example usage
my_list = [['Name', 'Age', 'Country'],
           ['John', '25', 'USA'],
           ['Emily', '30', 'Canada'],
           ['David', '27', 'Australia']]

html_table = list_to_html_table(my_list)
print(html_table)