
discord_ids = {
    "Mason Doyle": "946500419729903710",
    "Ethan Fenwick": "803675212934676510",
    "Carson Berry": "767241916336832552",
    "Trevor Stephens": "187382120992210945",
    "Matthew Kirby": "804459530242097214",
    "Connor Hjelm": "190247425368260608",
    "Liam Óg Campbell": "986414587257696297",
    "WILLIAM BLAKE": "595475431428325376",
    "Max Hubbauer": "997565080537407599",
    "Ev O'Connor": "1003983986915299339",
    "Ronnie Castellano": "888259040310857808",
    "Paul Morgan": "536198104932679681",
    "Jake Saito": "414577871189966849",
    "Zain Zahoor":"918286845924737054",
    "Charlie Kirby":"1054963061506719774",
    "Aaron Peterson": "284909222133628938"
}


def get_discord_name(owner_name):
    return f'<@{discord_ids.get(owner_name)}>'
