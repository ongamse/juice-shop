require 'linguist'

def analyze_repository_and_save_to_file(output_file_path)
  # Get the current repository path
  repo_path = Dir.pwd

  # Analyze the repository using Linguist
  repo_languages = Linguist::Repository.new(repo_path).languages

  # Write the results to the output file
  File.open(output_file_path, 'w') do |file|
    file.puts("Repository: #{repo_path}")
    file.puts("Detected Languages:")
    
    repo_languages.each do |language, percentage|
      file.puts("#{language}: #{percentage}%")
    end
  end
end

# Example usage
output_file_path = '/languages.txt'

analyze_repository_and_save_to_file(output_file_path)
