# Quiz Definer
It's an app where you can create quizes and determine the result of the quiz by numbers.
f. e. you can create quizes like, "Are you good enough at math?", or even "Who are you from Marvel's Avengers?".


## Test Creation Structure
<ul class="project-tree" style="list-style-type:none;margin: 0">
    <li>
        <span>Question1</span>
        <ul style="list-style-type:none;margin: 0">
            <li><span><b>(str)answer1</b></span> - <span><b>(int)value1</b></span></li>   
            <li>....</li>
            <li><span><b>(str)answer4</b></span> - <span><b>(int)value4</b></span></li>   
        </ul>
    </li>
    <li>
        <span>Question(n)</span>
        <ul style="list-style-type:none;margin: 0">
            <li><span><b>(str)answer1</b></span> - <span><b>(int)value1</b></span></li>   
            <li>....</li>
            <li><span><b>(str)answer4</b></span> - <span><b>(int)value4</b></span></li>    
        </ul>
    </li>
    <li>
        <span>Result1</span>
        <ul style="list-style-type:none;margin: 0">
            <li><span><b>(int)rangeLeft</b></span> - <span><b>(int)rangeRight</b></span></li> 
            <li><span><b>resultMessage</b></span></li>
        </ul>
    </li>
    <li>
        <span>Result(n)</span>
        <ul style="list-style-type:none;margin: 0">
            <li><span><b>(int)rangeLeft</b></span> - <span><b>(int)rangeRight</b></span></li> 
            <li><span><b>resultMessage</b></span></li>
        </ul>
    </li>
</ul>

As you are taking this test, you will answer questions, and each question will give you its points. In the result you will get your response if:
rangeLeft < your score <= rangeRight.
also the data about passing quiz is being collected and is displayed at analytics page, only author of the quiz can access it.

## Stack
Python + Django, Html + Css, Js, MongoDB(for stats), Sqlite3 => PostgreSQL(for auth and other data, will be changed to Postgre).

## Usage
Download or clone this repository. Run `pip install -r requirements.txt` through the terminal in the current folder (installed Python version required). then type `cd quiz_definer`.

To open the web app type `python manage.py runserver`

To stop developer mode in the terminal press Ctrl+C.

## Screenshots
![Screenshot 2024-02-22 173130](https://github.com/VladGaranovskyi/QuizDefiner/assets/114082118/fc8676ee-14e5-42f7-b698-852fb533f9b3)
![Screenshot 2024-02-22 173111](https://github.com/VladGaranovskyi/QuizDefiner/assets/114082118/67e4896e-4ddc-40b2-91be-03aeff7bb540)
![Screenshot 2024-02-22 173018](https://github.com/VladGaranovskyi/QuizDefiner/assets/114082118/2346a043-8485-474c-902c-0f2c8c781ac9)


