from sendEmail import sendEmail
from datetime import datetime

header_image = 'anniversary-header.png'
footer_image = 'anniversary-footer.png'


def sendAnniversaryEmail(first_name, last_name, gender, email, designation, doj):
    full_name = first_name + " " + last_name
    article = 'an' if designation[0] == 'A' or designation[0] == 'E' or designation[
        0] == 'I' or designation[0] == 'O' or designation[0] == 'U' or designation[0] == 'H' else 'a'
    pronoun = 'him' if gender == 1 else 'her'
    possesive_pronoun = 'his' if gender == 1 else 'her'
    no_of_years = datetime.today().date().year - doj.year
    year_string = 'year' if no_of_years == 1 else 'years'

    subject = "Happy Anniversary " + full_name + "!!"
    body = ("<p>Dear All,</p><p>" +
            "<strong>" + full_name + "</strong> celebrates " + possesive_pronoun + " work anniversary today (" + doj.strftime("%d %B") + "). " +
            full_name + " is " + article + " " + designation + " and has been a part of Utegration for " + str(no_of_years) + " " + year_string + ". Please send " + pronoun +
            " a note to wish " + pronoun + " a Happy Work Anniversary!!</p>" +
            "<p>Email: <a href='mailto:" + email + "' target='_top'>" + email + "</a></p><p>" +
            "Utegration hopes you have a wonderful day!!</p>")

    # print(html.format(style, body), subject)
    recievers = ["utegrationindia@utegration.com"]
    recievers = ["manjunatha.kashirudraiah@utegration.com"]
    print("Sending Anniversary Mail to " + full_name + "...")
    sendEmail(recievers, subject, body, header_image, footer_image)
