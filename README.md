![icone](https://github.com/M2007Taha/digital_transformation_in_mathematics/assets/109727381/237fe466-afde-46fd-88da-90c0a8060d58)

# πthon: A Mathematical Calculator for Pi Day and Beyond

#### Description:

πthon (pronounced "pie-thon") is a user-friendly Python application designed to perform various mathematical calculations, making it a valuable tool for students, educators, and anyone interested in exploring mathematical concepts. It's particularly well-suited for Pi Day celebrations, providing a fun and interactive way to engage with the fascinating world of pi.

#### Functionality

πthon offers a range of mathematical functions, including:

Factorials: Calculate the factorial of a number.
Fibonacci Sequence: Generate the Fibonacci sequence up to a specified number of terms.
Trigonometry: Compute sine, cosine, tangent, and cotangent of an angle in degrees or radians.
Exponentiation: Raise a base to a given exponent.
Absolute Value: Determine the absolute value of a number.
Greatest Common Divisor (GCD) and Least Common Multiple (LCM): Find the GCD and LCM of two numbers.
The application features a clear and intuitive graphical user interface (GUI) that simplifies user interaction with these functions.

#### Usage

Interface Overview: The application window consists of several tabs, each dedicated to a specific mathematical operation.
Input Fields: Enter the required values (e.g., numbers, angles) in the designated input fields within each tab.
Buttons: Click the corresponding buttons (e.g., "Calculate") to trigger the calculations.
Output Fields: The results of the calculations will be displayed in the corresponding output fields within each tab.
Prerequisites
Bash Shell: Ensure you have a working installation of the bash shell on your system.

Pyinstaller: Install the pyinstaller tool using your system's package manager. For example, on Ubuntu or macOS, use:

Bash
pip install pyinstaller
Use code with caution.
content_copy
Conversion Steps
Create the Bash Script:

Create a new file with a .sh extension (e.g., pithon_converter.sh).

Open the file in a text editor.

Copy and Paste the Script:

Copy the following bash script into the text editor:
Bash
#!/bin/bash

pyinstaller --icon=icon.ico -F --noconsole pithon.py
Use code with caution.
content_copy
Replace icon.ico with the actual path to your icon file (if you want to include an icon).
Replace pithon.py with the filename of your Python script.
Save the Script:

Save the changes made to the bash script.
Making the Script Executable
Change Permissions:

Open a terminal window and navigate to the directory containing the bash script.
Use the following command to grant execute permission to the script:
Bash
chmod +x pithon_converter.sh
Use code with caution.
content_copy
Running the Script
Execute the Script:

To run the converted bash script, simply type the following command in the terminal:
Bash
./pithon_converter.sh
Use code with caution.
content_copy
This will execute the pyinstaller command and generate the executable file for your Python script.

#### Pi Day Fun

πthon is ideal for Pi Day celebrations! You can use it to:

Calculate pi to a specific number of decimal places.
Explore the Fibonacci sequence and its relationship with the golden ratio.
Investigate trigonometric functions and their applications.
Experiment with various mathematical concepts in a visually appealing and interactive way.
#### Contributing

We encourage contributions to improve πthon. Feel free to fork the repository, make changes, and submit pull requests. Please ensure your contributions adhere to good coding practices and follow the project's style guidelines.

#### License

πthon is distributed under the MIT License. This allows for free use, modification, and distribution of the code with proper attribution.

#### Further Development

This project can be further extended by:

Adding support for additional mathematical functions.
Integrating with external libraries for more advanced calculations.
Enhancing the user interface for improved usability and accessibility.
We look forward to your feedback and contributions to make πthon even more valuable!
