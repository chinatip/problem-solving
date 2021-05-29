def breakingRecords(scores):
    highScore = scores[0]
    lowScore = scores[0]
    countHighBreak = 0
    countLowBreak = 0
    
    for i in range(len(scores)):
        currentScore = scores[i]
        if currentScore > highScore:
            countHighBreak +=1 
            highScore = currentScore
        if currentScore < lowScore:
            countLowBreak +=1 
            lowScore = currentScore