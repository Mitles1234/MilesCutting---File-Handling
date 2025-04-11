# TODO: Open "movies.txt" in write mode
with open("movies.txt", "w") as file:

    # TODO: Ask the user for a favorite movie THREE TIMES efficiently
    for i in range(3):
        movie = input(f'What is your #{i+1} favorite movie? ')
        
        # TODO: Write the movie to the file with a newline
        file.write(movie + '\n')

# TODO: Let the user know movies have been saved to file

print('Movies Saved!')
# TODO: Check the file and ensure it worked!
