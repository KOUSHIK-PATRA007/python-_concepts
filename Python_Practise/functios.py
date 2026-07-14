def wish(name,age,*marks,**kwargs):
    return f"Hi, {name}! You are {age} years old,you have score {sum(marks)} and status is {kwargs["status"]}"

print(wish("KOUSHIK",25,50,60,70,80, status='pass'))




def create_person_description(**kwargs):
    """Create a description from person attributes."""
    description = []
    for key, value in kwargs.items():
        description.append(f"{key}: {value}")
    return ", ".join(description)
print(create_person_description(name="Alice", age=30,
 job="Engineer"))
print(create_person_description(name="Bob", city="New York",
 hobby="Photography"))
