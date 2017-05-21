def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    sum = 0
    for trial in range(numTrials):
        trial_result = run_simulation()
        sum += trial_result
    ratio = float(sum/numTrials)
    return ratio

def run_simulation():
    bucket = ['G','G','G','G','R','R','R','R']
    count = 0
    same_color = 0
    for i in range(3):
        selection = random.choice(('G', 'R'))
        if selection == 'G':
            bucket.remove('G')
            count += 1
        else: 
            bucket.remove('R')
    if count == 3:
        same_color = 1
    return same_color
