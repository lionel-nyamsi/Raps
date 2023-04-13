from kivymd.uix.screen import MDScreen
import qrcode


class ConnexionPage(MDScreen):
    text_instructions = [
        "Pour connecter votre téléphone à votre console multimedia, suivez les étapes suivantes ci dessous:",
        "1.  Ouvrez l'application LIION ASSIST sur votre smartphone; Bien vouloir la télécharger sur le Playstore si elle n'est pas encore installée ;",
        "2.  Autorisez l'accès à l'appareil photo, au WIFI, et au micro puis, cliquer sur le bouton CONNECTER pour établir la connection ;",
        "3.  Positionnez votre téléphone face à la console pour scanner le code QR ci dessus;",
        "4.  Une fois connecté, vous pouvez à présent jouir des fonctionnalités offertes par LIION ASSIST."
    ]
    text_instruction = """1.  Ouvrez l'application LIION ASSIST sur votre smartphone; Bien vouloir la télécharger sur le Playstore si elle n'est pas encore installée ;\n2.  Autorisez l'accès à l'appareil photo, au WIFI, et au micro puis, cliquer sur le bouton CONNECTER pour établir la connection ;\n3.  Positionnez votre téléphone face à la console pour scanner le code QR ci dessus;\n4.  Une fois connecté, vous pouvez à présent jouir des fonctionnalités offertes par LIION ASSIST."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=150,
            border=1
        )
        code = "ce_texte_est_un_code"
        qr.add_data(code)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_qr.save("images/qrcode.png")
