import re
import random
class RuleBot:
  ###Negative Responses
  negative_responses=("no","nope","nah","sorry")
  ###exit responses
  exit_responses=("quit","pause","bye","exit","good bye")
  ###random questions
  random_questions=(
      "who is the leader here\n",
      "what is pollution?\n",
      "how coffee tasts?\n",
      "does earth have a leader?\n",
      "how to save earth?\n"
  )

  def __init__(self):
    self.botdict={'describe_planet_intent':r'.*\s*your planet.*',
                  'answer_why_intent':r'why.*',
                  'about_yourself':r'.*\s*you'
                  }
  
  def greet(self):
    self.name=input("what is your name?\n")
    will_help=input(
        f"Hi {self.name},I am a Rule Bot Will you help me to learn about this place?\n"
    )
    if will_help in self.negative_responses:
      print("Its okay, Have a nice day!")
      return
    self.chat()
  
  def make_exit(self,reply):
    for command in self.exit_responses:
      if reply==command:
        print("take care. good bye")
        return True
  
  def chat(self):
    reply=input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply=input(self.match_reply(reply))
  
  def match_reply(self,reply):
    for key,value in self.botdict.items():
      intent=key
      regex_pattern=value
      found_match=re.match(regex_pattern,reply)
      if found_match and intent=='describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent=='answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent=='about_yourself':
        return self.about_yourself()
    if not found_match:
      return self.no_match_intent()
  
  def describe_planet_intent(self):
    responses=("My planet is Uthopia having many species\n",
               "It is near Asgard, the planet you saw in Thor Rangnarok\n",
               "My planet has red moon and white sun\n",
               "my planet is very different from your planet\n")
    return random.choice(responses)

  def answer_why_intent(self):
    responses=("i came in peace\n",
               "I am here to collect data of this planet\n",
               "i heard coffee tasts good\n",
               "i wanted to see and meet humans\n")
    return random.choice(responses)

  def about_yourself(self):
    responses=("My name is Rule Bot, I want to be your friend\n",
               "I am 1 years old\n",
               "I am designed by Pragathi and Priyanka for their data science project\n",
               "Dr Kavitha is the best Data Science teacher.She gave an assignment to students to design me\n")
    return random.choice(responses)

  def no_match_intent(self):
    responses=("Interesting , please tell me more\n",
               "OHHH, but why?\n",
               "I see. can you share more?\n",
               "okay\n",
               "Why?\n")
    return random.choice(responses)

Bot=RuleBot()
Bot.greet()
