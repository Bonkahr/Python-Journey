import webbrowser

webbrowser.open("google.com", new=2)
help(webbrowser)

firefox = webbrowser.get(using="firefox")
firefox.open("google.com")
