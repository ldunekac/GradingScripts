# Grading Script Setup Notes

## Grading Policies
1. -50% off total points for 00:00:01 - 23:59:59 late.  (0 points after)
2. Failure to put submissions into single zip archive (-20% available points)
3. Failure to include all supporting files in archive (-20% available points)

***

## Using scripts

### Download assignments from BlackBoard
1. Goto assignment download
	- BlackBoard
	- Grade Center
	- Full Grade Center
	- Assignment File Download 
		\<Column Head for Assignment> (pull-down menu)

2. Select assignments to download
	- Show All (Bottom of **Select Users** section)
	- **1. Select Users:** \<Select All> (Checkbox in header)
	  **2. Select Files:** = Last attempt file
	  **3. Submit:** = "Submit"

3. Download assignments
	- Click *Download assignments now* link

4. Place into course directory

### Rubric File
**No Commas**
**No Quotes**

    CSCI 445 - Web Programming
    Unit 01 - Cyndi Rader
    
    Part 1
    [16 points] About Me Website
    [1/1] Correct html structure 
    
    Part 2
    [45 points] Turtle Coders Style Sheet
    [1/1] background color (#f4ffe4) for the body
    [1/1] color (#333333) for text
    
    Header:
    [1/1] background color (#d5edb3)
    [3/3] logo on the right side
    
    ================
    [0/0] Late // Points taken off for being late
    ===============
    Total:
    
    ----- Comments -----



### Extracting Files

Yah...  **Wrote own file extractor.**
    `uz.sh <unit folder> <unit rubric>`
    - unzips student submissions
    - copies rubric
    - adds student's id at top of rubric



### Grading Process
1. Create grading script, if warranted
    - place into Unit_xx folder
    
2. Example: grading Unit 01
`$ cd .../CSCI445/`
`$ unzip Unit_xx.zip`
`$ ./uz.sh Unit_xx Unit_xx_Rubric.txt`
`$ cd Unit_xx`
`$ cd $(next)`
`$ vi grade.txt`
*In a new terminal*
`$ cd .../CSCI445/Unit_xx`
`$ cd $(next)`
`$ cd <projectdir>`
`$ open <part1.html>`
    `<cmd> + <opt> + i` *in Safari (opens web inspector)*
`$ ../part1.sh <part1.html>`
`$ open <part2.html>`
*Compile grades*
`$ eg`
`$ cd ..`
`$ cd $(next)`

### Upload grades to BlackBoard
1. Go to "Full Grading Center" in BlackBoard

2. Select "Work Offline" and "Download" to get base-csv file
    - 1 Data: 
        - choose: *selected column*
        - select unit: *unit_02*
        - check: *Include Comments for this column*
    - 2 Options:
        - choose: *Delimiter Type - comma*
        - choose: *Include Hidden Information - yes*
    - 3 Save Location:
        - default: *Save Location - my computer*
    - 4 Submit:
    
3. After Downloading 
    - Rename to Unit_xx.csv before proceeding
    - Move file to the corresponding unit root directory

4. Run (from unit root, e.g. `~/CSCI_445/Unit_01/`)
`$ generateSubmissionFile.py Unit_xx.csv`  
    - Replace "xx" with unit number.
    - This will generate `upload.csv`

    - **note:** If you get errors here, check to make sure you chose the proper options in step #2.

5. Return to **BlackBoard**
    - Choose: *Full Grade Center*
    - Choose: *Work Offline*
    - Choose: *Upload*
    
        - Select the `upload.csv` you just generated
        - Specify: *comma delimited*
    - When (if) you get a success message...
    
6. Choose `<submit>` to record grades in grade center.

**notes:**

**Comments** from the comments block **did not upload**
    - this is a bug with blackboard

**Enter Comments Manually** <-- Do this after uploading grades
    - *Full Grade Center*
    - *Dropdown* next to student in assignment column
        - choose: *View Grade Details*
    - Choose: *Edit Grade*
    - Paste: Comment from upload.csv into *Feedback to User*
    - Choose: *\>*  (Next user) which is next to user name near top of page

Modified generateSubmissionFile.py (gsf) to copy rubric elements 
    to comments section
    - This will mess up `upload.txt` if there are commas or quotes (csv formatting chars)
    - qed **no commas** and **no quotes**

***

## File locations

**Scripts in**
~/Dev/CSCI445/GradingScripts/src/

**Course files in**
~/Documents/MyStuff/Education/CSM/Funding/Grading_445/

## Install steps (mac terminal)
1. Installed python from brew
	`$  ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`
	`$ brew install python`

2. Pulled source from git and added alias "gradeScripts"
	`$ git clone https://github.com/ldunekac/GradingScripts.git`
	`$ git remote add gradeScripts https://github.com/ldunekac/GradingScripts.git`

3. Backup bashrc
	`$ cp ~/.bashrc ~/.bashrc.bak`

4. Created aliases for scripts (add to ~/.bashrc)
    `alias next='python /Users/Craig/Dev/CSCI445/GradingScripts/src/nextToGrade.py'`
    `alias format='python /Users/Craig/Dev/CSCI445/GradingScripts/src/format.py'`
    `alias eg='python /Users/Craig/Dev/CSCI445/GradingScripts/src/evaluateGrade.py'`
    `alias gsf='python /Users/Craig/Dev/CSCI445/GradingScripts/src/generateSubmissionFile.py'`

5. Refresh your environment
	`$ source ~/.bashrc`

***

## Grade Notes
### Unit 1
**joh** 
- only submitted part 1 on time
- turned in part 2 before second deadline

