<b>Description</b>\
Ergo Cat's job is to interrupt your desktop screen time so that you take a break from staring at your screen for too long.

Ergo Cat is a customizable countdown timer that opens a random cat gif in your browser window (from giphy.com) at the end of a designated time (say, 20 minutes).

<b>Authors</b>
Ying Ying Liu, Harry Sanabria

<b>How to use (Mac OS): written for the non-engineer</b> \
(Sorry, I don't know how to do this on Windows. If you do, feel free to contribute to this file!) 
1. Download the file <code>ergo-cat-v2.py</code>
2. Drag the file to your Desktop \
    (if you would like to save this file somewhere else on your computer, read this on how to navigate to specific folders using Terminal: https://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html)
3. Open the Terminal application
4. In the command line, type <code>cd Desktop</code>
5. Press <code>Enter</code>
6. Type <code>python ergo-cat-v2.py</code>
7. Press <code>Enter</code>
8. You should see a timer countdown begin
9. That's it! Go about doing what you normally do on your computer. When the time is up, you should see a random cat gif take over your screen. Then you know it's time to take a break!
10. You can rerun the program by repeat steps 6 & 7. Or, you can use a shortcut by pressing the ↑ arrow on your keyboard: this will show you the last command you ran.  

<b>Customize the length of your timer</b>
1. Open <code>ergo-cat-v2.py</code> using a text editor of your choice (TextEdit comes pre-installed on Macs, I like TextMate)
2. On line 12, change the number in the variable <code>seconds = int(1800)</code> to the any number of seconds you like (20 minutes = 1200 seconds, 30 minutes = 1800 seconds, etc)
3. Save file
4. Run the program from Terminal

<b>Customize your gifs</b>
1. Open <code>ergo-cat-v2.py</code> using a text editor of your choice (TextEdit comes pre-installed on Macs, I like TextMate)
2. On line 26, locate <code>randomCatFetchURL = "http://api.giphy.com/v1/gifs/random?api_key=GUCeL1CQLcZdYsiIkRkfwOMvBL9lJoza&tag=cat"</code>
3. Change the string <code>cat</code> at the end of the long jumbly link to anything you like (<code>dog</code> for dog gifs, <code>birb</code> for birbs, etc)
4. Save file
5. Run program from Terminal
