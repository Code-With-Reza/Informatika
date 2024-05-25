import base64

# Read configuration from lol.rtx file
def read_config(filename):
    config = {}
    try:
        with open(filename, 'r') as file:
            encoded_data = file.read()
            decoded_data = base64.b64decode(encoded_data).decode('utf-8')
            for line in decoded_data.split('\n'):
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()
    return config  # Return an empty dictionary if file not found

# Main function
def main():
    # Read configuration
    config = read_config('lol.rtx')

    # Accessing variables from config
    temp_dir = config.get('tempDir', 'nones')
    debug_mode = config.get('debug', 'false').lower() == 'true'
    server_url = config.get('server', 'nones')
    
    if temp_dir == "nones" or server_url == "nones":
        print("Error, config deleted!")
    else:
        # Using the variables
        print("Temp directory:", temp_dir)
        print("Debug mode:", debug_mode)
        print("Server URL:", server_url)

if __name__ == "__main__":
    main()
