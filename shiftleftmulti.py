import subprocess
import guesslang

def run_analysis(language):
    if language == 'Java':
        command = 'sl analyze --app guessjava --java'
    elif language == 'JavaScript':
        command = 'sl analyze --app guessjs --js'
    elif language == 'Python':
        command = 'sl analyze --app guesspy --pythonsrc'
    elif language == 'TypeScript':
        command = 'sl analyze --app guessts --js'
    elif language == 'PHP':
        command = 'sl analyze --app guessphp --php'
    elif language == 'C#':
        command = 'sl analyze --app guessc# --C#'
    elif language in ('C', 'C++'):
        command = 'sl analyze --app guessc --c'
    elif language == 'Kotlin':
        command = 'sl analyze --app guesskot --kotlin'
    elif language == 'Scala':
        command = 'sl analyze --app guesssca --scala'
    else:
        print(f"Unsupported language: {language}")
        return

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def analyze_repository(repository_path):
    # Initialize the guesslang model
    model = guesslang.load_model()

    # Detect languages in the repository
    languages = model.predict_path(repository_path)

    # Run analysis for languages with percentages higher than 25%
    for language, percentage in languages.items():
        if percentage > 25:
            print(f"Detected language: {language} - Percentage: {percentage}%")
            run_analysis(language)

# Example usage:
repository_path =
analyze_repository(repository_path)

