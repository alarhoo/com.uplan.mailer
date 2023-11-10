from sendEmail import sendEmail
from datetime import datetime

header_image = 'anniversary-header.png'
footer_image = 'anniversary-footer.png'


def sendHolidayEmail(first_name, last_name, gender, email, designation, doj):
    # recievers = ["utegrationindia-hr@utegration.com", "utemployees@utegration.com"]
    full_name = first_name + " " + last_name
    article = 'an' if designation[0] == 'A' or designation[0] == 'E' or designation[
        0] == 'I' or designation[0] == 'O' or designation[0] == 'U' or designation[0] == 'H' else 'a'
    pronoun = 'him' if gender == 1 else 'her'
    possesive_pronoun = 'his' if gender == 1 else 'her'
    no_of_years = datetime.today().date().year - doj.year

    subject = "Happy Birthday " + full_name + "!!"
    body = ("<p>Dear All,</p><p>" +
            "<strong>" + full_name + "</strong> celebrates " + possesive_pronoun + " work anniversary today (" + doj.strftime("%d %B") + "). " +
            full_name + " is " + article + " " + designation + " and has been a part of Utegration for " + str(no_of_years) + " year. Please send " + pronoun +
            " a note to wish " + pronoun + " a Happy Work Anniversary!!</p>" +
            "<p>Email: <a href='mailto:" + email + "' target='_top'>" + email + "</a></p><p>" +
            "Utegration hopes you have a wonderful day!!</p>")

    # print(html.format(style, body), subject)
    recievers = ["utemployees@utegration.com"]
    sendEmail(subject, body, header_image, footer_image)
