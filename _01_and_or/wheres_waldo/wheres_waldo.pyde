"""
Make a program where the user has to find Waldo!
"""

# =========== SOUND =================
# Some computers are unable to play sounds. 
# If you cannot play sound on this computer, set canPlaySounds to false.
# If you are not sure, ask your teacher 
can_play_sounds = False

def setup():
    # Find a Where's Waldo picture and drop it onto the sketch.    
    global waldo


    # Use the size() function to set the width and height of your sketch
    size(500,500)
    waldo= loadImage ('waldo.jpg')
    waldo.resize(500,500)
    background(waldo)
    # Resize your waldo picture to the same size as the sketch
  
    # Use the background() function to make the waldo image your
    # sketch background
    
    
def draw():
    background(waldo)
    # If the user presses the mouse...
    # *Hint* use the mousePressed variable
    if mousePressed: 
        if (mouseX < 344 and mouseX > 313 and mouseY<349 and mouseY>252):
    
            text('Waldo Found!!!' ,300,300)
            play_woohoo()
        
        
        # Use this print statement to help you find the location
        # of Waldo to use in the code below
        
    
        # Check if the location of the mouse is anywhere on the image of Waldo.
        # If it is, print “Waldo found!”  Use the text() command to write it
        # on the sketch.
          
            # Use the play_woohoo() method below.
        
        # However, if the mouse is not on Waldo, print "Not here!" 
        # Use the text() command to write it on the sketch.
          
            # Use the play_doh() method below.
            
        pass
# =================== This code is needed to play sounds. ===================

#add_library('sound')

woohoo = None
doh = None

def play_woohoo():
    global woohoo
    if can_play_sounds:
        if woohoo is None:
            woohoo = SoundFile(this, "homer-woohoo.wav")
        woohoo.stop()
        woohoo.play()

def play_doh():
    global doh
    if can_play_sounds:
        if doh is None:
            doh = SoundFile(this, "homer-doh.wav") 
        doh.stop()
        doh.play()
