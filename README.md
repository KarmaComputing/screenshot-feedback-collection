# Collect User Feedback & take screenshot automatically

When users submit feedback about a web application, it's useful
to see a screenshot of the page they're providing feedback about.


This code will take a picture of the *dom* (like a screenshot) and
send it, along with text feedback to a location of your choice.

- Useful for getting actionable feedback from users who wish to send it

# How does it work

- Uses [html2canvas](https://html2canvas.hertzen.com/) to generate image of webpage
- User clicks 'feedback'
- Feedback & screenshot is sent whem submitted

**Note:** Ideally the [screen capture api](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Capture_API/Using_Screen_Capture) would be used, and will be added. Apple have still not implemented this api on iOS. Non iOS users can can real screenshots (thanks to `getDisplayMedia`). TODO - use `getDisplayMedia` if not an iOS user to get genuine screenshots.


### Send feedback
![Screenshot from 2021-07-06 23-05-38](https://user-images.githubusercontent.com/1718624/124672502-06d1fc00-deaf-11eb-806a-a1eeca9981ea.png)

### Capture feedback
![Screenshot from 2021-07-06 23-07-37](https://user-images.githubusercontent.com/1718624/124672526-13eeeb00-deaf-11eb-905f-e613c51f1217.png)


# Live Demo

https://replit.com/@chrisjsimpson/VelvetyStarchyDirectory#templates/index.html

# Endpoint to receive feedback

## Running Locally Setup
```
git clone https://github.com/KarmaComputing/screenshot-feedback-collection.git
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

1. Open index.html in your web browser

2. Run the endpoint

```
export FLASK_APP=app
export FLASK_DEBUG=1
flask run
```

3. Submit some feedback
