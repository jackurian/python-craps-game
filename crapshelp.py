import pandas as pd
import matplotlib.pyplot as plt

def chart():
    
    '''
    This function creates a chart that shows the probability of getting each possible roll, 
    specifically the number of possible ways to roll that number and the percentage chance 
    of that roll.

    You have to exit out of the chart before you can continue with the game, but you can save
    it to your computer first by clicking the floppy disk icon.
    
    '''

    crapsodds = pd.DataFrame({
        'Roll': [2,3,4,5,6,7,8,9,10,11,12],
        'WaysToRoll': [1,2,3,4,5,6,5,4,3,2,1]
    })
    crapsodds['Probability'] = crapsodds['WaysToRoll'] * 2.78

    plt.bar(crapsodds['Roll'], crapsodds['WaysToRoll'],
            width = 0.7,
            align = 'center',
            color = '#24135F')
    plt.ylabel("Number of Ways to Roll", color = '#24135F')
    plt.xlabel("Roll")
    plt.tick_params(axis = 'y', labelcolor = '#24135F')

    plt.twinx()
    plt.plot(crapsodds['Roll'], crapsodds['Probability'],
            color = '#DF4601',
            marker = 'o')
    plt.ylabel("Probability (%)", color = '#DF4601')
    plt.tick_params(axis = 'y', labelcolor = '#DF4601')

    plt.title("Craps Roll Outcomes")
    plt.tight_layout()
    plt.show()