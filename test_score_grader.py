# This code implements a US grading system for students' grades.

def get_score():
    '''This function get test scores from a user.'''
    while True:
        user_input = input('Enter your test score: ')
        try:
            float(user_input)
            break
        except ValueError as v:
            print('Invalid Entry! Enter values from 0 to 100.')

    return round(float(user_input))


def grade_score():
    '''This function grades a user's score.'''
    score = get_score()
    if score >= 60:
        print('Your Passing grade is: ')
        if score >= 97:
            print('A+ with a GPA of 4.33')
        elif score >= 93 and score <= 96:
            print('A with a GPA of 4.00')
        elif score >= 90 and score <= 92:
            print('A- with a GPA of 3.67')
        elif score >= 87 and score <= 89:
            print('B+ with a GPA of 3.33')
        elif score >= 83 and score <= 86:
            print('B with a GPA of 3.00')
        elif score >= 80 and score <= 82:
            print('B- with a GPA of 2.67')
        elif score >= 77 and score <= 79:
            print('C+ with a GPA of 2.33')
        elif score >= 73 and score <= 76:
            print('C with a GPA of 2.00')
        elif score >= 70 and score <= 72:
            print('C- with a GPA of 1.67')
        elif score >= 67 and score <= 69:
            print('D+ with a GPA of 1.33')
        elif score >= 63 and score <= 66:
            print('D with a GPA of 1.00')
        elif score >= 60 and score <= 62:
            print('C- with a GPA of 0.67')
    else:
        if score <= 59:
            print('Your grade is F. Sorry you did not pass the exam')


if __name__ == '__main__':
    grade_score()
    while True:
        print('Enter "y" to enter another score or Enter "n" to quit.')
        action = input('>> ')
        if action == 'y' or action == 'Y':
            grade_score()
        else:
            break
    print('Thank you for using our Grading System.')
