import re

def sanitize_filename(filename):
    # Remove invalid characters for Windows file names
    return re.sub(r'[<>:"/\\|?*]', '', filename)

if __name__ == "__main__":
    # Example usage
    original_filename = "SITTING DOWN WITH MISS INTERNATIONAL (ft. Shibuya Kaho) | Trash Taste #229-J125PKVDKpQ.mp4"
    sanitized_filename = sanitize_filename(original_filename)
    print(sanitized_filename)