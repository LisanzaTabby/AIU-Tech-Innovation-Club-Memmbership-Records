#Creating a club members list to store all the related members information
# combined with Dictionaries to store data with identifiers in managing the Member profiles
club_members = [
    {
        "Student_ID": "MID001",
        "Full Name": "Tabitha Tsisika Lisanza",
        "Gender": "Female",
        "Course": "BSc in Information Technology",
        "Year_Joined": "2025",
        "Area_of_Intereset": "Data Science",
    },
    {
        "Student_ID": "MID002",
        "Full Name": "Edith Nambia",
        "Gender": "Female",
        "Course": "MSc in Information Technology",
        "Year_Joined": "2023",
        "Area_of_Intereset": "Artificial Intelligence",
    },
    {
        "Student_ID": "MID003",
        "Full Name": "George Roberts",
        "Gender": "Male",
        "Course": "Diploma in AI",
        "Year_Joined": "2024",
        "Area_of_Intereset": "Artificial Intelligence",
    },
    {
        "Student_ID": "MID004",
        "Full Name": "Aaron James",
        "Gender": "Male",
        "Course": "Diploma in AI & Cybersecurity",
        "Year_Joined": "2022",
        "Area_of_Intereset": "Cybersecurity",
    },
    {
        "Student_ID": "MID005",
        "Full Name": "Anne Marie",
        "Gender": "Female",
        "Course": "MSc in Information Security",
        "Year_Joined": "2022",
        "Area_of_Intereset": "Cybersecurity",
    },
    {
        "Student_ID": "MID006",
        "Full Name": "John Doe",
        "Gender": "Male",
        "Course": "BSc in Data Science",
        "Year_Joined": "2026",
        "Area_of_Intereset": "Data Science",
    }    
]

# print (club_members[0])

# Task 2. Record Management Functions
# a) Display records function

def display_records():
    print("Club Members Records:")
    if not club_members:
        print("No records found.")
        return
    for member in club_members:
        print("-" * 30)
        print(f"Student ID: {member['Student_ID']}")
        print(f"Full Name: {member['Full Name']}")
        print(f"Gender: {member['Gender']}")
        print(f"Course: {member['Course']}")
        print(f"Year Joined: {member['Year_Joined']}")
        print(f"Area of Interest: {member['Area_of_Intereset']}")
        print("-" * 30)


# b) Add record function
def add_member(student_id, full_name, gender, course, year_joined, area_of_interest):
    
    new_member = {
        "Student_ID": student_id,
        "Full Name": full_name,
        "Gender": gender,
        "Course": course,
        "Year_Joined": year_joined,
        "Area_of_Intereset": area_of_interest,
    }
    
    # Check if the member already exists based on Student ID before adding to the list
    for member in club_members:
        if member["Student_ID"] == student_id:
            print(f"Member with Student ID {student_id} already exists.")
            return
    # adding the new member to the club_members list

    club_members.append(new_member)
    print("-" * 30)
    print(f"Member {full_name} added successfully.")
    print("-" * 30)

    # To display updated records after adding a new member
    display_records()


# c) Club members count function

def count_members():
    count = len(club_members)
    print(f"Total number of club members: {count}")

add_member("MID008", "Annie Johnson", "Female", "BSc in AI", "2025", "NLP") # new member added to the list
add_member("MID004", "Annie Johnson", "Female", "BSc in AI", "2025", "NLP") # existing member_ID added to the list

count_members()