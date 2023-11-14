import subprocess

def process_language_results(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        # Split the line into parts (percentage, size, language)
        parts = line.strip().split(':')

        if len(parts) == 3:
            percentage = float(parts[0].strip())
            size = parts[1].strip()
            language = parts[2].strip()

            # Check conditions (percentage greater than 25 and language is Java)
            if percentage > 25 and language.lower() == 'Java':
                print(f"Running command for Java ({percentage}%): {size}")
                # Replace the following line with your actual shell command
                result = subprocess.run(['sl analyze', '--app guessjava', '--java'])
            elif percentage > 25 and language.lower() == 'JavaScript':
                print(f"Running command for Javascript ({percentage}%): {size}")
                # Replace the following line with your actual shell command
                result = subprocess.run(['sl analyze', '--app guessjs', '--js'])
            elif percentage > 25 and language.lower() == 'TypeScript':
                print(f"Running command for TypeScript ({percentage}%): {size}")
                # Replace the following line with your actual shell command
                result = subprocess.run(['sl analyze', '--app guessts', '--js'])                
# Example usage
file_path = 'languages.txt'
process_language_results(file_path)
