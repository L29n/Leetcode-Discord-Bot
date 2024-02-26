from leetquestion import get_question, rescrape

def get_response(user_input : str) -> tuple[str, bool]:
    message = user_input.lower() # to digest the user input easier

    # Bot handles three cases "easy", "medium", or "hard" and gives a random leetcode question corresponding to that tag.
    match message:
        case "help":
            return ("Command List:\n*easy*, *medium*, *hard*  ->  generate a Leetcode question of that difficulty \n*update*  ->  update the dataset of questions (rescrapes the web)\n Format example: ```!leetcode easy```", False)
        case "easy":
            return (get_question("Easy"), True)
        case "medium":
            return (get_question("Medium"), True)
        case "hard":
            return (get_question("Hard"), True)
        case "update":
            return ("Success!", False) if rescrape() else ("Unsuccessful :(", False)
        case "":
            return ("Please choose from *easy*, *medium*, *hard* to generate Leetcode questions. Alternatively, you can check out *!leetcode help*. Format example: ```!leetcode easy```", False)
        case other:
            return ("Invalid Request. Please choose from *easy*, *medium*, *hard*. Alternatively, you can check out *!leetcode help*. Format example: ```!leetcode easy```", False)