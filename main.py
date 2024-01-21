import get_weather
import generate_prompt
import generate_img

cityName = input("Enter your city: ")

weatherInfo = get_weather.getWeather(cityName)

if weatherInfo == -1:
    print("Not a valid city")
else:
    print(weatherInfo)
    
    prompt = generate_prompt.generatePrompt(weatherInfo)

    print(prompt)

    imgUrl = generate_img.generateImg(prompt)

    print(imgUrl)
