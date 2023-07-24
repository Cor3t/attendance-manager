class User:
    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number
    
    def __str__(self) -> str:
        return self.name

class Group:
    def __init__(self, title) -> None:
        self.title = title
        self.users = []
    
    def add_user(self, user : User):
        self.users.append(user)

    def __str__(self) -> str:
        return self.title
    
class Attendance:
    def __init__(self) -> None:
        self.groups = []

    def add_group(self, group: Group):
        self.groups.append(group)
        print(f"{group} has been added")

    def add_user_to_group(self, group: Group, user: User):
        if len(self.groups) != 0:
            for i in self.groups:
                if i == group:
                    i.add_user(user)
                    return f"{user} has been added to {group}"
            else:
                return 'Could not find group'
        else:
            return 'No group added to attendance'
        
    def display_all_groups(self):
        for group in self.groups:
            print(group)
            


if __name__ == '__main__':
 
    group1 = Group('Python Class')
    group2 = Group('Java Class')

    attendance = Attendance()
    attendance.add_group(group1)
    attendance.add_group(group2)

    user1 = User('John', 123456)
    user2 = User('James', 123456)
    response = attendance.add_user_to_group(group1, user1)
    response2 = attendance.add_user_to_group(group1, user2)
    response2 = attendance.add_user_to_group(group2, user2)
    print(response)
    print(response2)



        