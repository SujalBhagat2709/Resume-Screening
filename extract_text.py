import re

def extract_text(file_path):
    
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    text = re.sub(r"\s+", " ", text)
    
    return text.strip()


if __name__ == "__main__":
    
    text = extract_text("resume.txt")
    
    print(text[:200])