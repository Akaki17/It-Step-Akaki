import mimetypes

def get_mim_type(filename):
    filename = filename.strip().lower()
    mime_type, _ = mimetypes.guess_type(filename)
    
    return mime_type or "application/octet-stream"

def main():
    user_input = input("Enter file name (with extension): ")
    mime_type = get_mim_type(user_input)
    
    print(mime_type)
    
if __name__ == "__main__":
    main()