from sendEmail import sendEmail
header_image = 'birthday-header.png'
footer_image = 'birthday-footer.png'


def sendBirthdayEmail(first_name, last_name, dob, gender, email, designation):
    full_name = first_name + " " + last_name
    article = 'an' if designation[0] == 'A' or designation[0] == 'E' or designation[
        0] == 'I' or designation[0] == 'O' or designation[0] == 'U' or designation[0] == 'H' else 'a'
    pronoun = 'him' if gender == 1 else 'her'
    possesive_pronoun = 'his' if gender == 1 else 'her'

    subject = "Happy Birthday " + full_name + "!!"
    body = ("<p>Dear All,</p><p>" +
            "<strong>" + full_name + "</strong> celebrates " + possesive_pronoun + " birthday today (" + dob.strftime("%d %B") + "). " +
            full_name + " is working as " + article + " " + designation + " with Utegration. Please send " + pronoun +
            " a note to wish " + pronoun + " a Happy Birthday!!</p>" +
            "<p>Email: <a href='mailto:" + email + "' target='_top'>" + email + "</a></p><p>" +
            "Utegration hopes you have a wonderful day!!</p>")

    # print(html.format(style, body), subject)
    recievers = ["utegrationindia@utegration.com"]
    recievers = ["manjunatha.kashirudraiah@utegration.com"]
    print("Sending Birthday Mail to " + full_name + "...")
    sendEmail(recievers, subject, body, header_image, footer_image)
