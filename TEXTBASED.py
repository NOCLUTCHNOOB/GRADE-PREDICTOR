import pickle
import numpy as np

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

numbers = []
def add_data():
    string = input()
    marks, total = map(float, string.split('/'))
    scaled_marks = (marks / total) * 20
    numbers.append(float(scaled_marks))

def get_user_data():
    print("Give accurate data for best prediction")
    print("All the scores should be in the format (MARKS/TOTAL MARKS)..eg.(8/10)") 
    print("Enter your mini test scores:")
    add_data()
    print("Enter your mid test scores:")
    add_data()
    print("Weekly Study Time (1:<2h, 2:2-5h, 3:5-10h, 4:>10h): ")
    numbers.append(int(input()))
    numbers.append(int(input("Age: ")))
    numbers.append(int(input("Daily Commute (1:<15m, 2:15-30m, 3:30-60m, 4:>1h): ")))
    numbers.append(int(input("Number of past class failures(0: You have never failed a class., 1:You have failed 1 class in the past., 2:You have failed 2 classes in the past., 3:You have failed 3 or more classes in the past.): ")))
    numbers.append(int(input("Amount of freetime:: 1: Very Low, 2: Low., 3: Medium (Normal amount of free time)., 4: High., 5: Very High: ")))
    numbers.append(int(input("Amount of time spent with friends:: 1: Very Low (almost never goes out; they are very isolated or always home)., 2: Low., 3: Medium (Goes out a normal amount, perhaps once or twice a week)., 4: High., 5: Very High (out with friends almost every day).")))
    numbers.append(int(input("Workday Alcohol Consumption:: scale(1-5): 1:Never or rare, 5: Very High: ")))
    numbers.append(int(input("Weekend Alcohol Consumption:: scale(1-5): 1:Never or rare, 5: Very High: ")))
    numbers.append(int(input("How is your health:: 1:Very Poor, 2:Poor, 3:Average, 4:Good, 5:Very Good: ")))
    numbers.append(int(input("Total Absences this semester: ")))

def prediction():
    user_data = np.array(numbers).reshape(1, -1)
    prediction = linear.predict(user_data)
    calc_final_marks(prediction)

def calc_final_marks(predicted_marks):
       marks = int(input("Enter the total marks for the final exam: "))
       predicted_marks = predicted_marks*marks/20
       print(f"Based on the data, the predicted final grade is: {predicted_marks}")

if __name__ == "__main__":
    get_user_data()
    prediction()    