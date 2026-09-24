import webbrowser
webbrowser.open("https://www.amazon.com")  #it will open any brower given in open()
webbrowser.open_new("https://www.flipkart.com")  #it will open browser in new tab
webbrowser.open_new_tab("https://www.flipkart.com")   #it will open URL in new browser tab

webbrowser.open("https://www.amazon.com",new=2)  #intention hai URL ko new tab me open karna.

webbrowser.open("https://www.flipkart.com", new=2, autoraise=True)   #autoraise=True ka purpose browser window ko foreground me laane ka request karna hai.
webbrowser.get()

#webbrowser.register()


