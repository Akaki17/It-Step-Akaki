

def serialize_student(student):
    try:
        with open('student.json', 'w') as f:
            json.dump(student.to_dict(), f)
        return 'Serialized with json'
    except Exception as e:
        print(f'JSON serialization failed: {e}')
        
    try:
        with open('student.pkl' 'wb') as f:
            pickle.dump(student, f)
        return 'Serialization with pickle'
    except Exception as e:
        print(f'Pickle serialization failed: {e}')
        
    try:
        with open('student.dill', 'wb') as f:
            dill.dump(student, f)
        return 'Serialization with dill.'
    except Exception as e:
        print(f'Dill serialization failed: {e}')
        
    return 'None of the method can serialize the passed object'

print(serialize_student(student1))
print(serialize_student(student2))
print(serialize_student(student3))
print(serialize_student(student4))