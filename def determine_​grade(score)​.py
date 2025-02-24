
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def main():
    try:
        # Ask the user for their exam score
        score = float(input("Please enter your exam score (out of 100): "))
        
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            return
        
        grade = determine_grade(score)
        print(f"Your grade is: {grade}")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
