class Course:
    def __init__(self, name, price, platform, quantity):
        self.name = name
        self.price = price
        self.platform = platform
        self.quantity = quantity

    def display_info(self):
        print(f"Course: {self.name}, Price: ${self.price}, Platform: {self.platform}, Quantity: {self.quantity}")


class OnlineStore:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"Courses available at {self.name}:")
        for course in self.courses:
            course.display_info()

    def sell_course(self, course_name, customer_name):
        for course in self.courses:
            if course.name.lower() == course_name.lower():
                if course.quantity > 0:
                    print(f"{course_name} course sold to {customer_name} for ${course.price}")
                    course.quantity -= 1
                    return
                else:
                    print(f"Sorry, {course_name} course is out of stock.")
                    return
        print(f"Sorry, {course_name} course not found in the store.")


if __name__ == "__main__":
    python_course = Course("Python Programming", 50, "Udemy", 50)
    ml_course = Course("Machine Learning", 100, "Coursera", 30)

    online_store = OnlineStore("COURSE_HUB")

    online_store.add_course(python_course)
    online_store.add_course(ml_course)

    online_store.display_courses()
    print()

    while True:
        choice = input("Do you want to buy a course? (yes/no): ")
        if choice.lower() == 'no':
            break
        elif choice.lower() == 'yes':
            course_name = input("Enter the name of the course you want to buy: ")
            customer_name = input("Enter your name: ")
            online_store.sell_course(course_name, customer_name)

    print("\nUpdated Course Inventory:")
    online_store.display_courses()
