from browser import Browser

browser = Browser(3)

browser.visit_page('google.com','google')
browser.visit_page('youtube.com','youtube')
browser.visit_page('github.com','github')

browser.show_recent_tabs()
browser.visit_page("chatgpt.com", "ChatGPT")

browser.show_recent_tabs()

browser.open_page("youtube.com")

browser.search("git")