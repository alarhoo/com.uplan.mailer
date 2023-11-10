# Generic Email Module to send emails for birthdays, anniverseries, and holidays
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid
import os
import traceback
import logging


def sendEmail(recievers, subject, body, header_image, footer_image):
    # Setup credentials and SMTP
    email_address = "noreplyindia@utegration.com"
    email_password = "UtegrationIndia@201801"
    smtp_host = "smtp.office365.com"
    smtp_port = 587

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = recievers

    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    header_image_id = make_msgid()
    footer_image_id = make_msgid()

    style = """.body-text {
                text-align: left;
                max-width: 440px;
                color: #000000 !important;
                font-size: 10pt !important;
                line-height: 1.5 !important;
                font-family: 'Rochester', cursive, 'Satisfy', 'Parisienne', 'Comic Sans MS', 'Lato', Tahoma, Verdana, 'Roboto', sans-serif !important;
                padding: 0px !important;
            }"""
    msg.set_content(
        """\
    """
    )
    msg.add_alternative(
        """\
        <!DOCTYPE html>
        <html>
        <head>
            <link href="https://fonts.googleapis.com/css?family=Parisienne|Rochester|Satisfy|Oleo+Script|Roboto&display=swap"
                rel="stylesheet">
            <style>
                {0}
            </style>
        </head>
        <body style="text-align:center;">
            <div style="text-align:center; max-width: 440px !important; margin:0 auto;">
                <table cellspacing="0" cellpadding="0" style="width: 440px; text-align:center;">
                    <tbody>
                        <tr>
                            <td style="background:#E6E6E6;padding:1px;width:100%">
                                <table style="width: 440px;">
                                    <tbody>
                                        <tr style="vertical-align: top;">
                                            <td style="text-align:center;background:white;padding:15px;width:100%;padding-bottom:30px;">
                                                <table style="display:inline-block;">
                                                    <tr style="vertical-align: top;">
                                                        <img height="60" width="200" src="cid:{header_image_id}" style="display:inline-block;" />
                                                    </tr>
                                                </table>
                                                <div class="body-text">
                                                    {1}
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table style="width: 440px;">
                                    <tr>
                                        <td style="background:#E3F2FD;width:100%;max-height:80px;height:80px;text-align:center;">
                                            <img height="80" width="300" src="cid:{footer_image_id}" style="display:inline-block;" />
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </body>
        </html>
    """.format(
            style,
            body,
            header_image_id=header_image_id[1:-1],
            footer_image_id=footer_image_id[1:-1],
        ),
        subtype="html",
    )
    # note that we needed to peel the <> off the msgid for use in the html.

    try:
        # Now add the related image to the html part.
        images_dir = os.getcwd() + "\\images\\"
        with open(images_dir + header_image, "rb") as img:
            msg.get_payload()[1].add_related(
                img.read(), "image", "jpeg", cid=header_image_id
            )

        with open(images_dir + footer_image, "rb") as img:
            msg.get_payload()[1].add_related(
                img.read(), "image", "jpeg", cid=footer_image_id
            )

        # Make a local copy of what we are going to send.
        with open("outgoing.msg", "wb") as f:
            f.write(bytes(msg))

        # Send the message via local SMTP server.
        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.ehlo()  # identify yourself with smtp
            smtp.starttls()  # encrypt trafic
            smtp.ehlo()

            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            smtp.close()
            print("Email Sent!")
    except Exception as e:
        logging.error("Something went wrong while sending email!!!" + str(e))
        logging.error(traceback.format_exc())
