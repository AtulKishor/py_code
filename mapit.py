import sys,webbrowser
print('arguments:',sys.argv[1:])


'''if len(sys.argv)>1:
    address = ','.join(sys.argv[1:])
    webbrowser.open("https://www.google.com/maps/place/"+address)
    '''



if len(sys.argv) > 1:
 # Get address from command line.
 address = ' '.join(sys.argv[1:])
else:
 # Get address from clipboard.
 address = '870 Valencia St, San Francisco, CA'
webbrowser.open('https://www.google.com/maps/place/' + address)
