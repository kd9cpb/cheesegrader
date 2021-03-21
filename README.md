# cheesegrader
properly re-doing Tom's 7th grade science fair project at age 30


Welcome to Cheesegrader. It averages grades. Nothing more, nothing less.

This code is featured in the story at https://kd9cpb.com/opp, and still has plenty of room for improvement :)

To use Cheesegrader, make sure PyYAML is installed (pip3 install pyyaml), and ensure the following three files are used correctly:

students.yml - This is where your class roster and all grades are stored
weights.yml - This sets the categories and assigns weights to said categories. Make sure total equals 100%.
lettergrades.yml - This determines the grading scale. Default is 90 = A. If you're somewhere that an A = 93, make sure to update this accordingly.

There's plenty of future improvement opportunites to this codebase. Here's a couple ideas:
- Support grades like A-, B+, etc.
- Support GPA calculation
- Support graphical output to show bar charts, bell curves, etc.
- Include option for teacher to set a curve
- Use something like Django to produce nice web-friendly output
- Send grades out via email
- Fancier output of averaged grades
