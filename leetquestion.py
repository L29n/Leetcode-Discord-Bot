from leetscrape import GetQuestionsList, GetQuestion, ExtractSolutions
from random import randint
from html2image import Html2Image
import requests

ls = GetQuestionsList()
ls.scrape() # leetscrape's Leetcode question scraper. Provides a dataframe to ls.questions
def get_question(difficulty : str) -> str:
    # leetscrape dataframe difficulty only has Easy, Medium, or Hard, which makes sense
    if difficulty not in ["Easy", "Medium", "Hard"]:
        return "Invalid diffculty. Choose from \"Easy\", \"Medium\", \"Hard\""
    
    questions = ls.questions[ls.questions["difficulty"] == difficulty] # column contains either "Easy", "Medium", or "Hard"
    questions = questions[questions["paidOnly"] == False].reset_index() # filters out the questions that require payment
    num_rows = questions.shape[0] # number of rows to randomly choose from

    # this would be on leetscrape's end, so maybe a different library should be used then
    if num_rows == 0: 
        return "No available questions."
    
    question_title = questions["title"][randint(0, num_rows)] # returns a random question of that difficulty
    get_question_key = '-'.join(question_title.lower().split(' ')) # this reformats the title in order to request the question body from leetscrape
    
    question_body = GetQuestion(titleSlug=get_question_key).scrape().Body
    get_img(question_body)

    response = f"Title: {question_title}\nLink: https://leetcode.com/problems/{get_question_key} \nThe solutions can also be found on the Leetcode website."
    return response


def rescrape() -> bool:
    ls = GetQuestionsList()
    ls.scrape() # leetscrape's Leetcode question scraper. Provides a dataframe to ls.questions  
    return ls.questions.shape[0] != 0


def get_img(html_str : str) -> str:
    hti = Html2Image()
    css = 'body {background: white;}'
    hti.screenshot(html_str=html_str, css_str=css, save_as='img.png')
    return 'img.png'