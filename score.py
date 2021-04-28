import config


score = 0
highscore = 0


def show_score():
    textSize(24)
    fill(255,255,255)
    text("Score: " + str(score), 0, 20)
    
    
def show_highscore():
    textSize(24)  
    fill(255, 191, 0)  
    text("Highscore: " + str(highscore), 0, 50)
    
    
def update_highscore():
    if score > highscore:
        with open(config.HIGHSCORE_FILE_PATH, "w") as file:
            file.write(str(score))
