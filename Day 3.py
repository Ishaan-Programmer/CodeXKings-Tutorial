# Problem 1
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')

# Problem 2
# shown in the terminal

# Problem 3
import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# Problem 4
import flask 

# Problem 5
import os

def print_directory_contents(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Print the header
    print(f"Contents of directory '{directory}':")
    
    # Iterate through the directory contents
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)

# Example usage:
directory_path = '/'  # Replace with your directory path
print_directory_contents(directory_path)