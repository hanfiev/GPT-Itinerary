from typing import Union
from fastapi import FastAPI
import openai
import os
from mangum import Mangum

openai.api_key = os.environ.get('openai_api_key')

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root():
    return "GPT-3 API"

@app.get("/itinerary")
def generate_itinerary(duration:int, city: Union[str, None] = None):
  prompt = f'Write an itinerary for {duration} day(s) trip at {city}. Include a recreation place and place to eat. response with this format only: time, the place name, latitude longitude (in array). use this structure template: 08:00, Empire state building, [40.7484, -73.9857]'
  
  response = openai.Completion.create(
            model='text-davinci-003', 
            prompt=prompt, 
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
  response_txt = response.choices[0].text
  data = response_txt.split('\n\n')
  days = []
  for index, item in enumerate(data):
      if len(data[index].split('\n')[1:]) > 1:
        activities = data[index].split('\n')[1:]
        day = []
        for activity in activities:
          day_template = {}
          activity = activity.split(',')
          day_template['time'] = activity[0].strip()
          day_template['place'] = activity[1].strip()
          day_template['latitude'] = activity[2].strip()[1:]
          day_template['longitude'] = activity[3].strip()[:-1]
          day.append(day_template)
          
        days.append(day)
  return days


@app.get("/itinerary-time")
def itinerarytime(duration:int, month: str, city: Union[str, None] = None):
  prompt = f'Write an itinerary for {duration} day(s) trip at {city} in {month}. Include a recreation place and place to eat. response with this format only: time, the place name, latitude longitude (in array). use this structure template: 08:00, Empire state building, [40.7484, -73.9857]'
  
  response = openai.Completion.create(
            model='text-davinci-003', 
            prompt=prompt, 
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
  response_txt = response.choices[0].text
  data = response_txt.split('\n\n')
  days = []
  for index, item in enumerate(data):
      if len(data[index].split('\n')[1:]) > 1:
        activities = data[index].split('\n')[1:]
        day = []
        for activity in activities:
          day_template = {}
          activity = activity.split(',')
          day_template['time'] = activity[0].strip()
          day_template['place'] = activity[1].strip()
          day_template['latitude'] = activity[2].strip()[1:]
          day_template['longitude'] = activity[3].strip()[:-1]
          day.append(day_template)
          
        days.append(day)
  return days